# Software Daily Test: Stale Leaders and Fencing Tokens — 2026-11-27

**Test ID:** MP-SOFTWARE-2026-11-27-01  
**Run type:** Standards-grounded scenario  
**Conditions:** single MP-guided documentation/research analysis; no baseline comparison  
**Context:** same-context · **Scorer:** self · **Blind:** no · **Execution:** standards/docs; no live cluster or fault injection  
**Scenario:** A distributed service elects a new leader after the old leader becomes unreachable or pauses. The old process later resumes and attempts a write. How can the system prevent that stale leader from modifying a protected resource?

## Scenario and operating invariant

The operating invariant is: **a write from an obsolete owner must not be accepted after a newer owner has taken authority.**

Example:
1. Server A acquires leadership and receives epoch/token 41.
2. A pauses or becomes isolated. Its lease expires.
3. The coordination service grants leadership to B with epoch/token 42.
4. A resumes and sends a delayed write using its old authority.
5. The protected resource must reject stale work rather than trusting A's local belief that it is still leader.

The critical distinction is between electing a leader and enforcing that leader's authority at the resource being modified. A coordination service can make a correct election while a separate storage service still accepts a delayed request from an old process.

## Selective pre-interpretation inventory

| MP concept | What I identify in this query |
|---|---|
| Architecture | Processes, coordination/consensus service, leases or sessions, ownership epochs, network, and the protected storage/resource. |
| Constraints | Partial failure, unbounded message delay, process pauses, lease expiry, quorum availability and the resource's validation capabilities. |
| Board | Cluster membership and quorum rules determine which process can acquire leadership; the protected resource has its own acceptance boundary. |
| P-Memory | Durable ownership epoch and the resource's record of accepted writes/tokens; P-Memory is not merely the process's local belief. |
| Editors (candidate) | Lease/session expiry and resource-side token validation can filter which ownership claims remain admissible. These are mechanisms, not intentional actors. |
| Ledger | Renewal traffic, quorum communication, recovery time and storage-side validation have ongoing resource costs; the key safety obligation is to ensure the resource does not accept work outside the current authority window. |
| Stability | The system must preserve single-writer safety despite old processes resuming and delayed requests arriving out of order. |

## Mechanism and evidence

A lease or distributed lock by itself does not make a protected resource safe. A process can be paused by garbage collection, scheduling, page faults or host suspension for longer than its lease. A request already sent can also be delayed in the network. When the process resumes, a local check that it once held the lock is not sufficient. Martin Kleppmann's analysis gives this stale-client failure and explains why checking lease expiry immediately before writing still leaves a pause/race window. [1]

The common defence is a **fencing token**: every successful acquisition receives a strictly increasing token. A new owner receives a larger token than any earlier owner. Every protected write carries its token, and the resource rejects a token lower than the latest token it has accepted. In the ordinary sequence, B writes with 42 and the resource then rejects A's later write with 41. The resource, not merely the client, must enforce the rule. [1]

There is a subtle limit to the simple “highest token seen” formulation. The resource cannot infer a new grant that it has not yet learned about. If A's delayed token-41 request reaches the resource after B has acquired token 42 but before the resource has seen or registered token 42, a resource that only compares against its highest previously accepted token may still accept 41. The exact guarantee therefore depends on how the protected resource validates the sequencer/token and how the new ownership epoch becomes authoritative at that resource. Where necessary, the resource must validate against the coordination authority or atomically establish the new epoch before permitting protected work. This is not solved by merely incrementing a number in the coordinator.

Google's Chubby paper describes sequencers containing the lock name, lock mode and lock generation number. The client attaches the sequencer to protected requests; the recipient server is expected to check its validity, either against its Chubby cache or against the most recent sequencer it has observed. Chubby also describes a bounded lock-delay as an imperfect compatibility mechanism for recipients that do not support sequencer checking. [2]

Other documented implementations illustrate related pieces:
- ZooKeeper's leader-election recipe uses ephemeral sequential znodes. The sequence orders candidates, while ephemeral ownership and watches support detecting leader departure. The documentation warns that a create may succeed even when the response is lost, so clients must handle uncertain outcomes and possible orphaned sequential nodes. This is an election recipe, not by itself proof that an arbitrary external storage service rejects stale writes. [3]
- Hazelcast's FencedLock uses a CP subsystem based on Raft and returns fencing tokens for clients to pass to an external service. Hazelcast explicitly describes the external service rejecting a former holder's lower token after the newer holder's token has been observed. [4]
- etcd's election implementation uses leases and creation revisions; its API exposes the leader key and revision for guarding operations through etcd transactions. This is useful when the protected operation is itself performed transactionally in etcd; it does not automatically fence writes to unrelated external systems. [5]

## Failure cases and discriminating evidence

| Failure explanation | What would distinguish it |
|---|---|
| Leader election is unsafe | Coordination history shows conflicting grants/terms or an invalid quorum decision. |
| Election is correct but resource enforcement is absent | One newer leader exists, yet the resource accepts a request from an older epoch. |
| Resource's remembered epoch lags the coordinator | The old write arrives before the resource has registered/validated the newer epoch. |
| Token check is not atomic with the write | A race can occur between validation and the protected mutation. |
| Token generation is not strictly monotonic across failover | A new owner can receive a token not greater than all prior owners. |

The next diagnostic experiment is a fault-injection sequence: pause A after it obtains 41; expire its session; elect B with 42; vary whether B has registered/validated 42 at the resource; then deliver A's delayed write before and after B's first write. Record coordinator state, resource epoch, accepted/rejected operations and final data. This distinguishes token generation, token propagation and resource enforcement. No such experiment was run in this test.

## Findings and limits

The coordination service establishes ownership, but the protected resource must enforce it. Fencing is effective only when token generation, propagation and resource-side validation form a coherent safety protocol. “We have leader election” and “we have a distributed lock” are not sufficient statements about external write safety.

The scenario is documentation-grounded. No ZooKeeper, etcd or Hazelcast cluster was deployed; no packet delay, process pause, lease expiry or storage race was injected. Product behaviours are version-sensitive and the cited documentation should be checked against the deployed version before implementation.

## Sources

1. Martin Kleppmann, “How to do distributed locking” (8 February 2016). Stale clients, process pauses, delayed requests and fencing-token requirements: https://martin.kleppmann.com/2016/02/08/how-to-do-distributed-locking.html
2. Mike Burrows, “The Chubby lock service for loosely-coupled distributed systems,” OSDI 2006. Sequencers, lock generation numbers, recipient validation and lock-delay: https://static.usenix.org/events/osdi06/tech/full_papers/burrows/burrows_html/
3. Apache ZooKeeper, “Recipes: Leader Election.” Ephemeral sequential znodes, predecessor watches and uncertain create outcomes: https://zookeeper.apache.org/doc/current/recipes.html
4. Hazelcast 5.7, “FencedLock.” CP subsystem, fencing tokens and external-resource rejection of stale tokens: https://docs.hazelcast.com/hazelcast/5.7/data-structures/fencedlock
5. etcd client v3, election implementation. Lease-backed election and creation revision handling: https://github.com/etcd-io/etcd/blob/main/client/v3/concurrency/election.go

## Score sheet

**Run type:** standards-grounded scenario **Conditions:** single MP-guided documentation analysis **Context:** same-context **Scorer:** self **Blind:** no **Execution:** standards/docs

| Dim | MP-guided | Note (failure mode for any 0/1) |
|---|---:|---|
| IQ1 Engages the question | 2 | States the stale-writer invariant and addresses resource-side protection. |
| IQ2 Mechanism and evidence | 2 | Distinguishes election, lease, token generation and resource enforcement; uses primary/documentation sources. |
| IQ3 Evidence boundaries | 2 | Clearly separates documented behaviour from unexecuted fault injection. |
| IQ4 Competing explanations | 2 | Separates election failure, stale resource epoch, missing enforcement and non-atomic validation with distinct observations. |
| IQ5 Next question or action | 2 | Specifies a concrete fault-injection matrix and records what to observe. |
| IQ6 Clarity and economy | 1 | The answer includes a subtle token-registration qualification that needs careful wording; the core protocol is still clear. |
| **IQ total** | **11/12** | |

| MPF dimension | Score | Note |
|---|---:|---|
| MPF1 Inventory first and concrete | 2 | Inventory precedes interpretation and maps coordinator, resource and token state. |
| MPF2 Proportionate selection | 2 | Uses only relevant core concepts and one candidate editor. |
| MPF3 Concept fidelity | 1 | Ledger is identified but the resource obligation is not fully quantified as energy/resource inflow and minimum maintenance payments. |
| MPF4 No unsupported mechanism | 2 | Lease and token mechanisms are sourced; no intention or automatic audit is attributed. |
| MPF5 Source use | 2 | Framework protocol consulted; Chubby and product mechanisms checked against source documentation. |
| MPF6 Reasoning audit actually used | 2 | Corrected the overly simple highest-token-seen explanation by distinguishing token issuance from what the protected resource has actually observed. |
| **MPF total** | **11/12** | |

**Integrity flags:** F1 No · F2 No · F3 No · F4 No · F5 No · F6 No.  
**Difference claimed?** No comparison condition was run.

**SCORES:** IQ_mp=11/12; MPF=11/12; scorer=self; blind=no

## Repository provenance

**Protocol retrieval (UTC):** 2026-11-27T10:23:16Z  
**Current main commit:** `c4405ba7a2c1572dee6ddb3cce151048e86cad39`

| File | Git blob SHA | SHA-256 |
|---|---|---|
| `tests/daily/README.md` | `04d295a20c67ff0774d89711c07a475616bf503e` | `d69d5220b45d68920d3cc9e1778dc1e0ff17d022dddcadac7ebb3770b09a8e74` |
| `tests/daily/SCORING.md` | `0b4f359fdeefdcdc55d55b94a94e8c8d801280a3` | `7f5045b4a3912ed1e951a79e6ac0b8b977fb70804074787d6454ab79d9bc9c79` |
| `tests/records/DEVELOPMENT_LOG.md` | `3e3f6913242cac552580caf556051003090041dd` | `77d70016210a6bcf64058184634db3b0f69c12a61aec149cec24d5b5f7d42a0b` |
