# Software Daily Test: Blood-Component Inventory Coordination

**Test ID:** MP-SOFTWARE-2026-11-06-01  
**Date:** 2026-11-06  
**Track:** Software daily test  
**Scenario selection:** Assistant-invented independently of the user's recent conversations, projects, interests, and hypotheses.  
**Method:** Three-way qualitative comparison: conventional planning; MP-guided planning; MP plus the Critical Thinking skill. Same assistant and conversation context; not blind, context-isolated, or independently assessed.

## Scenario

A regional hospital network wants coordinated visibility of blood-component inventory across multiple transfusion laboratories, hospitals, and remote storage points.

The system needs to track each component unit by unique identifier, component type, blood group, donation lineage, expiry, location, and status. It must distinguish quarantine, testing clearance, release, reservation, issue, return, transfer, discard, and expiry. Users need visibility into available, reserved, crossmatched, quarantined, and in-transit stock; inter-site transfers; physical stock discrepancies; emergency issue; and downtime.

### Boundaries and non-goals

- No clinical transfusion decisions.
- No invention or replacement of compatibility rules.
- No replacement of laboratory information systems or clinical authority.
- No autonomous override of quarantine, testing, or authorised release.
- The coordination system reports and reconciles operational state; it does not declare clinical suitability independently.

## Evidence reviewed

- British Society for Haematology, 2024, [Guidelines for the specification, implementation and management of IT systems in hospital transfusion laboratories](https://b-s-h.org.uk/guidelines/guidelines/guidelines-for-the-specification-implementation-and-management-of-it-systems-in-hospital-transfusion-laboratories): unit-level records, compatibility/crossmatch workflows, emergency issue, downtime, audit trails, alarms, fridge tracking, and contingency planning.
- Canadian Blood Services, [Blood system inventory management best practices guide](https://professionaleducation.blood.ca/en/transfusion/clinical-guide/blood-inventory-management): physical count and system reconciliation, avoiding unnecessary reservations, protecting O-negative stock, and redistribution of short-dated stock with appropriate transport, storage, and documentation.
- Government of India, [eRaktKosh — About](https://eraktkosh.mohfw.gov.in/eraktkosh/): centralised blood-bank management, donor lifecycle, component preparation, inventory visibility, alerts, and blood-bank networking.

These sources establish relevant operational requirements and existing system patterns. They do not constitute a complete procurement or implementation specification for this hypothetical network.

## A. Conventional software planning

A conventional plan organises work into:
1. Unit and component records.
2. Inventory and expiry management.
3. Laboratory-system integrations.
4. Inter-site transfer management.
5. Emergency and downtime workflows.
6. Audit, reporting, security, and reliability.

A plausible architecture includes a unit registry, inventory service, workflow/event history, laboratory adapters, transfer management, alerts, and reporting.

Risks identified include inaccurate stock, duplicate reservations or issue, expiry errors, interface failures, incorrect unit-patient association, storage/transport condition failures, emergency-workflow misuse, and inadequate access control or auditability.

## B. MP-guided planning

| MP concept | What I identify in this query |
|---|---|
| Board | Regional transfusion operation across laboratories, hospitals, and remote storage. |
| Memory | Persistent donation lineage and event history for each donation and its derived components. |
| Constraints | Expiry, storage conditions, laboratory release, compatibility procedures, location, transport, and access. |
| Editors | Validated testing, quarantine/release controls, reservation, issue authorisation, and discard rules. |
| Flow Under Constraint | Physical component movement and information flow between sites and systems. |
| Audits | Unit history, staff actions, approvals, emergency issue, transfers, and physical reconciliation. |
| Identity | Unique component identity, parent-donation lineage, current location/status, and patient association where applicable. |
| Working Lines | Candidate transfer routes; their feasibility is not established by the scenario. |
| No Sacred States | A software status is not proof of physical reality; units can move, be recalled, quarantined, or become otherwise unavailable. |
| Accumulation Patterns | Short-dated stock, reservations, stockouts, wastage, and demand imbalance across sites. |

**Organising invariant:** A unit must not be presented as available merely because a database says it is present. Availability requires support from validated records and the relevant operational checks. This is an inventory-integrity principle, not a clinical compatibility rule.

The plan separates state dimensions that a single status field could obscure:
- lifecycle state;
- inventory allocation;
- physical location;
- quality/hold state;
- patient association.

Suggested sequence:
1. Map authoritative sources and ownership for each field.
2. Establish unit-level identity and barcode capture.
3. Define the separate state dimensions and event history.
4. Integrate laboratory systems without overriding their authority.
5. Add transfer handling and physical reconciliation.
6. Add expiry/stock alerts and operational reporting.
7. Test downtime and recovery procedures.

**MP contribution:** It makes component lineage, eligibility, and physical location the organising centre. The dashboard becomes a view over these distinctions rather than the primary model.

## C. MP plus Critical Thinking skill

The challenge pass used the **Critical Thinking — Basic Skill** from the user's [memoryprismv1/cognitive-interface-ai-skills repository](https://github.com/memoryprismv1/cognitive-interface-ai-skills):

- Skill file: [critical-thinking/SKILL.md](https://github.com/memoryprismv1/cognitive-interface-ai-skills/blob/main/critical-thinking/SKILL.md)
- Skill file blob SHA at inspection: 0bd33321e535d9e68469307f2128cf27637046c9
- Skill status in that file: **Provisional; derived from current development records and not yet validated as a reliable capability.**

The skill's relevant behaviours include finding mismatches, comparing explanations, reconstructing causal trajectories where sequence matters, investigating existing evidence, separating different levels of claim, trying to break the preferred explanation, and leaving unresolved issues explicit. The challenge pass below is attributed to that skill; it is not presented as an independently invented generic checklist.

### Challenge findings

1. **Field-level authority:** identify the authoritative source for every critical field. The coordination layer must not overwrite authoritative clinical or laboratory results.
2. **Physical/software mismatch:** when physical location is unconfirmed or discrepant, show it as unconfirmed/discrepant rather than treating the last database location as current fact.
3. **Distributed reservation and issue:** stale views across sites can cause double reservation or issue. Allocation needs transactional controls and idempotent event handling. A transfer in progress must not be counted as available at both source and destination.
4. **Derived availability:** availability is derived from multiple validated dimensions, not a manually toggled status. Clinical suitability remains within the validated clinical process.
5. **Returned units:** a returned unit does not automatically become available. Capture return time, relevant conditions, inspection, and authorised release.
6. **Emergency issue:** the system must support fast, governed emergency workflows without inventing clinical rules or silently bypassing required authority.
7. **Downtime:** define which functions are disabled when live data or systems are unavailable; preserve approved manual procedures and later reconciliation. Cached “available” status must not masquerade as live validation.
8. **Local resilience:** redistribution can weaken a site's own buffer. Protect locally defined minimums and resilience rather than optimising only regional totals.
9. **Donation/component lineage:** preserve parent-child lineage so recalls and status changes can be traced to all derived components.

### Revised recommendation

Begin with a **read-only, unit-level visibility and reconciliation pilot**. Validate identity, lineage, source authority, location confidence, and physical/software reconciliation before enabling transfers or recommendations. Add transfer coordination only after the operational state model and recovery behaviour are proven. Keep clinical decisions and authorisations within existing validated systems and roles.

## Comparison and provisional finding

- **Conventional planning** produced a plausible modular application and a reasonable list of workstreams and risks.
- **MP** changed the organising model: lineage, eligibility, and physical location became central, and lifecycle, allocation, location, quality/hold, and patient association were separated.
- **Critical Thinking skill** challenged the proposed model against authority boundaries, stale distributed state, returns, downtime, local resilience, and the limits of automation. It narrowed the safe implementation sequence to a read-only pilot before transfer functionality.

The result suggests that MP can organise a complex software problem around the real-world object and its changing operational state. The Critical Thinking skill then tests the proposed account for mismatches, unsupported assumptions, and failure conditions. This is a provisional observation, not proof that MP is superior or that the Critical Thinking skill is independently reliable.

## Attribution and limitations

| Contribution | Attributed work |
|---|---|
| Conventional planning | Workstreams, plausible modular architecture, baseline risks. |
| MP-guided planning | Component lineage and operational state as organising centre; explicit separation of state dimensions; implementation sequence. |
| Critical Thinking skill | Challenge of authority, physical-vs-recorded state, distributed allocation, return handling, downtime, local resilience, and automation boundaries. |

This was a same-assistant, same-conversation qualitative comparison. It was not blind, context-isolated, or independently assessed. Topic selection was independent of the user's recent context; model evaluation was not independent. The Critical Thinking skill is marked provisional in its source repository. The test therefore cannot establish that the skill reliably caused every improvement, nor can it isolate the effect of MP from the effect of the challenge pass with experimental certainty.
