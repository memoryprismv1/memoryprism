# Smoke Test H — Translator versus Threshold — 2026-11-25

**Test ID:** MP-SMOKE-H-2026-11-25-01
**Test:** `tests/smoke/SMOKE_TESTS.md` § H
**Run type:** Assistant-generated, single condition (MP skill in use)
**Context:** same conversation as the repo read-through; self-scored; not blind
**Sources consulted:** `source-corpus/Memory-Prism-Framework.md` (Memory; Board), `source-corpus/foundations/Audits.md` (Threshold-Only Systems; Viability Envelope; Dormancy; Converged Architecture), `references/concepts.md`

## Prompt

> Is a spectrometer a translator in Memory Prism? Is a rock that cracks when stress passes a limit performing an audit?

## Answer produced

**Short answer:** Yes to the first, no to the second.

| MP concept | What I identify in this query |
|---|---|
| Translator | The spectrometer: it extracts differences (isotope ratios, spectral lines) from material structure |
| P-Memory | The isotope ratios the spectrometer reads; also the crack itself, as residue left by the stress event |
| Threshold (Audits essay) | The rock's fracture strength, crossed when stress exceeds it |
| Audit (candidate, rejected) | Nothing in the rock detects deviation or corrects it |

**Spectrometer → translator.** The Framework defines a translator as "any system capable of extracting differentiation from structure" and names "a spectrometer measuring isotopes" as one of its own examples. The translator does not create the memory; the isotope ratio exists whether or not anyone reads it. The Framework also makes translators board-dependent and costly, so a spectrometer's detection limit is a translator limit: "absence of detected residue reflects translator limitation, not absence of past interaction."

**Cracking rock → threshold, not audit.** The Audits essay makes exactly this contrast. Threshold-only systems "do not detect deviation… do not attempt correction… transition when limits are crossed." An audit is "the mapping of system state onto its viability envelope," and a viability envelope requires a boundary, active maintenance of gradients, detection of deviation, and correction funded by energy flow. "Rocks have thresholds. Cells have envelopes." The essay's summary chain for non-living systems is Energy → Accumulation → Threshold → Transition, with no audit step.

**The useful distinction between the two halves.** A spectrometer differentiates but does not, by itself, correct anything, so it is a translator but not an audit either. It becomes part of an audit only when wired into a loop that maps readings against a viability envelope and triggers correction (for example, process control that shuts a furnace when a spectral reading drifts). Translator and audit are different roles: every audit needs something that reads, but not every reader is part of an audit.

**One caveat flagged, not resolved.** The Framework's Feedback section says "Translators detect imbalance and trigger correction when thresholds are crossed", which could be read as tying translators to correction. Its Memory section's examples (archaeologist, spectrometer) clearly don't require correction. I read "trigger correction" as describing translators *inside* audit structures, not as part of the definition. [Reasonable inference]

**What the crack leaves behind:** the fracture is P-Memory of the stress event, and a geologist or an acoustic-emission sensor reading it would be the translator. The rock cracking is the threshold; reading the crack later is translation; neither is an audit.

## Smoke score (self, unblinded)

| Dimension | Score | Note |
|---|---:|---|
| 1 Engages the question | 2 | Direct yes/no first |
| 2 Consults correct source | 2 | Framework and Audits essay quoted; quotes checked against the corpus files |
| 3 Proportionate lenses | 2 | Only Audits essay used; table rows limited to four |
| 4 Domain accuracy | 2 | Light domain content; process-control example is generic |
| 5 Uncertainty vs fact | 2 | Feedback-section tension surfaced and labelled as inference |
| 6 Useful answer, no handoff | 2 | Adds the translator/audit role distinction |
| **Total** | **12/12** | Self-scored by the answering assistant; a ceiling score from the producer isn't strong evidence |

**Finding worth keeping:** the Framework's Feedback section phrase "Translators detect imbalance and trigger correction" is a possible source of the very confusion this smoke test targets. A one-line note in `concepts.md` (translator ≠ audit; a translator becomes part of an audit only inside a correction loop) would make that explicit. Not changed here, since ordinary test runs don't modify `skill/`.

## Score line

Not scored on the IQ rubric (na). Smoke-test score: 12/12 (self, unblinded).

SCORES: IQ=na/12; scorer=self; blind=no
