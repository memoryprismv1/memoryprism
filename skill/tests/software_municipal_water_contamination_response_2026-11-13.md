# Software Daily Test: Municipal Drinking-Water Contamination Response
**Test ID:** MP-SOFTWARE-2026-11-13-01  
**Date:** 2026-11-13  
**Selection:** Assistant-invented scenario selected independently of the user's recent conversations, projects, interests, phrasing or hypotheses.

## Scenario
A municipal water utility receives an alarming result from a distribution-zone sample. The contaminant is unknown. The signal may be real, a sampling/transport error, a laboratory issue, or a localised event. Several supply zones may connect through valves, reservoirs and pumping stations. The utility, public-health authorities, accredited laboratories, emergency responders, hospitals, schools, care facilities, tanker suppliers and communications teams must coordinate.

The platform coordinates incident evidence, sampling, laboratory workflows, network zones, operational actions, authority decisions, public advisories, alternate water, remediation and clearance. It must not diagnose health risk from incomplete data, autonomously issue public-health orders, or decide water is safe.

## Evidence and jurisdiction boundary
Sources below are mainly US and Australian examples, not universal legal rules. An implementation in India or elsewhere must map local utility, public-health and regulator authority, sampling standards, public-notification law and emergency plans.
- EPA incident response guidance separates investigation, operational responses/notifications and remediation/recovery. Indicators are assessed to determine whether contamination is ruled out, confirmed or remains possible: https://nepis.epa.gov/Exe/ZyPURL.cgi?Dockey=P100VVRC.TXT
- EPA sampling guidance covers collection, preservation, storage, transport and communication between utilities, responders and labs: https://www.epa.gov/waterlabnetwork/sampling-guidance-unknown-contaminants-drinking-water
- EPA remediation guidance divides work into characterisation, decontamination and clearance; phases can overlap and are incident-specific: https://www.epa.gov/waterutilityresponse/decontamination-drinking-water-and-wastewater-utilities
- Australian Drinking Water Guidelines warn that overwhelming laboratories with samples can harm quality control; backup laboratory capacity may be needed: https://guidelines.nhmrc.gov.au/australian-drinking-water-guidelines/part-3/chapter-9/9.9-incident-and-emergency-response-monitoring
- NSW Health describes utility/public-health responsibilities, repeat sampling upstream/downstream and consultation about boil-water alerts: https://www.health.nsw.gov.au/environment/water/Pages/nswhrp-microbiological.aspx
- CDC advisory communication toolbox: https://www.cdc.gov/water-emergency/media/pdfs/2024/08/dwact-2016.pdf

## A. Conventional planning baseline
Likely components: incident intake and credibility assessment; network/GIS model of sources, treatment plants, reservoirs, pressure zones, pipes, pumps and valves; sample plans, chain of custody and lab capacity; field/lab tests and quality controls; contamination source/extent model; isolation, flushing, disinfection and work orders; public-health advisory decisions; zone/customer and vulnerable-facility lists; public communication; tanker distribution; remediation, monitoring and clearance; audit, access, integration and offline field operation.

A module list alone does not ensure a lab result is tied to the correct sample, a zone is physically isolated, or an advisory reaches the right people.

## B. Memory Prism pass
### Pre-interpretation inventory
| MP concept | What I identify in this query |
|---|---|
| Board | Physical water network, utility operations, population and public-health environment under a suspected contamination event. |
| Memory | Network topology, operating history, samples, lab results, valve operations, advisories, exposure and remediation history. |
| Constraints | Hydraulic connectivity, pressure/flow, contaminant behaviour, sampling method, lab capacity, treatment capability, authority, time, access and alternate supply. |
| Editors | Utility operators, incident command, public-health authority, regulator, laboratory quality authority and authorised field staff with distinct decision rights. |
| Flow Under Constraint | Water, contaminant, samples, evidence, instructions, advisories and alternate supplies move through different physical and information networks. |
| Audits | Reconcile sample identity/custody; planned vs executed valve actions; advisory scope vs connected zones; clearance evidence vs restored service. |
| Identity | Sample, sampling point, supply zone, valve, reservoir, lab batch, result, advisory version and work order need stable identities. |
| Working Lines | Hydraulic pathways, sample transport, lab workflows, public-notification channels and tanker routes are distinct. |
| No Sacred States | “Sample collected”, “valve closed”, “zone isolated”, “advisory issued”, “flushed” and “safe” are not interchangeable or self-proving. |
| Accumulation Patterns | Exposure duration, affected population, lab backlog, uncertain zone boundaries, tanker demand and repeat sampling accumulate. |

Keep separate but linked histories for physical network state, contamination observations, sample custody/lab analysis, authority decisions, operational actions, population exposure and communications. A GIS isolation polygon is not proof of valve operation; a lab result is not meaningful without sample identity and quality context; a message sent is not proof of receipt.

## C. Critical Thinking package alone — embedded checklist NOT invoked
Reconstruct and challenge:
1. An indicator/complaint triggers an incident record; preserve what was observed and by whom.
2. Assess credibility using other operational data; do not prematurely label the contaminant.
3. Establish sampling locations/methods; record identity, time, collector, container, preservation, transport and custody.
4. Distinguish presumptive, screening, confirmatory and validated results according to method and contaminant.
5. Map possible hydraulic pathways using current topology, pressure and flow—not administrative zone labels alone.
6. Authorised utility/public-health decision-makers determine restrictions and public advice under local rules.
7. Valve actions are issued, acknowledged, executed and physically/operationally verified as distinct events.
8. Sample upstream/downstream and across connected zones to establish extent.
9. Plan alternate water against actual population, demand, access and replenishment.
10. Select remediation for the specific contaminant and infrastructure; no universal flush/disinfection recipe.
11. Base clearance on appropriate post-remediation evidence and approval, not elapsed time or a green dashboard.
12. Lift restrictions and restore service through the relevant authorised process.

Challenge assumptions:
- A positive sample may reflect contamination, collection contamination, transport failure or analytical error.
- A negative result does not prove the whole network safe if sampling is unrepresentative or the method unsuitable.
- Too many samples without laboratory capacity can degrade quality control.
- Contaminant movement depends on hydraulics, persistence, reaction, adsorption and operating conditions; administrative boundaries are not hydraulic boundaries.
- A database valve status may be stale; remote command acceptance does not prove physical closure.
- A boil-water advisory is not appropriate for every contaminant; chemical hazards may require different restrictions.
- A notice sent is not notice received; a tanker scheduled is not water delivered.
- Building plumbing and local storage can remain affected after a distribution zone is cleared.
- Lab turnaround targets must not pressure staff to bypass quality assurance.

Software can coordinate evidence, map possible exposure, manage sampling/work and communicate approved instructions. It cannot decide toxicology, public-health risk, legal authority, laboratory validity or safe-to-drink status on its own.

## D. Critical Thinking + embedded one-line MP checklist
The CT package includes a fixed, optional, read-only checklist. Exact wording: “For a query, does the ledger reconcile for that board under the specific constraints and editors?”
Checklist SHA: 8f12af7020757250c5decff0ba13ed75f0279b04. Reference-card SHA: eba72fd05d6758b2f88ecf1435f541e87fd3a8fe. CT skill SHA: eed085e5662742983520593579f45d29ca0f75ad.

Invoke it as one prompt only; do not expand it. Compare this condition with C: did it reveal a concrete mismatch or missing relationship not already found by CT? It may reinforce reconciliation across physical network state, evidence, decisions and action, but a repeated summary is not an incremental discovery.

## E. Optionality
Preserve genuinely different response strategies:
- Precautionary zone restriction while sampling refines scope: protects people quickly but risks unnecessary disruption.
- Targeted isolation and monitoring: limits disruption but risks missing connections if topology/flow data are stale.
- Source shutdown and alternate supply: reduces further input if source is controllable, but may create major shortages.
- Staged response: initial precautionary action, then expand/contract with validated evidence; needs fast trustworthy updates and clear authority.
- Intensified sampling without broad advisory: only if authorised health/utility assessment finds immediate risk sufficiently low; never a software default or model-generated safety conclusion.
Each option needs assumptions, evidence threshold, decision owner and review/expiry time. Software must not choose public-health risk tolerance.

## F. Good-Faith Collaboration & Approach Calibration
Question the product boundary: new municipal platform, coordination layer over SCADA/GIS/LIMS/customer systems, or narrower evidence-and-response ledger? Investigate existing systems and local authority before proposing replacement. If live telemetry/lab integration is unavailable, design a labelled manual/degraded path rather than pretending integration exists.

## G. Task Integrity
Protect the complete scope: sampling, custody, lab analysis, network isolation, public-health decision, advisories, alternate water, remediation, clearance and restoration. Track guidance vs scenario assumptions, unverified integrations and permissions. Do not report incident response complete when only an advisory or work order was issued.

## H. Verification Integrity
Make claims checkable:
- sample identity reconciles with collection, custody, transport, lab accession and result;
- result retains method, QC status, lab, timestamps and qualification;
- isolation order maps to assets, authoriser, field/telemetry confirmation and hydraulic evidence;
- affected-zone model is versioned with topology/flow assumptions;
- advisory has approved wording, scope, issue channels, delivery evidence and current status;
- tanker request reconciles to dispatch, delivery, quantity, quality and replenishment;
- remediation reconciles to assets/zones and responsible staff;
- clearance reconciles to approved sampling plan, valid results and designated authority;
- withdrawal of advisory and restoration are separate authorised events.
A status label is not verification.

## I. Software Literacy
Explain consequential choices plainly:
- A system of record is the authoritative home of a fact; lab, utility and health authority may own different facts.
- Chain of custody documents the sample path from collection through handling to lab receipt; a sample ID alone is insufficient.
- A hydraulic model estimates water movement based on current topology and operations; it is not direct observation.
- An event history records actions/observations; it does not prove them without reliable evidence.
- Integration requires rights, identifiers, data quality, timeliness and failure handling—not merely an API.
- Decision support can compare consequences but must not be mistaken for public-health authority.

## J. Peer Review
Post-hoc review found:
- Sample provenance and lab quality status must be first-class, not attachments.
- Zone maps can mislead if hydraulic connectivity and valve execution are not current.
- Advisory scope, actual reach and customer comprehension are different measures.
- Clearance is a separate evidence-backed decision; remediation completed is not the same as safe supply.
- Lab capacity and sample prioritisation are scarce resources; unbounded sampling can reduce quality.
- Building plumbing and local storage may remain affected after distribution clearance.
- Tanker allocation must consider vulnerable people, facilities, mobility and access, not just population density.
- Avoid replacing authoritative lab, SCADA, GIS or public-health systems without demonstrated need.

## K. Interface skills
Automaticity: use plain language while preserving distinctions between suspicion, confirmation, restriction, remediation and clearance. A Touch of Grace: report findings and necessary corrections without unsolicited agent commentary.

## L. Other creations and fit
- AEL Runtime Accountability: potentially records who proposed, authorised, communicated and executed consequential actions, with provenance and authority. Not executed as a runtime system here.
- Q-Batch: appropriate for genuinely isolated condition runs and offline comparison; not itself a water-response capability.
- Faking Vision, FV Robots and Self-Learning POC: not materially applicable to this text/data scenario; deliberately not forced into it.
- Peer Review was used as a review pass, but is not independent in this same-context exercise.

## Contribution observations
Conventional planning supplies modules. MP maps the physical network, evidence, authority and action histories. CT adds causal sequence, alternatives and supportability challenges. The optional checklist may offer a compact final reconciliation prompt, but its incremental value over CT alone remains unproven. Optionality preserves distinct strategies. Good-Faith Collaboration questions whether a new platform is the right intervention. Task Integrity protects scope and honest completion claims. Verification Integrity makes transitions checkable. Software Literacy clarifies architecture and authority. Peer Review finds omissions after a draft exists. Automaticity and A Touch of Grace shape delivery, not water-system mechanisms.

No empirical ranking or additive benefit is established. Sequential passes shared one model and context.

## Next controlled test
Use Q-Batch for fresh runs: baseline; MP; CT without checklist; CT with the fixed checklist; and selected individual skills (Optionality, Task Integrity, Verification Integrity, Good-Faith Collaboration, Software Literacy). Freeze scenario, resource list, output capture and criteria before execution. Anonymise outputs and use Peer Review offline. Record whether the checklist adds a specific reconciliation finding rather than repeating a summary.

## Limitations
Conceptual planning only; no implementation or live municipal data. Sources are jurisdiction-specific. Same-assistant sequential passes, not isolated or blind. Contributions are hypotheses pending Q-Batch and external evaluation.
