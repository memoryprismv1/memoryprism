# Software Daily Test: PostgreSQL Dead-Tuple Accumulation and Autovacuum — 2026-11-18

## Test type
Software / systems reasoning test. Test ID: MP-SOFTWARE-2026-11-18-01.

## Scenario
A PostgreSQL service shows rising table and index bloat, increasing dead tuples, and autovacuum runs that appear unable to catch up. Application latency is worsening. The task is to plan a safe diagnosis and remediation without assuming that increasing autovacuum workers or thresholds will solve the root cause.

## Operating invariant
Do not prescribe aggressive vacuum settings until identifying whether cleanup is being delayed by old transaction horizons, replication state, long-running transactions, insufficient maintenance capacity, or an incorrect interpretation of storage reuse. Preserve evidence and avoid disruptive changes before establishing the cause.

## Three-way planning comparison

### A. Conventional software planning
A conventional response might inspect table sizes and dead-tuple estimates, increase autovacuum frequency or worker capacity, and run manual VACUUM on the largest tables. This can help when maintenance capacity is genuinely insufficient, but it risks treating symptoms while a transaction horizon prevents removal of tuples.

### B. MP-guided planning with pre-interpretation inventory
First inventory the evidence and its provenance:
1. Identify affected relations and compare estimated dead tuples, live tuples, relation size and recent growth.
2. Inspect long-running transactions and backend_xmin / backend_xid information; distinguish an old transaction's snapshot horizon from its transaction identifier.
3. Check prepared transactions and replication slots, including xmin, catalog_xmin and restart_lsn where relevant.
4. Check standby feedback and replication state; determine whether a replica is retaining row versions needed by its queries.
5. Inspect autovacuum activity, worker availability, cost limits, per-table storage parameters and maintenance logs.
6. Separate dead tuples that are removable from tuples that remain visible to an old snapshot.
7. Distinguish space reusable inside a relation from space returned to the operating system. Ordinary VACUUM generally makes space reusable; it does not normally shrink the relation file.

This inventory avoids conflating “autovacuum is slow” with “vacuum cannot remove these tuples yet.”

### C. MP + Critical Thinking challenge pass
Challenge the leading hypothesis before changing settings:
- If a replication slot or old snapshot is holding back the visibility horizon, more workers do not make those tuples removable.
- If the horizon is clear but vacuum throughput is inadequate, capacity, cost throttling, table churn, indexes and worker scheduling become plausible targets.
- If the table is healthy but the disk footprint remains large, internal free space may be reusable without being returned to the filesystem.
- If transaction IDs approach wraparound risk, anti-wraparound vacuum and freezing requirements take priority over ordinary bloat optimisation.
- A replica, logical slot or prepared transaction should not be terminated casually; first establish ownership, business impact and recovery consequences.

## Ledger
Autovacuum has a concrete operating budget: worker slots, CPU and I/O capacity, cost throttling, available disk headroom, and time before transaction-ID age becomes dangerous. The database also carries a recovery budget: how long a blocker can remain, how much backlog can accumulate, and how much capacity remains to catch up. Increasing workers spends more system resources; it does not remove a visibility-horizon blocker. The plan must compare maintenance demand with available capacity and preserve sufficient headroom for normal workload and recovery.

## Research-grounded insight
PostgreSQL vacuum has several distinct jobs: reclaiming dead row versions when they are no longer potentially visible, making space reusable, updating planner statistics (via ANALYZE, which is related but distinct), and freezing old transaction IDs to prevent wraparound. Autovacuum is a maintenance system, not a guarantee that every dead tuple can be removed immediately. The visibility horizon can be constrained by transactions and replication-related state. Diagnosis must therefore precede tuning.

## Suggested implementation sequence
1. Capture a time-bounded baseline of relation statistics, transaction age, replication state, vacuum progress and disk usage.
2. Identify the oldest relevant retention horizon and trace it to its owning session, prepared transaction, slot or standby.
3. Confirm with the responsible service owner whether that state is expected and whether it can safely advance.
4. If the horizon is clear, estimate the maintenance throughput required and compare it with current autovacuum capacity and throttling.
5. Change one controlled parameter or remove one confirmed blocker at a time; record the before/after state.
6. Recheck dead-tuple trends, vacuum progress, query latency, transaction-ID age and disk usage. Do not use filesystem shrinkage as the only success criterion.

## Failure modes and recovery
- **More workers, no improvement:** return to visibility-horizon diagnosis; workers cannot remove tuples still potentially visible.
- **Unexpected replica or logical-replication impact:** restore the prior configuration where possible and investigate slot/standby dependencies before further changes.
- **Disk usage does not fall after VACUUM:** verify internal reuse and relation growth patterns; do not assume ordinary VACUUM promises OS-level file shrinkage.
- **Wraparound pressure discovered:** prioritise safe freezing and the documented emergency procedures; do not continue ordinary tuning as if this were routine bloat.
- **Statistics are stale or estimates misleading:** corroborate with progress views, logs and repeated observations rather than treating one estimate as ground truth.

## Capability contribution and attribution boundaries

| Capability | Contribution to this test | Attribution |
|---|---|---|
| P-Memory (Persistent Memory) | Preserves the diagnostic distinctions and the ordered evidence inventory across the reasoning process. | Applied in the plan; no production memory system was instrumented. |
| Episodic Memory | Keeps the sequence of observations, interventions and outcomes conceptually separate. | Proposed record-keeping practice, not an implemented telemetry feature. |
| Semantic Memory | Organises PostgreSQL concepts: visibility horizons, vacuum, freezing, slots and reusable space. | Applied as structured domain knowledge. |
| Procedural Memory | Encodes a cautious diagnose-before-tune workflow. | A proposed operational procedure, not an executed runbook. |
| Ledger | Makes maintenance capacity, resource consumption, disk headroom and recovery time explicit; distinguishes a throughput shortfall from a cleanup blocker that extra capacity cannot fix. | Applied as a domain-relevant planning account; no live resource measurements were taken. |
| Critical Thinking | Challenges the assumption that additional vacuum capacity solves every backlog. | Explicitly applied as a reasoning pass; not a separate blinded evaluator. |

## Evaluation criteria
A satisfactory plan must:
- Identify whether tuple removal is blocked by an old visibility horizon or limited by maintenance throughput.
- Inspect relevant transaction, prepared-transaction, replication-slot and standby state before destructive action.
- Explain the difference between reusable relation space and operating-system space reclamation.
- Account for transaction-ID freezing and wraparound risk.
- Propose reversible, observable interventions with clear before/after checks.
- Avoid claiming a diagnosis or performance improvement without measurements.

## Limits
This is a documented reasoning exercise, not a live database diagnosis. No PostgreSQL instance was queried, no configuration was changed, and no latency or bloat improvement was measured. Exact view columns and behaviour can vary by PostgreSQL version; consult the documentation for the deployed version before executing commands.

## Sources
- PostgreSQL 18 Documentation, Routine Vacuuming: https://www.postgresql.org/docs/18/routine-vacuuming.html
- PostgreSQL 18 Documentation, Automatic Vacuuming: https://www.postgresql.org/docs/18/runtime-config-vacuum.html
- PostgreSQL 18 Documentation, Progress Reporting: https://www.postgresql.org/docs/18/progress-reporting.html
- PostgreSQL 18 Documentation, Monitoring Statistics: https://www.postgresql.org/docs/18/monitoring-stats.html
- PostgreSQL 18 Documentation, Warm Standby and Hot Standby Feedback: https://www.postgresql.org/docs/18/warm-standby.html

## Provenance
Daily assistant-selected software topic. Scenario-based comparison of conventional planning, MP-guided planning and an MP + Critical Thinking challenge pass. Documentation-grounded, qualitative and unexecuted; no claim of production validation or measured improvement.
