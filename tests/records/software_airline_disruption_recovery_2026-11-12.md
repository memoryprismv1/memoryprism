# Software Daily Test: Multi-Airport Airline Disruption Recovery
**Test ID:** MP-SOFTWARE-2026-11-12-01  
**Date:** 2026-11-12  
**Selection:** Assistant-invented scenario selected independently of the user's recent conversations, projects, interests, phrasing or hypotheses.

## Scenario
A severe weather system closes a major hub airport for eight hours. Flights already airborne are diverted to several neighbouring airports. Some alternates have limited parking, ground handlers, gates, fuel, passenger processing and customs capacity. The hub's closure time is uncertain. Aircraft are now out of position; crews face duty-time limits; connecting passengers are stranded; aircraft rotations and subsequent flights are disrupted. Weather is also degrading capacity at one alternate.

An airline group needs a coordination platform spanning its operations control centre, airport partners, ground handlers, crew control, maintenance, passenger services and external air traffic/network management partners.

The platform should coordinate disruption facts, candidate recovery plans, resource constraints, approvals, execution events, passenger reaccommodation and communications. It must not replace air traffic control, airport authority, flight dispatch, licensed operational judgement or safety procedures.

## Research grounding
- Su et al. (2021), *Airline Disruption Management: A Review of Models and Solution Methods*, describes disruption from weather, airport closure and maintenance, and the recovery of aircraft, crews and passengers by airline operations control: https://doi.org/10.1016/j.eng.2020.08.021
- EUROCONTROL Airport Collaborative Decision Making describes transparent, timely information exchange among airport operators, aircraft operators, ground handlers, ATC and the Network Manager, particularly around turn-round and pre-departure processes: https://www.eurocontrol.int/concept/airport-collaborative-decision-making
- EUROCONTROL's 2025 A-CDM specification describes milestone-based tracking linking inbound flights to outbound turn-round estimates and notifications: https://www.eurocontrol.int/publication/eurocontrol-specification-airport-collaborative-decision-making-cdm
- A September 2026 research paper examines collaborative airline/network-manager recovery with capacity constraints and fairness considerations: https://www.sciencedirect.com/science/article/pii/S1366554526003169

## Baseline: conventional software planning
A conventional decomposition would include:
- disruption event intake and operational situation board;
- flight, aircraft, tail, route, slot and airport-capacity data;
- diversion handling and alternate-airport capacity;
- aircraft rotation and fleet recovery;
- crew assignment, qualification, location and duty/rest legality;
- passenger itinerary, reaccommodation, connection protection and care;
- maintenance, fuel, parking, gates, stands, ground handling and baggage;
- partner communication and acknowledgement;
- recovery-plan options, approval and execution tracking;
- customer notifications and estimated recovery times;
- integrations, access control, audit logs, resilience and reporting.

This is a sensible baseline but risks becoming a collection of modules without a clear account of which operational facts are authoritative, how conflicting plans are reconciled, or when a recovery option is no longer feasible.

## MP pass — full framework
### Pre-interpretation inventory
| MP concept | What I identify in this query |
|---|---|
| Board | A distributed airline/airport/network operating environment under weather, capacity, safety, legal, commercial and passenger-service constraints. |
| Memory | Flight and aircraft rotations, crew duty history, passenger itineraries, airport resources, disruption decisions, milestones and execution history. |
| Constraints | Runway/airspace capacity, weather, slots, stands, gates, handling, fuel, maintenance, crew duty/rest, border processing, passenger needs and airport curfews. |
| Editors | Airline operations control, crew control, maintenance control, airport operations, ground handlers, ATC/network management and authorised dispatch/flight operations roles. Their authority is not interchangeable. |
| Flow Under Constraint | Aircraft, crews, passengers, baggage, information, service capacity and recovery instructions move through linked but distinct networks. |
| Audits | Reconcile planned vs cleared vs executed flight movements, resource reservations, crew legality, passenger reaccommodation and service delivery. |
| Identity | Flight instance, aircraft tail, crew member, passenger itinerary/booking, airport resource, diversion event and recovery plan need stable identities. |
| Working Lines | Flight legs, aircraft rotations, crew pairings, passenger connections, ground-handling chains and partner communications are distinct operational paths. |
| No Sacred States | Scheduled, estimated, assigned, accepted, departed, arrived, diverted, parked and boarded are not equivalent states; a plan is not execution. |
| Accumulation Patterns | Aircraft displacement, crew duty consumption, missed connections, baggage separation, gate/stand queues, passenger-care demand and network delays accumulate and propagate. |

MP organising model: maintain linked but separate operational histories for flight movement, aircraft rotation, crew legality/location, passenger itinerary and care, airport/ground resource availability, and authority/approval. A diversion recorded by an airline is not proof of landing; an airport stand reservation is not proof the aircraft is parked; a proposed crew reassignment is not proof it is legal or accepted.

## Critical Thinking pass
Reconstruct the operational trajectory and challenge assumptions:
1. Weather forecast and capacity restriction emerge; airline/network partners revise capacity estimates.
2. Flights airborne receive diversion instructions from the relevant operational authorities; the airline records the operational event but does not issue ATC clearances.
3. The alternate airport accepts or refuses each arrival based on actual capacity, not nominal capacity alone.
4. On landing, the aircraft needs a stand, handling, fuel, passenger processing and potentially maintenance; a runway slot does not guarantee these resources.
5. The crew's duty clock and rest requirements continue to constrain recovery; moving an aircraft without a legal crew plan may simply create a stranded asset.
6. Passengers on the diverted flight may have different onward routes, immigration status, accessibility needs and connection priorities. Rebooking a passenger does not move their baggage or guarantee a seat on the new flight.
7. The reopened hub may have reduced capacity and a backlog; “airport open” does not mean normal throughput.
8. Recovery plans must account for knock-on rotations at downstream airports, curfews, aircraft maintenance windows, crew positioning and the next day's schedule.
9. The same scarce seat, stand, crew or aircraft cannot be committed to multiple recovery options simultaneously.
10. Forecasts, estimated times and resource statuses must carry provenance, update time and uncertainty. Late partner messages can invalidate a previously viable plan.
11. The platform can calculate and compare feasible options, but cannot decide flight safety, issue ATC clearances or override legal/operational authority.

Potential invariant: every proposed recovery action must remain feasible against the latest known flight, aircraft, crew, airport-resource and passenger states, with the relevant authority's approval and execution separately evidenced.

## Optionality pass
The useful output is not one “optimal recovery plan” too early. Preserve materially different strategies:
- **Return-to-hub first:** prioritise positioning aircraft back once the hub reopens; may increase congestion and leave passengers at alternates longer.
- **Operate from alternates:** temporarily run selected flights from diversion airports; may preserve some passenger journeys but requires crews, aircraft, handling and passenger redistribution.
- **Cancel and reset:** cancel selected rotations and reposition aircraft/crews for the next operating period; sacrifices immediate service but can prevent cascading infeasible promises.
- **Protect critical connections/passengers:** prioritise passenger continuity and care over maximising flight count; can increase fleet/crew recovery cost.
- **Network-wide coordinated recovery:** coordinate with the network manager and airports using capacity and fairness constraints; may require accepting a locally suboptimal airline plan.

These are strategies with different costs and dependencies, not interchangeable buttons. The system should preserve alternatives with their assumptions and expiry conditions, and identify when new information invalidates one.

## Good-Faith Collaboration & Approach Calibration pass
Do not assume the first proposed architecture is right. Investigate whether this should be a new central platform, a coordination layer over existing airline/airport systems, or a narrower recovery-decision service. Challenge the model's own assumptions about data access, real-time partner integration, and who owns operational decisions. If reliable real-time capacity feeds are unavailable, state that constraint and design a degraded/manual workflow rather than pretending integration exists. Do not ask the user to supply ordinary domain research the assistant can investigate.

## Task Integrity pass
Preserve the requested scope across the full disruption lifecycle: airborne diversions, arrival acceptance, airport resources, aircraft/crew recovery, passenger/baggage recovery, downstream rotations, partner coordination, approvals, execution and communications. Record exclusions (ATC control, dispatch authority, safety decisions). Track assumptions, sources, versions, unverified integrations and what is actually tested. Prevent a polished architecture from implying that live feeds, partner permissions or operational approval pathways have been secured.

## Verification Integrity pass
Make completion cheap to check:
- each diversion reconciles to an actual arrival/departure event or explicit unresolved status;
- each aircraft assignment reconciles to tail identity, location, maintenance state and next-leg feasibility;
- each crew assignment reconciles to qualification, duty/rest legality, acceptance and actual report;
- each passenger reaccommodation reconciles to a confirmed seat/booking, ticket status, baggage handling and passenger notification;
- each airport resource reservation reconciles to a partner acknowledgement and actual use/release;
- each recovery plan has version, assumptions, approver, expiry and execution outcome;
- every estimated time and capacity figure shows source, timestamp and confidence/status.
A dashboard green state is not evidence unless its underlying event and source can be inspected.

## Software Literacy pass
Explain consequential design choices in user-decision terms:
- A **system of record** is the authoritative place where a particular fact is maintained; not every partner shares one.
- An **event stream** records what happened and when; it does not automatically make the event true or authoritative.
- An **optimiser** can suggest a plan from supplied constraints; it cannot guarantee the constraints are complete or current.
- **Integration** is not simply “connect the APIs”; partner data rights, schemas, freshness, uptime, identity matching and correction rules matter.
- A central platform may simplify coordination but risks becoming a false authority. A federated coordination layer may respect existing systems but needs reconciliation and degraded-mode handling.
The human should be able to decide scope and risk without having to understand implementation internals.

## Peer Review pass
Review the proposed architecture against its purpose, not the number of modules. Findings:
- **Critical omission risk:** passenger and baggage state can diverge; a rebooked passenger may have baggage still routed elsewhere.
- **Authority risk:** airline coordination software could be mistaken for operational control or ATC authority.
- **Capacity risk:** airport acceptance, stand availability, ground handling, passenger processing and fuel are separate constraints.
- **State/provenance risk:** plans, partner acknowledgements and physical events must not be collapsed.
- **Recovery risk:** reopening the hub does not clear aircraft, crew and passenger backlogs automatically.
- **Fairness risk:** optimisation criteria may disadvantage passengers with complex itineraries or airlines with weaker bargaining power for scarce network capacity.
- **Coverage gap:** contingency operations during prolonged partner-system outages need explicit treatment.
No implementation files were built; this is a planning review, not a code review.

## Interface passes
- **Automaticity:** keep the user-facing explanation readable without removing operational distinctions.
- **A Touch of Grace:** surface findings and necessary caveats, not unsolicited commentary about the user or previous assistants.

## Other creations: fit and boundaries
- **AEL Runtime Accountability:** potentially useful for recording who proposed, authorised and executed a decision, with provenance and decision authority. It is a separate runtime/accountability layer, not a flight-recovery optimiser or source of operational truth. This scenario does not execute AEL.
- **Q-Batch of Evidence:** appropriate method for running isolated resource conditions and comparing preserved outputs offline. It is the evaluation infrastructure, not a capability inside the airline platform.
- **Faking Vision:** not materially relevant to this text/data coordination scenario; no visual-media investigation requirement. Do not force it into the architecture.
- **Peer Review:** used here as a post-hoc review capability; it does not replace independent review or Q-Batch isolation.

## Shared qualitative criteria
Scores 0–2 are provisional self-assessments of what each pass surfaced, not empirical effect sizes.

| Criterion | Conventional | MP | CT | Optionality | Task Integrity | Verification Integrity | Software Literacy | Peer Review |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Identifies operational invariant | 1 | 2 | 2 | 1 | 1 | 1 | 0 | 1 |
| Separates real vs recorded/assumed state | 1 | 2 | 2 | 1 | 2 | 2 | 1 | 2 |
| Exposes dependencies/authority | 1 | 2 | 2 | 1 | 1 | 1 | 2 | 2 |
| Identifies failure/recovery paths | 1 | 1 | 2 | 2 | 1 | 2 | 1 | 2 |
| Improves sequencing/decision options | 1 | 1 | 2 | 2 | 2 | 1 | 1 | 1 |
| Challenges technical supportability | 1 | 1 | 2 | 1 | 1 | 1 | 2 | 2 |
| Reduces checking/decision burden | 1 | 1 | 1 | 1 | 2 | 2 | 2 | 1 |
| **Provisional total / 14** | **7** | **10** | **13** | **9** | **10** | **10** | **9** | **11** |

Do not interpret these numbers as controlled evidence. The passes are sequential and share context. Scores are a structured way to expose hypotheses about contribution; blind external evaluation is needed to test them.

## Attribution summary
- **Memory Prism:** provides an inspectable structural map of the operating environment and its linked histories.
- **Critical Thinking:** challenges the map and proposed explanations, reconstructs causal sequence and exposes unsupported assumptions.
- **Optionality:** preserves materially different recovery strategies before premature optimisation.
- **Good-Faith Collaboration & Approach Calibration:** helps choose whether to investigate, change approach, proceed with bounded assumptions or stop; here it challenged whether a new platform is even the right intervention.
- **Task Integrity:** protects scope, provenance, omissions and truthful completion claims across the work.
- **Verification Integrity:** turns completion claims into inexpensive, inspectable reconciliations.
- **Software Literacy:** supports informed human decisions about architecture, authority and trade-offs.
- **Peer Review:** independently structured post-hoc gap-finding; in this run, it surfaced baggage divergence, capacity, authority, fairness and outage-mode omissions.
- **Automaticity and A Touch of Grace:** shape the human-facing interface rather than adding domain mechanisms.
- **AEL Runtime Accountability:** potential decision-provenance/authority record layer; not executed in this test.
- **Q-Batch:** the method needed to isolate and compare these conditions properly.
- **Faking Vision / FV Robots / Self-Learning POC:** not applicable to this particular software scenario; their absence is deliberate, not a negative evaluation.

## Limitations and next test
Same assistant and conversation, with skill passes performed sequentially against one scenario. This is not a clean A/B test, independent deployment, or blind evaluation. CT is MP-derived in lineage; the embedded optional checklist is not invoked as a separate condition in this software test. The software plan is a conceptual design, not an implementation or operational certification.

Next controlled step: use Q-Batch to run baseline and selected skill/resource conditions in isolated batches, freeze the scenario and criteria in advance, preserve outputs, then use Peer Review offline. Run each creation against task types suited to its purpose rather than expecting every creation to improve every task.
