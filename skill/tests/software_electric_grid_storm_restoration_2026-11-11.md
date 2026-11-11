# Software Daily Test: Electric-Grid Restoration After a Major Storm
**Test ID:** MP-SOFTWARE-2026-11-11-01  
**Date:** 2026-11-11  
**Selection:** Assistant-invented scenario selected independently of the user's recent conversations, projects, interests, or hypotheses.

## Scenario
A regional electricity distribution operator must restore service after a severe storm damages transmission connections, substations, distribution feeders and local lines. Flooding and fallen trees restrict access. Some areas have downed conductors that must be made safe before repair. Hospitals, water and wastewater facilities, emergency services, communications sites, shelters and residential customers are affected. Local crews are insufficient, so mutual-aid crews and contractors are arriving from other utilities.

The software system coordinates damage reports, hazard isolation, switching requests and instructions, crew qualifications and assignments, materials, access restrictions, critical-load dependencies, restoration estimates, customer communications and actual service restoration.

It must not autonomously issue switching instructions, declare equipment safe, energise circuits, override system operators, or make public-safety decisions.

## Critical Thinking lineage and checklist status
- **MP skill:** `memoryprismv1/memoryprism/skill/SKILL.md`, blob SHA `8208fdfb794a2cf78c2b1a310912eddfc2dc80a5`.
- **Critical Thinking skill:** `memoryprismv1/cognitive-interface-ai-skills/critical-thinking/SKILL.md`, blob SHA `eed085e5662742983520593579f45d29ca0f75ad`. The source labels it provisional and explicitly describes MP as separate and optional.
- **Embedded optional checklist:** `critical-thinking/MEMORY-PRISM-CHECKLIST.md`, blob SHA `8f12af7020757250c5decff0ba13ed75f0279b04`. Fixed, read-only, one-line prompt: “For a query, does the ledger reconcile for that board under the specific constraints and editors?”
- **Reference card:** `critical-thinking/MEMORY-PRISM-REFERENCE.md`, blob SHA `eba72fd05d6758b2f88ecf1435f541e87fd3a8fe`.
- Critical Thinking is MP-derived in lineage. Its package includes an optional tiny MP checklist. That checklist is not the full MP skill and must not be expanded or treated as mandatory.
- This experiment explicitly separates whether the checklist is invoked at runtime from whether the Critical Thinking package is used.

## Five comparison conditions
A. **Conventional planning:** no MP or Critical Thinking skill invoked.  
B. **MP alone:** full MP skill invoked.  
C. **Critical Thinking package alone, embedded checklist not invoked:** run the CT inquiry behaviours; do not use the optional checklist.  
D. **Critical Thinking package + embedded one-line checklist invoked:** same CT package, with the fixed checklist used as an additional prompt. Do not expand it.  
E. **Full MP + Critical Thinking package:** both skills invoked; the optional checklist may be used but is not a substitute for the full MP skill.

This design tests the checklist's incremental contribution within CT, the portability of CT package behaviours without invoking the full MP skill, and the interaction between full MP and CT. CT's MP-derived lineage remains explicit; no condition is described as intellectually independent of MP's origin.

All conditions are produced by the same assistant in one conversation. Shared context, learned knowledge, sequential contamination and self-assessment remain. This is a structured qualitative probe, not a controlled causal experiment.

## A. Conventional planning
### Requirements and architecture
- Incident and operational-period management.
- Network model: substations, feeders, switches, protective devices, lines, transformers, customers and dependencies.
- Damage and hazard reports, source, timestamp, location, severity and verification status.
- Outage management and customer-impact estimates.
- Crew and contractor registry, skills, authorisations, safety training, location, shift/rest, equipment and mutual-aid affiliation.
- Work orders, dispatch, travel/access constraints, materials, estimated restoration time and completion evidence.
- Switching request, review, approval, instruction, read-back, execution confirmation and independent status verification.
- Critical customer and lifeline prioritisation, including changing incident needs.
- Customer/public communications, outage maps, estimated restoration times and correction history.
- Audit, permissions, offline operation, integrations with GIS, SCADA/ADMS, OMS, workforce, inventory and communications systems.

Likely components: incident service, network/GIS model, outage/damage service, crew/resource management, work management, switching workflow, priority/impact service, communications, event store, integrations and reporting.

Main risks: stale network topology; inaccurate damage reports; unsafe switching; wrong-device identification; crew skill mismatch; duplicate assignments; inaccessible work sites; material shortages; misleading restoration estimates; unverified energisation; poor coordination with water/telecom/emergency services; offline updates and mutual-aid onboarding.

## B. MP alone
### Pre-interpretation inventory
| MP concept | What I identify in this query |
|---|---|
| Board | A damaged regional electrical network operating under changing weather, access, topology, staffing, public-safety and regulatory conditions. |
| Memory | Persistent network configuration, outage and damage history, switching state, work orders, crew qualifications, decisions, resource use and restoration evidence. |
| Constraints | Electrical topology, protection, isolation, switching authority, worker safety, access, weather, equipment compatibility, crew availability, materials, critical loads and communications. |
| Editors | Authorised system operators, switching authorities, field supervisors, safety personnel and incident command roles, each with bounded responsibility. |
| Flow Under Constraint | Electricity, switching instructions, crews, equipment, materials, damage information and public warnings move through constrained pathways. |
| Audits | Reconcile planned switching with authorised and executed operations; compare reported restoration with verified network state and customer supply. |
| Identity | Stable identity for network assets, devices, circuits, outage events, work orders, crews, switching orders and restoration claims. |
| Working Lines | Feeders, tie switches, roads, access routes, communication channels and mutual-aid interfaces; some routes carry power, others carry people or information. |
| No Sacred States | A device marked open, a crew marked on site, or an outage marked restored may not reflect the physical state. |
| Accumulation Patterns | Unresolved faults, crew queues, material depletion, cascading outages, delayed critical services and repeated restoration attempts accumulate. |

MP model: keep separate histories for network topology/state, hazard/damage observations, switching authority and execution, crew/work progress, critical-service consequences, and customer restoration. A planned switching state is not an executed state; a completed repair is not proof of safe energisation; energisation is not proof that every customer has supply.

## C. Critical Thinking package alone — embedded checklist not invoked
### Reconstruct the operational trajectory
1. Storm forecasts trigger staging and mutual-aid mobilisation.
2. The storm passes; hazards, access restrictions and damage are assessed.
3. Downed lines and dangerous sites are identified and isolated by authorised personnel.
4. Network operators establish the actual topology and identify viable restoration paths.
5. Switching plans are prepared, checked against other orders and approved by the proper authority.
6. Crews are matched to work based on qualification, equipment, location, access and safety.
7. Repairs and switching are executed in a controlled sequence with field confirmation.
8. Protection and system conditions are checked before energisation.
9. Restoration is verified through operational telemetry and field/customer evidence.
10. Critical facilities and other customers are progressively restored; estimates and priorities change as conditions become clearer.

### Challenge assumptions
- A customer outage report is not a verified fault location. Multiple reports may describe one upstream failure; some failures produce no report.
- A network map is not guaranteed current topology. Previous switching, field changes, damaged assets and temporary configurations must be reconciled.
- A switching request is not an approved order; an approved order is not proof it was correctly executed; a field report is not necessarily independent confirmation.
- Correct device identity is safety-critical. Wrong-device operation is a known switching hazard; confirmation must bind the instruction to an unambiguous asset and current state.
- Crew availability is not crew suitability. Qualifications, authorisations, rest, equipment, local procedures and site hazards matter, especially for incoming mutual-aid teams.
- Restoring the most customers per job is not the only priority. Critical loads, cascading dependencies, public safety, access, repair feasibility and network stability affect sequencing.
- “Critical facility” is contextual and may change over time. A water plant or communications facility may become more consequential as backup power and fuel run down.
- An estimated restoration time is a forecast, not a promise. Preserve assumptions, confidence, source and revision history.
- A crew marking work complete does not prove the circuit is safe to energise. Required tests, clearances, grounds and switching controls belong to authorised procedures.
- Offline field reports arrive late or out of order. Distinguish event time from upload time; reconcile conflicting reports without silently rewriting history.
- Optimisation cannot override electrical safety, switching authority or operating limits. Software can surface conflicts and candidate sequences, not take control of the grid.
- Mutual-aid crews bring different systems, terminology and procedures. The platform needs controlled onboarding and clear local supervision, not assumed interoperability.

### Supportability
The system can coordinate records, identify conflicts, propose work priorities and show uncertainty. It cannot infer the actual electrical state from a dashboard alone or guarantee that field work was performed correctly. SCADA/ADMS and operational procedures remain authoritative for their defined functions; the proposed platform should integrate rather than casually replace them.

## D. Critical Thinking package + its embedded checklist
The CT package is unchanged. The one-line checklist is invoked as an optional prompt: does the restoration ledger reconcile for this network board under the actual constraints and editors?

In this scenario, applying it directs attention to whether the accounting of the damaged network, available resources, authorised operations, energy/service restoration and ongoing maintenance burden is coherent under the actual operating conditions. It does not supply a complete domain model, a full MP analysis, or a safety procedure.

**Incremental checklist question:** Did this one-line prompt reveal a material dimension, contradiction or missing dependency not already surfaced by CT alone? Record the actual difference; do not award credit merely because the prompt was displayed.

## E. Full MP + Critical Thinking package
MP provides the full inspectable domain inventory and links the relevant histories; CT challenges the resulting representation through sequence reconstruction, counterexamples, evidence checks and supportability questions.

Combined invariant: preserve a trustworthy relationship between the network's physical configuration, hazard/damage evidence, authorised switching decisions, field work, verified energisation and actual customer/lifeline restoration, while keeping resource and priority decisions traceable.

Suggested implementation sequence:
1. Map authority, safety procedures and system-of-record boundaries.
2. Establish canonical network asset identity and versioned topology.
3. Integrate hazard, outage and field observations with provenance and time.
4. Model switching request, approval, instruction, read-back, execution and verification as separate events.
5. Add crew qualification, mutual-aid onboarding, assignment and work completion.
6. Add critical-load and dependency-aware prioritisation with explicit human authority.
7. Integrate customer communications and uncertainty-aware restoration estimates.
8. Exercise wrong-device prevention, conflicting switching orders, inaccessible sites, missing telemetry, failed communications, crew fatigue, mutual-aid mismatch, repeated faults and partial restoration.
9. Pilot in advisory/read-only mode before expanding operational authority.

## Shared qualitative evaluation
Scale: 0 = absent; 1 = partial; 2 = clear. Scores below are provisional self-assessments, not independent measurements. The checklist's incremental effect must be evaluated by comparing C with D, not by comparing D with A alone.

| Criterion | A Conventional | B MP | C CT, no checklist | D CT + tiny checklist | E MP + CT |
|---|---:|---:|---:|---:|---:|
| Identifies operating invariant | 1 | 2 | 2 | 2 | 2 |
| Separates physical from recorded/assumed state | 1 | 2 | 2 | 2 | 2 |
| Exposes dependencies and authority boundaries | 1 | 2 | 2 | 2 | 2 |
| Identifies failure modes and recovery paths | 1 | 1 | 2 | 2 | 2 |
| Improves implementation sequencing | 1 | 1 | 2 | 2 | 2 |
| Questions technical/operational supportability | 1 | 1 | 2 | 2 | 2 |
| Reduces cognitive load without losing domain detail | 2 | 1 | 2 | 2 | 2 |
| **Provisional total / 14** | **8** | **10** | **14** | **14** | **14** |

These are planning-stage estimates based on the constructed drafts, not results of blind independent scoring. The checklist condition is deliberately not awarded an improvement absent an identifiable new contribution. If C and D remain materially identical, record that the tiny checklist did not add a detectable dimension in this scenario. Do not interpret the score ceiling or ties as proof of equivalence.

## Attribution and interpretation
- Conventional planning contributes expected architecture decomposition and standard modules.
- MP contributes the full query-to-concept inventory and explicit organisation of constraints, editors, flows, identity, state distinctions and accumulation.
- CT package contributes curiosity-led inquiry, mismatch detection, alternative explanations, causal reconstruction, evidence checking, counterexamples and supportability challenges. Its intellectual lineage is MP-derived.
- Embedded checklist contributes only the optional one-line reconciliation prompt. Its incremental contribution must be identified by comparing C and D.
- Full MP + CT is not the same condition as CT plus its tiny embedded checklist. The checklist is fixed, optional and not a miniature full framework.
- Overlap is expected; do not force exclusive attribution to MP or CT.
- No causal conclusion is possible from this same-context, self-scored run.

## Research grounding
- FEMA's January 2025 Power Outage Incident Annex describes restoration priorities, coordination across utilities and governments, critical asset lists, mutual assistance and situational reporting: https://www.fema.gov/sites/default/files/documents/fema_incident-annex_power-outage.pdf
- NERC EOP-006-3 sets requirements for system-restoration coordination plans and personnel readiness to coordinate restoration while maintaining reliability: https://www.nerc.com/standards/reliability-standards/eop/eop-006-3
- U.S. National Academies describes a general restoration model: assess damage, provide resources, prioritise repairs based on load criticality and resource availability, implement repairs and reassess system state: https://www.nationalacademies.org/read/24836/chapter/8
- DOE CESER describes coordination with utilities, states, FEMA and mutual-assistance partners, including damage assessment, equipment and material needs: https://www.energy.gov/ceser/response-recovery
- EPA guidance for water/wastewater utilities notes that critical-load priority decisions depend on local emergency protocols and responsible authorities; water facilities can become increasingly critical as outages continue: https://nepis.epa.gov/Exe/ZyPURL.cgi?Dockey=P10138HK.TXT
- EPRI research on distribution operations highlights switching-order safeguards and clear roles between field crew leaders, outage schedulers and system operators: https://restservice.epri.com/publicdownload/000000000001010649/0/Product
- These are U.S.-oriented sources and do not define universal legal authority. A real implementation must use the relevant country's grid code, utility safety rules, control-room procedures and regulatory framework.

## Findings to record after comparison
1. What did conventional planning identify without skill prompts?
2. What additional dimensions appeared with full MP?
3. What did CT surface with its embedded checklist deliberately not invoked?
4. What changed when the one-line checklist was invoked? Identify only genuine incremental observations.
5. What did full MP + CT produce that neither package alone produced?
6. Which dimensions overlapped, and which appeared only in one condition?
7. Did any approach reduce cognitive load while retaining useful operational detail?
8. Did any approach claim a software capability that the actual control environment cannot safely support?

## Limitations
- Same assistant, same conversation, sequential drafts; context contamination cannot be excluded.
- CT is MP-derived in lineage; this experiment tests package/runtime behaviour, not independent origin.
- The embedded checklist is a fixed optional prompt, not the full MP skill. It must not be modified or expanded.
- Self-assessed rubric scores are provisional; blind external scoring and fresh isolated contexts were not available.
- This scenario is a general distribution restoration coordination problem. Actual operational and legal boundaries are jurisdiction- and utility-specific.
