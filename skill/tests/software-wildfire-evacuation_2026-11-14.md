# Wildfire evacuation coordination — software daily test — 2026-11-14

## Test type
Software daily test. Scenario independently invented for this date and not selected from recent conversation topics.

## Scenario
A fast-moving wildfire threatens several settlements. Wind changes alter the projected fire path; some roads close, evacuation traffic builds, buses and accessible transport are needed, and shelters approach capacity. Emergency managers need a shared operational picture while information is incomplete and changing.

## Core problem
Coordinate evacuation-relevant information without allowing software to silently assume legal authority or convert uncertain estimates into claims of safety.

The system may need to reconcile:
- fire perimeter, spread estimates, wind and uncertainty;
- evacuation zones, orders, warnings and their issuing authorities;
- road closures, capacity, congestion and responder access;
- buses, accessible vehicles, pickup points and passenger manifests;
- hospitals, care homes and residents needing assistance;
- shelter locations, verified capacity, staffing and supplies;
- warnings sent, acknowledged, delivery failures and evacuation progress.

## Operating invariant
Every operational recommendation must be traceable to current, time-stamped information and must preserve the distinction between an authorised decision, a modelled estimate, a reported observation and an unverified assumption. The system must not issue legal evacuation orders or declare a route safe on its own.

## Three-way planning comparison

### A. Conventional software planning
A conventional approach would likely begin with stakeholder requirements, data sources, role-based access, maps, status dashboards, alerting, integrations and workflow definitions.

Strengths:
- Familiar decomposition into users, modules, interfaces and integrations.
- Can produce a conventional backlog and implementation plan.

Risks to test:
- Requirements may treat feeds and status fields as authoritative without recording provenance or freshness.
- A dashboard can make stale or uncertain data look current.
- The design may focus on displaying evacuation status without resolving conflicts between orders, road conditions, transport capacity and shelter capacity.

### B. Memory Prism-guided planning
Pre-interpretation inventory:

| MP concept | What I identify in this query |
|---|---|
| Board | The incident area and its changing operational state, bounded by fire behaviour, road networks, available transport, shelter capacity and emergency authority. |
| Memory | Prior reports, incident updates, orders, acknowledgements and status records persist and may become stale. |
| Constraints | Fire spread, weather, road capacity, travel time, vehicle availability, accessibility, shelter capacity and legal authority. |
| Editors | Authorised officials issue or revise orders; dispatchers allocate resources; field reports and verified feeds update the operational picture. |
| Flow Under Constraint | People, vehicles, information and resources move through a changing network under time pressure. |
| Audits | Every status needs source, timestamp, confidence/verification state and change history. |
| Identity | A location, road segment, shelter, vehicle or person must retain stable identity across changing reports and systems. |
| Working Lines | The system must distinguish observed, reported, modelled, planned, ordered, acknowledged and completed states. |
| No Sacred States | No route, shelter capacity or risk estimate should remain trusted merely because it was previously accepted. |
| Accumulation Patterns | Congestion, unmet transport demand, shelter occupancy and unacknowledged warnings accumulate over time. |

Likely planning improvements:
- Treat freshness and provenance as first-class data, not optional metadata.
- Model the incident as a changing network of dependencies rather than a static map with pins.
- Keep separate state transitions for proposed, authorised, communicated, acknowledged and completed actions.
- Make uncertainty visible and prevent stale values from silently persisting as facts.
- Plan for partial connectivity, duplicate reports, contradictory feeds and delayed updates.

### C. Memory Prism + Critical Thinking
Critical Thinking adds an explicit challenge to the proposed explanation and design:
- What is the actual operational invariant, rather than the dashboard's apparent purpose?
- Which facts are measured, reported, inferred, planned or authorised?
- What evidence would falsify the current route or capacity assumption?
- Can the proposed automation be supported by available data and decision authority?
- What happens when two authoritative sources conflict, or when no source is current?

This examination should challenge MP-derived candidate mappings too; MP concepts do not make a mapping true merely by naming it.

## Capability contribution and attribution boundaries

| Capability | Relevance to this scenario | Status |
|---|---|---|
| Memory Prism | Exposes persistent state, constraints, editors, state transitions and accumulated pressures. | Applied as a planning lens. |
| Critical Thinking | Challenges assumptions, tests claim levels and asks what evidence would break the design. | Applied as an examination lens; not an isolated blind run. |
| CT optional MP checklist | “For a query, does the ledger reconcile for that board under the specific constraints and editors?” | Optional; not treated as a separate full MP application. |
| Optionality | Supports alternate evacuation, transport and shelter paths when a route or resource fails. | Relevant design consideration; no standalone execution. |
| Good-Faith Collaboration & Approach Calibration | Helps reconcile conflicting reports and role-specific interpretations without pretending all sources have equal authority. | Relevant design consideration; no standalone execution. |
| Task Integrity | Keeps the delivered system within the requested coordination scope rather than silently taking command authority. | Relevant design consideration; no standalone execution. |
| Verification Integrity | Requires evidence before marking routes, warnings, transport or evacuation as verified/completed. | Relevant design consideration; no standalone execution. |
| Software Literacy | Tests whether proposed live feeds, geospatial processing, optimisation and integrations are technically supportable. | Relevant design consideration; no standalone execution. |
| Peer Review | Could review preserved outputs and challenge omissions. | Not run. |
| Automaticity | Could support routine checks and alerting once their conditions and authority are explicit. | Potential only; not run. |
| A Touch of Grace | Could improve communications under stress without obscuring operational facts. | Potential only; not run. |
| AEL Runtime Accountability | Could record who/what made a decision, under which authority and evidence. | Supporting infrastructure; not executed. |
| Q-Batch of Evidence | Could run isolated conditions and preserve comparable outputs for offline evaluation. | Supporting infrastructure; not executed. |
| Faking Vision / FV Robots / Self-Learning POC | No demonstrated need in this scenario. | Not applicable to this test. |

## Suggested architecture and sequencing
1. **Authority and source model:** identify who can issue orders, who can report observations, and which systems provide estimates. Define provenance, timestamps, confidence and conflict handling.
2. **Core incident state:** represent zones, roads, shelters, facilities, vehicles and people/resources with stable identities and explicit state histories.
3. **Operational constraints:** model travel times, road capacity, accessibility, shelter capacity, staff and responder access.
4. **Coordination workflows:** support authorised zone changes, transport dispatch, shelter assignment, warnings, acknowledgements and exception handling.
5. **Resilience:** handle stale feeds, loss of connectivity, duplicate/conflicting reports, offline field updates and degraded operation.
6. **Decision support:** only after the data and authority model is reliable, add route and resource recommendations with visible uncertainty and human approval.
7. **Evaluation:** replay realistic incident timelines, including wind shifts, road closures, failed communications, shelter saturation and contradictory reports.

## Failure modes and recovery paths
- **Stale perimeter or weather feed:** mark stale, preserve last-known value with timestamp, request alternate confirmation; never present it as current.
- **Road closure not propagated:** reconcile field reports and transport telemetry; allow an authorised dispatcher to block a route pending verification.
- **Shelter capacity over-reported:** distinguish nominal, staffed, accessible and currently available capacity.
- **Warning delivered but not acknowledged:** keep delivery and acknowledgement as separate states; trigger follow-up through alternate channels.
- **Vehicle or passenger status duplicated:** use stable identities and idempotent event handling; retain conflict records for resolution.
- **Network outage:** support offline lists and radio/voice fallback, with later reconciliation that does not overwrite newer verified events.
- **Conflicting evacuation instructions:** surface the conflict and authority chain; do not resolve it by silently choosing the latest timestamp.

## Evaluation criteria
1. Did the approach identify the actual operating invariant?
2. Did it distinguish real-world state from recorded or assumed state?
3. Did it expose dependencies and authority boundaries?
4. Did it identify failure modes and recovery paths?
5. Did it improve implementation sequencing?
6. Did it question whether proposed capabilities are technically and operationally supportable?
7. Did it reduce unnecessary cognitive load without replacing useful domain detail with framework jargon?

Do not award a higher result merely for longer or more technical output. Attribute MP and CT contributions separately. Do not infer independent causal contributions from sequential same-assistant reasoning in one conversation.

## Research basis
- NIST Technical Note 2262r1 (March 2025), *WUI Fire Evacuation and Sheltering Considerations: Assessment, Planning, and Execution (ESCAPE)*. It discusses decision support, evacuation timing relative to fire arrival, decision zones and the role of authorised officials.
- NIST 2025 update on pre-planning, multiple routes and communication methods, dynamic decision zones, and circumstances in which nearby sheltering may be safer than vehicle evacuation.
- Systematic review of wildfire evacuation infrastructure and planning, including transport networks, congestion, exposure, vulnerable populations, shelters and resource coordination.
- 2023 goal-programming research on early evacuation of vulnerable people and relief distribution.

## Limits
This is a scenario-based planning analysis, not a deployed-system test, user study, tabletop exercise or isolated A/B experiment. No capability has been shown to improve evacuation outcomes. The authority model, data quality and operational procedures require validation with emergency-management professionals and local law.

## Provenance
Prepared from the 2026-11-14 daily test research and analysis in this conversation. AEL, Q-Batch and Peer Review were not executed.
