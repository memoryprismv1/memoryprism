# Daily Test Scoring

One rubric for every daily record (normal and software), so scores can be compared across days. It rates **the answer** and **the method**. It never rates the user.

Applies to records dated **2026-11-24 onward**. Earlier records used several incompatible formats (maxima of 8, 12 and 14) and are not re-scored.

## What a score means

- Scores are **diagnostic**, not a competition or a performance claim.
- Most daily runs are self-scored by the same assistant, in the same conversation, unblinded. Say so in the record. Such scores can support "observed in this run", never "demonstrated".
- Always record the failure mode behind any 0 or 1.

## The two scales

Score each dimension **0, 1 or 2**. Report the two totals separately and never add them together: one measures the answer, the other measures use of Memory Prism.

| Scale | Applies to | Dimensions | Maximum |
|---|---|---|---|
| **IQ — Inquiry Quality** | every condition (baseline, MP-guided, MP + other skill) | 6 | 12 |
| **MPF — MP Fidelity** | MP-guided conditions only (mark baseline "n/a") | 6 | 12 |

If a dimension genuinely cannot apply, mark it **n/a** and report against the applicable maximum (for example `MPF 8/10`). Do not mark n/a to avoid a low score.

## IQ — Inquiry Quality

| # | Dimension | 0 | 1 | 2 |
|---|---|---|---|---|
| IQ1 | **Engages the question as asked** | Answers a different question, or buries the settled answer under a framework exercise | Answers, but narrows the user's framing early or delays the settled part | Settled part first; user's framing preserved; open part clearly identified |
| IQ2 | **Mechanism and evidence accuracy** | Material errors, or unsupported claims stated as fact | Broadly correct but with a notable omission, over-generalisation (one species or system stretched to all) or weak sourcing | Accurate mechanisms; claims traceable to cited sources; scope stated |
| IQ3 | **Evidence boundaries** | Hypothesis, analogy or a coherent story presented as established | Partly labelled; the evidence level of a key claim is unclear | Observed, sourced, inferred and speculative kept apart where it matters; what was *not* tested is stated |
| IQ4 | **Competing explanations** | One story defended; no alternatives | Alternatives named but not tied to different predictions | At least two plausible explanations kept alive, each with what it predicts and what would separate them (or a justified statement that none compete) |
| IQ5 | **Next question or action** | None, generic ("research more"), or handed back to the user | Specific but not diagnostic: the result would not change a belief or action | Concrete, doable and diagnostic; the assistant already did the researchable step |
| IQ6 | **Clarity and economy** | Terminology obscures, repeats or replaces domain language | Understandable, with avoidable overhead or repetition | Understandable without MP knowledge; every term earns its cost; length fits the question |

**Software inquiries**, look for in IQ2–IQ5: the operating invariant is stated; distinct system states are kept distinct (intended, delivered, acknowledged, adopted, observed); failure timing, unknown outcomes and recovery are addressed; observability and rollback are considered; documentation or standards are cited and any disagreement with them is argued, not assumed; the record says plainly that no live system was run, if none was.

**Normal inquiries**, look for in IQ2–IQ5: the actual physical, biological or social mechanism; scope limits (which species, material or conditions); the distinction between a measured result and a plausible mechanism; and a test or observation that could separate explanations.

## MPF — MP Fidelity

| # | Dimension | 0 | 1 | 2 |
|---|---|---|---|---|
| MPF1 | **Inventory first and concrete** | No inventory, or it comes after the interpretation, or rows paste definitions | Inventory present but partly generic, or placed late | Table precedes interpretation; each row names a concrete feature of this query |
| MPF2 | **Proportionate selection** | Concepts or lenses forced for coverage; empty or "not relevant" rows | Mostly selective with one or two rows that add nothing | Every row or lens earns its keep; candidates marked as candidates |
| MPF3 | **Concept fidelity** | Constraints merged with editors, Ledger demoted or collapsed into Flow or Accumulation, P-Memory narrowed to records or intent | One distinction blurred, or Ledger skipped where resources or maintenance clearly mattered | Constraint/editor and Ledger/Flow/Accumulation kept distinct; Ledger concrete where it bears on persistence; P-Memory not narrowed |
| MPF4 | **No unsupported mechanism** | Invents an editor, audit or translator, or implies sensing, intent or governance without support | An analogy or threshold treated as more than a lead | Threshold is not called an audit; analogies stay leads; anthropomorphism avoided |
| MPF5 | **Source use** | MP definitions given from memory where interpretation mattered, or misstate the source | Source consulted but loosely applied | Framework or essay consulted where interpretation mattered, and claims match it (**n/a** if no MP-interpretation question arose) |
| MPF6 | **Reasoning audit actually used** | Not run, or recited as a list, or dumped on the user | Run, but changed nothing material | Audit led to a visible correction, added limitation or better alternative; nothing dumped on the user |

## Integrity flags

Declare each as **No** or **Yes**. Any **Yes** must be explained in the record and applies the cap.

| Flag | Cap |
|---|---|
| F1 A cited source was not actually opened or checked | IQ2 ≤ 1 |
| F2 A citation or quotation could not be verified or was fabricated | IQ2 = 0 |
| F3 A literature review was presented as an experiment, a proposed test as completed, or a same-conversation comparison as independent | IQ3 = 0 |
| F4 The user's contribution was inflated, understated, or the user was graded | The record must be corrected before it is filed |
| F5 An editor, audit or translator was asserted without a supporting mechanism | MPF4 = 0 |
| F6 The next research step was handed back to the user although it could be done | IQ5 ≤ 1 |

## Reading and comparing scores

- **Compare conditions on IQ only.** Baseline versus MP-guided is a comparison of answers (IQ). MPF describes how Memory Prism was used and does not enter the comparison.
- **Claim a difference only when** (a) it is at least 3 points on IQ, (b) each differing dimension cites the passage that justifies it, and (c) the record says who scored and whether blind. Otherwise write "no demonstrated difference".
- A low MPF with a high IQ is a legitimate finding: the answer was good but MP was misused or unnecessary.
- If MP added only overhead (IQ6 lower than baseline with no IQ gain elsewhere), say so plainly. That is useful signal about when not to invoke MP.
- Never present a self-scored result as an independent evaluation.

## Provenance fields

Every record's score sheet states these, using one value each:

| Field | Values |
|---|---|
| Run type | user-led · user-guided correction · assistant-generated synthesis · standards-grounded scenario · live implementation |
| Conditions | list the conditions actually run |
| Context | same-context · isolated |
| Scorer | self · second model · human |
| Blind | yes · no |
| Execution | literature · standards/docs · live run · none |

## Score sheet (copy into every record)

```markdown
## Score sheet

**Run type:** …  **Conditions:** …  **Context:** …  **Scorer:** …  **Blind:** …  **Execution:** …

| Dim | Baseline | MP-guided | Note (failure mode for any 0/1) |
|---|---:|---:|---|
| IQ1 Engages the question | | | |
| IQ2 Mechanism and evidence | | | |
| IQ3 Evidence boundaries | | | |
| IQ4 Competing explanations | | | |
| IQ5 Next question or action | | | |
| IQ6 Clarity and economy | | | |
| **IQ total** | /12 | /12 | |
| MPF1 Inventory first and concrete | n/a | | |
| MPF2 Proportionate selection | n/a | | |
| MPF3 Concept fidelity | n/a | | |
| MPF4 No unsupported mechanism | n/a | | |
| MPF5 Source use | n/a | | |
| MPF6 Reasoning audit used | n/a | | |
| **MPF total** | n/a | /12 | |

**Integrity flags:** F1 No · F2 No · F3 No · F4 No · F5 No · F6 No
**Difference claimed?** No demonstrated difference / Observed in this run: … (see rule above)

SCORES: IQ_baseline=…/12; IQ_mp=…/12; MPF=…/12; scorer=self; blind=no
```

If a record has a single condition, delete the unused column and the `IQ_baseline` field. If a record has extra conditions (for example MP + Critical Thinking), add a column; do not score the other skill's own method on MPF.

## Index entry format

Append one entry per record to `tests/records/DEVELOPMENT_LOG.md`, immediately before `## Collection rule`. Keep it to three sentences or fewer; the record holds the detail.

```markdown
- [Title](file_name.md) — Test ID; run type; conditions. One-sentence finding. Scores: IQ x/12 (baseline y/12), MPF z/12; self-scored, same-context, unblinded. Limits: one short clause.
```

## Procedure (about five minutes)

1. Fix the run type, conditions, context, scorer and blind status first.
2. Score IQ for each condition, writing the failure mode next to any 0 or 1.
3. Score MPF for MP-guided conditions only.
4. Declare the integrity flags and apply caps.
5. Decide whether a difference may be claimed. If unsure, write "no demonstrated difference".
