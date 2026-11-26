# Invented-Machine Blind Test 2: Paper-Design Viability Review (Sauravi TSM-40) — 2026-11-26

**Test ID:** MP-BLIND-2026-11-26-02
**Run type:** Controlled blind test with isolated agents and a hidden key; the question was "should this machine be built as drawn?"
**Conditions:** MP reviewer vs plain reviewer
**Context:** isolated · **Scorer:** separate agent, blind to condition · **Labels:** randomised (MP = A)
**Assets:** `assets/2026-11-26_invented_machine_tsm40/` (spec without design summary, hidden key, both reviews, blind score, unblinded labels)

## Origin

Owner's proposal after Blind Test 1: "Another usage will be regarding viability of a machine blueprint. A machine which hasn't been built yet but exists in paper." Owner's reading of results so far: MP is "a good deconstruction tool rather than a construction tool."

## Design changes from Test 1

- The spec's "Notable Design Choices" section was removed (`spec_viability_no_design_summary.md`) to remove the ceiling effect.
- Each reviewer wrote: a verdict (build as drawn / build with changes / do not build), a design-issues table with mechanism, consequence, severity and design change, viability calculations, and prototype tests.
- Scorer rules: key items read as design weaknesses (2 = flagged with right mechanism and a design change); extra issues classified Valid-important / Valid-minor / Wrong; calculations checked; scorer did its own energy balance.

## Results (unblinded)

| | MP | Plain |
|---|---|---|
| Key points (of 46; all items fair) | 38 | 35 |
| Caught / Partly / Missed | 17 / 4 / 2 | 16 / 3 / 4 |
| Extra issues: important / minor / wrong | 5 / 4 / 0 | 3 / 9 / 0 |
| Calculations: correct / rough / wrong | 6 / 4 / 0 | 7 / 5 / 0 |
| Harmful recommendations | 0 | 0 |
| Verdict | Do not build as drawn | Do not build as drawn (build with changes, then prototype) |

**Scorer verdict:** MP modestly better; the difference is real but small.

## The decisive finding (both reviews; scorer confirmed independently)

The energy budget does not close. PV ≈ 1.64 kWp × 3.0–5.5 peak sun hours × 0.70–0.75 ≈ 3.4–6.8 kWh/day, against 7–18 kWh/day for 4–7 h of grinding at ~2.6 kW electrical. Sustained run time ≈ 1.3–3.9 h/day; at most ~700–850 full-load hours/year vs 1,000–1,400 claimed (~40–55% of stated output). The battery only shifts energy within a day.

## Differences

- **MP only:** motor pulley held by a single set screw; panel soiling from the mill's own dust; no lid interlock or belt guard with an emergency stop that depends on the controller (stone stores ~1 kJ); flour likely to hit the 55 °C trip in hot weather.
- **Plain only:** stronger parked-wind overturning check; fuse/SPD sizing; phase-cable ampacity; better storage-drain fix; scored higher on the motor pivot bushes.
- **Both missed:** trap of greasing the dry-running feed bushes; flour-residue hygiene in humidity; the stone-speed trip missing moderate belt slip.

## Reading

For "should this be built as drawn?", MP worked as a deconstruction tool and found more serious flaws; plain expert reasoning found more minor ones. Ledger ("can it pay its running costs?") points directly at the issue that sinks this design. One machine, one run per condition: the 3-point gap is a lead, not proof.

## Limits

Same model family for all agents. The key was written as a maintenance key and read as design weaknesses. Single scorer.

## Score line

Not scored on the IQ rubric (na). Hidden-key score: MP 38/46, plain 35/46.

SCORES: IQ=na/12; scorer=independent agent; blind=yes
