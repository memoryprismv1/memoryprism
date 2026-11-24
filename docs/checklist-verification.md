# Checklist and source verification

Verification performed 2026-11-23 for Starter Kit v1.1. It records what was checked against the Framework and the seven essays, what was wrong, what was changed, and what remains for the project owner to decide. It is a working record, not part of the framework.

## 1. Framework: PDF versus Markdown

**Question:** is there a Markdown version of the Framework, and does it match the PDF?

**Result:** yes. `skill/memory-prism/references/source-corpus/Memory-Prism-Framework.md` exists and matches `MemoryPrism-Framework.pdf` (11 pages, generated 28 March 2026) at **0.986 word-level similarity**. No conversion of the PDF was needed.

Method: text layer extracted with `pdftotext`, normalised (case, punctuation, quotation marks, page chrome) and compared word by word with the Markdown. Repeatable with `python3 tools/check_repo.py`.

Every difference is benign:

| Difference | Explanation |
|---|---|
| Print date, URL footer, page numbers in the PDF | Browser print chrome, not content |
| Contact email after the legal licence in the PDF | Restored to the Markdown on 2026-11-23 |
| The killifish / hibernating-mammals sentence is garbled in the PDF text layer | Overlapping glyphs in extraction; the Markdown has the correct sentence |
| "Usage Instructions" is a hyperlink in the Markdown | The PDF prints the URL |

One real defect was found and fixed: the Markdown had empty `##`/`###` heading lines above every section title (26 in the Framework), so the section structure was invisible to retrieval. Titles were moved onto their heading lines. A token-level assertion confirmed the words are unchanged.

## 2. Is the source set complete?

All eight texts are present: the Framework, four Foundation essays (Boards, Audits, Identity, Flow Under Constraint) and three Supplementary essays (Working Lines, No Sacred States, Accumulation Patterns). **Nothing is missing.** The same heading defect affected six of the seven essays (141 empty headings) and was fixed the same way. Escaped list and quote markers were also unescaped.

**Not checked:** the essays against the live pages at memoryprism.com (no network access). The corpus README says they were extracted from the project's archived export.

## 3. Did the checklist and skill cover the Framework's own concepts?

The Framework has twelve sections. Earlier versions of the checklist and skill covered some and silently dropped others.

| Framework concept | v1.0 canonical checklist | Old skill checklist | Old SKILL.md | v1.1 |
|---|---|---|---|---|
| Memory | yes | yes | yes | yes |
| Constraints, Editors, Board | yes | yes | yes | yes |
| Ledger | thin (3 bullets) | yes | yes | yes (own step 3b) |
| **Translator** | one caveat in Q5 | one caveat | **absent** | yes |
| Legacy | no | yes | yes | yes |
| **Viability band, correction window** | **no** | passing mention | passing mention | yes |
| **Elasticity, inertia, lag** | **no** | **no** | **no** | yes |
| **Constraint assertion (feedback)** | **no** | **no** | **no** | yes |
| Living matter (open and closed ledgers) | no | yes | yes | yes |
| Architecture, Stability | no | yes | yes | yes |

## 4. Item-by-item check of the checklist against the sources

| Item | Source checked | Verdict | Action |
|---|---|---|---|
| Q1 P-Memory note | Framework "Memory"; `user-orientation.md` | Supported | None |
| Q2 board, constraints, editors, nesting | Framework "Constraints", "Editors", "Board" | Supported. "Learned conventions, institutional rules" are legacy-based constraints, a reasonable extension | None |
| Q2 board variables | Boards essay | **Missing.** Budget, transport capacity, scale, sparsity, disturbance regime and turnover rate were absent | Added as an optional prompt |
| Q3a flow and accumulation | Flow Under Constraint; Accumulation Patterns | Supported | None |
| Q3b ledger | Framework "The ledger", "Dead, alive, maybe-dead…" | Supported. Open/closed ledgers and deferred payment confirmed | Expanded from three bullets |
| Q3 "reserve" under accumulation | Accumulation Patterns | **Not in the essay.** The essay's non-load-bearing material is *filler* that cushions, not a reserve | "Reserve" kept only in the ledger step; accumulation now says "cushioning or filler" |
| Q4a pile check | Accumulation Patterns (cohesion, connectivity, load-bearing subset) | Supported | Essay terms added |
| Q4b drift and maintenance | Framework "Stability"; Boards "maintenance-to-intake"; Accumulation "cost" | Supported | None |
| Q4c identity | Identity essay | **Drifted.** "Same entity over time" is philosophical identity; the essay describes membership and role governance in systems with a boundary, finite energy and conditional response | Reworded as membership and role governance; extensions to software and groups stated as explicit extensions |
| Q5 detect / interpret / correct | Framework "Translator", "Feedback loops"; Audits | Supported | Added cost of reading, over-reading, and disturbance-versus-correction rate |
| Q5 stability | Framework "Still stable, but for how long?" | **Missing.** Stability as confinement of change; lag as stored stress | Added one bullet |
| Q5 paths that carry failure | Working Lines | Supported | None |
| Q5 internal failure vs higher-board override | Boards essay | Supported | None |
| Q6 best next question | Method, not a source claim | Not source-derived | None |
| Lens: Boards | Boards essay | Incomplete (see Q2 variables) | Fixed |
| Lens: Audits | Audits essay | Incomplete: envelope, disturbance vs correction omitted | Fixed |
| Lens: Identity | Identity essay | Drifted (see Q4c) | Fixed |
| Lens: Flow | Flow essay | Incomplete: continuity, exploitation, position omitted | Added in `lenses.md`; entry question mentions flows that cannot stop |
| Lens: Working Lines | Working Lines essay | Supported | None |
| Lens: No Sacred States | No Sacred States essay | Supported. Recognition as board-dependent is not in the checklist | Noted in `lenses.md` |
| Lens: Accumulation Patterns | Accumulation Patterns | Supported apart from "reserve" | Fixed |
| Operating rules, reasoning audit, response shape | Repository policy | Not source claims | Kept; duplicates removed |

## 5. Structural defects fixed

1. **Two divergent checklists.** `starter-kit/…v1.0.md` (six questions) and `skill/references/starter-kit.md` (seven, with Ledger split out) differed in content and numbering. There is now one canonical file; the skill holds a byte-identical copy, checked by `tools/check_repo.py`.
2. **Numbering.** The skill copy had sub-questions "4a, 4b, 4c" under question 5, and seven questions where the README and docs said six. v1.1 has six questions with consistent sub-labels (3a, 3b, 4a to 4c).
3. **Lens-count conflict.** v1.0 and the docs said "one or two by default"; the skill said "no fixed maximum". v1.1 states **no quota and no cap; often one or two earn their place** (see decision D2).
4. **Maintainer material inside the checklist.** Cross-domain smoke tests, revision criteria and a handoff note sat in the user-facing checklist. The smoke tests duplicated `SMOKE_TESTS.md` A to E; the rest moved to `CONTRIBUTING.md`.
5. **`SKILL.md` was not a valid skill.** It had no frontmatter, repeated the "visible pre-interpretation inventory" section twice, and ran 17.5 KB. The rewrite is valid, 7.9 KB, and loads references on demand.
6. **Tests lived inside the skill.** 57 files shipped with every install. They now sit in `tests/`.
7. **Smoke test F was misplaced** after the evaluation question; it now sits with the other prompts. G (Ledger is core) and H (translator versus threshold) were added to cover the concepts the skill most often mishandled.
8. **Daily tests had no scoring.** Existing records used rubrics with maxima of 8, 12 and 14. See `tests/daily/SCORING.md`.

## 6. Decisions (recorded 2026-11-23, project owner)

| # | Decision | Applied |
|---|---|---|
| D1 | The Working Lines essay governs. | `user-orientation.md` now reads "Working lines: the paths along which force, energy or coordination already move, and so where stress and failure concentrate." The source-precedence guard stays in `SKILL.md`. |
| D2 | No quota or cap on optional lenses; "often one or two earn their place" is an observation, not a default. Lenses never replace or demote core concepts; Ledger stays core. | Wording kept in the checklist and docs. |
| D3 | Checklist v1.1 is canonical. | A minimal v1.0 stub marked superseded remains at the old path and points to v1.1. No checklist content is duplicated. |
| D4 | Both board definitions are kept; the Framework's is canonical. | `concepts.md` documents the two levels (survival environment versus structural elaboration with thresholds and state transitions). |
| D5 | Identity is membership and role governance, and the name is kept. Applying it to software and groups is an explicit extension of a biological essay. | Checklist 4c, the lens table, `lenses.md`, docs and wiki seed rewritten. Applications must name the boundary, what may operate within it, roles and locations, resources and costs, conditions for toleration, restriction, displacement or removal, and how roles change or fade. Presence, permission and function are kept distinct. |

Also applied: the contact email from the PDF was restored to the Framework Markdown.

## 7. Not done

- The 54 existing test records (including the two dated 2026-11-23) were moved byte-for-byte but not edited or audited. Older ones contain earlier paths and blob SHAs that point to earlier commits; those stay as provenance.
- `case-studies/` was left in place.
- DOI and citation metadata were not re-verified.
