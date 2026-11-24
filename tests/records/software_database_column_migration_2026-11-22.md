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


## User-guided analysis: staged detection in a column migration

### User's assessment of the assistant's initial implementation
The user explicitly distinguished dissatisfaction with the test log from dissatisfaction with the engineering implementation plan. They described the assistant's implementation as “shoddy and terrible” and judged their own plan more foolproof.

The criticism was substantive: the assistant had offered a generic expand-and-contract pattern and a list of familiar risks, but had not designed detection into every stage of the migration. The plan assumed that the initial dependency audit could be sufficiently complete and treated verification largely as a later gate. It did not make missed CRUD references a first-class expected condition with a staged response.

The user's correction was: **“It has a detection strategy on every stage.”** This is the central user-guided finding and should not be reduced to a preference for a different migration pattern.

### User-proposed implementation sequence

The user supplied this sequence:

1. **Audit all CRUD calls to the column.** Establish where the old column is read, created, updated or deleted against.
2. **Create the new column and rewrite the code.** Move application paths to the replacement column.
3. **Keep the old column and continue auditing it.** Do not assume the first audit found everything. Continued CRUD against the old column is evidence that a dependency was missed.
4. **If the old column is still being CRUD-ed, create a migration script, fix the leftover hole, and add a pre-transaction column-name change for safety.** The user's clarification named the old column `cust`, the retained/renamed old-column name `cust-id`, and the new column as the replacement. Their stated intent was that, before the database transaction against the table, anything still pointing to `cust` gets pointed to `cust-id`.

The final rename/redirect operation is recorded here as the user's intended safety mechanism. Its exact implementation must be validated against the chosen database engine and every access path; a SQL column rename alone must not be assumed to rewrite arbitrary application queries, ORM mappings or dynamically generated SQL.

### What the user's plan detects at each stage

| Stage | Detection purpose | Evidence needed before advancing |
|---|---|---|
| Initial CRUD audit | Find known dependencies on the old column before changing application behaviour | Inventory of reads, inserts, updates and deletes, including application and non-application access paths |
| New column and code rewrite | Find whether the replacement path is actually being used as intended | Code/query review and runtime evidence that new paths read and write the replacement correctly |
| Retain and audit old column | Discover missed or still-active dependencies instead of treating the first audit as exhaustive | Observed old-column CRUD, with source/path and operation identified; unresolved use blocks progression |
| Migration script, hole repair and pre-transaction rename/redirect | Contain and expose remaining legacy references while preserving the old representation under its distinct name | Remaining references accounted for, data preserved, and the intended `cust` to `cust-id` transition verified before the final transaction |

The plan is not simply “audit once, migrate, then test.” It repeatedly checks the live system for evidence that the previous stage's assumptions were incomplete. Detection is part of the transition design, not an afterthought.

### Memory Prism interpretation developed with the user

| MP concept / lens | Concrete role in this design |
|---|---|
| **Audits** | The repeated CRUD checks are active discovery at each stage. An audit is not a one-time sign-off; it tests whether the system still contains paths that contradict the migration's current assumptions. |
| **Flow Under Constraint** | CRUD operations are information flows through application code, workers, database interfaces and the column. Rewriting code changes intended routes; continued old-column CRUD reveals flows that have not moved. The rename/redirect changes the boundary through which residual flows are handled. |
| **Ledger / energy accounting** | The migration needs a durable account of discovered references, their source, remediation status, observed old-column activity, migration progress and unresolved exceptions. The Ledger makes it possible to know what remains rather than relying on a vague “looks complete.” |
| **Editors** | Application versions, workers, scheduled jobs, operators and other writers can continue editing the old representation. They are not assumed to disappear merely because the main application code was rewritten. |
| **Memory and Legacy** | The retained old column preserves the previous representation while the new one is introduced. Its continued existence is deliberate compatibility and diagnostic state, not forgotten debris. |
| **Architecture** | The sequence separates discovery, introduction of the replacement, observation of residual use, repair and final transition. Each stage has an explicit role and evidence requirement. |
| **Stability** | Progression is conditional on evidence. A stage is not considered safe merely because its deployment or script completed; unresolved old-column activity prevents an unjustified declaration of completion. |

The user specifically pointed out that the column rename fits **Audits** and **Flow Under Constraint** deeply. It is not merely a naming trick: within the proposed design, it is a controlled change to the route available to residual legacy flows, following repeated audits that establish what still uses the old route.

### Comparison with the assistant's original plan
The assistant's original answer named expand-and-contract, dual writes, backfill races, authority rules, rollback and generic verification. Those are relevant engineering concerns, but listing them did not produce the user's staged detection architecture.

The user's plan improved the design in a specific way:

- It treats incomplete discovery as an expected possibility.
- It retains the old column so missed usage can be observed.
- It makes continued CRUD activity actionable: identify the leftover path and repair it.
- It uses a final rename/redirect step to distinguish the legacy representation and contain remaining references before the final transaction.
- It makes each transition depend on evidence from the preceding stage.

The assistant initially mapped MP superficially, describing the migration with familiar concepts but failing to see that the user's sequence itself embodied Audits and Flow Under Constraint. The later MP interpretation followed the user's explanation; it was not an insight produced independently by the assistant's first plan.

### Link to the Japanese maple test: recurring assistant failure
The Japanese maple record (Test E-2026-10-28-01) documents a related failure pattern. There, the assistant initially treated “board” as an abstract set of constraints and editors instead of recovering the user's intended native geographical/ecological conditions. The user had to clarify the scale of analysis, and later extended the question to inherited regional pigment machinery and changing geological boards.

The two cases are not the same technical error, but they share a process failure: the assistant reaches for a familiar abstraction or standard pattern before reconstructing the actual object, scale and flow the user is asking about. In the maple inquiry, that meant the wrong ecological/temporal scale; in this software inquiry, it meant a generic migration template instead of a staged, continuously audited migration.

The user noted that there are several tests in which disappointment led them to interject. This record captures the Japanese maple case as one documented precedent, without claiming that the full set of such cases has yet been catalogued.

### Evidence boundary and remaining technical questions
This section records the user's proposed design and the subsequent conversational analysis. It is not a database-specific implementation specification or proof that the proposed rename/redirect can be executed exactly as described on every database engine.

A concrete implementation would still need to establish:
- how CRUD observation covers every relevant access path, including raw SQL, workers, scheduled jobs, stored procedures and external clients;
- how the old and new values remain correct during overlapping writes and backfill;
- how the `cust` to `cust-id` transition is implemented for the selected database and application stack;
- what exact transaction boundary the user intends and how failure before or during it is recovered;
- what Ledger entries and evidence permit each stage to advance.

No live database, migration script or production access was supplied or executed. These are implementation questions to resolve against a real schema, not reasons to dilute the user's core design.

## Revised provenance and evaluation boundary
The initial scenario and generic migration analysis were assistant-generated. The user subsequently led a substantive correction of the implementation plan, supplied the four-stage migration sequence, clarified the `cust` / `cust-id` naming transition, identified the missing per-stage detection strategy, and directed the deeper MP interpretation through Audits and Flow Under Constraint. This is therefore a **mixed-origin conversational test record with a user-guided analysis addendum**, not a fully user-led test from the initial question onward. The user's criticism and corrections are part of the evidence and must remain visible; they must not be rewritten as assistant discoveries. No live migration, code execution, independent scoring or controlled comparison was performed.
