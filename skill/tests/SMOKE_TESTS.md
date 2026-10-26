# Memory Prism Skill — Smoke Tests

These tests check whether the skill uses the source corpus accurately and proportionately. They test behaviour, not the ability to repeat Memory Prism vocabulary.

## Source-grounding test

**Prompt:** “What does Memory Prism mean by memory, constraints, editors and boards? How are they distinct?”

**Pass:** consults `references/source-corpus/Memory-Prism-Framework.md`; preserves distinctions (for example, constraints bound what is possible, whereas editors differentially shape which viable configurations persist); flags ambiguity rather than importing generic systems terminology.

**Fail:** answers from the checklist alone; collapses constraints and editors; implies intent where the source says none is required; treats source inclusion as independent empirical proof.

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
