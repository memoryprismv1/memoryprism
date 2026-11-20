# Memory Prism Tests — How to Conduct Them

This README is the handoff guide for running the Memory Prism tests in this folder. Read it at the start of a new chat so the test method does not have to be reconstructed from conversation history.

## What the tests are testing

The central question is whether a person can use the **same general-purpose Memory Prism inquiry checklist** to investigate an unfamiliar subject without first becoming a domain specialist or preparing a domain-specific checklist.

The person begins with an ordinary question, observation or curiosity. They use Memory Prism, logic, reasoning and sanity checks to explore it. The assistant supplies additional information, sources and research when asked, and helps resolve factual or technical questions.

This is not an examination of the user's specialist knowledge. Do not grade the user on whether they already know the relevant science, engineering or terminology. Record only what the user actually brought to the inquiry: observations, everyday knowledge, prior familiarity, logical steps, comparisons and questions.

The checklist is platform-neutral. A person can use it while researching alone or asking a human expert questions; an AI can use the same checklist. The subject changes, not the inquiry framework.

## The two daily topics

A daily batch contains exactly two topic-led inquiries:

1. **Normal inquiry:** a question from any non-software subject area. Choose an accessible, genuinely interesting question that can be investigated from an ordinary starting point.
2. **Software inquiry:** a question or scenario about software, data, infrastructure, system behaviour, reliability, migration, security, operations or design. Keep it genuinely about a software system; do not turn every software test into a business-coordination or logistics exercise.

The assistant chooses both topics. Do not ask the user to pick from a menu or supply topics. Present one question at a time. Avoid repeating recent topics and vary the subject matter and type of problem.

## How to run each inquiry

### 1. Give the user an ordinary starting question

Ask one clear question, without pre-answering it, supplying a solution outline, or giving the user a domain-specific interrogation checklist.

The question should invite investigation rather than test recall. The user does not need to know the specialist vocabulary in advance.

### 2. Let the user lead the inquiry

The user explores using Memory Prism, logic, reasoning and sanity checks. They decide what to examine, which explanations to challenge and what additional information they need.

The assistant's role is to support that inquiry—not to take it over.

- Preserve the user's original observation and framing. Do not prematurely narrow it to the first familiar explanation.
- Treat a proposed mechanism or variable as a hypothesis to investigate, not as something to dismiss because it was not in the assistant's initial model.
- When the user asks for information, explain it in ordinary language. When they ask to find or verify something, research it and provide sources.
- Follow useful leads across subject areas when the user's question warrants it. Do not force cross-domain analogies; establish the actual mechanism in each domain.
- Do not repeatedly ask the user to identify the next research step when the requested research can be done.
- Do not dump a full domain explanation before the user has had room to think.

### 3. Use Memory Prism correctly

For an exploratory question where Memory Prism is being used, begin the first substantive response with a **selective pre-interpretation inventory**:

| MP concept | What I identify in this query |
|---|---|

Include only concepts that clarify the actual question or a plausible deeper follow-up. Describe the concrete feature or relationship; do not copy definitions into the rows. Do not force every concept or every optional lens into the table, and do not add empty “not relevant” rows.

Keep the original Framework concepts intact: Memory, Constraints, Editors, Board, Legacy, Ledger / energy accounting, Living matter, Architecture and Stability. Ledger is an original core concept, not an optional lens. The seven supporting essay lenses—Boards, Audits, Identity, Flow Under Constraint, Working Lines, No Sacred States and Accumulation Patterns—are available selectively; they are not mandatory stages.

**Do not require a separate domain-specific checklist.** The user does not have to supply one, know one exists, or learn specialist terminology to begin. Use the general Memory Prism inquiry checklist. Acquire subject-specific facts and mechanisms progressively through the conversation and research as needed. This does not mean that specialist expertise or specialist evidence is never needed for a definitive technical judgement; it means the user does not need to bring that expertise as an entry requirement.

The six-question **Assistant reasoning audit** in the Starter Kit is AI-only. Apply it internally to improve the assistant's work. It is not a user questionnaire, not a human interview checklist, and not another Memory Prism lens.

### 4. Keep evidence and uncertainty honest

Distinguish, when it matters:

- what the user directly observed;
- what a source or measurement establishes;
- what is a reasonable inference;
- what remains a hypothesis or open question.

Research the specific uncertainty rather than repeating generic explanations. Cite external factual claims. Do not present a literature review as a new experiment, a proposed test as a completed test, or a same-conversation comparison as an independent blind evaluation.

If explanations compete, preserve them long enough to identify what evidence would distinguish them. A coherent Memory Prism mapping is not proof that a causal claim is true.

### 5. Close and record the inquiry

Do not interrupt the user's exploration to write a report. When the inquiry is complete, create one concise, useful record that preserves the actual route taken: the starting question, the user's observations and contributions, the selective MP inventory, information researched, evidence, corrections, findings and unresolved questions.

Record the user's demonstrated knowledge accurately. Do not inflate ordinary observations into specialist expertise, and do not treat the absence of specialist knowledge as a failure.

## Test record conventions

- Keep **one substantive inquiry per file**.
- Use a dated filename. Normal example: `mangrove_water_balance_2026-11-20.md`. Software example: `software_dns_cutover_2026-11-20.md`.
- Use test IDs in the existing style: `MP-YYYY-MM-DD-01` for a normal test and `MP-SOFTWARE-YYYY-MM-DD-01` for a software test.
- Put the selective MP inventory before the main interpretation or findings.
- Include sources and provenance. State whether the record is a conversational inquiry, literature-informed synthesis, standards-grounded scenario, live implementation, or another type. Be explicit about what was and was not tested.
- Use the existing daily records as format references. Adapt the sections to the actual inquiry; do not add headings that imply work that was not performed.
- Append one index entry per new test to `DEVELOPMENT_LOG.md`, immediately before `## Collection rule`. The log is an index, not a second results report.
- Keep related observations and transfer checks inside their parent test record. Do not edit old test records to make them fit a new run. Cumulative reviews and batch reports belong to downstream review/reporting work.

For a normal inquiry, the record will usually need the question, observation, MP inventory, mechanism and evidence, findings, limits and sources.

For a software inquiry, record the scenario and operating invariant, MP inventory, relevant system states and constraints, evidence or standards, failure and recovery behaviour, and limits. A conventional-versus-MP or additional Critical Thinking comparison is included only when it was actually conducted and is part of that test's objective. Keep those conditions distinct; do not attribute another method's contribution to Memory Prism.

## Repository and continuity rules

- Work from the current repository state, but make changes on a **new branch**. Never commit directly to `main`; open a pull request for review.
- Daily test batches normally add two new test records and their two index entries. Do not modify `SKILL.md`, the Starter Kit, source-corpus files, smoke tests or historical test records as part of an ordinary test run.
- When reading repository files, fetch only what is needed. Cache fetched files for the chat and record the retrieval time (UTC), full current-main commit SHA, each Git blob SHA and a SHA-256 hash. Reuse that cache during the chat rather than repeatedly reading GitHub. The user will indicate when a newer version should be fetched.
- Do not upload the test ZIP or unrelated binary/image payloads to GitHub. Test records and index entries are text files.

## New-chat handoff

At the start of a new chat, read this README, the current `skill/SKILL.md` and `skill/references/starter-kit.md), then check the latest daily records and the end of `DEVELOPMENT_LOG.md`. Cache the fetched files as described above. Do not ask the user to reconstruct the protocol from memory.

The following is sufficient as a handoff message:

> Continue the Memory Prism tests using `skill/tests/README.md`. Choose today's normal and software topics; do not ask me to choose. Give me one ordinary question at a time. I will lead the inquiry using Memory Prism, logic, reasoning and sanity checks. You provide additional information and research when I ask. Do not require domain-specific checklists or prior specialist knowledge from me.
