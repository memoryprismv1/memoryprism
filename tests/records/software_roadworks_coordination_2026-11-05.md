# Software Daily Test: Citywide Roadworks and Utility-Conflict Coordination

**Test ID:** MP-SOFTWARE-2026-11-05-01  
**Date:** 2026-11-05  
**Track:** Software daily test  
**Selection:** Assistant-invented scenario, not derived from the user's projects or recent conversations.  
**Test type:** Three-condition comparison: conventional software planning, MP-guided planning, and MP plus critical challenge.

## Purpose

Continue the software test track. This test examines whether MP helps organise a multi-party scheduling problem around the real-world operating conditions, and whether a critical challenge pass exposes assumptions that planning alone may miss.

This is a constructed scenario, not a real procurement or implementation recommendation.

## Scenario brief

A metropolitan road authority has approved a new coordination platform for planned roadworks and utility work across its road network. The decision to build the platform has already been made; build-versus-buy is outside the scope of this test.

The platform must coordinate planned activities from:
- the road authority's own maintenance teams;
- water and wastewater utilities;
- electricity and gas utilities;
- telecommunications providers;
- contractors working on behalf of those organisations.

Requirements:
- Each organisation can submit proposed work with location, work type, planned start/end, road-space impact, and responsible contact.
- The platform identifies spatial and temporal overlaps with other proposed or approved work.
- Conflicts are routed to the relevant organisations for review and resolution.
- Approved work can be rescheduled, modified, or rejected by authorised parties.
- Emergency work can be registered even when normal lead times are impossible.
- Public-facing road disruption information can be published from approved records.
- Every decision, schedule change, and override must be traceable.

Non-goals:
- Controlling traffic signals or physical road barriers.
- Replacing each utility's asset-management or work-order system.
- Automatically deciding which organisation has priority in every conflict.
- Guaranteeing that field work happens exactly as scheduled.

Assumptions for the exercise:
- The authority controls the platform and its approval workflow.
- Participating organisations have different internal systems and data quality.
- Work locations may be represented as road segments, polygons, addresses, or map-drawn areas.
- Field schedules can change after approval.

## External domain evidence consulted

The Federal Highway Administration's guidance describes project coordination as involving who is involved, when work can occur, and what it accomplishes. It identifies coordination across agencies and across projects as a way to reduce conflicts and disruption.

FHWA guidance also notes that utility coordination should occur early and involve affected utilities and relevant agencies. Its current right-of-way and utilities chapter includes utility coordination, agreements, and location of existing facilities as distinct topics.

Sources:
- FHWA, “Guide to Project Coordination for Minimizing Work Zone Mobility Impacts,” Chapter 2: https://ops-dr.fhwa.dot.gov/publications/fhwahop16013/chap2.htm
- FHWA, “PDDM 12: Right of Way and Utilities”: https://highways.dot.gov/federal-lands/pddm/right-way-utilities
- FHWA, “4.0 Work Zone Impacts Management Strategies”: https://ops-dr.fhwa.dot.gov/wz/resources/publications/trans_mgmt_plans/sec4.htm

These sources support the domain context and need for coordination; they do not prescribe the architecture below.

## Condition A — conventional software-planning pass

### Problem framing

Build a multi-organisation roadworks scheduling and permit-coordination platform that collects proposed work, detects conflicts, supports review and approval, and publishes approved disruption information.

### Workstreams

1. **User and organisation management**
   - Register participating organisations.
   - Define users, roles, and approval authority.
   - Support delegated contractor access.

2. **Work submission**
   - Create and edit work proposals.
   - Capture location, time window, work type, impact, and contacts.
   - Attach maps, drawings, and supporting documents.

3. **Conflict detection**
   - Detect overlapping locations and time windows.
   - Identify nearby work that may affect the same route or traffic flow.
   - Support configurable conflict rules.

4. **Review and resolution**
   - Notify affected parties.
   - Record comments and proposed schedule changes.
   - Approve, reject, or return proposals for revision.

5. **Emergency work**
   - Register urgent work.
   - Notify affected parties.
   - Reconcile emergency records with normal planning afterwards.

6. **Public information**
   - Publish approved closures and disruption windows.
   - Provide feeds for public websites and journey-planning partners.

7. **Reporting and audit**
   - Track decisions and schedule changes.
   - Report conflict frequency, delays, and coordination outcomes.

8. **Integration and rollout**
   - Import existing planned-work records.
   - Provide APIs and exports.
   - Pilot with selected utilities before network-wide rollout.

### Preliminary architecture

A modular application with organisation and identity management, a work proposal service, geospatial conflict detection, workflow/notification services, public information APIs, and an audit log. A relational database with spatial support is a plausible starting point, subject to scale and integration requirements.

### Main risks identified

- Inconsistent location formats.
- Poor or stale schedule data.
- Different approval processes across organisations.
- Excessive conflict notifications.
- Emergency work bypassing normal workflows.
- Incorrect public disruption information.
- Integration and access-control failures.

## Condition B — MP-guided planning pass

### Pre-interpretation inventory

| MP concept | What I identify in this query |
|---|---|
| Board | The shared road network over a period of planned and actual work, with limited road space and competing uses |
| Memory | Persistent proposals, approvals, schedule changes, actual work events, and prior decisions |
| Constraints | Road capacity, time windows, permit conditions, utility access, safety requirements, and each organisation's authority |
| Editors | Approval rules, conflict rules, and authorised decisions that filter which proposed work can proceed and under what conditions |
| Flow Under Constraint | Physical traffic movement, work activity, and the information exchanged between organisations |
| Audits | Traceable approvals, objections, overrides, schedule changes, and emergency-work reconciliation |
| Identity | Work item, location, organisation responsible, contractor, approval authority, and current revision |
| Working Lines | Candidate work windows and alternative routes or staging arrangements; actual options depend on local conditions |
| No Sacred States | A proposal or approved schedule is provisional; field conditions can invalidate the plan |
| Accumulation Patterns | Repeated deferrals, overlapping projects, recurring emergency repairs, and unresolved conflicts can accumulate into future congestion or maintenance pressure |

### Central organising idea

The platform is not merely a calendar with a map. It coordinates competing claims on shared physical space, while the people submitting and approving work do not all have the same authority or information.

The important objects are not just work orders. They are:
- proposed use of a particular piece of road space;
- the time interval during which that use is expected;
- the organisations affected;
- the authority that can approve or alter it;
- the actual field activity, which may diverge from the approved plan.

### Proposed core invariant

**Every displayed approved work plan must identify its current revision, approving authority, location/time scope, and whether it is still believed to match field reality.**

A work proposal is not the same as an approved plan. An approved plan is not proof that work is happening as scheduled. A published public notice is not the authoritative work record.

### Separate lifecycle dimensions

Avoid one status field attempting to represent everything.

- **Proposal lifecycle:** draft, submitted, under review, revised, approved, rejected, withdrawn.
- **Schedule state:** proposed window, approved window, revised window, actual start/end.
- **Field execution:** not started, underway, paused, completed, abandoned, unknown.
- **Conflict state:** none detected, potential conflict, review required, resolved, accepted with conditions.
- **Publication state:** not publishable, ready, published, corrected, withdrawn.

This avoids confusing a workflow decision with physical reality. For example, work can be approved but not yet started; underway but running outside the approved window; or complete while the public notice remains active.

### Proposed sequence

1. Establish organisation identity, roles, and approval authority.
2. Agree on location representation and spatial precision.
3. Define work proposal and revision history.
4. Build temporal and spatial conflict detection.
5. Build multi-party review and resolution workflows.
6. Add emergency work registration and after-the-fact reconciliation.
7. Publish public-facing information only from approved, current records.
8. Add operational analytics after schedule and field data quality are understood.

### MP-specific planning shift

The main shift is from a feature-led permit workflow to a model that keeps proposed, approved, published, and actual work separate.

That changes the data model and the order of implementation. The platform must preserve the difference between a plan, an authorisation, and an event in the street.

## Condition C — MP plus critical challenge pass

The challenge pass tests the plan's assumptions and operational failure cases.

### Challenges and corrections

1. **What exactly counts as a spatial conflict?**
   - Two work areas may overlap geometrically but not operationally conflict if they occupy different road levels or sides.
   - Nearby work may conflict without polygon overlap if it affects the same diversion route or traffic queue.
   - Conflict detection needs a configurable impact model, not just intersecting shapes.

2. **How reliable are submitted locations?**
   - A road name or address may be too coarse for safe coordination.
   - Utilities may have uncertain subsurface locations; field verification may change the work footprint.
   - Store source, precision, and confidence/quality of location data. Do not imply survey-grade certainty from a rough map pin.

3. **Who has the authority to resolve a conflict?**
   - The platform cannot infer legal priority from the order in which requests arrive.
   - Authority may depend on permit conditions, road classification, emergency status, statutory rules, and local agreements.
   - Model decision rights explicitly and keep the rationale attached to the decision.

4. **What happens when field reality diverges from the approved plan?**
   - Crews may start late, uncover unexpected infrastructure, extend work, or stop early.
   - A field update should not silently rewrite the approved record.
   - Preserve planned and actual times separately; trigger re-evaluation when deviations affect another party.

5. **Can emergency work be delayed by the normal workflow?**
   - It must not be. Emergency registration should be fast and support retrospective completion of required information.
   - Emergency status should trigger notifications and later reconciliation, not erase the work from the coordination history.

6. **Can the system accidentally create false certainty for the public?**
   - A public map showing an approved closure may be wrong if work is postponed or abandoned.
   - Public notices need freshness rules, update ownership, and explicit status.
   - A notice should be withdrawn or corrected when the underlying work changes.

7. **How should recurring work and deferrals be handled?**
   - Repeatedly moving a project can create a false impression that it has been resolved.
   - Preserve deferral history and show cumulative impact, not just the latest date.
   - Detect repeated conflict patterns that may require a higher-level corridor plan.

8. **What if one organisation does not participate or update its records?**
   - The system cannot coordinate information it never receives.
   - Define minimum participation obligations, escalation routes, and a visible “data not confirmed” state.
   - Do not treat absence of a submitted work item as evidence that no work will occur.

9. **What is the authoritative record?**
   - Permit approval, utility work order, contractor schedule, and public notice may live in different systems.
   - Establish which system owns each fact and whether the platform is authoritative, a synchronised coordination layer, or both.
   - Conflict resolution and audit history depend on this distinction.

### Revised recommendation

Build the platform around a versioned work record and explicit separation of:
- proposal;
- approval;
- planned schedule;
- actual field activity;
- public notice.

Start with a corridor-level pilot involving a small number of participating organisations. Test spatial conflict rules against real historical cases, including false positives and near-miss conflicts. Add public publishing only after schedule updates and field deviations can be represented reliably.

## Comparative matrix

| Dimension | Conventional planning | MP-guided | MP + critical challenge |
|---|---|---|---|
| Initial framing | Multi-party scheduling and permit platform | Shared-space coordination under constraints | Coordination quality depends on authority, location certainty, and field updates |
| Core model | Work proposals, conflicts, approvals, notices | Distinct claims on space, decisions, and physical execution | Versioned record separating proposal, approval, schedule, actual work, publication |
| Conflict detection | Spatial/temporal overlap | Competing use of shared road space | Geometric overlap is not sufficient; indirect network impacts matter |
| State handling | Workflow statuses | Separate proposal, schedule, field, conflict, publication dimensions | Preserve deviations and corrections without overwriting approved history |
| Authority | Roles and permissions | Editors/approval decisions | Legal/contractual authority must be explicit and contextual |
| Emergency work | Emergency workflow | Exception to normal scheduling | Fast registration plus retrospective reconciliation |
| Public information | Publish approved closures | Public notice as a separate representation | Freshness, withdrawal, and correction are mandatory |
| Main risk | Integration and stale data | Confusion between plan and reality | False certainty from uncertain location, missing participants, and field divergence |
| Delivery sequence | Build modules and pilot | Establish records and distinctions before workflows | Validate data/authority and conflict model in a corridor pilot before public publishing |

## Findings

### What changed?

- The conventional plan was plausible and identified major functional areas.
- MP made the separation between proposal, approval, planned schedule, actual field activity, and public notice the organising structure.
- The challenge pass showed that spatial-temporal overlap is not equivalent to operational conflict, and that missing participation or stale field updates can make the platform falsely reassuring.

### What can be attributed to MP?

The explicit separation of the different representations of a work item emerged in the MP-guided framing. It makes a useful data-model distinction visible.

The critical challenge pass contributed the deeper tests around legal authority, location precision, indirect network effects, and data participation. These findings belong to the challenge pass rather than uniquely to MP.

### Provisional assessment

MP appears useful for exposing distinctions between a proposed action, an authorised action, and what actually happens. In this scenario, that distinction affects the core data model and workflow.

The challenge pass adds value by questioning whether the platform can know enough, and whether its apparent certainty is justified.

This is not proof of MP superiority. All three passes were generated by the same assistant in the same conversation; no blind review, independent software architect scoring, or context isolation was available.

## Evaluation criteria for future software tests

Apply the same criteria to future software scenarios:
1. Did the approach identify the real operating invariant?
2. Did it distinguish intended/authorised state from actual state?
3. Did it identify dependencies, authority, and data ownership?
4. Did it expose failure modes and recovery paths?
5. Did it improve implementation sequencing?
6. Did it identify where the system could create false certainty?
7. Did it reduce unnecessary cognitive load without sacrificing useful domain detail?

Do not score an answer as better merely because it is longer or more technical.

## Sources

- FHWA, “Guide to Project Coordination for Minimizing Work Zone Mobility Impacts,” Chapter 2: https://ops-dr.fhwa.dot.gov/publications/fhwahop16013/chap2.htm
- FHWA, “PDDM 12: Right of Way and Utilities”: https://highways.dot.gov/federal-lands/pddm/right-way-utilities
- FHWA, “4.0 Work Zone Impacts Management Strategies”: https://ops-dr.fhwa.dot.gov/wz/resources/publications/trans_mgmt_plans/sec4.htm

## Next probe

Use another software scenario in which the need for a coordination system is established, but where the central invariant and authority structure differ. This will help test whether MP's value is general or specific to shared-space scheduling.
