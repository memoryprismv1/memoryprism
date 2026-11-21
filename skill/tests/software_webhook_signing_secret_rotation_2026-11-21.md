# Software Daily Test: Planned Rotation of Webhook Signing Keys — 2026-11-21

## Test type
Software daily test. Test ID: MP-SOFTWARE-2026-11-21-01.

## Scenario
A service sends signed webhook events to a receiver. The signing key is due for routine rotation. The sender and receiver are operated by the same organisation, and the signature format can carry multiple signatures during a transition. Deliveries must continue while configuration changes roll out, and the receiver must reject forged, altered, stale or duplicate events.

This is a planned rotation. Suspected compromise is a separate case: a key known to an attacker must not remain trusted merely to make the transition convenient.

## Operating invariant
Every accepted delivery must validate against a currently trusted key and the exact content and authenticated metadata. A planned rotation should avoid a delivery gap; retries must not apply the same logical event twice; and the old key must cease to be trusted after the authorised overlap. A compromised key must be revoked, not retained as a compatibility fallback.

## Pre-interpretation Memory Prism inventory

| MP concept | What I identify in this query |
|---|---|
| Board | Publisher, receiver, secret store, deployed receiver instances, delivery queue/retry system, network and downstream event processor. Instances may hold different configuration versions during rollout. |
| P-Memory (Persistent Memory) | Durable key-version state and the receiver's record of processed event IDs preserve which credential was active and which logical events have already taken effect. |
| Constraints | Deployment timing, secret propagation, signature format, retry horizon, timestamp tolerance, clock skew, key-storage access and event-processing capacity. |
| Editors | Signature verification, activation/revocation, freshness checks, retries and idempotency determine which deliveries are accepted and which effects persist. |
| Ledger | The overlap creates a finite security-exposure window; the operational account also includes deployment time, retry backlog, monitoring and recovery capacity. The old key's trust must not remain open indefinitely. |
| Architecture | Signing, verification, secret storage, event identity, replay checks and business processing are separate stages. Verification must use the same body bytes that were signed. |
| Identity (optional lens) | Key version identifies the credential used; webhook/event ID identifies the logical event across attempts. They must not be conflated. |
| Working Lines (optional lens) | Secret distribution, publisher signing, receiver verification, retries and downstream processing form separate paths. A component left on old-only configuration can break the cutover. |
| No Sacred States (optional lens) | “New key installed” is not a global state while instances roll, queues contain old attempts and configuration propagates at different speeds. |

## Mechanism and evidence

### 1. Signature validity, freshness and one-time processing are different properties
The Standard Webhooks specification recommends signing the event ID, delivery-attempt timestamp and body together. The attempt timestamp is refreshed on retries, while the logical event ID stays the same. The timestamp supports replay protection; the stable event ID supports idempotency. These solve different problems:

- Signature verification authenticates the signed content and metadata.
- Timestamp tolerance limits acceptance of old captured attempts.
- Event-ID deduplication prevents repeated delivery of one logical event from creating a second effect.

A receiver that only checks a valid HMAC but ignores freshness and event identity is incomplete.

### 2. Verify the actual request bytes
JSON parsing and re-serialization can change whitespace, ordering or escaping. Standard Webhooks warns that the sent body must be the same as the body that was signed. GitHub's guidance likewise demonstrates verifying the received payload body with HMAC-SHA256 and using a constant-time comparison. The receiver should preserve the raw body for verification, reject altered content, and only then parse it.

### 3. Planned rotation can use a bounded overlap where the protocol supports it
Standard Webhooks defines the signature header as a list of signatures to support zero-downtime key rotation. During a planned transition, the sender can sign with both current and old keys for a set period, and a receiver can test the signatures against its configured trusted keys.

A controlled sequence is:
1. Generate a new endpoint-specific key and store it securely as a new version; do not overwrite the old value in place.
2. Deploy receiver support for both current and next key versions to every active instance.
3. Confirm the receiver fleet has converged, then configure the sender to emit both signatures using the specified format.
4. Test old-only, new-only, invalid, altered-body, stale-timestamp and duplicate-event cases.
5. Monitor which key version validates real deliveries, including queued and retried attempts.
6. Stop signing with the old key, then remove it from the receiver trust set after the planned overlap and relevant retry period.
7. Verify that an old-only signature is rejected after retirement.

Provider support is a constraint: not every webhook service supports multiple signatures or the same rotation sequence. Verify the actual provider's documented behaviour rather than assume Standard Webhooks compatibility.

### 4. Important security finding: the specification's compromise advice is unsafe as written
The Standard Webhooks specification says its multiple-signature rotation can apply even in circumstances such as key compromise. It says that signing with multiple keys, “even compromised ones,” does not diminish security because a consumer still requires a valid signature.

That assurance does not follow from the described verifier behaviour. The same specification says consumers may try each signature until one matches. If an attacker possesses the old symmetric key and the receiver continues trusting it, the attacker can generate a valid old-key signature. The attacker can also choose a fresh timestamp and a new event ID if those fields are not otherwise constrained. The receiver's “one valid signature is enough” rule would accept the forged request. Therefore, overlapping acceptance of a known-compromised key preserves the attacker's ability to forge deliveries during the overlap.

The safer branch is:
- Routine, planned expiry: bounded dual-key overlap can support continuity.
- Suspected or confirmed compromise: revoke the compromised key immediately; do not accept old-key-only signatures as a fallback. Handle delivery disruption through the incident and recovery process.

This is a reasoning challenge to the source specification's security claim, not a claim that the specification itself makes this distinction.

### 5. Retry handling needs durable identity
Standard Webhooks recommends a stable webhook ID as the idempotency key and explains that the same ID remains across retries, while the attempt timestamp changes. Its operational guidance recommends retries over multiple days. A receiver should not rely solely on a short timestamp window or a very short deduplication cache where its actual replay/retry horizon is longer. Retention and idempotent side effects must be designed for the provider's real retry and recovery behaviour.

## Suggested implementation and verification sequence
1. Classify the reason for rotation: routine/expiring or suspected compromise.
2. Identify the provider's signature scheme, key distribution behaviour, all receiver instances, delivery queues, retry schedule and downstream side effects.
3. For planned rotation, stage the new key and dual-key receiver support before enabling dual signing.
4. Verify the raw body plus authenticated metadata; use constant-time comparison for symmetric signatures.
5. Test key versions, invalid signatures, body mutation, stale timestamps, duplicate IDs, concurrent retries and receiver instances with different configuration versions.
6. Monitor key-version acceptance, configuration convergence, delivery failures, retry age and duplicate suppression.
7. Stop using the old key, remove it from the trusted set and verify that old-only signatures fail.
8. If compromise is suspected, skip the compatibility overlap and revoke the old key; investigate exposure and recover failed deliveries without trusting the compromised credential.

## Failure modes and recovery
- **Receiver instances disagree about trusted keys:** inspect deployed configuration versions and secret-store propagation; complete or roll back the receiver rollout before switching the sender.
- **New signature fails while old succeeds:** check key selection, signature format, signed bytes and deployment state. Preserve old trust only for a planned rotation.
- **Deliveries fail during overlap:** check every receiver instance and the sender's actual signature header; rely on durable retries while correcting the mismatch.
- **Body verification fails after parsing:** verify the untouched raw request body before parsing or re-serializing JSON.
- **Old key still validates after retirement:** check every worker, verifier and cached key version; remove trust consistently and test rejection.
- **Retry creates a duplicate effect:** make event-ID deduplication durable and atomic with the business-state update.
- **Captured request is accepted too late:** enforce signed attempt-timestamp tolerance and clock synchronisation; do not treat event-ID deduplication as a substitute for replay protection.
- **Old key may be compromised:** revoke it; do not restore old-key acceptance merely to make the normal rotation sequence pass.

## Evaluation criteria
- Trusted active signatures validate; invalid signatures and modified bodies fail.
- Verification uses exact request bytes and constant-time comparison for HMAC.
- Authenticated timestamp freshness is checked.
- A repeated logical event cannot create a second business effect.
- Planned overlap is bounded, observable and removed.
- Old-only signatures fail after retirement.
- A compromised key is not retained as a trusted fallback.
- Secret values and raw signatures are excluded from source control and routine logs.

## Limits
This is a standards-grounded design and failure-analysis scenario, not a live webhook implementation or key rotation. No sender, receiver, secrets manager, queue or production delivery stream was configured. Multiple-signature overlap applies only where the selected protocol/provider supports it. Actual retry horizons, timestamp tolerance and key distribution behaviour must be verified for the chosen implementation.

## Sources
- Standard Webhooks, specification: https://github.com/standard-webhooks/standard-webhooks/blob/main/spec/standard-webhooks.md (multiple signatures and rotation: § webhook headers; signed ID/timestamp/body, freshness and idempotency: § verifying webhook authenticity).
- GitHub Docs, “Validating webhook deliveries”: https://docs.github.com/en/webhooks/using-webhooks/validating-webhook-deliveries

## Provenance
Assistant-selected software topic for 2026-11-21, outside recent DNS migration, database maintenance and event-processing topics. Standards-grounded design exercise. Includes a critical examination of the Standard Webhooks specification's claim about keeping a compromised key in a multiple-signature rotation. No live implementation, credential or production event stream was tested.