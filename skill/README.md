# Memory Prism — Platform-Neutral AI Skill

This folder contains a platform-neutral skill definition and its complete source reference library.

## Package layout

- `SKILL.md` — assistant operating instructions.
- `references/starter-kit.md` — canonical checklist v1.0.
- `references/source-corpus/Memory-Prism-Framework.md` — searchable text rendering of the Framework.
- `references/source-corpus/foundations/` — complete Foundation texts: Boards, Audits, Identity, Flow Under Constraint.
- `references/source-corpus/supplementary/` — complete Supplementary texts: Working Lines, No Sacred States, Accumulation Patterns.
- `references/source-corpus/README.md` — reading hierarchy, canonical URLs, provenance, attribution and licence.
- `tests/SMOKE_TESTS.md` — behavioural tests, including explicit source-grounding tests.

## Read the sources; don't force them all

The skill's source set is the Framework plus **four Foundation essays and three Supplementary essays**. These are provided in full so an assistant can consult the original wording. Availability is not mandatory application: consult the Framework first when interpreting Memory Prism, then read only relevant essays. Do not force all seven essays into every response.

The published PDF remains the canonical Framework artifact in the repository root. The bundled Markdown Framework text is a searchable text rendering from the project's archived source export; consult the PDF and official Framework page where exact wording, typography, or layout matters.

- Framework and DOI: https://www.memoryprism.com/framework · https://doi.org/10.5281/zenodo.19287268
- Official licence: https://www.memoryprism.com/license
- Source URLs and attribution: `references/source-corpus/README.md`

## Design principle

The skill uses the source material to improve fidelity, not to replace domain expertise or produce exhaustive analysis. Answer settled questions directly, distinguish source claims from verified domain evidence, let each lens earn its keep, and stop when a useful next question appears.

## Adapting to a platform

Platforms may require different metadata, directory names, or invocation declarations. Add a thin platform-specific wrapper if needed. Keep the core instructions and source corpus platform-neutral; don't let an adapter change the source boundary or behavioural rules.

## Quick start

1. Read `SKILL.md`.
2. For a Memory Prism definition or interpretation question, consult `references/source-corpus/README.md`, then the Framework and relevant essay(s).
3. Use `references/starter-kit.md` when applying the checklist.
4. Run the smoke tests to check source fidelity, proportional lens selection, and assistant-led research.
