# Memory Prism — Platform-Neutral AI Skill

This folder contains a platform-neutral skill definition intended to be adapted to different AI assistants without changing the underlying checklist.

## Files

- `SKILL.md` — the assistant's operating instructions.
- `references/starter-kit.md` — the canonical checklist reference.
- `tests/SMOKE_TESTS.md` — practical behaviour tests and pass criteria.

## Design principle

The skill teaches an assistant how to use the Memory Prism starter kit selectively. It must not turn the checklist into an exhaustive protocol, replace domain expertise, or require the final answer to expose framework terminology.

The framework PDF remains the foundational artifact. The checklist uses exactly seven supporting essays listed in the reference.

## Adapting to a platform

Platforms may require different metadata, directory names, packaging, or invocation declarations. Make those adaptations in a thin platform-specific wrapper. Keep the central instructions and reference checklist platform-neutral, and do not let an adapter change the source boundary or behavioural rules.

## Quick start

1. Read `SKILL.md`.
2. Read `references/starter-kit.md` when applying the checklist.
3. Use the smoke tests to check whether the assistant answers settled questions directly, researches without offloading work to the user, and avoids forced use of every lens.

## Status

This is a portable base package. It intentionally avoids dependence on one vendor's frontmatter schema, tool names, APIs, or runtime.
