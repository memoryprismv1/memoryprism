# Memory Prism Source Corpus

This directory bundles the Framework text and the complete texts of the Foundation and Supplementary essays needed by the platform-neutral Starter-Kit skill. The skill can consult primary text directly instead of trying to reconstruct Memory Prism from the short checklist.

## Source hierarchy

### Framework — primary source
- [Memory Prism Framework](https://www.memoryprism.com/framework) — [DOI 10.5281/zenodo.19287268](https://doi.org/10.5281/zenodo.19287268)
- Local text: [Memory-Prism-Framework.md](Memory-Prism-Framework.md)

The official published PDF remains the canonical framework artifact at the repository root. The Markdown file is a searchable text rendering from the project's archived source export; title/duplicate-heading formatting was normalized for retrieval. If exact wording, typography, or page layout matters, consult the PDF and official page.

### Foundation — four operators
These define the four Foundation concepts: memory, constraints, editors, and boards, through their central essays.

| Essay | Local text | Canonical source |
|---|---|---|
| Boards | [foundations/Boards.md](foundations/Boards.md) | https://www.memoryprism.com/essays/foundations/boards |
| Audits | [foundations/Audits.md](foundations/Audits.md) | https://www.memoryprism.com/essays/foundations/audits |
| Identity | [foundations/Identity.md](foundations/Identity.md) | https://www.memoryprism.com/essays/foundations/identity |
| Flow Under Constraint | [foundations/Flow-under-Constraint.md](foundations/Flow-under-Constraint.md) | https://www.memoryprism.com/essays/foundations/flow-under-constraint |

### Supplementary — three structural extensions
These extend the available analysis without becoming mandatory steps in every application.

| Essay | Local text | Canonical source |
|---|---|---|
| Working Lines | [supplementary/Working-Lines.md](supplementary/Working-Lines.md) | https://www.memoryprism.com/essays/supplementary/working-lines |
| No Sacred States | [supplementary/No-Sacred-States.md](supplementary/No-Sacred-States.md) | https://www.memoryprism.com/essays/supplementary/no-sacred-states |
| Accumulation Patterns | [supplementary/Accumulation-Patterns.md](supplementary/Accumulation-Patterns.md) | https://www.memoryprism.com/essays/supplementary/accumulation-patterns |

## Attribution and licence

The official project identifies Memory Prism v1.0 as **CC BY-NC 4.0**.

- DOI: https://doi.org/10.5281/zenodo.19287268
- Project licence page: https://www.memoryprism.com/license
- Licence text: https://creativecommons.org/licenses/by-nc/4.0/

Retain attribution and licence notices with copies and adaptations. Commercial use requires separate permission. Third-party material cited within an essay may be governed by its own terms.

## Provenance and fidelity

The texts were extracted from the project's archived combined source export and placed into individual Markdown files. Duplicate title/heading artifacts and obvious page-join markers were normalized at extraction. No argument-level revision was intended.

**Revision 2026-11-23 (formatting only).** The extraction had left empty `##`/`###` heading lines above each section title in seven of the eight files. Each title was moved onto its heading line, and escaped list/quote markers (`\-`, `\>`) were unescaped. A word-level comparison confirmed the text of every file is unchanged by this step.

**Framework text checked against the PDF.** `Memory-Prism-Framework.md` was compared with the text layer of `MemoryPrism-Framework.pdf` (11 pages, generated 28 March 2026). Word-level similarity is 0.986. All differences are PDF page chrome (print date, URL footer, page numbers), and one passage whose glyphs overlap in the PDF text layer (the killifish/hibernating-mammals sentence), which the Markdown has correctly. `python3 tools/check_repo.py` repeats the check.

**Not verified.** The seven essays were not compared with the live pages at memoryprism.com (no network access during the revision). Consult the official pages for the current web copy.

Because these are source extracts rather than new canonical publications, consult the PDF for the published Framework layout.

## How the skill should use this corpus

1. For framework definitions, boundaries, or interpretation questions, consult the Framework first.
2. Consult only the relevant Foundation essay or essays next.
3. Consult Supplementary essays only when they add something to the current question.
4. Use the Starter Kit checklist to find a useful entry point and the best next question.
5. Do not read or recite all eight texts on every turn. Source availability provides grounding; it does not impose universal application.
6. Do not treat inclusion in the corpus as empirical verification. Source claims can still require domain-level verification.
7. The Starter Kit's source boundary is precisely this Framework plus these four Foundation and three Supplementary essays. Domain/application essays outside this set are not automatically required.
