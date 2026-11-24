# Software Daily Test: Wildfire Evacuation and Temporary Shelter Coordination
**Test ID:** MP-SOFTWARE-2026-11-09-01  
**Date:** 2026-11-09  
**Selection:** Assistant-invented scenario selected independently of the user's recent conversations, projects, interests, and hypotheses.

## Skill lineage and runtime conditions
- **Memory Prism skill:** `memoryprismv1/memoryprism/skill/SKILL.md`, blob SHA `8208fdfb794a2cf78c2b1a310912eddfc2dc80a5`; Starter Kit `skill/references/starter-kit.md`, blob SHA `07c6594a41ce05f7d06b14c59770d78775983520`.
- **Critical Thinking skill:** `memoryprismv1/cognitive-interface-ai-skills/critical-thinking/SKILL.md`, blob SHA `0bd33321e535d9e68469307f2128cf27637046c9`; status in source is provisional.
- Critical Thinking was developed using MP thinking and is therefore **derived in lineage**. The test asks whether it can operate as a separately packaged skill **without MP being invoked at runtime**. It does not claim independent intellectual origin.
- Conditions B and C below are separate runtime instructions. The model's learned knowledge and prior exposure cannot be erased, so this is not a claim of cognitive or historical isolation.

## Scenario
A regional emergency-management organisation wants a coordination platform for wildfire evacuation and temporary shelter operations. It must support incident command, emergency operations centres, fire and law-enforcement agencies, transport operators, public works, healthcare providers, shelter operators, animal services and neighbouring jurisdictions.

During a fast-moving wildfire, officials may need to change evacuation zones, close roads, assign transport, redirect residents, open or expand shelters, manage capacity and services, and communicate updated instructions. Some people self-evacuate; others need accessible transport, medical transport, language assistance, support for children, pets or livestock, or help locating family members. In some situations evacuation routes may become unsafe and authorised officials may shift to shelter-in-place or direct people to pre-designated temporary fire refuge areas.

The platform coordinates information and actions. It does not predict fire behaviour authoritatively, issue evacuation orders autonomously, determine that a route is safe, or replace incident command.

## Four runtime conditions
A. Conventional software planning, with neither skill invoked.  
B. MP skill alone.  
C. Critical Thinking skill alone, with no MP checklist, framework table, or explicit MP terminology invoked at runtime.  
D. MP and Critical Thinking together.

**Lineage qualification:** C is independent execution of a separately packaged, MP-derived skill. It is not independent origin. Its behaviours may carry intellectual capabilities developed through MP thinking; that is the intended portability question, not a reason to pretend the lineage does not exist.

All four drafts are produced by the same assistant in one conversation. Shared context, learned knowledge, sequential contamination and self-evaluation remain. This is a structured qualitative probe, not a blind or controlled causal experiment.

## A. Conventional software planning
### Core requirements
- Incident, jurisdiction, authority and operational-period configuration.
- Geospatial evacuation zones, hazard perimeters, decision zones, road network, closures, route restrictions and refuge areas.
- Public warning and instruction management, channels, languages, accessibility formats, issue times and acknowledgements where feasible.
- Evacuation demand estimates by area and population/service needs.
- Transport resources: vehicle type, capacity, accessibility, operator, location, availability, fuel, crew and assignment.
- Pickup locations, staging areas, movement status and destination.
- Shelter registry: location, operational status, capacity, occupancy, accessible facilities, medical capability, staffing, supplies, animal accommodation and restrictions.
- Evacuee support and accountability, including family reunification and privacy controls.
- Resource requests, mutual aid, logistics, staffing, supply and incident action plans.
- Event history, role-based access, audit logs, reporting, maps, mobile/offline capability and external integrations.

### Plausible architecture
Incident and jurisdiction service; geospatial data service; operational status/event store; evacuation zone and route management; demand and transport resource coordination; shelter capacity/service registry; notification and public information service; task/resource request workflow; identity/access/audit layer; mobile/offline client and integration gateway.

### Main risks
Stale hazard/road data; inaccurate shelter occupancy; double-assigned vehicles; route changes not reaching drivers; people sent to full or unsuitable shelters; inaccessible messaging; conflicting jurisdictional instructions; unreliable communications; poor offline reconciliation; privacy breaches; false precision in demand estimates.

## B. MP skill alone
### Pre-interpretation inventory
| MP concept | What I identify in this query |
|---|---|
| Board | A changing incident area across multiple jurisdictions, with fire behaviour, terrain, roads, weather, communications, authority structures and shelter geography. |
| Memory | Persistent records of zone versions, orders, road observations, resource assignments, movement, shelter occupancy, service status and previous operational decisions. |
| Constraints | Fire spread, smoke, road capacity, travel time, vehicle capability, staff availability, shelter capacity, accessibility, communications, legal authority and time. |
| Editors | Incident command and legally authorised officials who decide evacuation, shelter-in-place, zone changes and operational priorities; transport/shelter managers control their own resources within delegated authority. |
| Flow Under Constraint | People, vehicles, warnings, supplies, medical support and operational information move through limited routes and receiving facilities. |
| Audits | Comparing assigned movements with actual departure/arrival, shelter intake with capacity, and issued warnings with delivery/acknowledgement evidence. |
| Identity | Incident, zone, order, vehicle/resource, shelter, household/person record and operational task must retain stable identities across updates. |
| Working Lines | Roads, bridges, communication networks, pickup points and shelter intake channels are operational pathways that can enable movement or transmit disruption. |
| No Sacred States | A road marked open, a shelter marked available, or an evacuation order marked issued may not reflect current physical conditions or actual receipt. |
| Accumulation Patterns | Evacuee arrivals, vehicle queues, shelter occupancy, unmet needs, resource depletion and unresolved requests accumulate over time. |

### MP-guided organising model
Do not treat evacuation as one status or a single route-optimisation problem. Keep linked but distinct operational histories:
1. **Threat and decision:** hazard observations/forecasts, decision zones, authorised protective action, effective time and subsequent revisions.
2. **Population and need:** estimated population, self-evacuation assumptions, assistance requirements, uncertainty and changes as people move.
3. **Movement:** route state, vehicle/resource assignment, pickup, departure, en-route observations, arrival and failed/aborted movement.
4. **Reception:** shelter status, capacity, occupancy, service capability, intake and onward transfer.
5. **Communications and authority:** who issued which instruction, to whom, through which channel, and what evidence exists that it was received.
6. **Resource sustainability:** fuel, crews, supplies, rest, medical capability, shelter staffing and replenishment.

The platform should preserve both the planned state and observed state. A dispatched bus is not proof of pickup; an open shelter is not proof of available beds; a sent warning is not proof that a household received it.

### MP-only likely contribution
MP makes the system's parallel histories and the difference between declared, assigned, observed and completed states more explicit. It also foregrounds accumulation: queues, shelter saturation and unmet needs can emerge even when individual task records look normal.

## C. Critical Thinking skill alone — MP not invoked at runtime
### Reconstruct the operational trajectory
A wildfire evacuation is a sequence of decisions and changing physical conditions, not merely a list of zones and resources.

1. Fire and weather observations arrive from sources with different coverage, delay and uncertainty.
2. Incident command evaluates threat, time available, population exposure, road network, shelter options and alternatives.
3. An authorised official selects and issues a protective action for a defined zone and time.
4. Public warning and targeted notification begin, but not everyone receives or understands the message at the same time.
5. Residents self-evacuate or request assistance; some are already moving before the formal order.
6. Transport resources are dispatched; pickup, boarding and departure may be delayed or fail.
7. Roads can become blocked or unsafe while vehicles are en route.
8. Shelters receive arrivals, but their actual capacity and service capability can change with staffing, supplies, power, water, medical needs and animal intake.
9. Command may revise zones, close routes, redirect vehicles, open additional shelters, or change protective action.
10. Re-entry and reunification occur later, under separate authority and conditions.

### Challenge the obvious software assumptions
- **A map is not the territory.** Perimeter, road, smoke and weather layers have different update times, uncertainty and provenance. Show source and observation time; don't blend them into one apparently authoritative live map.
- **A route is not safe because it is shortest.** Safety and usability depend on fire behaviour, smoke, traffic, vehicle type, bridge limits, closures and command judgement. Routing can support authorised decisions, not certify safety.
- **An order is not receipt.** A message can be issued, delivered to a carrier, delivered to a device, read, understood or acted upon. These are different claims. Many residents will not have a trackable device.
- **Demand estimates are not counts.** People may be absent, duplicated across datasets, visiting, at work, in institutions, or already evacuated. Record estimate method, time, uncertainty and source.
- **Capacity is not a single number.** A shelter's nominal beds do not establish usable capacity for families, wheelchairs, medical needs, service animals, pets or livestock. Capacity depends on services, staffing, supplies and constraints.
- **Assignment is not movement.** A bus allocated to a pickup does not mean it arrived, boarded people, departed or reached a shelter. Each event needs an actor/source and time.
- **People are not cargo.** Tracking must be proportionate, privacy-protective and designed for reunification and safeguarding. Do not require individual registration as a condition of evacuation or shelter access.
- **Decision authority is not interchangeable.** Incident command, local authorities, transport operators and shelter managers have different powers. The system must represent jurisdiction-specific delegation and mutual-aid arrangements.
- **Shelter-in-place/refuge is not an algorithmic fallback.** Whether evacuation remains safer than sheltering is a life-safety judgement based on current conditions and designated locations; software must not silently switch strategy.
- **No-notice events break orderly workflows.** Residents may self-evacuate before warnings; communications, power and road networks may fail simultaneously.
- **Offline operation is essential.** Field teams need usable maps, assignments and forms without reliable connectivity. Synchronisation must reconcile delayed and conflicting updates without erasing history.
- **A green dashboard can be false reassurance.** Missing reports are not evidence of no problem. Display unknown/stale status distinctly from safe/available.

### Technical and operational supportability
A coordination platform can aggregate reports, display uncertainty, track tasks and support communication. It cannot guarantee evacuation completion, physical road safety, correct shelter suitability, or population accountability. Those depend on field observations, human decisions, local plans, functioning communications and real resources.

### CT-only likely contribution
The skill independently executing at runtime is used to reconstruct a plausible operational sequence, seek mismatches, challenge assumptions, distinguish source claims from physical facts, and test whether the software can actually support its promised functions. These behaviours were developed through MP thinking; this condition tests their portability without invoking MP instructions or checklist.

## D. MP + Critical Thinking together
### Combined operating invariant
Maintain a trustworthy, time-aware relationship between:
- the threat information and its uncertainty;
- the authorised protective-action decision;
- the population and assistance demand being estimated;
- the resources and routes assigned;
- the movement that actually occurred;
- the receiving shelter's real, changing capability;
- the communications and evidence supporting each transition.

This is a set of linked histories, not one master status.

### Recommended data model
- Incident and operational period.
- Geospatial zone with version, effective time, decision authority and linked threat evidence.
- Observation/forecast record with source, location, observation time, ingestion time, uncertainty and supersession.
- Protective-action decision and order, with issuer, authority basis, zone, action, effective time, revision and public instruction.
- Population/demand estimate, method, geography, timestamp, confidence and assistance categories; avoid unnecessary personally identifying detail.
- Transport resource, crew, capability, location, availability, assignment and actual movement events.
- Route segment status with source, observation time, vehicle restrictions and confidence.
- Shelter facility with operational status, nominal and usable capacity, service capabilities, staffing, supplies, occupancy and last verified time.
- Intake/arrival and unmet-needs record, with privacy safeguards.
- Communications record with intended audience, channel, issued/delivered/read/acknowledged distinctions where measurable.
- Resource request and fulfilment history.
- Append-only event/provenance log, including corrections, offline capture time, sync time and source.

### Implementation sequence
1. Map local authorities, command roles, jurisdiction boundaries, protective-action procedures and mutual-aid agreements.
2. Build incident/zone/order versioning and authoritative event provenance.
3. Integrate road, weather, fire and GIS sources while preserving source, time and uncertainty.
4. Add shelter registry with capability-based usable capacity, not only nominal beds.
5. Add transport resources, assignments and movement-state tracking.
6. Add accessible multilingual public messaging and operational acknowledgement, without equating delivery with comprehension.
7. Add offline field workflows and robust conflict reconciliation.
8. Run tabletop and functional exercises: sudden road closure, shelter saturation, failed bus pickup, disconnected district, contradictory perimeter reports, late self-evacuees, animal overflow, power loss, and shift handover.
9. Only then evaluate optimisation or predictive functions, and keep them advisory.

### Combined contribution
MP provides a visible map of the different histories, constraints, pathways and accumulations. Critical Thinking tests the map against a real sequence, plausible failures and the limits of what software can know or control. The combined method can improve inspectability and challenge, but no improvement should be credited without a comparison that reduces shared-context contamination.

## Shared qualitative evaluation
Scale: 0 = absent; 1 = partial; 2 = clear. Scores are self-assessments by the same assistant and are not independent measurements.

| Criterion | A Conventional | B MP only | C CT only | D MP + CT |
|---|---:|---:|---:|---:|
| Identifies the operating invariant | 1 | 2 | 2 | 2 |
| Separates physical state from recorded/assumed state | 1 | 2 | 2 | 2 |
| Exposes dependencies and authority boundaries | 1 | 2 | 2 | 2 |
| Identifies failure modes and recovery paths | 1 | 1 | 2 | 2 |
| Improves implementation sequencing | 1 | 1 | 2 | 2 |
| Questions technical/operational supportability | 1 | 1 | 2 | 2 |
| Reduces cognitive load without replacing domain detail with jargon | 2 | 1 | 2 | 2 |
| **Total / 14** | **8** | **10** | **14** | **14** |

The numerical scores are not evidence of a skill effect. In this constructed comparison, CT-only and combined outputs reach the same rubric score. That may indicate that the derived CT skill can carry useful inquiry behaviours without MP being invoked, but this cannot be established from one same-context, self-scored run. MP's contribution is visible as a more explicit domain inventory; CT's contribution is visible in the sequence reconstruction and adversarial checks. The dimensions overlap.

## Attribution and lineage
- **Conventional planning:** ordinary architecture decomposition and expected modules.
- **MP runtime:** explicit query-to-concept inventory; organisation around linked histories, authority, constraints, flows, state distinctions and accumulation.
- **Critical Thinking runtime:** causal trajectory reconstruction, alternative/failure examination, evidence and uncertainty distinctions, assumption challenges, supportability checks.
- **Derived lineage:** Critical Thinking was created through MP thinking. Its ability to perform these moves without MP being invoked at runtime is a portability question, not proof of unrelated origin.
- **Overlap:** CT-only and MP-only both surface some of the same dimensions. That is expected given lineage; it must not be treated as two independent discoveries or used to erase CT's operational independence.
- **Combination:** D makes the MP inventory explicit and then applies CT challenge behaviours to it. No incremental rubric gain over CT-only is demonstrated.

## Research grounding
- FEMA, *Federal Evacuation Support Annex*, Second Edition, April 2025. Describes state/local responsibility, federal support, distinct general-population/patient/animal evacuation needs, critical transportation, route status, shelter capacity and changing conditions. https://www.fema.gov/sites/default/files/documents/fema_rd_federal-evacuation-support-annex_042025.pdf
- FEMA, *Planning Considerations: Evacuation and Shelter-in-Place* (2019). Covers authority, accessibility, transportation, sheltering, evacuee accountability, zonal strategies, flexibility and whole-community planning. https://www.fema.gov/sites/default/files/2020-07/fema_DRRA-1209-planning-considerations-evacuation-shelter-in-place_guide.pdf
- NIST, 2025 update to ESCAPE wildfire evacuation and sheltering guidance. Emphasises no-notice evacuations, multiple routes and communications, temporary fire refuge areas, and changing decision zones as threat increases. https://www.nist.gov/news-events/news/2025/04/nist-updates-critical-wildfire-evacuation-and-sheltering-guidance
- FHWA evacuation operations primer: shelter capacity should be kept current and coordinated with transportation operations; special-needs shelters and pickup locations require coordination. https://ops-dr.fhwa.dot.gov/publications/evac_primer/16_tier_i.htm
- These are U.S. federal planning references, not universal legal or operational requirements. Actual authority and workflows depend on jurisdiction and local plans.

## Findings
1. Conventional planning identifies a plausible module set but can under-specify the relationship between orders, people, movement, route conditions and shelter capability.
2. MP alone makes parallel histories and differences between declared, assigned, observed and completed states visible.
3. Critical Thinking alone, without invoking MP at runtime, independently reconstructs a sequence and challenges assumptions about route safety, order receipt, capacity, demand, authority, offline operation and software limits.
4. The CT behaviours are MP-derived in lineage. Their operation without MP invocation is evidence consistent with portability, but not a controlled demonstration of independent cognitive origin or robust general transfer.
5. MP and CT overlap in the dimensions they surface. The four-way comparison should report overlap rather than force exclusive ownership.
6. The combined condition does not score above CT-only on this qualitative rubric; no additive benefit is demonstrated.
7. The system should be an evidence-aware coordination aid, not an autonomous evacuation decision-maker or a guarantee of physical safety.

## Limitations and next test
- Same assistant and same conversation; context is shared, drafts are sequential and may contaminate one another.
- CT is derived from MP thinking; this comparison tests runtime portability only.
- Scores are self-assessed and not blind or independent.
- The scenario is generic and research is grounded mainly in U.S. guidance; local jurisdiction and operating procedures would change requirements.
- A stronger follow-up would run each condition in separate fresh contexts with identical scenario inputs, randomise output order for an external assessor, and separately tag: (a) dimensions present in the conventional baseline, (b) dimensions newly surfaced by each skill, (c) overlap, and (d) dimensions appearing only in combination.
