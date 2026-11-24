# Memory Prism skill

`memory-prism/` is a self-contained skill folder in the standard `SKILL.md` + `references/` layout. It contains everything an assistant needs and nothing it does not: no tests, no repository documentation.

```text
memory-prism/
├── SKILL.md                      instructions (frontmatter + workflow)
└── references/
    ├── checklist.md              the Starter Kit (copy of starter-kit/…-v1.1.md)
    ├── concepts.md               Framework concept map and misuse traps
    ├── lenses.md                 the seven lenses as the essays state them
    ├── user-orientation.md       the user's own wording of the concepts
    └── source-corpus/            Framework text + the seven essays, with provenance
```

The assistant reads `SKILL.md` when the skill triggers and opens the reference files only when needed (see the table in `SKILL.md`).

## Install

- **Claude (claude.ai, Desktop, mobile):** zip the `memory-prism` folder so that `memory-prism/SKILL.md` is at the top level of the archive, then upload it under Settings → Capabilities → Skills. Build the archive with `cd skill && zip -r memory-prism.zip memory-prism`.
- **Claude Code:** copy the `memory-prism` folder to `~/.claude/skills/` (all projects) or `.claude/skills/` in a project.
- **Other assistants:** paste `SKILL.md` and `references/checklist.md` into the system prompt or project instructions. The core instructions are platform-neutral. Keep the source corpus available if the platform supports file retrieval.

If a platform needs different metadata or directory names, add a thin wrapper and leave `SKILL.md`, the references and the source corpus unchanged.

## Keeping the checklist in sync

`references/checklist.md` must be byte-identical to `starter-kit/Memory-Prism-Starter-Kit-Checklist-v1.1.md`. Edit the file in `starter-kit/`, then copy it over. `python3 tools/check_repo.py` fails if they differ.

## Tests

Tests live in [`../tests/`](../tests/README.md), outside the skill.
