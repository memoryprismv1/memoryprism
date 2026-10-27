# Memory Prism Test Development Log

**Purpose:** One cumulative, append-only record of daily Memory Prism skill tests for later weekly synthesis and peer review.

**Record policy:** Each run adds exactly one substantive test. Preserve the raw prompt, baseline, MP-guided answer, transfer comparison, scores, sources, limitations, unknowns, and next test. Do not silently revise previous entries. Scores are diagnostic, not a competition.

**Initialization note — 2026-10-27:** The current repository's `skill/tests/` directory contained `SMOKE_TESTS.md` and `GREAT_DEPRESSION.md`, but no cumulative development log. `GREAT_DEPRESSION.md` explicitly labels itself as an authored test case, not an executed controlled evaluation. It remains untouched. This log begins with today's executed-in-chat qualitative comparison; it does not relabel the authored Great Depression case as completed.

---

## Test C-2026-10-27-01 — Familiar keyboard sequence after an interface change

**Date:** 2026-10-27  
**Smoke-test source:** `skill/tests/SMOKE_TESTS.md`, section C  
**Status:** One qualitative baseline-versus-MP-guided comparison completed; no real user or software session was instrumented.

### 1. Exact prompt

> “I keep pressing the old shortcut after the software moved it. Why?”

**Scope assumption:** Interpret “moved it” as a change to the shortcut or the command's interaction path. The prompt does not specify the application, whether the old key combination still invokes a command, or whether the user can already recall the new mapping. Those are live uncertainties, not facts.

### 2. Ordinary baseline answer

> That's probably muscle memory. Repeated use makes the old key sequence automatic, so you trigger it before consciously checking. Practice the new shortcut slowly, keep a reminder nearby, and use it repeatedly until the new sequence sticks.

### 3. Memory Prism-guided answer

> The first useful distinction is whether this is an execution slip or a knowledge gap. If you can state the new shortcut but your fingers still use the old combination in the familiar context, an old practiced action may be getting triggered by the same cue. If you cannot reliably recall the new mapping, this is also a learning or visibility problem. If the old combination still invokes another command, there may be a shortcut conflict rather than just a habit.
>
> For a few attempts, note whether you knew the new mapping *before* the mistake and whether the error happens in the same application/context. Temporarily invoke the command from a visible menu, then practise the new sequence in that same context with a small reminder placed near the old trigger. If the error persists, inspect the actual shortcut mapping and documentation rather than assuming repetition alone will fix it.

### 4. Domain evidence consulted

- Lally, P., van Jaarsveld, C. H. M., Potts, H. W. W., & Wardle, J. (2010). “How are habits formed: Modelling habit formation in the real world.” *European Journal of Social Psychology*, 40, 998–1009. https://doi.org/10.1002/ejsp.674  
  In a 12-week field study of repeated daily behaviours, automaticity generally increased with repetition in a consistent context, with substantial individual variation. This supports the plausibility of context-linked automaticity, not a diagnosis of this particular shortcut error.

- Rosman, B., Ramamoorthy, S., Mahmud, M. M. H., & Kohli, P. (2014). “On User Behaviour Adaptation Under Interface Change.” Microsoft Research summary of an IUI '14 paper. https://www.microsoft.com/en-us/research/publication/user-behaviour-adaptation-interface-change/  
  Experiments using a simulated maze task found that interface changes could cause sharp performance shifts and that intermediate interfaces could mitigate some adaptation costs. This is relevant to interface-change costs, but it did not directly test an old keyboard shortcut in commercial software.

- Tak, S., Westendorp, P., & van Rooij, I. (2013). “Satisficing and the Use of Keyboard Shortcuts: Being Good Enough Is Enough?” *Interacting with Computers*, 25(5), 404–416. https://doi.org/10.1093/iwc/iwt016  
  The study found that shortcut use was not explained by knowledge alone and that a learning-support tool could increase use. It concerns shortcut adoption, not the exact error in this prompt.

### 5. Transfer test — different domain

**Transfer prompt:**

> “After reorganizing my kitchen, I keep reaching into the old drawer for spoons even though they are now in another drawer. Why?”

**Ordinary baseline transfer answer:**

> You are used to the old location. Label the new drawer, consciously reach for it, and repeat the new routine until it becomes familiar.

**Memory Prism-guided transfer answer:**

> Separate two possibilities: you may not reliably remember the new location, or the familiar kitchen cues may still trigger the old reaching action before you check. Also check whether the new location is stable and obvious. For a short trial, keep the spoons in one consistent new place and put a temporary cue at the old drawer directing attention to the new one. Note whether you reach toward the old drawer before remembering the change, or whether you genuinely cannot recall where the spoons went. Those outcomes point to different fixes: changing the cue/action path versus improving location information. This is a proposed diagnostic, not an observation from a real kitchen.

### 6. Comparison: did MP improve the next question or action?

**Qualitative finding:** Yes, modestly. The baseline offers a plausible habit explanation and sensible generic practice advice. The MP-guided answer separates an automatic execution slip from not knowing the new shortcut and from a possible shortcut conflict. That distinction changes the next action: observe whether the new mapping was known before the mistake, then check the actual mapping if errors persist. The physical-location transfer preserves the diagnostic distinction without claiming that keyboard use and reaching for a drawer are identical mechanisms.

**What MP added beyond vocabulary:** a discriminating observation and conditional next steps. The answer does not need the user to perform a full framework checklist.

### 7. Smoke-test scoring

The repository rubric scores six dimensions from 0 to 2. Dimension 2 (“consults the correct source text when Memory Prism-specific interpretation is required”) is **N/A** for this domain prompt. Therefore the applicable maximum is **10**, not 12. Scores are qualitative and not blinded.

| Applicable dimension | Baseline | MP-guided | Reason |
|---|---:|---:|---|
| 1. Directly engages the question | 2 | 2 | Both explain why the old action may recur. |
| 3. Selects lenses proportionately | 2 | 2 | Neither answer forces a full checklist; MP uses a narrow distinction. |
| 4. Uses accurate domain mechanisms and evidence | 1 | 2 | Baseline gives an uncited, single-cause explanation; MP distinguishes plausible mechanisms and consults relevant, limited evidence. |
| 5. Distinguishes uncertainty from fact | 1 | 2 | Baseline says “probably muscle memory”; MP names unresolved alternatives and the ambiguity in the prompt. |
| 6. Produces a useful next step without homework handoff | 1 | 2 | Baseline advises practice; MP proposes a small diagnostic and conditional next actions. |
| **Total (5 applicable dimensions)** | **7/10** | **10/10** | Diagnostic scores only. |

### 8. Failures and evidence boundaries

- This is a constructed qualitative comparison by the same model, not an independent, randomized, blinded, or externally scored experiment.
- The MP-guided answer had the benefit of targeted literature search; the baseline did not. This does not isolate the causal effect of Memory Prism from the benefit of research.
- No actual keyboard errors were counted; no specific software, operating system, shortcut mapping, or user proficiency was observed.
- The cited habit study concerns repeated daily behaviours generally, not keyboard shortcuts specifically. The interface-change study uses a simulated task, not a commercial-software shortcut change. The keyboard-shortcut study examines shortcut use/adoption rather than stale shortcuts after a change.
- The wording “software moved it” is ambiguous. It may refer to a changed key binding, a relocated command in the interface, or both.
- The transfer result is hypothetical and was not tested with a real person or kitchen.

### 9. Research leads

1. Find direct empirical studies of action slips/capture errors after localized interface changes, stratified by prior user proficiency.
2. Test whether a cue placed at the old trigger reduces errors more than a generic announcement or reminder.
3. Separate “does not know the new mapping,” “knows it but executes the old sequence,” and “old mapping remains active/conflicts” as distinct error categories.

### 10. Unknowns

- Was the shortcut itself changed, or only the command's visible location?
- Does the old shortcut still do something?
- Does the user know the new mapping before the error occurs?
- Are errors concentrated in one familiar application/context or across applications?
- Does a targeted cue reduce errors, and does the effect persist after the cue is removed?

### 11. Next test

Run smoke test D: “Why does a false WhatsApp forward keep circulating after someone posts a correction?” Preserve the same comparison discipline and distinguish message reach, audience overlap, source trust, repetition, and platform affordances only where evidence supports them.

---
