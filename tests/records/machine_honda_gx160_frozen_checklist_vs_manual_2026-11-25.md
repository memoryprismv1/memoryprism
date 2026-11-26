# Machine Test: Honda GX160 — Frozen MP Checklist vs Honda's Schedule — 2026-11-25

**Test ID:** MP-MACHINE-2026-11-25-02
**Run type:** Assistant-led MP derivation from design specs only, frozen in a file before opening the manufacturer's schedule, then compared
**Context:** same conversation; self-assessed; partly blind (no maintenance pages opened before freezing; general training knowledge of small engines not excluded)
**Frozen file:** `assets/2026-11-25_honda_gx160/mp_checklist_frozen.md` (file time 2026-11-25 23:30:27 IST; SHA-256 c654a422a8ac1bcdcf96a39f4c12ce394a680f622cc4ee250833fd30f54bd734)
**Deliverable:** a Claude Sheets checklist and log (Checklist, Log, vs Honda, Notes). Content reproduced below.

## Method

1. Read only design specs: air-cooled 4-stroke OHV single, cylinder inclined 25°; flywheel-fan cooling; splash lubrication with no oil filter, ~0.6 L; Oil Alert low-level shutdown; transistorized magneto; float carburetor with strainer; dual-element air cleaner; mechanical governor; recoil starter; ~3 L tank; optional spark arrester; no hour meter.
2. Derive and freeze M01–M24 with MP.
3. Open Honda's GX120/160/200 owner's manual and compare; add Honda-only items H01–H05.

## Result counts

| Verdict | Items |
|---|---|
| Match | 13 |
| MP stricter (sooner than Honda) | 4 |
| MP looser | 1 |
| MP added | 4 |
| Partly | 3 |
| MP missed | 4 |
| **Total** | **29** |

## Item table

| ID | Task | MP | Honda | Verdict |
|---|---|---|---|---|
| M01 | Oil level (engine level) | Each use | Each use | Match |
| M02 | Air filter visual | Each use | Each use | Match |
| M03 | Air filter clean | 25 h | 50 h (dusty: more often) | MP stricter |
| M04 | Paper element replace | 100–200 h | 300 h / yearly | MP stricter |
| M05 | Fuel, leaks, line cracks | Each use | Each use | Match |
| M06 | Fins and fan screen clear | Each use | Each use | Match |
| M07 | First oil change | 5–10 h | 20 h / first month | MP stricter |
| M08 | Oil change | 50 h | 100 h / 6 months | MP stricter |
| M09 | Plug inspect/gap | 50–100 h | 100 h | Match |
| M10 | Plug replace | 200–300 h | 300 h / yearly | Match |
| M11 | Spark arrester | 100 h | 100 h | Match |
| M12 | Sediment cup | 100 h | 100 h | Match |
| M13 | Storage: stabilise or drain fuel | Before storage (>30 days) | Same; "can deteriorate within 30 days" | Match |
| M14 | Valve clearance | 300 h | 300 h (dealer) | Match |
| M15 | Combustion chamber decarbon | 500 h | 500 h (dealer) | Match |
| M16 | Fasteners, shields | 50 h | Each use (pre-op) | MP looser |
| M17 | Fuel tube | 2 years | 2 years | Match |
| M18 | Recoil rope | 100 h | — | MP added |
| M19 | Governor linkage | 100 h | — | MP added |
| M20 | Oil Alert wire check | 100 h | — | MP added |
| M21 | Idle speed | 300 h | 300 h (dealer) | Match |
| M22 | Track running hours | Once (fit hour meter) | Log hours for commercial use | Partly |
| M23 | Oil condition (milky = water) | Each check | — | MP added |
| M24 | Storage prep | Before storage | Before storage, with extra steps | Partly |
| H01 | Reduction case oil (geared models) | — | Each use (check) | MP missed |
| H02 | Fuel tank and filter clean | — | ~300 h / yearly (reading uncertain) | Partly |
| H03 | Storage: oil into cylinder, close valves | — | Before storage | MP missed |
| H04 | No plastic cover; no water into air cleaner/muffler | — | Rule | MP missed |
| H05 | Oil-bath air cleaner refill | — | When cleaning | MP missed |

## Findings

- MP reliably finds **what** needs attention; it is weaker on exact **numbers** and model-specific procedures.
- **Cautious bias:** where MP had no number, it chose the safe side every time (oil 50 h vs 100 h; first change 5–10 h vs 20 h).
- Every miss was a variant detail or known procedure, not a reasoning gap. The geared variant appeared in the spec listings and was overlooked.
- Ledger reasoning ("no filter, so draining is the only removal path") produced the right intent for oil care.

## Limits

General training knowledge may account for some matches. The schedule PDF text came through with misaligned columns; the 100 h oil change is confirmed by two other sources, but sediment cup, spark plug check, spark arrester and fuel tank/filter intervals are best readings.

## Sources

- Honda GX120/GX160/GX200 owner's manual (cdn.powerequipment.honda.com, 00X37Z4V6000)
- LS Engineers, GX160 Maintenance Information (PDF)
- Honda Engines, GX160 specifications pages

## Score line

Not scored on the IQ rubric (na). Against Honda's schedule: 13 match, 4 MP stricter, 1 looser, 4 added, 3 partly, 4 missed (of 29).

SCORES: IQ=na/12; scorer=self; blind=no
