# Software Daily Test: DNS Endpoint Migration Under Cached and Stale Resolver State — 2026-11-20

## Test type
Software daily test. Test ID: MP-SOFTWARE-2026-11-20-01.

## Scenario
A service is moving from an old IP address to a new deployment. The operator changes the authoritative DNS record, but some clients continue reaching the old endpoint. The migration must preserve availability while recursive resolvers, forwarders, local stub resolvers and application-level caches hold different answers. The plan must also account for negative caching and resolvers that can serve stale data when they cannot refresh from authoritative servers.

## Operating invariant
Changing the authoritative record does not instantly invalidate answers already cached elsewhere. Both old and new endpoints must remain viable for the period during which real clients may still be directed to either one. The cutover and rollback plan must account for positive TTLs, negative TTLs, optional serve-stale behaviour and any additional client-side caching.

## Pre-interpretation Memory Prism inventory

| MP concept | What I identify in this query |
|---|---|
| Board | The DNS and service environment across authoritative name servers, recursive resolvers, forwarders, local stub resolvers, clients and both service endpoints. Each layer has its own state and failure conditions. |
| P-Memory (Persistent Memory) | Cached positive and negative DNS answers are persistent state left by earlier queries. A later authoritative change does not erase those cached answers in place. |
| Constraints | Resource-record TTLs, negative-cache TTLs, resolver policy, reachability of authoritative servers, client-side caches and the capacity of both service endpoints. |
| Editors | TTL expiry, successful refresh, negative caching and resolver stale-serving policy filter which answer continues to be returned to a client. |
| Ledger | The migration consumes a finite overlap budget: old-endpoint capacity, new-endpoint capacity, authoritative query volume after TTL reduction, monitoring and operator time, and time reserved for rollback. A low TTL can increase refresh traffic; closing the old endpoint too early spends the recovery margin. |
| Architecture | The layered separation between authoritative data, recursive caches, local resolvers and application clients explains why one record update does not change every consumer at once. |
| Flow Under Constraint (optional lens) | Queries and answers pass through caching layers; each layer can return its stored answer until its cache rules require refresh. |
| No Sacred States (optional lens) | TTL expiry does not always mean an expired answer disappears immediately: RFC 8767 permits a recursive resolver to serve stale data in specified refresh-failure conditions. |
| Audits (optional lens) | A cutover needs tests from representative recursive resolvers and actual client stacks, not just a check that the authoritative zone contains the new address. |

## Three-way planning comparison

### A. Conventional software planning
A conventional migration might lower the record TTL, wait for “DNS propagation,” change the address and shut down the old endpoint. This can work when the cache behaviour and timing assumptions are understood, but the phrase “DNS propagation” can obscure several separate states:
- A resolver may already hold the old answer with the original, longer TTL.
- A negative answer may be cached under the zone's SOA-derived negative TTL rather than the A/AAAA record's TTL.
- A recursive resolver may serve stale data if it cannot refresh from authoritative servers.
- An operating system, runtime or application may maintain an additional cache outside the recursive resolver.
- A and AAAA records, aliases and their targets may not all have been migrated consistently.

### B. MP-guided planning with a state and resource inventory
1. **Inventory the actual name chain.** Identify every relevant A and AAAA record, CNAME and target, authoritative zone, recursive resolver path, forwarder, local resolver and application cache. Do not assume that checking one resolver proves all clients see the same state.
2. **Lower positive TTLs early.** Publish the intended lower TTL and allow at least the previous, longer TTL interval to pass before cutover, allowing for zone publication and observed resolver behaviour. A newly published short TTL does not retroactively shorten copies already cached with the old TTL.
3. **Check negative caching separately.** RFC 2308 derives negative-answer caching from the minimum of the SOA record's TTL and the SOA MINIMUM field. Review that value before introducing a new name or depending on a previously non-existent name becoming visible.
4. **Prepare both endpoints.** Bring the new endpoint to readiness before changing DNS. Keep the old endpoint serving valid traffic and reserve enough capacity for clients that continue using cached old answers.
5. **Change authoritative data and verify it.** Confirm the intended records at the authoritative servers, then query a representative set of recursive resolvers and actual client environments. Observe A and AAAA separately.
6. **Keep an overlap window.** Do not retire the old endpoint merely because the authoritative answer has changed or one public resolver returns the new address. Retain it for the measured positive-cache horizon, relevant stale-serving policy and any additional client cache behaviour that exists in the deployed stack.
7. **Plan rollback as another cached transition.** Reverting the authoritative record does not instantly redirect everyone back. Keep both endpoints capable of serving traffic while the reverse cache transition takes effect.
8. **Reassess the Ledger.** A very short TTL may increase query and refresh load. Verify that authoritative infrastructure, recursive dependencies and both service endpoints have enough capacity for the chosen overlap and monitoring window.

### C. MP + Critical Thinking challenge pass
Challenge the migration at the boundaries where a simple TTL-only explanation fails:

- **TTL lowered too late:** resolvers that cached the old record before the change keep their remaining original TTL. The new TTL affects later answers, not already cached entries.
- **New name previously returned NXDOMAIN:** negative caching can preserve the non-existence answer according to the SOA-derived negative TTL. Lowering the A-record TTL does not clear it.
- **Authoritative server becomes unreachable during refresh:** RFC 8767 allows a recursive resolver to use stale data under specified conditions. Expiry alone is therefore not proof that the old address has stopped being served.
- **A and AAAA disagree:** IPv4 and IPv6 clients may continue reaching different endpoints if only one record family is changed or verified.
- **Application or local cache outlives the resolver answer:** DNS TTL does not automatically specify every application's own cache behaviour. Inspect and test the actual client stack rather than assuming protocol-level expiry controls every layer.
- **Rollback is treated as instantaneous:** the reverse update has its own cache and overlap period. Maintain service capacity for both directions.

Do not describe DNS as a globally synchronised switch. It is a distributed naming system whose cached views converge through expiration and refresh, with optional stale-answer behaviour in some failure conditions.

## Research-grounded insight
RFC 1035 defines a resource-record TTL as the time interval that the record may be cached before the source should be consulted again. That defines the cache lifetime of a particular answer; it does not remotely delete copies already held by resolvers.

RFC 2308 gives negative answers their own cache lifetime. For NXDOMAIN and NODATA responses, the authoritative server includes the zone's SOA record, and the negative TTL is based on the minimum of the SOA TTL and SOA MINIMUM field.

RFC 8767 defines serve-stale behaviour: when a recursive resolver cannot refresh expired data from authoritative servers, it may use retained expired data to improve DNS resilience. The feature is a refresh-failure resilience behaviour, not a promise that every resolver always serves stale data.

## Suggested implementation sequence
1. Map the full DNS record chain and the cache layers used by real clients.
2. Record current positive TTLs and the zone's negative-cache TTL.
3. Lower TTLs sufficiently ahead of the planned change and allow the previous TTL horizon to pass.
4. Prepare the new endpoint and confirm it can handle expected traffic.
5. Change authoritative records, verifying A and AAAA answers and any CNAME targets.
6. Observe answers from representative recursive resolvers and production client paths.
7. Maintain old/new endpoint overlap for the measured cache and client behaviour; keep rollback capacity.
8. Retire the old endpoint only when evidence shows that relevant traffic has drained and the remaining stale/client cache risk is acceptable.

## Failure modes and recovery
- **Traffic continues to the old endpoint:** keep it serving; determine whether the source is a valid cached answer, stale serving, an unmodified record or an application cache.
- **Some clients cannot resolve a newly introduced name:** inspect negative caching and the SOA-derived TTL before changing unrelated positive-record TTLs.
- **IPv4 works but IPv6 reaches the old service:** compare A and AAAA records and the client path separately.
- **Resolver answers disagree:** capture the resolver identity, answer, TTL and timestamp; do not label every difference propagation failure without identifying which cache returned it.
- **Rollback increases errors:** keep both endpoints viable and wait for the reverse cache transition while checking actual client resolution paths.
- **Authoritative query load spikes after TTL reduction:** review the cache-hit and query-volume effects, then adjust the TTL and capacity plan without assuming that a longer TTL removes all other cache layers.

## Capability contribution and attribution boundaries

| MP concept | Contribution to this test | Status |
|---|---|---|
| Memory / P-Memory (Persistent Memory) | Treats cached positive and negative answers as persistent state from earlier queries. | Applied to the DNS cache model. |
| Constraints | Makes TTL, negative-cache duration, resolver policy and endpoint capacity explicit. | Applied. |
| Editors | Explains how expiry, refresh, negative caching and stale-serving policy filter which answer remains usable. | Applied. |
| Board | Maps the authoritative, recursive, local and client environments at their relevant layers. | Applied. |
| Ledger | Accounts for old/new endpoint capacity, extra query load, operator time and rollback margin. | Applied. |
| Critical Thinking | Challenges the assumptions that an authoritative edit invalidates caches, that TTL reduction is retroactive, or that expiry always prevents stale answers. | Applied as a reasoning pass; not an independent blinded evaluator. |

## Evaluation criteria
- Existing cached answers are distinguished from newly published authoritative answers.
- The TTL reduction is made sufficiently early to account for the previously published TTL.
- Negative caching is handled independently from positive A/AAAA TTLs.
- Serve-stale behaviour is considered where the actual resolver supports it.
- A and AAAA plus relevant CNAME chains are verified.
- Old and new endpoints remain available for the measured overlap period.
- Rollback includes the time required for a reverse cache transition.
- The resource and time budget includes extra query load, monitoring and recovery capacity.
- No claim of instantaneous or globally simultaneous DNS propagation is made.

## Limits
This is a documentation-grounded migration scenario, not a live DNS cutover. No resolver fleet, application runtime or production domain was queried. Resolver serve-stale configuration, local/application caching and TTL clamping vary by implementation and must be measured in the actual environment. The test does not claim that all recursive resolvers serve stale data.

## Sources
- Mockapetris, P. (1987), RFC 1035, “Domain Names — Implementation and Specification,” Resource Record format and TTL. https://www.rfc-editor.org/rfc/rfc1035.html
- Andrews, M. (1998), RFC 2308, “Negative Caching of DNS Queries (DNS NCACHE).” https://www.rfc-editor.org/rfc/rfc2308.html
- Lawrence, D., Kumari, W. and Sood, P. (2020), RFC 8767, “Serving Stale Data to Improve DNS Resiliency.” https://www.rfc-editor.org/rfc/rfc8767.html

## Provenance
Assistant-selected software topic for 2026-11-20, deliberately outside recent database-maintenance, message-processing and production-logistics topics. Standards-grounded scenario comparing conventional planning, MP-guided state/resource accounting and an MP + Critical Thinking failure-boundary pass. No live DNS configuration, cutover or production outcome is claimed.
