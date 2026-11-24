# Software Daily Test: Semiconductor Fabrication Lot Scheduling — 2026-11-17

## Test type
Software daily test. Scenario independently invented for this date and not selected from recent conversation topics.

## Scenario
A semiconductor wafer fabrication facility must schedule lots through complex, re-entrant process routes. Lots have product-specific recipes and tool eligibility. Photolithography operations require auxiliary resources such as reticles and pods. Equipment breakdowns, uncertain processing times, maintenance, metrology holds and changing priorities continually alter the executable schedule.

## Operating invariant
A lot may advance only when its next process operation is valid for that lot, its current state, the selected tool and all required auxiliary resources. A schedule is a proposal; equipment and process-control systems must establish whether an operation can actually execute.

## Three-way planning comparison

### A. Conventional software planning
Likely architecture:
- Manufacturing execution system (MES).
- Production planning and scheduling.
- Equipment integration and dispatch.
- Recipe and process-control management.
- Reticle and auxiliary-resource management.
- Metrology and quality systems.
- Maintenance and equipment qualification.
- Traceability and genealogy.

Risks:
- Tool availability may be confused with tool eligibility.
- A tool may be available but awaiting qualification after maintenance.
- A reticle may exist but be allocated to another machine.
- An approved recipe may not be approved for a particular tool/chamber configuration.
- A lot may have completed a process step but remain on quality hold.
- A schedule may become invalid between generation and execution.

### B. Memory Prism-guided planning

Pre-interpretation inventory:

| MP concept | What I identify in this query |
|---|---|
| Board | Fab production environment, including tools, lots, recipes, resources and process constraints. |
| Memory | Lot genealogy, equipment history, recipe revisions, maintenance, metrology and prior process events. |
| Constraints | Tool eligibility, process windows, contamination compatibility, reticles, pods, capacity and deadlines. |
| Editors | Process engineering, equipment engineering, production control, quality and authorised release personnel. |
| Flow Under Constraint | Lots moving through re-entrant process routes and shared equipment. |
| Audits | Actual tool execution, recipe identity, metrology, qualification and process history. |
| Identity | Lot, wafer, recipe version, operation, tool, chamber, reticle and pod identities. |
| Working Lines | Planned, dispatched, started, completed, measured, held and released are distinct states. |
| No Sacred States | Earlier tool or recipe approval may no longer apply after maintenance or a process change. |
| Accumulation Patterns | Queue growth, work-in-progress, equipment downtime and delayed metrology accumulate across process stages. |

Likely improvements:
- Make eligibility and execution state first-class data.
- Distinguish tool availability, qualification, recipe compatibility and chamber condition.
- Preserve lot and wafer genealogy across re-entrant process routes.
- Treat reticles and pods as exclusive, stateful auxiliary resources.
- Keep planned, dispatched, executed, measured, held and released states separate.
- Preserve the history and reason for schedule changes.

### C. Memory Prism + Critical Thinking
Critical Thinking challenges both the design and the MP mappings:
- Is the lot's current process state established by execution records or inferred from the schedule?
- Does tool status represent physical availability, qualification, recipe compatibility and chamber condition separately?
- Can a reticle be reserved by two competing schedules?
- Does maintenance completion automatically restore qualification, or is a separate approval required?
- What happens when metrology results arrive after downstream operations have already been planned?
- Can the proposed optimiser model re-entrant routes and auxiliary-resource conflicts?
- Can the system fall back safely when the optimiser cannot produce a valid schedule?

MP labels do not make a mapping correct merely by naming it; domain evidence must support each mapping.

## Research-grounded scheduling insight
A 2026 photolithography scheduling study models dynamic job arrivals, uncertain setup and processing times, random machine breakdowns and stochastic downtime. It uses rolling-horizon scheduling: solve against a current snapshot, execute part of the plan, then reschedule as conditions change.

The study includes machine eligibility, sequence-dependent setup times, reticles and pods as auxiliary resources. Its case study uses a data-driven simulation model of a real manufacturing area, enabling offline comparison without disrupting live production.

## Suggested implementation sequence
1. Establish canonical identities for lots, wafers, operations, tools, chambers, recipes and auxiliary resources.
2. Model approved process routes and tool/recipe eligibility.
3. Integrate actual equipment state and maintenance qualification.
4. Model reticle, pod and other auxiliary-resource allocation.
5. Reconcile execution events, metrology and quality holds.
6. Implement rolling-horizon scheduling and dispatch.
7. Add simulation and offline replay before considering live optimisation.
8. Add guarded fallback behaviour for infeasible schedules, missing state and integration failures.

## Failure modes and recovery
- **Tool breakdown:** remove unavailable capacity, preserve in-process state and reschedule affected lots.
- **Maintenance complete but qualification pending:** keep tool unavailable for operations requiring that qualification.
- **Reticle conflict:** prevent simultaneous allocation; resolve resource ownership before dispatch.
- **Recipe revision:** re-evaluate affected scheduled operations against the new approved version.
- **Metrology failure:** place affected lot on hold and prevent dependent operations where required.
- **Stale equipment feed:** mark state uncertain and avoid dispatch based on stale availability.
- **Optimiser failure:** fall back to a validated dispatch policy or controlled manual process.

## Capability contribution and attribution boundaries

| Capability | Potential contribution | Status |
|---|---|---|
| Memory Prism | Persistent state, constraints, editors, histories and process transitions. | Applied as planning lens. |
| Critical Thinking | Challenges state assumptions, feasibility and automation boundaries. | Applied as examination lens; not isolated blind run. |
| CT optional MP checklist | “For a query, does the ledger reconcile for that board under the specific constraints and editors?” | Not separately invoked or evaluated. |
| Optionality | Alternative tool assignments and recovery schedules. | Relevant; not separately executed. |
| Good-Faith Collaboration & Approach Calibration | Coordination across process, equipment, production and quality teams. | Relevant; not separately executed. |
| Task Integrity | Prevents scheduler from assuming process-engineering or release authority. | Relevant; not separately executed. |
| Verification Integrity | Requires evidence for tool qualification, process execution and lot release. | Relevant; not separately executed. |
| Software Literacy | Challenges feasibility of MES/equipment integration and optimisation. | Relevant; not separately executed. |
| Peer Review | Independent review of preserved outputs. | Not run. |
| Automaticity | Routine validation, monitoring and dispatch checks. | Potential only. |
| A Touch of Grace | Clear operator-facing exception and recovery communication. | Potential only. |
| AEL Runtime Accountability | Decision and authority provenance. | Not executed. |
| Q-Batch of Evidence | Isolated comparisons and preserved test outputs. | Not executed. |
| Faking Vision / FV Robots / Self-Learning POC | No demonstrated requirement. | Not applicable. |

## Evaluation criteria
1. Did the approach identify the actual operating invariant?
2. Did it distinguish real-world state from recorded or assumed state?
3. Did it expose dependencies and authority boundaries?
4. Did it identify failure modes and recovery paths?
5. Did it improve implementation sequencing?
6. Did it question whether proposed capabilities are technically and operationally supportable?
7. Did it reduce unnecessary cognitive load without replacing useful domain detail with framework jargon?

Do not score better merely because an answer is longer or more technical. Attribute MP and CT contributions separately. Sequential same-assistant reasoning in one conversation is not independent causal evidence.

## Limits
This is a scenario-based planning analysis, not a deployed-system test, live-fab trial or isolated A/B experiment. No capability has been shown to improve throughput, yield or reliability. Any production scheduler must be validated against fab-specific process rules, data quality, safety controls and operator authority.

## Sources
- Deenen et al. (2026), “Scheduling with constraint programming in the dynamic and stochastic environment of a semiconductor photolithography area”: https://link.springer.com/article/10.1007/s10696-026-09666-5
- Survey, “Problems and Solution Methods of Machine Scheduling in Semiconductor Manufacturing Operations”: https://www.mdpi.com/2071-1050/15/17/13012
- Deenen et al. (2023), “Lithography reticle scheduling in semiconductor manufacturing”: https://doi.org/10.1080/0305215X.2023.2285416

## Provenance
Prepared from the 2026-11-17 daily test research and analysis in this conversation. AEL, Q-Batch and Peer Review were not executed.
