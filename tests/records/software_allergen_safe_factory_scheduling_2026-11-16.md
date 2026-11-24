# Software Daily Test: Allergen-Safe Food Factory Scheduling — 2026-11-16

## Test type
Software daily test. Scenario independently invented for this date and not selected from recent conversation topics.

## Scenario
A multi-product food factory uses shared production lines and equipment. Products have different allergen profiles. The factory wants to meet production targets while preventing allergen cross-contact and maintaining traceability.

The system must coordinate:
- Recipes, ingredient lots and allergen profiles.
- Supplier substitutions and specification changes.
- Shared equipment, utensils, transfer lines and difficult-to-clean locations.
- Production sequence, batch sizes and line capacity.
- Approved cleaning procedures and validation evidence.
- Cleaning execution, inspection and verification.
- Rework and work-in-progress.
- Packaging, label versions and changeover checks.
- QA holds, batch release and genealogy.

## Operating invariant
A production sequence is permissible only when the product, ingredients, equipment, cleaning controls, verification evidence and labelling state satisfy the applicable approved requirements. The scheduler may recommend sequences; it must not declare a hazard controlled or release product merely because a workflow step is marked complete.

## Three-way planning comparison

### A. Conventional software planning
Likely modules:
- Production order management.
- Recipe and ingredient management.
- Production-line scheduling.
- Cleaning and sanitation work orders.
- Quality assurance and release.
- Packaging and label management.
- Inventory and traceability.

Strengths:
- Familiar decomposition into users, modules, interfaces and integrations.
- Supports conventional backlog and workflow planning.

Risks:
- A cleaning task marked complete may not mean the required verification passed.
- A recipe change may invalidate a previously approved changeover.
- A supplier substitution may alter an allergen profile.
- Rework may introduce an allergen into an otherwise suitable product.
- A product may be correctly manufactured but incorrectly labelled.

### B. Memory Prism-guided planning

Pre-interpretation inventory:

| MP concept | What I identify in this query |
|---|---|
| Board | Factory production environment bounded by product, equipment, hygiene and food-safety constraints. |
| Memory | Recipe histories, batch records, cleaning records, supplier changes and validation evidence. |
| Constraints | Allergen profiles, equipment design, cleaning effectiveness, production capacity, staffing and labelling rules. |
| Editors | Production planners, sanitation teams, QA, suppliers and authorised release personnel. |
| Flow Under Constraint | Ingredients, work-in-progress, equipment, people and finished products moving through the factory. |
| Audits | Cleaning validation, verification, batch genealogy, recipe approval and label checks. |
| Identity | Product, ingredient lot, recipe version, equipment, production run and finished batch. |
| Working Lines | Scheduled, produced, cleaned, inspected, verified, released and labelled are distinct states. |
| No Sacred States | A previously validated cleaning process may require revalidation after relevant changes. |
| Accumulation Patterns | Residues, rework, queues and unresolved cleaning exceptions can accumulate. |

Likely improvements:
- Treat allergen changeover rules as operational dependencies, not a static lookup table.
- Preserve the exact ingredient lot and recipe version used for each production run.
- Distinguish cleaning execution, inspection, verification and QA disposition.
- Prevent a schedule from using a transition unless its required controls are approved and current.
- Preserve exceptions and the evidence used to resolve them.

### C. Memory Prism + Critical Thinking
Critical Thinking challenges both the design and the MP mappings:
- Does the system know the actual allergen profile of the ingredient lot, or only the default recipe profile?
- Does a cleaning completion record prove the validated procedure was followed?
- Is the cleaning procedure validated for this equipment and this product transition?
- What happens when a supplier changes an ingredient specification?
- Can the scheduler distinguish a permissible sequence from one that merely saves time?
- Is the proposed optimisation technically supportable without making food-safety decisions itself?

MP labels do not make a mapping correct merely by naming it; domain evidence must support each mapping.

## Proposed state and dependency model
A production transition should depend on:
1. Approved product recipe and version.
2. Ingredient lots with current specifications and allergen declarations.
3. Equipment identity and previous product history.
4. Approved cleaning procedure for the specific transition.
5. Cleaning execution record.
6. Required inspection and verification results.
7. QA authorisation where required.
8. Correct packaging and label version.

The system must not collapse these into one “changeover complete” flag. Cleaning completion is not the same as verified effectiveness, and neither automatically authorises finished-product release.

## Capability contribution and attribution boundaries

| Capability | Potential contribution | Status |
|---|---|---|
| Memory Prism | Persistent state, constraints, editors and histories. | Applied as planning lens. |
| Critical Thinking | Challenges assumptions, evidence and automation boundaries. | Applied as examination lens; not isolated blind run. |
| CT optional MP checklist | “For a query, does the ledger reconcile for that board under the specific constraints and editors?” | Not separately invoked or evaluated. |
| Optionality | Alternative production sequences and line allocation. | Relevant design consideration; not separately executed. |
| Good-Faith Collaboration & Approach Calibration | Coordination across production, sanitation, QA and suppliers. | Relevant; not separately executed. |
| Task Integrity | Keeps scheduling separate from food-safety release authority. | Relevant; not separately executed. |
| Verification Integrity | Separates cleaning completion from verified effectiveness. | Relevant; not separately executed. |
| Software Literacy | Tests whether integrations and optimisation are technically supportable. | Relevant; not separately executed. |
| Peer Review | Independent review of preserved outputs. | Not run. |
| Automaticity | Routine checks for invalid transitions and missing evidence. | Potential only. |
| A Touch of Grace | Clear exception messages and handoff communication. | Potential only. |
| AEL Runtime Accountability | Decision and approval provenance. | Not executed. |
| Q-Batch of Evidence | Isolated, comparable test conditions. | Not executed. |
| Faking Vision / FV Robots / Self-Learning POC | No demonstrated need in this scenario. | Not applicable. |

## Suggested implementation sequence
1. Build ingredient, recipe, allergen and equipment identity models.
2. Establish product-to-product changeover rules and approved cleaning procedures.
3. Record actual production, cleaning and verification events with timestamps and provenance.
4. Integrate packaging and label controls.
5. Implement scheduling with explicit hard constraints and authorised overrides.
6. Add exception handling for substitutions, rework, failed cleaning and equipment changes.
7. Add optimisation only after the safety and authority model is reliable.
8. Validate with mock recalls, adversarial changeovers and supplier/recipe change scenarios.

## Failure modes and recovery
- **Supplier substitution:** hold affected planning until the new specification and allergen profile are reviewed and approved.
- **Failed cleaning verification:** prevent the dependent production transition; retain results and route to authorised corrective action.
- **Recipe revision:** invalidate dependent schedules and assess whether cleaning or label approvals need renewal.
- **Rework introduced:** preserve genealogy and reassess allergen compatibility before reuse.
- **Equipment change or maintenance:** reassess applicability of cleaning validation and approved procedures.
- **Label mismatch:** hold packaging/release and reconcile product identity, recipe version and label version.
- **Missing records:** treat the required control as unverified, not implicitly passed.

## Evaluation criteria
1. Did the approach identify the actual operating invariant?
2. Did it distinguish real-world state from recorded or assumed state?
3. Did it expose dependencies and authority boundaries?
4. Did it identify failure modes and recovery paths?
5. Did it improve implementation sequencing?
6. Did it question whether proposed capabilities are technically and operationally supportable?
7. Did it reduce unnecessary cognitive load without replacing useful domain detail with framework jargon?

Do not score better merely because an answer is longer or more technical. Attribute MP and CT contributions separately. Sequential same-assistant reasoning in one conversation is not independent causal evidence.

## Research basis
- Minnesota Department of Agriculture, food allergen control guidance for manufacturers: https://www.mda.state.mn.us/food-feed/food-allergen-control
- UK Food Standards Agency, allergen cleaning guidance and review: https://www.food.gov.uk/business-guidance/allergen-guidance-for-food-businesses
- Research and technical literature on allergen cleaning validation and changeover controls: https://pubmed.ncbi.nlm.nih.gov/?term=food+allergen+cleaning+validation+manufacturing

## Limits
This is a scenario-based planning analysis, not a deployed-system test, factory trial, food-safety validation or isolated A/B experiment. No capability has been shown to reduce cross-contact or improve compliance. Actual controls must be defined and validated by qualified food-safety personnel against applicable regulations, product characteristics and equipment.

## Provenance
Prepared from the 2026-11-16 daily test research and analysis in this conversation. AEL, Q-Batch and Peer Review were not executed.
