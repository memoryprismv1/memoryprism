---
name: memory-prism
description: Apply the Memory Prism framework (memory, constraints, editors, boards, ledger, translators, viability) to enter an unfamiliar topic or explain an observation by asking what makes something form, persist, change or fail. Works for science, engineering, software and operations, history, and everyday puzzles. Opens with a short concept-mapping table, does the next research step itself, and ends with a sharper next question. Use whenever the user mentions Memory Prism, MP, P-Memory, boards, editors, ledger, the starter kit or the seven lenses, asks what Memory Prism means, or poses an open-ended "why does X persist, drift, fail or behave differently here?" question. Do not use for settled facts, simple transformations, or routine procedures.
---

# Memory Prism

Help the user get traction on an unfamiliar topic: find the structure that shapes it, do the next obvious piece of research, and hand back a better question. Do not produce a formal analysis, show every lens, or turn the reply into a wiki.

## When to use it

Use it for open-ended inquiry: exploring a topic, explaining an observation, comparing cases, investigating why something forms, persists, drifts or fails.

Skip it, or use it only on the open part, when the user wants a settled fact, a simple transformation, or a specialist procedure to be followed directly. Answer the settled part first.

## What to read, and when

Load only what the question needs. Never read all of it by default.

| Need | Read |
|---|---|
| Applying Memory Prism to a topic (almost always) | `references/checklist.md` — the six questions, seven lenses, operating rules, reasoning audit |
| Mapping onto concepts; a distinction matters (constraint/editor, ledger/flow, audit/threshold) | `references/concepts.md` |
| Considering a specific lens | the entry in `references/lenses.md`, then the essay itself if wording matters |
| What Memory Prism *means*, its definitions, boundaries or intended reading | `references/source-corpus/Memory-Prism-Framework.md` first, then only the relevant essay in `references/source-corpus/foundations/` or `supplementary/` |
| Checking your reading of a concept against the user's own wording | `references/user-orientation.md`. It is a check, not a source: where it differs from the Framework or an essay, the source governs. Known case: Working Lines are functional pathways where force, energy or coordination already move; failure can follow those same paths. They are not pre-existing weaknesses. |
| Provenance, licence, canonical URLs | `references/source-corpus/README.md` |

For definitional questions, consult the Framework text itself. Do not answer from the checklist or from memory, do not swap in generic systems theory, and do not treat a claim in the source as empirically verified just because it is there. If exact wording or layout matters, the PDF at the repository root is canonical.

## Workflow

1. **Start from the user's observation.** Keep their framing long enough to see what caught their attention. Do not make them fill in a checklist.
2. **Answer the settled part directly.**
3. **Build the inventory** (next section) and put it first.
4. **Construct the domain inquiry.** Identify which domains may be relevant to the question. Develop the questions that need investigating within each relevant domain, and identify possible relationships, dependencies, comparisons or conflicts between domains. These are question-specific structures, not checklists supplied by the disciplines. Use Memory Prism to help discover and organise them.
5. **Investigate using domain knowledge.** Use the terminology, evidence, established methods and causal mechanisms of the relevant fields. Research the actual mechanisms rather than treating a structural resemblance as proof.
6. **Do the next obvious research or check yourself.** Search, inspect supplied material, compare, calculate, or propose a concrete test. Do not repeatedly hand research back to the user.
7. **Separate knowledge levels** when it matters: [Fact], [Reasonable inference], [Speculation], [Open question]. Cite external factual claims. Keep competing explanations alive until evidence separates them, and say what evidence would.
8. **Run the reasoning audit silently** (six questions at the end of `references/checklist.md`) and revise. Surface only material findings.
9. **Stop when there is traction.** Typically one to three structural observations, one important uncertainty, and one to three concrete next moves. Let the user's curiosity choose the route.

## The inventory table

For an exploratory question where Memory Prism is in use, the first substantive part of the reply is a compact table. It is an inspectable map of your reading, placed before any interpretation, so the user can correct it.

| MP concept | What I identify in this query |
|---|---|

Rules:
- Describe the actual feature, condition, process or residue in the query. Never paste definitions.
- Include a row only if it clarifies the question or a plausible follow-up. Omit the rest. No empty or "not relevant" rows.
- Mark candidate mappings as candidates, not findings.
- Use **P-Memory (Persistent Memory)** as the label for the Memory concept. It covers naturally occurring structures as well as produced ones. An intended goal is one case, not a requirement.
- Do not infer an editor merely because something changed, an audit merely because a state was restored, or a translator merely because something is measured.
- Do not add the table for settled facts, simple transformations, or when MP is not being invoked.

## Core concepts versus optional lenses

The Framework's core concepts orient your reasoning: Memory, Constraints, Editors, Board, Translator, Ledger, viability band and correction window, elasticity/inertia/lag, constraint assertion, Legacy, living matter, Architecture, Stability. Details and misuse traps are in `references/concepts.md`.

**Ledger is an original Framework concept, not an optional lens and not an addition.** Consider it whenever resource availability, reserves, maintenance cost or recovery capacity bear on persistence. Make it concrete. Keep it distinct from Flow (movement) and Accumulation (build-up). Constraints bound what is possible; editors shape what lasts. Never merge those two.

The seven essays are optional lenses: Boards, Audits, Identity, Flow Under Constraint, Working Lines, No Sacred States, Accumulation Patterns. Use none, one or several, as the problem warrants. There is no quota and no cap. A lens must earn its keep: drop it if it did not change what you noticed, inferred, researched or asked next.

## Behavioural rules

The operating rules in `references/checklist.md` apply. Most important:

- **Do not outsource inquiry construction to assumed expertise.** An expert may possess deep disciplinary knowledge without having a ready-made checklist for the particular question. Do not assume that intra-domain or inter-domain inquiry structures already exist. Construct the questions required by the problem.
- **Domain mechanisms outrank analogy.** Similar structure across domains is a lead, not proof of a shared mechanism.
- **No unsupported anthropomorphism.** Nothing senses, interprets, intends, corrects or governs unless a mechanism supports it. A threshold is not an audit.
- **No assumption laundering.** A hypothesis stays a hypothesis; fit with the framework is not evidence.
- **No fake completeness, no checklist theatre.** Do not recite the checklist or manufacture an exhaustive analysis.
- **No homework handoff.** Do not end with a question just to keep the conversation going.
- **Clarify only when blocked.** Otherwise state a reasonable assumption and proceed.
- **Never invent an editor, or claim information was unavailable without checking.**
- **Say what was and was not done.** Do not present a literature review as an experiment, a proposed test as a completed one, or a same-conversation comparison as an independent evaluation.

## Failure modes

Reciting the checklist · demoting Ledger · merging constraints and editors · forcing all seven lenses · defending the user's first idea as a conclusion · paraphrasing a source when exact meaning matters · repeating generic hypotheses instead of researching the specific uncertainty · overstating causation from correlation or anecdote · producing a report when a starter route was asked for.

## Success criterion

The user ends closer to understanding, with less supervisory effort and a clearer path to the next discovery. You can point back to source text when interpreting Memory Prism, and you leave routes open instead of furnishing every room.

## Running or scoring tests

If this skill is used inside the Memory Prism repository, the daily-test protocol is `tests/daily/README.md` and the rubric is `tests/daily/SCORING.md`. The skill behaviour smoke tests are `tests/smoke/SMOKE_TESTS.md`. These live outside the skill folder on purpose and are not needed for normal use.
