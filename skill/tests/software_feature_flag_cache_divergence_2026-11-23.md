# Software Daily Test: Inconsistent Feature-Flag State Across Distributed Caches

**Test ID:** MP-SOFTWARE-2026-11-23-01  
**Date:** 2026-11-23  
**Type:** Assistant-selected software scenario; documentation-informed design and failure analysis  
**Status:** Closed as a documentation-grounded analysis. No live distributed deployment, code change, or production measurement was performed.

## Scenario

A service runs 30 instances. A feature flag changes from OFF to ON. Some instances begin serving the new behaviour quickly, while others continue using stale configuration for minutes. A subset of instances restarts during propagation.

The operating question is: when is the change actually in effect, how can divergence be detected, and what should each instance do when it cannot obtain fresh configuration?

## Selective Memory Prism inventory

| MP concept | Mapping to the subject |
|---|---|
| P-Memory | Each process retains its locally adopted configuration snapshot and version |
| Board | Instances, configuration control plane, network, SDKs, local stores, deployment environment |
| Constraints | Polling interval, stream interruption, network partitions, restart timing, cache lifetime, and rollout policy |
| Editors | Update delivery, local adoption, refresh logic, fallback behaviour, and targeting rules |
| Ledger | Network requests, refresh work, cache capacity, latency budget, and recovery capacity |
| Architecture | A central configuration source with independently updated local copies |
| Working Lines | Streaming, polling, relay/proxy delivery, and local cache refresh paths |
| Accumulation Patterns | Each instance accumulates its own history of received and adopted configuration versions |
| Audits | Per-instance version and freshness reporting can reveal which processes remain stale |

## System behaviour and evidence

Feature-flag SDKs commonly maintain local configuration state and evaluate flags locally, rather than making a remote request for every application decision. LaunchDarkly documents streaming and polling update modes and local in-memory evaluation. AWS AppConfig Agent similarly caches configuration locally and refreshes it in the background; its documented behaviour can continue serving the last known good configuration when the configuration source is unavailable.

This makes local caching both a resilience mechanism and a source of divergence. A configuration update has at least three distinct moments:

1. The control plane accepts or publishes the new configuration.
2. The update is delivered to a particular instance.
3. That instance adopts the new version and begins evaluating against it.

Those moments are not interchangeable. A successful control-plane update does not prove that every process has adopted the new state.

AWS AppConfig also documents entity-based gradual deployment, which can preserve a consistent configuration version for a given entity across compute resources during a rollout. LaunchDarkly documents stale-cache troubleshooting and the possibility of instances remaining out of sync within cache/refresh behaviour.

## Findings and design implications

### 1. Define effectiveness at the instance level

Version the configuration. Each instance should expose at least its adopted version, last successful refresh time, cache age, and delivery/connection state. Fleet-level reporting should show propagation latency and the distribution of adopted versions—not merely whether the control plane reports a successful publish.

### 2. Choose stale-state policy by consequence

There should not be one universal stale-cache rule for every flag.

- Cosmetic or low-risk presentation flags may tolerate brief divergence.
- Gradual rollouts should use stable assignment for the relevant user or entity, avoiding arbitrary behaviour changes between requests.
- Data-migration or routing flags need explicit compatibility and version checks.
- Emergency kill switches need a stronger freshness objective and a clearly specified response when an instance is disconnected.
- Access-control and security decisions should not rely on a stale feature flag as the sole security boundary.

### 3. Make recovery behaviour explicit

Specify whether each flag serves last-known-good state, fails closed, or follows another fallback when refresh fails. Test stream interruption, polling delay, restart during rollout, network partition, stale cache, recovery, and rollback. Record both the duration and scope of divergence.

### 4. Treat audits as state reconstruction

The important audit question is not simply “did we publish the flag?” It is “which instances adopted which version, at what time, and what behaviour did they serve before adoption?” This reconstructs the actual fleet state rather than assuming the control-plane state is universal.

## Main finding

The cache is simultaneously a resilience layer and a divergence boundary. The system's real configuration state is distributed across independently updated processes. A reliable rollout therefore needs version visibility, per-instance adoption evidence, consequence-specific stale-state policy, and tested recovery behaviour.

## Limits

- This is a design/failure analysis based on public product documentation, not a live test of LaunchDarkly, AWS AppConfig, or a custom feature-flag service.
- Exact propagation guarantees depend on SDK, configuration, topology, and service plan; no universal propagation time is asserted.
- No measured reliability improvement or performance result is claimed.

## Sources

- LaunchDarkly documentation: SDK configuration delivery, streaming and polling, and local in-memory evaluation.
- LaunchDarkly documentation: troubleshooting stale configuration and persistent-store/cache consistency.
- AWS AppConfig Agent documentation: local configuration caching, background refresh, and last-known-good behaviour.
- AWS AppConfig documentation: entity-based gradual deployments and consistent entity assignment.
