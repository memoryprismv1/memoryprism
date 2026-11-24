# Contributing to Memory Prism

Thank you for helping improve the documentation or starter kit.

Memory Prism is intended to help people enter unfamiliar topics and find a productive next question. Contributions should preserve that role rather than expand the checklist into a comprehensive protocol.

## Before proposing a change

Please identify:
1. The exact wording or behaviour that failed.
2. The domain and prompt where it failed.
3. What the assistant did as a result.
4. The smallest change likely to improve it.

Prefer evidence from use over speculative additions. Do not add a new checklist item merely because it sounds useful in isolation.

## Editorial principles

- Preserve the source boundary: the Framework and exactly seven supporting essays for the starter kit.
- Keep optional lenses optional.
- Prefer domain mechanism and evidence over analogy.
- Do not treat a coherent hypothesis as an established fact.
- Do not require every question to be answered.
- Do not make the user do research the assistant can do.
- Keep the starter kit portable and platform-neutral.

## What belongs where

- `MemoryPrism-Framework.pdf`: foundational framework artifact.
- `starter-kit/`: the one canonical checklist. Edit it here, then copy it to `skill/memory-prism/references/checklist.md`.
- `skill/memory-prism/`: the installable skill (instructions, references, source corpus). No tests.
- `tests/`: `smoke/` (skill behaviour), `daily/` (protocol and scoring), `records/` (completed records and index).
- `docs/`: human-facing orientation, explanatory reference and verification notes.
- `wiki-seed/`: pages prepared for copying into the separate GitHub Wiki repository.
- `tools/check_repo.py`: run before opening a pull request.

Please keep changes focused and explain the failure or need they address.

## Revising the checklist

Keep a checklist item only if it helps produce a better next question across more than one domain. Revise or remove an item if it:

- forces every topic into the same shape;
- repeats another question in different vocabulary;
- answers a question before evidence has been gathered;
- encourages analogy in place of mechanism;
- makes the assistant ask the user to do the assistant's research;
- turns the starter kit into a complete audit protocol;
- introduces a concept that does not change the next step.

Watch for overlap between flow/accumulation (3a) and maintenance/removal (4b); preserve the distinction only where it helps.

Any claim about what the Framework or an essay says must be traceable to its text. Record the check in `docs/checklist-verification.md`.

## Reporting a test of the checklist

1. Which question or instruction helped uncover a useful next step?
2. Which wording caused forced analysis, redundancy or metaphor instead of mechanism?
3. What did the checklist fail to notice?
4. What small revision would improve portability without making it longer or more prescriptive?

Recommend targeted changes and explain the observed failure that justifies each one. Do not rewrite the whole checklist by default.
