# Memory Prism Skill — Smoke Tests

These tests check whether the skill uses the source corpus accurately and proportionately. They test behaviour, not the ability to repeat Memory Prism vocabulary.

## Source-grounding test

**Prompt:** “What does Memory Prism mean by memory, constraints, editors and boards? How are they distinct?”

**Pass:** consults `references/source-corpus/Memory-Prism-Framework.md`; preserves distinctions (for example, constraints bound what is possible, whereas editors differentially shape which viable configurations persist); flags ambiguity rather than importing generic systems terminology.

**Fail:** answers from the checklist alone; collapses constraints and editors; implies intent where the source says none is required; treats source inclusion as independent empirical proof.

## User-orientation fidelity test

**Prompt:** “Explain Memory, Board, Constraints, Editors, Audits, Identity, Flow Under Constraint, Working Lines, Accumulation Patterns and No Sacred States using the user's orientation.”

**Pass:** consults `references/user-orientation.md`; preserves the user's wording and point of view; recognises that it describes the same existing concepts rather than introducing a new theory or competing definitions; consults the Framework and relevant essays when canonical definitions matter.

**Fail:** recasts the orientation as a new application layer, silently rewrites the user's descriptions, treats it as a replacement for the Framework, or ignores it and reproduces muddled interpretations.

## P-Memory scope and retrieval test

**Prompt:** “Is an atom a persistent structure? Is dark matter? What about a naturally occurring physical phenomenon and a deliberately produced software record?”

**Pass:** retrieves the P-Memory (Persistent Memory) interpretation; recognises naturally occurring and deliberately produced persistent structures as possible instances; does not require an agent, intention, storage, recognition, or a deliverable; distinguishes persistence from permanence and considers the relevant timescale; keeps the Framework as the canonical source.

**Fail:** interprets Memory as recollection or stored data only; treats intended outcomes as the only valid cases; marks a physical phenomenon inapplicable merely because nobody is trying to produce it; or treats every momentary state as automatically persistent.

## Selective inventory and Ledger test

**Prompt:** “Why can some seeds remain viable for decades, and how should a database column migration be planned while old and new application versions overlap?”

**Pass:** builds a problem-led inventory with only relevant concepts plus genuinely useful follow-up candidates; includes Ledger for the seed's stored energy and maintenance/viability budget, and for migration resources such as compute, I/O, lock duration, connection capacity, operator time, dry-run cost, timeout and rollback capacity. Distinguishes Ledger from Flow and Accumulation. Makes no requirement to include every MP concept.

**Fail:** produces a fixed all-concepts table; omits Ledger where available energy, resources or time-to-recovery materially constrain viability; or adds Ledger as a generic label without identifying actual inputs, reserves, expenditure or minimum maintenance costs.

## Ledger distinction test

**Prompt:** “What is the difference between Ledger, Flow Under Constraint and Accumulation Patterns?”

**Pass:** Ledger accounts for energy/resources available, consumed, reserved and required for minimum maintenance; Flow describes movement and transfer; Accumulation describes what builds up or becomes structurally concentrated. The answer uses the Framework's energy-accounting meaning and does not reduce Ledger to money or generic project budgeting.

**Fail:** treats the three as synonyms; mentions only costs without available resources or minimum maintenance; or forces an energy analogy where the domain has no meaningful resource account.

## Assistant reasoning audit test

**Prompt:** Give an exploratory answer to a topic where the initial explanation is plausible but rests on hidden assumptions and omits relevant information.

**Pass:** internally examines inherited assumptions, information used or missed, constraints shaping the answer, any editor actually supported by evidence, reasoning shortcuts, and alternative structures; revises the answer accordingly; surfaces material limitations without dumping the six questions on the user.

**Fail:** produces a plausible but scattered explanation; merely repeats the audit questions without using them; invents an editor; or makes the user identify omissions and repair the reasoning.

## Foundation versus Supplementary test

**Prompt:** “How do the four Foundation essays relate to Working Lines, No Sacred States and Accumulation Patterns?”

**Pass:** consults the four Foundation texts and the relevant Supplementary texts; distinguishes the four-operator foundation from supplementary structural lenses; explains the relationship without treating all seven as mandatory stages.

**Fail:** doesn't consult the texts; collapses all seven into an undifferentiated list; invents source claims; or applies all lenses by default.

## A — Pasta and sauce adhesion

**Prompt:** “Why does sauce cling to some pasta shapes better than others?”

**Look for:** geometry, surface texture, starch, sauce viscosity, temperature, and a useful variable comparison or experiment.

**Failure signs:** merely saying “surface area matters”; invoking every lens; inventing unsupported detail without distinguishing it from established food science.

## B — Traffic signals and learned conventions

**Prompt:** “Why do people coordinate around traffic lights so reliably, and what breaks when the convention changes?”

**Look for:** physical layout and visibility, learned shared meaning, conflicting expectations, transition risk, and evidence or a grounded example.

**Failure signs:** reducing the system to geometry alone; treating a learned convention as a physical law; implying the same mechanism governs all social and physical systems.

## C — Familiar keyboard sequence after an interface change

**Prompt:** “I keep pressing the old shortcut after the software moved it. Why?”

**Look for:** learned action path, repetition, feedback, relearning cost, and a practical adjustment.

**Failure signs:** turning this into a full systems report; explaining behaviour solely through metaphor; failing to give useful advice.

## D — A WhatsApp forward after debunking

**Prompt:** “Why does a false WhatsApp forward keep circulating after someone posts a correction?”

**Look for:** different transmission routes, audience overlap or mismatch, source trust, repetition, platform affordances, and evidence that could distinguish explanations.

**Failure signs:** asserting that correction never works; presenting a plausible social mechanism as proven without evidence; overlooking domain research.

## E — A power bank left in a drawer

**Prompt:** “Should I leave my power bank at 100% charge in a drawer for months?”

**Look for:** direct practical answer first, model-specific manufacturer guidance where possible, and battery chemistry/storage charge as the open detail.

**Failure signs:** delaying the answer to apply the checklist; assuming 100% is the ideal resting state; replacing device guidance with analogy.

## Scoring (per test)

Score each dimension 0, 1, or 2:
- **0:** absent or clearly mishandled.
- **1:** partly useful, with a notable omission or overreach.
- **2:** clear and useful.

Dimensions:
1. Directly engages the question.
2. Consults the correct source text when Memory Prism-specific interpretation is required.
3. Selects lenses proportionately.
4. Uses accurate domain mechanisms and evidence.
5. Distinguishes uncertainty from fact.
6. Produces a useful answer or next step while avoiding homework handoff.

Maximum: 12 per test. Scores are diagnostic, not a competition; note the failure mode behind low scores.

## Evaluation question

**Did the source corpus help the assistant interpret Memory Prism more faithfully, and did the checklist help find a better next question or action?** If not, identify the missing source or instruction before changing the checklist.


## F — Mantis shrimp club and “strongest material” claims

**Prompt:** “The mantis shrimp's striking club is sometimes described as one of the strongest materials in nature. Is it literally the strongest material on Earth, and how does it survive repeated impacts?”

**Look for:** separating the whole biological structure from a material tested in isolation; identifying the relevant performance measure (impact resistance, hardness, fracture toughness, energy dissipation, or strength); explaining the club's layered/composite architecture only to the level supported by evidence; distinguishing a plausible mechanism from demonstrated performance; and checking what is known about damage, wear, and biological maintenance.

**Failure signs:** declaring a universal “strongest material” without specifying a metric; treating hardness, strength, and toughness as interchangeable; assuming the club never accumulates damage or that its maintenance mechanism is known without evidence; turning an appealing “animal cement” analogy into a factual explanation; or using Memory Prism structure as a substitute for materials-science sources.

**Discriminating next question:** Which measured property and test conditions support the “strongest” claim, and what evidence connects the club's microstructure to its impact performance over repeated strikes?
