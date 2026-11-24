# Software Daily Test: Infrastructure Construction Change Control
**Test ID:** MP-SOFTWARE-2026-11-08-01  
**Date:** 2026-11-08  
**Selection:** Assistant-invented scenario selected independently of the user's recent conversations, projects, interests, and hypotheses.  
**MP skill revision:** `memoryprismv1/memoryprism/skill/SKILL.md`, blob SHA `8208fdfb794a2cf78c2b1a310912eddfc2dc80a5`; Starter Kit `skill/references/starter-kit.md`, blob SHA `07c6594a41ce05f7d06b14c59770d78775983520`.  
**Critical Thinking skill revision:** `memoryprismv1/cognitive-interface-ai-skills/critical-thinking/SKILL.md`, blob SHA `0bd33321e535d9e68469307f2128cf27637046c9` (source marks the skill provisional).

## Scenario
Design a software service for a large infrastructure construction project. An owner, lead designer, specialist engineering consultants, main contractor, subcontractors, suppliers, and site supervisors need to manage proposed design and scope changes after the project baseline has been agreed.

A change may begin with an unexpected site condition, a design error, a client request, a regulatory requirement, or a contractor proposal. It may affect drawings, specifications, quantities, procurement, temporary works, safety documentation, programme, budget, permits, work already completed, inspections, and handover records.

The system must coordinate requests, impact assessments, decisions, authorised instructions, document revisions, distribution and acknowledgement, site implementation, verification, and commercial/schedule consequences. It must not itself make engineering, safety, contractual, or statutory decisions.

## Evaluation design
Four conceptual conditions:
A. Conventional software planning, without either skill.
B. MP skill alone.
C. Critical Thinking skill alone.
D. MP and Critical Thinking together.

These are authored by the same assistant in one conversation. They are not context-isolated, blind, or independently evaluated. The comparison is therefore a structured qualitative probe, not a controlled experiment. The four conditions are separated conceptually, but contamination from shared model context cannot be ruled out.

## A. Conventional software planning
### Core requirements
- Project and contract configuration, including baseline scope, design, programme, cost plan, approval roles, and jurisdiction/contract-specific rules.
- Change request intake, originator, reason, affected location/assets/work packages, supporting evidence, urgency, and linked RFIs or site observations.
- Technical, safety, statutory, procurement, commercial, schedule, and stakeholder impact assessments.
- Approval routing using project-specific delegated authority and contract roles.
- Controlled issue of instructions and revised drawings/specifications.
- Distribution to affected parties, acknowledgement, and confirmation of the current applicable revision.
- Implementation tasks, inspections, as-built updates, cost/time tracking, and closure.
- Searchable history, permissions, audit trail, notifications, reporting, and integrations with document/BIM/project-management systems.

### Plausible architecture
A change register/service; project and contract configuration; document/version service; workflow and approval engine; impact/dependency service; task and implementation tracking; notification/integration layer; audit/event store; reporting interface.

### Main risks
Incorrect authority configuration; stale documents; approvals not reaching site; hidden dependencies; duplicate requests; changes implemented before approval; inconsistent cost/programme/design baselines; poor offline connectivity; over-notification; disputes over what was instructed and when.

## B. MP skill alone
### Pre-interpretation inventory
| MP concept | What I identify in this query |
|---|---|
| Board | The project operates within a particular contract, approved baseline, design environment, site condition, regulatory setting, procurement structure, and delivery programme. |
| Memory | Persistent history of the original baseline, proposed changes, evidence, decisions, instructions, revisions, acknowledgements, site actions, and resulting asset state. |
| Constraints | Contractual authority, engineering standards, safety, permits, budget, schedule, physical site conditions, procurement lead times, and dependencies between work packages. |
| Editors | People and bodies with actual authority to review, approve, reject, issue instructions, accept work, or authorise commercial changes. Their authority differs by contract and subject. |
| Flow Under Constraint | Requests, technical information, instructions, revised documents, materials, labour, cost, and schedule effects move between organisations and work fronts. |
| Audits | Comparison of approved information with issued documents, site receipt, work performed, inspection evidence, and final as-built records. |
| Identity | A change needs a stable identity across its request, assessments, approvals, instructions, document revisions, tasks, and commercial consequences. |
| Working Lines | Dependencies between drawings, specifications, calculations, permits, procurement, temporary works, site instructions, inspections, and handover. |
| No Sacred States | “Approved” does not mean issued, received, understood, implemented, inspected, or incorporated into the as-built record. These are different states. |
| Accumulation Patterns | Small changes can accumulate into design drift, unresolved dependencies, rework, procurement disruption, approval backlog, and cumulative cost/schedule effects. |

### MP-guided organising model
Rather than treating change as one workflow record, hold the project as a set of connected histories:
1. **Change identity and rationale:** what is being proposed, why, by whom, where, and against which baseline.
2. **Authority and decision:** who may assess, approve, reject, or issue the contractual instruction.
3. **Information revision:** which drawings, specifications, calculations, permits, and related documents change, and which revision is currently applicable.
4. **Physical implementation:** which work fronts, materials, teams, and completed work are affected; what was actually done and verified.
5. **Consequences:** cost, time, safety, quality, procurement, and downstream asset/handover effects.

Keep these linked without collapsing them into one status. A single change can be approved while its drawing is not yet issued; a drawing can be issued while a site team has not acknowledged it; work can be complete while inspection or as-built updates remain outstanding.

### MP-only likely contribution
MP broadens the representation beyond a conventional request/approval workflow. It foregrounds identity continuity, linked histories, parallel state dimensions, dependencies, and accumulated effects. It does not by itself guarantee that the assistant will challenge weak assumptions or reconstruct every failure trajectory.

## C. Critical Thinking skill alone
### Inquiry and challenge pass
Start with the mismatch between the software's recorded state and the project's contractual, documentary, and physical state. Do not assume the word “change” denotes one object or one lifecycle.

Reconstruct a plausible sequence:
1. A condition or need is observed on site or in design.
2. Someone records a request, RFI, nonconformance, or proposal.
3. The appropriate technical people assess feasibility and consequences.
4. The contractually authorised role decides whether to approve, reject, or request more information.
5. An authorised instruction is issued where required.
6. Controlled documents are revised and released.
7. Affected organisations receive and acknowledge the applicable information.
8. Procurement and site activities are adjusted.
9. Work is carried out, inspected, and recorded.
10. Commercial and schedule consequences are assessed and agreed under the contract.
11. As-built and handover records are reconciled.

### Challenges and counterexamples
- **Request is not instruction.** A site conversation, RFI response, email, or proposed sketch may not be a contractual instruction. The system must not silently promote informal communication into authority.
- **Approval is not implementation.** An approved change may still be blocked by permits, procurement, design completion, or site sequencing.
- **Document issue is not site receipt.** A new drawing in a central repository does not prove the crew has stopped using the superseded revision.
- **A single status field is misleading.** Approval, contractual instruction, document release, distribution, acknowledgement, physical completion, inspection, and commercial settlement can progress independently.
- **Work may already have happened.** A change can arrive after affected work has been installed. The system needs to preserve what was built, when, under which information, and whether it is accepted, altered, or subject to concession/rework.
- **Urgency is not a permission model.** Safety-critical or emergency work may require a special authorised route, but the system must model the actual contract and emergency governance rather than invent a universal bypass.
- **Authority is contextual.** A low-cost change can have high safety, statutory, operational, or whole-life impact. Cost-only approval thresholds are inadequate.
- **Impact is not merely a number.** The system should retain assumptions, affected work packages, dependencies, uncertainty, and source evidence behind cost and schedule estimates.
- **Corrections must be visible.** Preserve original events and append corrections or superseding decisions with actor, timestamp, reason, and source; do not rewrite history.
- **External systems remain authoritative for some facts.** The platform may link to signed instructions, controlled drawing repositories, BIM models, ERP/procurement, schedules, and inspection systems. It should not claim to replace them unless the organisation explicitly makes it the system of record.
- **Offline site conditions matter.** Acknowledgement and synchronisation may be delayed. Show when data was captured versus when it reached the service; don't represent a stale view as current.

### Technical/operational supportability
A single application can coordinate references, workflow, and evidence, but it cannot guarantee that the physical site follows the latest instruction. That requires operational controls, document distribution, site briefings, contract-defined authority, and verification. A universal workflow template is not supportable across all contracts without configurable governance and explicit local validation.

### CT-only likely contribution
The skill is strongest at reconstructing the sequence, identifying mismatches and counterexamples, challenging assumed authority, and separating recorded events from real-world work. It may discover similar dimensions to MP independently; that overlap is a test result, not an attribution error.

## D. MP + Critical Thinking together
### Combined model
The MP inventory supplies a broad map of the entities, constraints, authorities, flows, dependencies, and accumulated consequences. Critical Thinking then interrogates each proposed relationship and asks whether the causal sequence and evidence actually support it.

The combined central invariant is:

**Maintain a trustworthy, traceable relationship between (1) the change being proposed, (2) the authority and decision governing it, (3) the controlled information that defines the work, and (4) the physical work actually performed and accepted—while preserving the commercial and schedule consequences.**

This is not a claim that all four dimensions can be reduced to one canonical record. They should be separate but linked.

### Recommended domain model
- Change case: stable identity, origin, rationale, location, affected assets/work packages, status of proposal.
- Baseline snapshot: linked scope/design/document/programme/cost versions and effective dates.
- Assessment records: discipline-specific impact, assumptions, dependencies, evidence, owner, date, confidence, unresolved items.
- Decision and authority record: decision-maker, authority basis, approval/rejection/conditions, effective time, signed source.
- Instruction record: issuer, contract basis, recipient, scope, effective date, linked decision.
- Document revision records: document identity, revision, supersession, release status, distribution targets, acknowledgements.
- Implementation records: work front, task, material/procurement changes, crew briefing, actual start/finish, evidence, inspection and acceptance.
- Consequence records: cost/time claims, risk, quality, safety, permit and whole-life effects; distinguish estimate, submitted claim, assessed amount, and agreed amount.
- Event/provenance log: actor, source, event time, capture time, correction links, attachments, and immutable history.

### Implementation sequence
1. Pilot one project and one contract form; map its actual authority and instruction procedures with contract/legal/project professionals.
2. Establish stable change identity and immutable event history.
3. Link each case to baseline versions and affected work packages/documents.
4. Implement authority/decision/instruction as distinct records and transitions.
5. Add controlled document revision, distribution, and site acknowledgement.
6. Add physical implementation, inspection, and as-built reconciliation.
7. Add commercial/schedule consequence tracking and integrations only after the core chain is reliable.
8. Test with scenarios: rejected request; approved but not instructed; instructed but document not issued; revised document not received; work performed against superseded drawing; emergency action; partial implementation; disputed cost/time claim; retrospective correction.

### Combined contribution
MP provides an explicit map of the domain dimensions and their relationships. Critical Thinking tests whether those relationships survive a real timeline, counterexamples, authority checks, and evidence scrutiny. Their overlap is substantial: both can surface state distinctions, dependencies, and provenance. The combination may make the dimensions more visible and then more rigorously tested, but this test does not establish that the combination is superior to either skill alone.

## Shared evaluation criteria
Scale: 0 = absent; 1 = partial; 2 = clear. Scores are qualitative self-assessments by the same assistant, not independent measurements.

| Criterion | A Conventional | B MP | C Critical Thinking | D MP + CT |
|---|---:|---:|---:|---:|
| Identifies the operating invariant | 1 | 2 | 2 | 2 |
| Separates real-world state from recorded/assumed state | 1 | 2 | 2 | 2 |
| Exposes dependencies and authority boundaries | 1 | 2 | 2 | 2 |
| Identifies failure modes and recovery paths | 1 | 1 | 2 | 2 |
| Improves implementation sequencing | 1 | 1 | 2 | 2 |
| Questions technical/operational supportability | 1 | 1 | 2 | 2 |
| Reduces cognitive load without replacing domain detail with jargon | 2 | 1 | 2 | 2 |
| **Total (out of 14)** | **8** | **10** | **14** | **14** |

Scores should not be interpreted as proof of skill effects. The CT-only draft was especially explicit about causal sequence and counterexamples; the MP-only draft was strongest at surfacing a domain map and parallel histories. The combined version is clearer as a model, but did not score above CT alone on the selected rubric. MP's potential value may lie in making a larger set of relevant dimensions inspectable, not necessarily in improving every criterion score.

## Attribution: overlap and distinct contributions
- **Conventional planning:** standard architecture decomposition, roles, workflow, integrations, auditability, and familiar project risks.
- **MP:** structured the domain into board/constraints, memory, editors/authority, flows, audits, identity, working lines, state distinctions, and accumulation. It made parallel histories and their links explicit.
- **Critical Thinking:** independently surfaced timeline reconstruction, counterexamples, informal-versus-authorised instruction, event provenance, corrections, offline conditions, and the limits of software control over physical work.
- **Overlap:** both MP and Critical Thinking can add dimensions. In this run, both identified that approval, issue, receipt, implementation, and acceptance are not interchangeable. Do not assign the discovery exclusively to one skill merely because it appears in its output.
- **Combination:** MP's map gave CT more explicit dimensions to challenge; CT tested whether the map represented a viable real-world sequence. This is a plausible interaction observed in the drafts, not independently established causality.

## Research grounding
- Scottish Government construction procurement handbook, Chapter 16: change control should assess cost, programme, specification and stakeholder impacts; inform and consult relevant parties; update documents; record and authorise decisions; implement changes. It stresses aligning the design baseline, cost plan, and programme, and specifies that contractual instructions must be issued by the authorised role. https://www.gov.scot/publications/project-initiation-business-cases-handbook/pages/16/
- RICS, *Change Control and Management* (2024): guidance emphasises project-specific contractual roles, change versus variation distinctions, procedures, documentation, and digital portals. https://www.rics.org/profession-standards/rics-standards-and-guidance/sector-standards/construction-standards/black-book/change-control-and-management-1st-edition2
- The Scottish Government guidance is jurisdiction-specific and should not be treated as a universal legal template. Contract forms and applicable law determine the actual authority and notice requirements.

## Findings
1. Conventional planning produces a plausible feature and architecture list but tends to compress distinct operational states into a workflow unless deliberately challenged.
2. MP alone contributes a useful structured domain map and makes parallel histories and accumulated dependencies salient.
3. Critical Thinking alone can also add substantial dimensions, especially causal sequence, counterexamples, authority boundaries, and real-world versus recorded state.
4. MP and Critical Thinking overlap materially; they are not cleanly separable into “warehousing” versus “questioning” contributions. Both can add dimensions.
5. In this run, CT alone and MP+CT reach the same qualitative score. The combined answer is more explicitly organised, but no incremental score gain is demonstrated.
6. The strongest candidate invariant is the traceable relationship among change identity, authority/decision, controlled information, and physical implementation/acceptance, with commercial and schedule consequences linked but distinct.
7. The system should coordinate evidence and workflow, not pretend to guarantee site compliance or replace contract-specific professional authority.

## Limitations and next test
- Same assistant, same conversation, and shared model context; not blind or context-isolated.
- The four drafts were composed sequentially and can contaminate one another.
- Scores are self-assessed and may favour dimensions the rubric makes salient.
- The Critical Thinking skill is provisional; this is not independent validation.
- The scenario is a generic multi-party infrastructure project; actual contracts and jurisdictions vary.
- A stronger follow-up would run each condition in separate context windows with identical scenario inputs, randomise output order for an external assessor, and record each newly introduced dimension before revealing the other conditions.
