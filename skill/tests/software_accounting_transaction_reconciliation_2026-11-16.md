# Software Daily Test — Cross-System Accounting Transaction Reconciliation

**Test ID:** MP-SOFTWARE-2026-11-16-02  
**Date:** 2026-11-16  
**Selection:** Assistant-invented data-integrity scenario, deliberately outside physical logistics/coordination.  
**Status:** Design analysis completed in conversation; no implementation or independent scoring.

## Scenario

An organisation must reconcile transaction exports from two accounting systems with different field names, formats and transaction identifiers. The desired output is a persistent, auditable record of what was compared, what evidence supports each decision, what remains unresolved and who approved it—not merely a list of matched rows.

## Pre-interpretation inventory

| Concept | Working interpretation |
|---|---|
| Memory | Persistent, auditable reconciliation record, not a temporary match report. |
| Board | Accounting environment, source systems, export conventions, period and approval process. |
| Constraints | Formats, transaction semantics, currencies, date conventions, privacy, accounting rules and evidence limits. |
| Editors | Matching rules, exception classification, reviewer decisions and approval rules. |
| Audits | Source totals, row accounting, duplicate detection and traceable decisions. |
| Identity | Whether records represent the same economic transaction despite different source identifiers. |
| Flow Under Constraint | Import → normalise → propose matches → review → approve → export/report. |
| Working Lines | Ambiguous identity, sign conventions, rounding, date shifts, splits, reversals, duplicates and schema changes. |
| Accumulation Patterns | Reusable mappings, match evidence and recurring exception patterns. |
| No Sacred States | “Paid”, “cleared” and “matched” may not mean the same thing in both systems. |

## A. Conventional planning

Parse both CSVs, map columns, standardise dates and amounts, match by amount/date, produce matched and unmatched lists, then export. This hides a dangerous assumption: equal amounts and nearby dates prove transaction identity.

## B. MP-guided planning

- Preserve original rows and values alongside normalised representations.
- Establish source-specific field semantics before treating fields as equivalent.
- Treat matching as a proposal mechanism, not an authority that establishes identity.
- Keep reviewer decisions and supporting evidence in a persistent ledger.
- Represent ambiguous, split, reversed and one-to-many relationships explicitly.
- Audit source totals, row counts, duplicate/repeated imports and decision traceability.
- Distinguish source-system states from the reconciliation system's own decision state.

Pipeline: `Original files → Normalised records → Candidate matching → Review/decisions → Reconciliation record`.

## C. MP + challenge pass

Try to disprove proposed matches. Counterexamples include two legitimate same-amount/same-date transactions; one-to-many or split postings; reversals; duplicate imports; posting/settlement date shifts; and amounts matching only after currency conversion or rounding.

The system should preserve evidence and uncertainty, recording a supported reconciliation decision rather than simply asserting that two rows match.

**Attribution:** This used Critical-Thinking-style challenge behaviours from the test protocol. The separate Critical Thinking skill package was not loaded or executed; do not record this as a verified skill run.

## Proposed modular design

1. **Input contracts:** source formats, field meanings, provenance and supported variants.
2. **Import/normalisation:** preserve original data and create traceable normalised records.
3. **Candidate matching:** propose relationships without final authority.
4. **Decision ledger:** accepted, rejected and unresolved decisions with evidence and reviewer attribution.
5. **Reconciliation output:** reusable records and exception reports.
6. **Verification:** row counts, totals, duplicate imports and traceability.

The first hard blocker is representative exports and the actual accounting rules. Choosing a language or database before understanding these inputs is premature. Keep the first release read-only: immutable inputs, previewable proposals, separate decision records, manual review of ambiguity, no write-back.

## Assistant reasoning audit

| Question | Finding |
|---|---|
| What assumptions did it inherit? | It initially treated matching as the goal; the defensible goal is an auditable reconciliation outcome. |
| What information did it use or fail to use? | Generic scenario only; actual exports, accounting policies, source docs and approval rules were absent. |
| What constraints shaped the answer? | Read-only operation, integrity, incomplete identifiers, multiple transaction relationships, privacy and source semantics. |
| Which editor favoured that response? | Matching rules and reviewer authority determine which proposals survive into the accepted record. |
| Where did reasoning take a shortcut? | It assumed a canonical transaction model could be defined without real examples and legitimate variants. |
| What alternative structures could produce a better result? | Row matcher, evidence-based reconciliation ledger or broader integration platform; the ledger best fits the stated need without expanding scope. |

## Comparison

| Approach | Strength | Weakness |
|---|---|---|
| Conventional | Quickly identifies parsing, mapping and matching. | Can mistake superficial similarity for transaction identity. |
| MP-guided | Centres source meaning, durable output, state distinctions, authority and auditability. | Depends on real exports and rules to validate the model. |
| MP + challenge | Exposes split, reversal, duplicate and ambiguity cases by trying to falsify matches. | Not an independently executed Critical Thinking skill run. |

## Result and limitations

The strongest design is an evidence-based reconciliation record with candidate matching as one component. The updated orientation and reasoning audit changed the planning target, distinguished constraints from active decision editors and exposed the premature canonical-model assumption.

This was sequential, same-assistant, same-conversation and not blind or context-isolated. No representative exports or accounting policies were supplied. No code was written, tested, integrated or deployed. No independent assessment or operational safety outcome exists.

**Assessment:** Promising planning result; actual data contracts remain unvalidated.
