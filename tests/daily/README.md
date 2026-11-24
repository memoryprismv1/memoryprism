# Daily Tests — How to Run Them

Read this at the start of a new chat so the method does not have to be reconstructed from conversation history. Scoring is in [`SCORING.md`](SCORING.md). Finished records and the index live in [`../records/`](../records/).

## What the daily tests are testing

Can a person use the **same general-purpose Memory Prism checklist** to investigate an unfamiliar subject without first becoming a domain specialist or preparing a domain-specific checklist?

The person starts with an ordinary question, observation or curiosity and explores it with Memory Prism, logic, reasoning and sanity checks. The assistant supplies information, sources and research when asked, and resolves factual or technical questions. The subject changes each day; the inquiry framework does not.

This is **not** an examination of the user. Do not grade the user on whether they already know the science, engineering or terminology. Record only what the user actually brought: observations, everyday knowledge, logical steps, comparisons and questions. Scores in [`SCORING.md`](SCORING.md) rate the *answer and the method*, never the user.

## The two daily topics

A daily batch contains exactly two topic-led inquiries:

1. **Normal inquiry:** a question from any non-software subject. Accessible, genuinely interesting, investigable from an ordinary starting point.
2. **Software inquiry:** a question or scenario about software, data, infrastructure, system behaviour, reliability, migration, security, operations or design. Keep it genuinely about a software system. Do not turn every software test into a business-coordination or logistics exercise.

The assistant chooses both topics. Do not ask the user to pick from a menu. Present one question at a time. Check the index for recent topics, avoid repeats, and vary the subject and the type of problem.

## Running each inquiry

### 1. Give an ordinary starting question

Ask one clear question. Do not pre-answer it, outline a solution, or hand the user a domain-specific interrogation list. It should invite investigation, not test recall.

### 2. Let the user lead

The user decides what to examine, which explanations to challenge and what information they need. The assistant supports the inquiry and does not take it over.

- Preserve the user's original observation and framing. Do not narrow it to the first familiar explanation.
- Treat a proposed mechanism or variable as a hypothesis, not something to dismiss because it was not in the assistant's initial model.
- When asked for information, explain it in ordinary language. When asked to find or verify something, research it and give sources.
- Follow useful leads across subject areas, but do not force cross-domain analogies; establish the actual mechanism in each domain.
- Do not repeatedly ask the user to name the next research step when the research can simply be done.
- Do not dump a full domain explanation before the user has had room to think.

If the user does not lead (they ask the assistant to just write it up), the run is still valid but is recorded as **assistant-generated** (see run types below), and that limitation is stated in the record.

### 3. Use Memory Prism correctly

For an exploratory question where MP is in use, the first substantive response begins with the **selective pre-interpretation inventory**:

| MP concept | What I identify in this query |
|---|---|

Include only concepts that clarify the actual question or a plausible follow-up. Describe the concrete feature; do not paste definitions. No empty "not relevant" rows. Core Framework concepts (including Ledger and Translator) stay core; the seven essay lenses are used selectively. Full rules: [`../../skill/memory-prism/SKILL.md`](../../skill/memory-prism/SKILL.md) and [`../../starter-kit/Memory-Prism-Starter-Kit-Checklist-v1.1.md`](../../starter-kit/Memory-Prism-Starter-Kit-Checklist-v1.1.md).

Do **not** require a domain-specific checklist. The user does not need to supply one or know one exists. Subject facts are acquired progressively through conversation and research. This does not mean specialist evidence is never needed for a definitive technical judgement; the user simply does not need to bring it as an entry requirement.

The six-question **Assistant reasoning audit** is AI-only and internal. It is not a user questionnaire and not another lens.

### 4. Keep evidence and uncertainty honest

Distinguish, when it matters: what the user directly observed; what a source or measurement establishes; what is a reasonable inference; what remains hypothesis or open question.

Research the specific uncertainty instead of repeating generic explanations. Cite external factual claims. Do not present a literature review as a new experiment, a proposed test as a completed one, or a same-conversation comparison as an independent blind evaluation. If explanations compete, keep them alive until you can say what evidence would separate them. A coherent MP mapping is not proof of a causal claim.

### 5. Close and record

Do not interrupt the user's exploration to write a report. When the inquiry is complete, write one concise record that preserves the route actually taken: the starting question, the user's observations and contributions, the selective MP inventory, what was researched, evidence, corrections, findings, unresolved questions, and the score sheet from [`SCORING.md`](SCORING.md). Record the user's demonstrated knowledge accurately. Do not inflate ordinary observations into expertise, and do not treat absent specialist knowledge as a failure.

## Run types (state one in the record's header)

| Run type | Meaning |
|---|---|
| **User-led inquiry** | The user directed the investigation; the assistant researched on request. |
| **User-guided correction** | The assistant led, but the user supplied a substantive correction or reframing. Record exactly what the user supplied. |
| **Assistant-generated synthesis** | The assistant chose the topic and produced the explanation without a user-led inquiry. Literature- or documentation-informed. |
| **Standards-grounded scenario** | A software design exercise grounded in standards/documentation; no live system. |
| **Live implementation** | Code or a system was actually run. Say what was measured. |

Also state the **comparison conditions** actually run (single answer; conventional vs MP; MP vs MP + Critical Thinking; and so on). A Critical Thinking or other-skill comparison is included only when it was conducted and is part of that test's objective, and its contribution is never attributed to Memory Prism.

## Record conventions

- **One substantive inquiry per file**, saved in `tests/records/`.
- Filename: normal `topic_slug_YYYY-MM-DD.md`; software `software_topic_slug_YYYY-MM-DD.md`.
- Test ID: normal `MP-YYYY-MM-DD-01`; software `MP-SOFTWARE-YYYY-MM-DD-01`. Increment the final number for additional tests on the same day.
- Put the selective MP inventory before the main interpretation or findings.
- Include sources and provenance. State what was and was not tested.
- Adapt sections to the actual inquiry. Do not add headings that imply work that was not done.
- For a **normal** inquiry the record usually needs: question, observation, MP inventory, mechanism and evidence, findings, limits, sources, score sheet.
- For a **software** inquiry: scenario and operating invariant, MP inventory, relevant system states and constraints, evidence or standards, failure and recovery behaviour, limits, sources, score sheet.
- Keep related observations and transfer checks inside the parent record. Do not edit old records to make them fit a new run. Cumulative reviews and batch reports belong to downstream review work, not the daily collector.
- Append **one index entry per new test** to [`../records/DEVELOPMENT_LOG.md`](../records/DEVELOPMENT_LOG.md), immediately before `## Collection rule`. The log is an index, not a second results report. Index entry format is in [`SCORING.md`](SCORING.md#index-entry-format).

Records created before this README (up to 2026-11-23) use older, inconsistent rubric formats and maxima (8, 12 and 14). They are historical and are not re-scored. Compare new records only with new records.

## Repository and continuity rules

- Work from the current repository state but make changes on a **new branch**. Never commit directly to `main`; open a pull request.
- A daily batch normally adds two records and two index entries. Do **not** modify `skill/`, `starter-kit/`, `skill/memory-prism/references/source-corpus/`, `tests/smoke/`, or historical records as part of an ordinary test run.
- Fetch only the files you need. Cache them for the chat and record the retrieval time (UTC), the full current-main commit SHA, each Git blob SHA and a SHA-256 hash. Reuse the cache rather than re-reading GitHub. The user will say when to fetch a newer version.
- Do not upload the test ZIP or unrelated binary/image payloads. Records and index entries are text files.
- Historical records cite earlier paths such as `skill/SKILL.md` and `skill/tests/…` together with blob SHAs. Those are provenance pointers to earlier commits and stay as written. Current paths are listed in [`../../CHANGELOG.md`](../../CHANGELOG.md).

## New-chat handoff

At the start of a new chat, read this README and [`SCORING.md`](SCORING.md), then `skill/memory-prism/SKILL.md` and `skill/memory-prism/references/checklist.md`, then the latest records and the end of `tests/records/DEVELOPMENT_LOG.md`. Cache them as described above. Do not ask the user to reconstruct the protocol from memory.

A sufficient handoff message:

> Continue the Memory Prism daily tests using `tests/daily/README.md` and `tests/daily/SCORING.md`. Choose today's normal and software topics; do not ask me to choose. Give me one ordinary question at a time. I will lead the inquiry using Memory Prism, logic, reasoning and sanity checks. You provide additional information and research when I ask. Do not require domain-specific checklists or prior specialist knowledge from me.
