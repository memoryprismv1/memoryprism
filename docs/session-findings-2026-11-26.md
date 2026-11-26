# Session Findings — 25–26 November 2026

A summary of a long working session between the owner and Claude: reading the repo, running tests, a person-led inquiry, three machine tests and two blind tests on an invented machine. Individual results are in `tests/records/`; this page draws them together.

## 1. What Memory Prism is for

The owner's position, stated during the session:

- "It was supposed to be a people exercise, not making AI smarter. But it also needs to provide AI the correct questioning method on how to use it with a person."
- "Me needs a checklist to understand what something does, why and the bigger picture… humanity having a leg up in understanding things is the point here."
- "This is a thinking exercise. A thought experiment… If this happens, what background processes are required."
- "MP isn't obviously going to 100%, it doesn't have domain knowledge."

Implication: MP supplies the questions; domain knowledge supplies the answers. Tests that score an assistant's answer measure only the AI-led half.

## 2. The person-led method (now in `skill/memory-prism/references/person-led.md`)

- The person reasons and chooses the route; the assistant is the research arm.
- Start from a question whose premise the person can check themselves. Questioning the premise is the method working.
- Let the person map the topic onto concepts; respond concept by concept (confirm with an instance, adjust a misfit with a reason, note scale, add at most one or two).
- Turn "if X, then…" into required processes (detect, decide, signal, act/seal, pay) and report each as exists / doesn't / unknown.
- Treat a mismatch as another player not yet counted (another editor, board or flow).
- Name specifically what the person's logic got right.
- No homework for the person.

## 3. Results across tests

| Test | Setting | Result |
|---|---|---|
| Smoke H, G | AI-led, self-scored | Correct readings; flagged two possible Framework/essay wording issues |
| Bread, TLS (same context) | AI-led, contaminated baseline | No demonstrated difference |
| Bread, TLS (isolated, blind) | AI-led | MP +4 (bread), +1 (TLS); gains in evidence handling, loss in clarity |
| Fruit browning → bananas → fruit drop | Person-led | Person's logic reached correct structural hypotheses; transfer to bananas worked |
| Potholes | AI-led logic pass | 5/5 required processes confirmed; Board check corrected the imported mechanism |
| Prusa MK3S+ | AI-led, not blind | Matched most routine items; useful additions; one domain fact wrong |
| Honda GX160 | AI-led, frozen before comparison | 13 match, 4 stricter, 1 looser, 4 added, 3 partly, 4 missed |
| Invented machine: maintenance | Blind, isolated | Tie 44/46; ceiling effect |
| Invented machine: viability | Blind, isolated, harder spec | MP 38 vs 35/46; more serious flaws found; both caught the decisive energy shortfall |

## 4. Patterns

1. **Deconstruction rather than construction** (owner's reading). MP is strongest at taking something apart to understand it or to judge whether it will survive. When an expert-level assistant produces a checklist, MP adds little; when a non-specialist has to build understanding, the deconstruction is the construction.
2. **MP finds what; domain knowledge supplies numbers and procedures.** Misses were domain facts (Z lead-screw lubrication, coating solvents, geared-engine gearbox oil, storage fogging).
3. **Cautious bias without data.** Where MP had no number it chose the safe side (GX160: four stricter intervals; TSM-40: seven too-frequent, none too rare).
4. **Strongest concepts:** Translators ("check manually what no sensor reads"), Ledger ("can it pay its running costs?"; this exposed the TSM-40 energy shortfall), Board (corrected imported mechanisms), Working Lines (cable flex points, high-current terminals).
5. **Weakest concept in machines:** Editors (only the maintainer filters what persists).
6. **Clarity cost.** Concept tables cost clarity for an expert reader; for a non-specialist they may be the useful map.

## 5. Possible wording issues surfaced (for owner review, not changed)

- Framework, Feedback section: "Translators detect imbalance and trigger correction" may blur translator and audit (smoke test H).
- Audits essay: "mode shift is audit-driven" may overreach for orthodox seed dormancy (smoke test G).

## 6. Suggested next tests

- Ablation: the skill's working rules without MP concepts vs with them.
- A rate-estimation step for Ledger items, to test whether it corrects the cautious-interval bias.
- Fault diagnosis (effect back to cause) on a machine with a hidden fault key.
- Non-physical systems (a rumour, a tradition, an ignored rule) to find where MP's edges are.
- Repeat person-led sessions, measured by whether the person can explain, ask a sharper question and transfer to a new case.

## 7. Method notes for future blind tests

- Freeze derivations (with hash) before opening the reference.
- Strip framework method notes and randomise labels before scoring.
- Remove summary sections that list hazards, or the test hits a ceiling.
- All agents are currently the same model family; treat results as evidence, not proof.
