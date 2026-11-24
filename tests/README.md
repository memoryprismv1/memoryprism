# Tests

Tests are kept outside the installable skill folder (`skill/memory-prism/`) so that the skill stays small and the records do not travel with it.

| Folder | What it is | Start with |
|---|---|---|
| [`smoke/`](smoke/) | Behavioural checks of the skill: source grounding, concept fidelity, proportionate lens use, and cross-domain portability (A–H). | [`SMOKE_TESTS.md`](smoke/SMOKE_TESTS.md) |
| [`daily/`](daily/) | The daily two-topic inquiry protocol (one normal, one software) and its scoring rubric. | [`README.md`](daily/README.md), [`SCORING.md`](daily/SCORING.md) |
| [`records/`](records/) | Every completed test record, plus the one-line-per-test index. | [`DEVELOPMENT_LOG.md`](records/DEVELOPMENT_LOG.md) |

Smoke tests answer "does the skill behave as intended?". Daily tests answer "can a person use the same general checklist on an unfamiliar subject?". The two use different rubrics on purpose.
