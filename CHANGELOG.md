# Changelog

## 2026-11-23 — Restructure, checklist v1.1, daily scoring

### Why
The skill was not a valid skill file, two different checklists existed under one name, tests were bundled inside the skill, and the daily tests had no scoring. Details and evidence: [`docs/checklist-verification.md`](docs/checklist-verification.md).

### What changed
- **Checklist v1.1** is now the single canonical checklist (`starter-kit/`). Six questions with consistent sub-labels; Ledger is its own step; Identity and the lens summaries realigned to the essays; Framework terms that earlier versions dropped (Translator, viability band and correction window, elasticity/inertia/lag, constraint assertion, living matter) restored.
- **Skill** rebuilt as an installable folder, `skill/memory-prism/`, with valid frontmatter, a 7.9 KB `SKILL.md` (was 17.5 KB), and on-demand references: `checklist.md`, `concepts.md`, `lenses.md`, `user-orientation.md`, `source-corpus/`.
- **Source corpus:** Framework Markdown verified against the PDF (0.986 word-level similarity); empty headings repaired in eight files with a word-for-word check; all seven essays confirmed present.
- **Tests** moved out of the skill into `tests/`: `smoke/`, `daily/` (new README and `SCORING.md`), `records/`. Smoke test F re-ordered; G and H added.
- **Docs, wiki seed, CONTRIBUTING, README** updated to match. `tools/check_repo.py` added.

### Owner decisions applied (D1 to D5)
Working Lines wording in `user-orientation.md` corrected to follow the essay; no quota or cap on lenses; a superseded v1.0 stub kept at the old checklist path; both board definitions kept with the Framework canonical; Identity described as membership and role governance with software and group uses marked as extensions; contact email restored to the Framework Markdown. See `docs/checklist-verification.md` section 6.

### Unchanged
- `MemoryPrism-Framework.pdf`, licence and citation files, the 54 test records (including the two dated 2026-11-23) and their index entries (byte-identical, moved only).

### Path map

| Old | New |
|---|---|
| `skill/SKILL.md` | `skill/memory-prism/SKILL.md` (rewritten) |
| `skill/references/starter-kit.md` | `skill/memory-prism/references/checklist.md` (replaced; identical to canonical) |
| `skill/references/user-orientation.md` | `skill/memory-prism/references/user-orientation.md` |
| `skill/references/source-corpus/` | `skill/memory-prism/references/source-corpus/` |
| `starter-kit/Memory-Prism-Starter-Kit-Checklist-v1.0.md` | `starter-kit/Memory-Prism-Starter-Kit-Checklist-v1.1.md` (v1.0 remains as a superseded stub) |
| `skill/tests/README.md` | `tests/daily/README.md` (rewritten), plus new `tests/README.md` |
| `skill/tests/SMOKE_TESTS.md` | `tests/smoke/SMOKE_TESTS.md` |
| `skill/tests/*.md` and `DEVELOPMENT_LOG.md` | `tests/records/` |

Historical records cite the old paths together with blob SHAs. Those citations point to earlier commits and are intentionally left as written.
