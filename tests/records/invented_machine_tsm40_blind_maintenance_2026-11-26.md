# Invented-Machine Blind Test 1: Maintenance Checklist (Sauravi TSM-40) — 2026-11-26

**Test ID:** MP-BLIND-2026-11-26-01
**Run type:** Controlled blind test with isolated agents and a hidden answer key on a fictional machine (no manual exists anywhere, removing training-data leakage)
**Conditions:** MP solver vs plain solver
**Context:** isolated (four separate agents) · **Scorer:** separate agent, blind to condition · **Labels:** randomised (MP = X)
**Assets:** `assets/2026-11-26_invented_machine_tsm40/` (spec, hidden key, both checklists, blind score, unblinded labels)

## Design

1. **Designer agent** invented the Sauravi TSM-40 Towable Solar Stone Mill (trailer, 4 × 410 W PV, 5.4 kWh LiFePO4, 2.2 kW BLDC motor, gravity-tensioned poly-V belt, Sorel-cement-bonded stones, hot dusty monsoon climate). It wrote a spec sheet with no maintenance hints and a hidden key of 23 items: wear and failure mechanisms with intervals, at least four modelled on real but less-obvious failure modes, two traps and at least two sensor gaps.
2. **MP solver** and **plain solver**: same instructions and tools, spec only; the MP solver also loaded the skill.
3. **Scorer**: key + both checklists, labels X/Y randomised. Rules fixed in advance: 2 Caught / 1 Partly / 0 Missed per key item; intervals Accurate if within half to double; traps only if warned against; sensor gaps only if recognised; unfair items excluded.
4. Leak check of the spec by grep only (the coordinator did not read the key before scoring). Framework method note stripped from the MP checklist before scoring.

Note: the plain solver ran on the evening of 25 Nov; the MP solver could not run until 26 Nov because of a usage limit. Same spec, same instructions.

## Results (unblinded)

| | MP | Plain |
|---|---|---|
| Points (of 46; all 23 items judged fair) | 44 | 44 |
| Caught / Partly / Missed | 21 / 2 / 0 | 21 / 2 / 0 |
| Traps caught (of 2) | 1 | 2 |
| Sensor gaps caught (of 3) | 3 | 3 |
| Intervals Accurate / Too often / Too rare | 14 / 7 / 0 | 16 / 2 / 3 |
| Harmful advice | 0 | 0 |

**Scorer verdict:** no meaningful difference.

## Notable differences

- MP missed the trap of lubricating the dry-running UHMW-PE feed bushes (noted they run dry; no warning).
- MP intervals were too frequent seven times, too rare never: same cautious lean as the GX160 test.
- MP fixed root causes more often (isolating pads at the PV clamps instead of only inspecting for galvanic corrosion).
- Both missed unloading the runner stone before towing (false brinelling prevention).

## Main limitation: ceiling effect

The original spec ended with a "Notable Design Choices" section that listed most hazards. Both solvers nearly maxed out, so the test could not separate them. Blind Test 2 removed that section.

## Other limits

All agents are the same model family, so designer and solvers may "think alike". One machine, one run per condition.

## Score line

Not scored on the IQ rubric (na). Hidden-key score: MP 44/46, plain 44/46.

SCORES: IQ=na/12; scorer=independent agent; blind=yes
