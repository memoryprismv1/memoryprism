# Software Daily Test: Message Ordering and Delivery Guarantees — 2026-11-26

**Test ID:** MP-SOFTWARE-2026-11-26-01  
**Run type:** Assistant-generated synthesis  
**Conditions:** single MP-guided standards/documentation analysis; no baseline comparison  
**Context:** same-context · **Scorer:** self · **Blind:** no · **Execution:** official product documentation; no live broker or application run  
**Scenario:** How can a message broker preserve ordering when messages are processed concurrently, retried after failure, and delivered to multiple consumers?

## Scenario and operating invariant

Example: an order emits `OrderCreated`, `PaymentAuthorized` and `OrderDispatched`. The operating invariant is that events with a causal dependency for one order must not be applied in an invalid sequence. Independent orders need not be globally serialized.

The phrase "message ordering" hides several different states:
- published to the broker;
- persisted/committed by the broker;
- delivered to a consumer;
- acknowledged by the consumer;
- processed by the application;
- external business effect committed.

A broker's enqueue or log order does not, by itself, prove that consumers completed business effects in that order.

## Selective pre-interpretation inventory

| MP concept | What I identify in this query |
|---|---|
| Architecture | Producers, partitions/queues, consumer groups, acknowledgements, retry paths, application state and external databases. |
| Constraints | Required ordering scope, partition count, consumer concurrency, retry policy, failure recovery and throughput. |
| Board | The ordering domain: global stream, partition, queue or business-entity key. |
| P-Memory | The durable log, offsets, event identifiers and application records left by prior processing. |
| Flow Under Constraint (candidate) | Events move through delivery and retry paths; a retry path can let later events overtake an earlier failed event. |
| Ledger | Messages received, acknowledged, retried and committed are distinct accounting states; business effects and duplicate work must also be accounted for. |
| Stability | Business invariants must survive consumer crashes, redelivery, rebalancing and partial completion. |

## System mechanisms and evidence

### Kafka: ordered partitions and transactions

Kafka divides a topic into ordered partitions. A producer can select a semantic key (for example, order ID) so events for the same entity are routed to the same partition. Within a consumer group, each partition is assigned to one consumer at a time. This allows parallelism across partitions while retaining per-partition order. [1]

Kafka producer idempotence prevents duplicate log entries from certain resend scenarios. Kafka transactions can atomically write produced records and consumed offsets for a Kafka read-process-write workflow. The documentation explicitly distinguishes at-most-once and at-least-once consumer processing based on whether the offset is committed before or after processing. These transactional guarantees do not automatically make arbitrary external database or payment effects exactly-once. [1]

### RabbitMQ: FIFO queue versus observed processing order

RabbitMQ queues are FIFO structures. However, priorities and multiple active consumers can change the order observed by consumers; a requeued or redelivered message may be observed after later messages. RabbitMQ documents two approaches when ordering matters: a single active consumer for a queue, or streams (append-only logs with offsets). For per-entity ordering with concurrency, messages can be partitioned by entity key across multiple queues, each with a single active consumer. [2]

The important distinction is between queue order and completion order. Two consumers can receive messages in enqueue order but finish their work in the opposite order.

### Pulsar: Key_Shared

Pulsar's `Key_Shared` subscription allows multiple consumers to share a subscription while messages with the same key are delivered to one consumer in order. There is a producer-side requirement: disable batching or use key-based batching, because ordinary batching can combine different keys and break the intended routing semantics. [3]

This is a useful demonstration that concurrency is not necessarily global: independent keys can be processed concurrently while each key has a serial processing lane.

## Failure and recovery behaviour

A typical failure window:

1. Consumer receives message 10.
2. It performs the business operation.
3. It crashes before acknowledging message 10.
4. The broker redelivers message 10.
5. The business operation may be attempted again.

If the consumer acknowledges before the business operation commits, a crash can lose the effect. If it commits the effect before acknowledging, a crash can cause duplicate delivery. Therefore, consumers need idempotency or a transaction boundary that covers the relevant state changes.

A second ordering failure:

1. Message 10 fails and is sent to a delayed retry path.
2. Message 11 is allowed to proceed.
3. Message 11 commits before message 10 is retried.
4. The application has observed an order different from the original sequence.

The design must decide whether to block the affected key/partition, preserve order through a keyed retry mechanism, or allow reordering and make the business operation tolerant of it. The original answer mentioned delayed retries and reordering but did not fully specify an ordered retry architecture.

### Producer-side dual write

A further failure occurs before the broker receives an event. If an application commits a database update and separately publishes an event, a crash between the two operations can leave the database changed but no event published. Reversing the order can publish an event for a transaction that later rolls back.

The transactional outbox pattern writes the business update and an event record in the same database transaction; a separate publisher sends the outbox event. Duplicate publication remains possible, so consumers still need idempotency. AWS Prescriptive Guidance describes the dual-write failure modes, outbox transaction and duplicate-message considerations. [4]

## Findings

The system cannot promise arbitrary global ordering and unrestricted concurrent processing without coordination or serialization somewhere. A practical design first identifies the causal ordering boundary:
- global order only when the whole stream genuinely depends on sequence;
- per-entity order when events for the same entity are causally dependent;
- no ordering constraint between independent entities.

Then it chooses a mechanism that matches that boundary: partition by key, one active consumer per queue/partition, or a keyed subscription. Retry and acknowledgement rules must preserve the same invariant. The outbox addresses reliable event creation at the producer; idempotent consumers address repeated delivery; neither alone guarantees correct business ordering across external systems.

## Limits and omissions

- No Kafka, RabbitMQ or Pulsar cluster was run.
- No crash injection, retry timing experiment, throughput benchmark or external database transaction was tested.
- The answer compared selected documented behaviours, not every broker configuration or version.
- The initial answer did not develop an end-to-end ordered retry design, consumer rebalance edge cases, poison-message policy, or a concrete monitoring/rollback plan.
- "Exactly once" was correctly bounded to Kafka's transactional Kafka-to-Kafka processing in the explanation, but the general phrase remains easy to overstate; external side effects require their own transactional/idempotency design.

## Sources

1. Apache Kafka 4.1, *Design*: semantic partitioning by key, consumer group partition assignment, idempotent producer and transactional processing: https://kafka.apache.org/41/design/design/
2. RabbitMQ 4.3, *Queues*: FIFO semantics, ordering changes with priorities/requeue and multiple active consumers, single active consumer, streams and entity-key partitioning: https://www.rabbitmq.com/docs/queues
3. Apache Pulsar, *Work with consumer*: Shared versus Key_Shared semantics and key-based batching requirement: https://pulsar.apache.org/docs/client-libraries/consumers/
4. AWS Prescriptive Guidance, *Transactional outbox pattern*: dual-write problem, atomic outbox record, duplicate delivery and idempotent consumers: https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/transactional-outbox.html

## Score sheet

**Run type:** assistant-generated synthesis **Conditions:** single MP-guided answer **Context:** same-context **Scorer:** self **Blind:** no **Execution:** standards/docs

| Dim | MP-guided | Note |
|---|---:|---|
| IQ1 Engages the question | 2 | Directly addresses concurrency, ordering and retries. |
| IQ2 Mechanism and evidence | 2 | Product behaviours checked against official documentation; boundaries stated. |
| IQ3 Evidence boundaries | 2 | No live broker run; Kafka exactly-once scope and external effects distinguished. |
| IQ4 Competing explanations | 1 | Several architectures compared, but the answer did not give a complete separating test for every failure hypothesis. |
| IQ5 Next question or action | 1 | Identifies design choices but does not build or execute a fault-injection test. |
| IQ6 Clarity and economy | 1 | The response was long and repeated the ordering-boundary point. |
| **IQ total** | **9/12** | |

| MPF dimension | Score | Note |
|---|---:|---|
| MPF1 Inventory first and concrete | 0 | Inventory was placed after the main explanation in the actual answer. |
| MPF2 Proportionate selection | 2 | Selected architecture, constraints, board, P-Memory, Flow, Ledger and Stability for this problem. |
| MPF3 Concept fidelity | 1 | Ledger was identified, but the actual explanation blurred message-state accounting with resource accounting and did not fully operationalise it. |
| MPF4 No unsupported mechanism | 2 | No unsupported editor, audit or translator was asserted. |
| MPF5 Source use | 2 | Skill/checklist consulted and official vendor/AWS documentation opened. |
| MPF6 Reasoning audit actually used | 0 | No visible revision from the internal audit; the missing ordered-retry design remained. |
| **MPF total** | **7/12** | |

**Integrity flags:** F1 No · F2 No · F3 No · F4 No · F5 No · F6 No.  
**Difference claimed?** No comparison condition was run.

**SCORES:** IQ_mp=9/12; MPF=7/12; scorer=self; blind=no

## Repository provenance

**Protocol retrieval (UTC):** 2026-11-26T12:20:14Z  
**Current main commit:** `5f3379274b79bb63a71a3ce3af09bd3f597fe587`

| File | Git blob SHA | SHA-256 |
|---|---|---|
| `tests/daily/README.md` | `04d295a20c67ff0774d89711c07a475616bf503e` | `d69d5220b45d68920d3cc9e1778dc1e0ff17d022dddcadac7ebb3770b09a8e74` |
| `tests/daily/SCORING.md` | `0b4f359fdeefdcdc55d55b94a94e8c8d801280a3` | `7f5045b4a3912ed1e951a79e6ac0b8b977fb70804074787d6454ab79d9bc9c79` |
| `skill/memory-prism/SKILL.md` | `23ce6795cee602ec2037cdd431ddf81fc8ae5480` | `74e60dd2eaa718bbb01d8fbe8d60b2a7a119c3efd32b0f52c356e5c6283158e4` |
| `skill/memory-prism/references/checklist.md` | `1be28163166ea70104122ab2f3b6ebc73a92f98e` | `2aee3a467798aa9e421947b0771968b745627aff938af59be51d26e3c624e095` |
| `tests/records/DEVELOPMENT_LOG.md` | `c8a44ed328102c41d9beb1a8662dfa8f3c7098d3` | `682a5f59d24265b062bc2ec394c09800f0be4cade83e2f2fe50eab2f07620518` |
