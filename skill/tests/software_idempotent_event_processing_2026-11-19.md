# Software Daily Test: Idempotent Event Processing Under Retries and Unknown Outcomes — 2026-11-19

## Test type
Software daily test. Test ID: MP-SOFTWARE-2026-11-19-01.

## Scenario
An event-driven service consumes messages from a broker with at-least-once delivery. A consumer updates its database and acknowledges the message. A network timeout occurs during commit or acknowledgement. The broker redelivers the message, and the service must avoid applying the same logical operation twice without silently discarding legitimate later events.

## Operating invariant
A retry must not create a second effect for the same logical operation, and a deduplication mechanism must not suppress a distinct operation merely because its payload looks similar. The system must preserve enough durable evidence to resolve whether an operation was already applied.

## Pre-interpretation Memory Prism inventory

| MP concept | What I identify in this query |
|---|---|
| Board | The consumer, message broker, database, network and downstream services across separate failure domains. |
| P-Memory (Persistent Memory) | Durable operation identity and committed processing outcome retained so a redelivery can be distinguished from new work. |
| Constraints | At-least-once delivery, transaction boundaries, uniqueness guarantees, retention periods and uncertain network outcomes. |
| Ledger | Retry attempts consume broker throughput, worker time, database connections, CPU, I/O, storage and operator attention; deadlines and recovery capacity are finite budgets. |
| Flow Under Constraint | Messages, acknowledgements, database writes and outbox events crossing system boundaries. |
| Audits | Unique-key conflicts, durable processing records, transaction results and reconciliation checks. |
| Identity | Stable logical operation IDs, producer/tenant scope and event version; payload equality alone does not establish identity. |
| Working Lines | The interval between durable commit and acknowledgement; the dual-write gap between database commit and message publication. |
| Accumulation Patterns | Deduplication records, retry queues, outbox backlogs and poison-message queues can grow over time. |

## Three-way planning comparison

### A. Conventional software planning
A conventional implementation might configure broker retries, add a processed-message table, and acknowledge messages after the database update. This is a useful starting point, but several details determine correctness:
- Is the deduplication key stable and scoped to the correct producer or tenant?
- Is recording the message as processed atomic with the business-state update?
- What happens if the database commits but the acknowledgement is lost?
- Can two consumers process the same message concurrently?
- Does deduplication retention outlast the maximum plausible redelivery window?
- If an external side effect is involved, can it be made idempotent or reconciled independently?

### B. MP-guided planning with pre-interpretation inventory
Treat identity and durable state as first-class design elements:
1. Define a stable operation identity. Do not use a payload hash alone where two legitimate operations may have identical content.
2. In one database transaction, insert the deduplication record under a uniqueness constraint and apply the corresponding business-state change.
3. If the key already exists, read the stored outcome and treat the delivery as a duplicate only if it is the same logical operation and the earlier effect is known to have committed.
4. Acknowledge the broker message only after the durable transaction succeeds.
5. For database changes that must publish events, write an outbox record in the same database transaction as the state change. Publish it asynchronously and make downstream consumers idempotent too.
6. Define retention and cleanup rules for deduplication and outbox records; do not delete evidence before the replay horizon has passed.
7. Record an explicit state for uncertain external outcomes rather than translating every timeout into “failed”.

### C. MP + Critical Thinking challenge pass
Challenge the design against failure timing:
- **Crash before database commit:** the transaction rolls back; redelivery should perform the operation.
- **Commit succeeds, acknowledgement fails:** redelivery occurs; the durable deduplication record must prevent a second effect.
- **Two consumers race:** uniqueness and transaction isolation must ensure only one operation applies.
- **Database commits, event publish fails:** the outbox record remains available for later publication.
- **Publish succeeds, publisher crashes before marking sent:** the event may publish again; downstream idempotency is still required.
- **External API times out after acting:** outcome may be unknown; use the provider's idempotency key or a reconciliation query rather than blindly repeating the side effect.
- **Deduplication record expires too early:** an old replay can become a duplicate effect; retention must match the system's actual replay and recovery policy.

“Exactly once” should not be claimed as a property of the entire distributed workflow merely because one broker or database offers a narrower exactly-once feature. State precisely which boundary is protected and which effects remain at-least-once or require reconciliation.

## Ledger
Retries are not free. Every attempt consumes broker capacity, worker time, database connections, transaction/lock time, I/O and often storage for deduplication and outbox records. A retry policy therefore needs a bounded attempt/time budget, backoff and jitter, and a limit that prevents failing dependencies from consuming the capacity needed for recovery. Timeout values also spend a finite latency budget across the end-to-end operation; setting each component timeout independently can exceed the caller's deadline. The system should reserve enough capacity to process healthy traffic and drain backlogs after an incident.

## Research-grounded insight
At-least-once delivery intentionally trades possible duplicate delivery for resilience against message loss. The consumer therefore needs idempotent processing. A transactional outbox addresses the dual-write problem between a database update and event publication, but does not remove the possibility of duplicate publication; downstream consumers still need idempotency. Distributed commit timeouts create an unknown-outcome problem: the operation may have committed even when the caller did not receive confirmation.

## Suggested implementation sequence
1. Map the actual transaction boundaries and every external side effect.
2. Define operation identity and key scope with explicit collision and replay rules.
3. Implement atomic deduplication plus business-state mutation in the same database transaction.
4. Add concurrency tests for duplicate deliveries and simultaneous consumers.
5. Add a transactional outbox for events derived from committed database changes.
6. Make downstream consumers idempotent and define how external APIs handle unknown outcomes.
7. Set retention from the maximum replay, restore and disaster-recovery horizon.
8. Inject crashes and network failures at each boundary; verify durable state after restart.

## Failure modes and recovery
- **Duplicate effect after redelivery:** inspect whether deduplication and the business mutation shared one transaction; repair the boundary before increasing retries.
- **Legitimate operation suppressed:** review key scope and identity construction; do not deduplicate on content equality alone.
- **Outbox backlog grows:** inspect publisher health, poison events and retry policy while preserving unpublished rows.
- **Deduplication storage grows without bound:** define safe retention based on replay guarantees and archive/reconcile before deletion.
- **External outcome remains unknown:** use provider-side idempotency or authoritative reconciliation; do not assume timeout equals failure.

## Capability contribution and attribution boundaries

| Capability | Contribution to this test | Status |
|---|---|---|
| P-Memory (Persistent Memory) | Durable operation identity and prior outcome allow a redelivery to be interpreted against persistent state. | Applied as a design lens. |
| Episodic Memory | Ordered event/attempt history helps reconstruct where a failure occurred. | Proposed observability; not implemented. |
| Semantic Memory | Organises delivery guarantees, transaction boundaries, outbox and idempotency concepts. | Applied as domain knowledge. |
| Procedural Memory | Defines the repeatable consume, transact, record, acknowledge and reconcile sequence. | Proposed workflow; not executed. |
| Critical Thinking | Challenges the assumption that timeout means failure or that broker-level exactly-once covers external effects. | Applied as a reasoning pass; not an independent blinded evaluator. |

## Evaluation criteria
- A duplicate delivery cannot apply the same database effect twice.
- Two concurrent consumers cannot both win the same operation identity.
- Acknowledgement happens only after durable processing.
- Database state and outbox intent are committed atomically.
- Downstream duplicate publication is handled safely.
- Unknown external outcomes are not misclassified as definite failure.
- Key scope and retention do not suppress legitimate work or permit stale replays to duplicate effects.
- The design states exactly which guarantees are provided and where reconciliation remains necessary.

## Limits
This is a design and failure-analysis exercise, not a deployed broker/consumer test. No implementation, load test, chaos test or production metric was run. Correct transaction and acknowledgement behaviour depends on the selected broker, database, client library and external API. The design must be validated against those concrete semantics.

## Sources
- Microsoft Azure Architecture Center, “Idempotent Consumer pattern”: https://learn.microsoft.com/en-us/azure/architecture/patterns/idempotent-consumer
- AWS Prescriptive Guidance, “Transactional outbox pattern”: https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/transactional-outbox.html
- Google Cloud Spanner documentation, “Exactly-once processing and at-most-once acknowledgment”: https://cloud.google.com/spanner/docs/queues/queues-at-most-once

## Provenance
Assistant-selected software topic for 2026-11-19, deliberately outside business coordination and logistics. Documentation-grounded scenario comparing conventional planning, MP-guided design and an MP + Critical Thinking challenge pass. No live implementation or production outcome is claimed.
