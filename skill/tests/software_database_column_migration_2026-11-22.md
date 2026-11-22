# Software Daily Test: Online Database Column Migration — 2026-11-22

## Test type
Software daily topic. Test ID: MP-SOFTWARE-2026-11-22-01.

## Scenario
A production service must replace a database column while the service remains online. A rolling deployment means old and new application versions may run simultaneously. Existing rows need backfilling, concurrent writes must not be lost, and rollback must remain possible during the transition.

## Operating invariant
At every point in the migration, every active application version must be able to read and write the data it is responsible for without silently losing an accepted update. The system must have an explicit authority rule for the old and new representations, and rollback must not depend on data that has already stopped being maintained.

## Pre-interpretation Memory Prism inventory

| MP concept | What I identify in this query |
|---|---|
| Board | Database, application instances, background workers, migration job, queues, replicas and deployment/control plane. |
| Editors | Old and new application versions, backfill workers, concurrent user writes, retries and operators can all change relevant state. |
| Constraints | Availability, lock duration, table size, write rate, deployment overlap, replication lag, storage and rollback window. |
| Memory | Existing rows and schema/application versions preserve prior state and compatibility assumptions. |
| Ledger / energy accounting | Backfill throughput competes with production workload; remaining work, retry backlog, lock time, replication lag and rollback capacity must be accounted for. This record does not quantify those costs. |
| Flow Under Constraint | Reads, writes, backfill batches, replication and deployment move through different paths and at different rates. |
| Accumulation Patterns | Backfill progress, lag, failed rows and retry queues accumulate over time; a completed job count is not by itself proof of correct data. |
| Audits / Evidence | Row-level comparison, counts, sampled checks, error logs and version inventories provide evidence of convergence. |
| No Sacred States | “Migration complete” is not a safe global state while old instances, workers or rollback paths still depend on the old representation. |

## Conventional migration pattern
An expand-and-contract approach is a sound starting pattern:

1. Add the new column in a schema change compatible with the currently deployed application.
2. Deploy application code that can tolerate both representations.
3. Establish how writes to the old and new columns remain consistent.
4. Backfill existing rows in bounded batches.
5. Verify the new representation and switch reads.
6. Confirm old application instances and workers are gone.
7. Retain rollback compatibility for an explicitly bounded period.
8. Remove the old column in a later deployment.

This sequence is a pattern, not a universal recipe. Exact DDL, locking and backfill behaviour depend on the database engine, version, table shape and workload.

## MP-guided analysis: state and race conditions
The most consequential interval is the overlap between application versions, backfill and live writes.

Potential failures include:

- An old instance writes only the old column after a row has been backfilled.
- A backfill reads an old value, a user updates the row, and the backfill later overwrites the newer value.
- A new instance writes both columns but one write fails or is applied inconsistently.
- A background worker retains an old schema assumption after web instances have been upgraded.
- The application switches reads before all relevant rows have been populated and verified.
- A rollback restores old code after the old column has stopped receiving authoritative updates.

The backfill race is particularly important. A naive “copy old to new” update can overwrite a newer value unless the operation is guarded by a version, timestamp, conditional predicate or another explicit concurrency strategy. The correct method depends on the application's consistency model.

Dual-writing also needs an authority rule. If both columns can be independently edited, “write both” does not resolve which value wins after partial failure or concurrent updates. Prefer a clearly defined source of truth and a controlled transition; where possible, keep related writes in one database transaction and make repair/reconciliation observable.

## Evidence and database-specific caveat
PostgreSQL documentation illustrates why the database-specific migration plan matters: ALTER TABLE subcommands have different lock requirements; some operations rewrite a table; adding a volatile default can rewrite the table and indexes; and constraint validation can be separated from adding a NOT VALID constraint to reduce disruption to concurrent updates. These details are not interchangeable across database engines or versions.

Source: PostgreSQL documentation, “ALTER TABLE”: https://www.postgresql.org/docs/current/sql-altertable.html

## Failure, recovery and verification
Before switching reads, verify at least:

- Every relevant row has a valid new value, with exceptions explicitly enumerated.
- Old/new values agree wherever the migration invariant requires agreement.
- Concurrent updates during backfill cannot be overwritten by stale copies.
- All application instances, workers and scheduled jobs have a known schema-compatibility state.
- Replication lag and migration backlog are within operational limits.
- The rollback path still has the data it needs.
- Interruption and restart of the backfill are safe and idempotent.
- The old column is not removed until the rollback window and dependency checks are complete.

Test interruption at multiple points, not just the successful path. A migration script exiting with status zero is not proof that the application has reached a consistent state.

## Findings
The familiar expand-and-contract pattern remains the appropriate starting point. The useful MP contribution in this analysis is to make the overlapping editors, time-dependent compatibility, backfill accumulation and operational ledger visible together.

The most important technical risks are not solved by naming those elements. They require concrete concurrency controls, an authority rule, database-specific lock analysis, row-level verification and a rollback design.

The core invariant is stronger than “the migration script finished”: accepted writes must remain represented correctly throughout the transition, including during backfill, rolling deployment, retries and rollback.

## Limits
- This is a hypothetical design analysis, not a live database migration.
- No database engine, schema, table size, write rate or application code was supplied.
- PostgreSQL documentation is used to illustrate engine-specific behaviour; the scenario itself is not restricted to PostgreSQL.
- No migration code, backfill query, load test, interruption test or production metric was executed.
- The user did not lead the inquiry or supply observations in this run.

## Source
- PostgreSQL documentation, “ALTER TABLE”: https://www.postgresql.org/docs/current/sql-altertable.html

## Provenance and evaluation boundary
Assistant-selected software scenario for 2026-11-22. This record documents an assistant-generated design analysis. It is **not a completed canonical user-led daily test** under `skill/tests/README.md`. No separate Critical Thinking skill was loaded or executed, and no controlled conventional-versus-MP comparison or independent scoring was performed. The MP inventory organises the scenario; it does not establish a measured improvement in migration safety.
