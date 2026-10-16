# Memory Prism Skill — Smoke Tests

These tests check assistant behaviour, not whether an assistant can repeat Memory Prism terminology. A passing response should make useful progress while avoiding forced analysis.

## Global pass criteria

A response passes when it:
- starts from the actual question or observation;
- answers settled parts directly;
- uses only relevant lenses;
- distinguishes evidence from inference when it matters;
- performs the next obvious research or comparison step when tools are available;
- leaves the user with a useful next move rather than a long list of homework;
- avoids pretending that analogy establishes mechanism.

A response fails when it recites the full checklist, forces all lenses, manufactures an exhaustive analysis, or repeatedly asks the user to direct the research.

## Test A — Pasta and sauce adhesion

**Prompt:** “Why does sauce cling to some pasta shapes better than others?”

**Look for:** geometry, surface texture, starch, sauce viscosity, temperature, and retention; a useful variable comparison or experiment.

**Failure signs:** merely saying “surface area matters”; invoking every lens; inventing unsupported detail without distinguishing it from established food science.

## Test B — Traffic signals and learned conventions

**Prompt:** “Why do people coordinate around traffic lights so reliably, and what breaks when the convention changes?”

**Look for:** physical layout and visibility, learned shared meaning, conflicting expectations, transition risk, and evidence or a grounded example.

**Failure signs:** reducing the system to geometry alone; treating a learned convention as a physical law; implying the exact same mechanism governs every social and physical system.

## Test C — Familiar keyboard sequence after an interface change

**Prompt:** “I keep pressing the old shortcut after the software moved it. Why?”

**Look for:** learned action path, repetition, feedback, relearning cost, and a practical adjustment.

**Failure signs:** turning this into a full systems report; explaining behaviour solely through metaphor; failing to give useful advice when the likely answer is settled enough.

## Test D — A WhatsApp forward after debunking

**Prompt:** “Why does a false WhatsApp forward keep circulating after someone posts a correction?”

**Look for:** different transmission routes, audience overlap or mismatch, source trust, repetition, platform affordances, and evidence that could distinguish explanations.

**Failure signs:** asserting that correction never works; presenting a plausible social mechanism as proven without evidence; overlooking domain research.

## Test E — A power bank left in a drawer

**Prompt:** “Should I leave my power bank at 100% charge in a drawer for months?”

**Look for:** direct practical answer first, model-specific manufacturer guidance where possible, battery chemistry and storage charge as the open detail.

**Failure signs:** delaying the answer to apply the checklist; assuming 100% is the ideal resting state; replacing device guidance with analogy.

## Test F — Mother of Thousands on native versus invaded boards

**Prompt:** “Why might Mother of Thousands produce enormous numbers of plantlets yet remain much less dominant in its native range than in some invaded habitats?”

**Look for:** the user's hypothesis is preserved as a testable possibility; native and invaded evidence are not conflated; recruitment and substrate are investigated; the assistant researches rather than repeatedly asking the user to supply the next question.

**Failure signs:** treating the substrate hypothesis as established without direct evidence; blaming one factor prematurely; using anecdotes as scientific proof; drifting to unrelated lenses; asking the user to lead every search.

## Scoring (per test)

Score each dimension 0, 1, or 2:
- **0:** absent or clearly mishandled.
- **1:** partly useful, with a notable omission or overreach.
- **2:** clear and useful.

Dimensions:
1. Directly engages the question.
2. Selects lenses proportionately.
3. Uses accurate domain mechanisms and evidence.
4. Distinguishes uncertainty from fact.
5. Produces a concrete next step or useful answer.
6. Preserves curiosity and avoids handing off assistant work.

Maximum: 12 per test. Scores are diagnostic, not a competition; note the failure mode behind every low score.

## Evaluation question

After each test, ask: **Did Memory Prism help the assistant find a better next question or action than it would have found otherwise?** If not, identify the wording or lens that caused the failure before changing the checklist.
