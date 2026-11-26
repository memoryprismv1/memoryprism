# Scoring: Design Viability Reviews A and B — Sauravi TSM-40

Inputs read: spec_v.md, vault/key.md, A.md, B.md only.

## 1. Key coverage

Fairness: every item can be inferred from spec_v.md. Even without the "notable design choices" summary, each key item's spec basis (materials, fits, missing washers/ferrules/drain/relief port, 10° tilt, Sorel bond water sensitivity, dry-running bushes, 45/12 mA draws, 250 rpm trip, no spindle support mentioned) is still in the remaining text. No items are marked UNFAIR, so the maximum is 46 points (23 items).

| Key ID | Item | Fair? | A score | A refs | B score | B refs | Note |
|---|---|---|---|---|---|---|---|
| K01 | PV glass soiling (10° tilt, mill dust, AR coat) | Yes | 2 | A D01 (dust on 10° panels, cleaning provision, keep exhaust off array) | 1 | B 3.2 (soiling at 10° listed only as an uncertainty; no mitigation) |  |
| K02 | Panel clamp galvanic corrosion + vibration loosening | Yes | 2 | A D10, D11 | 2 | B D22 | Both: isolating pads, bonding, locking/anti-seize. |
| K03 | MC4/PV cabling; IR test blind to series faults | Yes | 1 | A D12 | 1 | B D24 | Both cover tie UV failure, chafing and IR lockout with clip/conduit fixes; neither notes that a loose/part-seated MC4 becomes a hot high-resistance joint the IR test cannot see. |
| K04 | Enclosure condensation, no drain, vent blinding | Yes | 2 | A D07 | 2 | B D09 | Both: vent relocation, drain, coating/anti-condensation. |
| K05 | LFP heat ageing; single centre NTC; limits at abuse level | Yes | 2 | A D02 | 2 | B D03, D04 |  |
| K06 | Busbar joints: Al creep, no Belleville, dissimilar metals | Yes | 2 | A D03, 3.3 | 2 | B D02 |  |
| K07 | Idle-storage parasitic drain | Yes | 2 | A D04, 3.2 | 2 | B D05, 3.3 | B's fix (MPPT upstream of load isolator) is particularly good. |
| K08 | Controller studs / ferrule-less terminals loosening | Yes | 2 | A D08 | 2 | B D10 | Both cite vibration rather than thermal cycling, but the fixes (ferrules, locking nuts, torque) are right. |
| K09 | Motor cable flex fatigue at gland | Yes | 2 | A D14 | 2 | B D13 (consequence), D11 (strain-relief gland, larger loop) | A states the mechanism more clearly. |
| K10 | Motor cooling path clogging | Yes | 2 | A D16 | 2 | B D27 |  |
| K11 | Pivot pin/sintered bushes binding/wear | Yes | 1 | A D13 (bush wear only) | 2 | B D13 (hammer/fret, misalignment; dust-sealed bushes) | A misses binding/loss of gravity tension from dust/dried oil. |
| K12 | Poly-V belt wear/slip; 250 rpm trip blind to moderate slip | Yes | 2 | A D13, 3.5, test 9 | 2 | B D12, 3.6, test 9 | Both flag slip with a mechanism and a design fix (A: wrap/slack-side tension; B: rib-count rating). Neither notes the 250 rpm trip allows ~40% slip unalarmed. |
| K13 | Motor pulley single set screw / taper-lock fretting | Yes | 2 | A D15 | 0 | - | B has no pulley-retention finding. |
| K14 | Lower 30208 grease, no relief, preload drift | Yes | 2 | A D22, D20 | 2 | B D18 |  |
| K15 | Upper bearing Al housing outer-ring creep | Yes | 2 | A D21 | 2 | B D17, 3.8 |  |
| K16 | False brinelling during towing | Yes | 2 | A D23 | 2 | B D20 |  |
| K17 | Stones glazing/furrow wear vs 30 mm allowance | Yes | 2 | A D17 | 2 | B D15 |  |
| K18 | Feed agitator cam/finger fatigue | Yes | 2 | A D24 | 2 | B D28 |  |
| K19 | Hopper magnet tramp-iron build-up | Yes | 1 | A D24 (finger falls downstream of magnet; second magnet) | 1 | B D28 (magnet downstream of agitator) | Neither addresses build-up on the magnet washing into the stones. |
| K20 | Chamber/chute residue hygiene in humidity | Yes | 0 | - | 0 | - | Missed by both. |
| K21 | TRAP: greasing UHMW feed-spout bushes | Yes | 0 | A D24 (shield bushes; no warning) | 0 | - | Neither warns. Neither recommends greasing them either (B's 'greaseable' bushes in D13 are the motor pivot, not the feed spout). |
| K22 | TRAP: washing stones/chamber with water | Yes | 2 | A D18 (dry-only cleaning) | 2 | B D14 (ban on wet cleaning) |  |
| K23 | Protection function tests (E-stop, hopper sensor) | Yes | 1 | A D25 (single-channel controller-dependent E-stop), test 11 | 0 | B D16 (hopper sensor delay; not about failure/fouling or testing) | Neither covers dust fouling of the capacitive sensor or periodic proof-testing. |
**Key totals:** A 38/46 (17 caught, 4 partly, 2 missed). B 35/46 (16 caught, 3 partly, 4 missed).
Main differences: A gets K13 (pulley fretting), K01 (soiling mitigation) and part of K23. B scores better on K11 (dust-sealed pivot bushes).

## 2. Extra issues (not matching a key item)

### A
| ID | Issue | Class | Comment |
|---|---|---|---|
| D01 | PV/battery cannot sustain the duty | Valid-important | Decisive. The calculation checks out (Section 3). |
| D06 | ~100-140 W controller loss in a sealed polycarbonate box | Valid-important | Realistic. Derating or trips at 46 °C ambient. |
| D19 | Flour temperature will hit the 55 °C trip | Valid-important | The mechanism is real. The grain inlet temperature of 35-46 °C is pessimistic, but even with 30 °C grain the trip is likely at the upper heat fractions. |
| D25 | No lid interlock, single-channel controller-dependent E-stop, no belt guard, ~1 kJ coasting runner | Valid-important | A significant safety gap that B omits. |
| D26 | Canopy wind load and tongue weight while towing | Valid-important | 265 Pa at a 21 m/s relative wind is correct. |
| D05 | Weak passive balancing; SOC drift | Valid-minor | |
| D09 | Controller (55 A) and isolator margin vs 50-54 A | Valid-minor | |
| D11 | Module microcracks from towing | Valid-minor | |
| D20 | Thermal preload/gap drift of the spindle bearing pair | Valid-minor | Plausible, but the bearing span is assumed. |

Count: 5 important, 4 minor, 0 wrong.

### B
| ID | Issue | Class | Comment |
|---|---|---|---|
| D01 | Energy budget does not close | Valid-important | Correct. Includes a useful annual-hours check. |
| D07 | Enclosure heat ~143 W | Valid-important | |
| D21 | Parked wind uplift and overturning | Valid-important | The Cf of 1.3 for net uplift is on the high side for a 10° monopitch (about 0.7-1.3 depending on blockage). Even at the low end the uplift is ~3 kN against 6.3 kN weight with an eccentric load, so the point stands. |
| D06 | SOC drift and balancing | Valid-minor | |
| D08 | Controller sizing margin | Valid-minor | |
| D11 | 6 mm² H07RN-F phase cable ampacity; Hall EMI | Valid-minor | Arithmetic is right (42 A rms vs ~30 A derated). Conservative for a short run in free air. |
| D16 | 60 s hopper run-on gives dry stone running; restart against a packed gap | Valid-minor | |
| D19 | Ambiguous gap/relief load path; zinc-plated spring embrittlement | Valid-minor | A fair reading of the spec. |
| D23 | Module microcracks | Valid-minor | |
| D25 | No SPD; 15 A fuse below 1.5 × Isc (~10.5 A for this 72-cell module) | Valid-minor | Correct per IEC 62548. |
| D26 | No pre-charge on isolator closing | Valid-minor | |
| D29 | Instrumentation gaps | Valid-minor | |

Count: 3 important, 9 minor, 0 wrong. B lists more minor issues but misses A's guarding/E-stop safety finding and the flour-temperature trip.

## 3. Calculations

### My energy balance (from spec_v.md)
- **PV:** 1.64 kWp × 3.0-5.5 PSH × PR 0.70-0.75 ≈ 3.4-6.8 kWh/day (about 5 kWh in a typical dry-season day, about 3.5 kWh in the monsoon).
- **Load:** 2.2 kW shaft / 0.88 / 0.97 ≈ 2.58 kW electrical, about 50 A at 51.2 V. Across 40-60 kg/h this is roughly 1.8-2.6 kW. Demand at 4-7 h/day is 7-18 kWh/day.
- **Battery:** usable ≈ 4.3-4.9 kWh. It only shifts energy within a day; the first day from full gives about 3.5-4 h.
- **Standby:** 45 mA ≈ 2.3 W, negligible.
- **Sustained run time:** about 1.3-3.9 h/day, about 2-2.5 h/day at full load in good sun.
- **Annual:** ≈ 1.64 × 1,500 × 0.75 ≈ 1,850 kWh, so at most about 700-850 full-load h/yr against the 1,000-1,400 h claimed.

**Result:** the energy budget does not close. Expect roughly 40-55% of the claimed output. Both reviews reach this.

### A
| Calc | Verdict | My check |
|---|---|---|
| 3.1 Energy budget | Correct | 3.7/5.5/6.8 kWh and 1.4-3.8 h/day match my figures. |
| 3.2 Storage drain | Correct | 45 mA × 2,016 h = 91 Ah (86%). |
| 3.3 Joint heating | Correct | 52² × 0.5 mΩ = 1.35 W. |
| 3.4 Enclosure ΔT | Roughly right | The enclosure size is assumed. 100-140 W on 0.52 m² at 5.5 W/m²K gives 35-49 K, which is plausible. |
| 3.5 Belt geometry/tension | Correct | C ≈ 401 mm, wrap ≈ 130°, Fe = 238 N. |
| 3.6 Flour ΔT | Roughly right | 0.5 × 2.2 kW into 40 kg/h at 1.6 kJ/kg·K gives 62 K. The grain inlet temperature is pessimistic. |
| 3.8 Spindle thermal gap | Roughly right | The arithmetic is right; the span is assumed. |
| 3.9 Stone energy | Correct | J ≈ 0.5 + 0.52 ≈ 1.0 kg·m², E ≈ 1.0 kJ. |
| 3.11 PV voltage/current/fuse checks | Correct | |
| D26 Towing wind load | Roughly right | q ≈ 267 Pa is right; the force coefficient is assumed. |

Total: 6 correct, 4 roughly right, 0 wrong.

### B
| Calc | Verdict | My check |
|---|---|---|
| 3.2 Energy balance | Correct | 6.2/3.7 kWh and 2.3 h/day match. The annual figure (1,450 kWh/kWp × 0.95) is slightly optimistic but on the safe side for the conclusion. |
| 3.3 Storage drain | Correct | |
| 3.4 Sol-air temperature | Correct | 46 + 0.9 × 800/17 = 88 °C. |
| 3.5 Enclosure ΔT | Roughly right | Assumed size. |
| 3.6 Belt geometry | Correct | C 401 mm, wrap 131.8°, T1/T2 348/110 N. |
| 3.6 Belt capacity | Roughly right | The per-rib rating is assumed and B flags it for verification. |
| 3.6 Start-up inertia | Roughly right | 0.76 kg·m² treats the stone as a solid disc and understates the rim-ring share (about 1.0 kg·m² is more likely). The conclusion is unchanged. |
| 3.7 Wind uplift | Roughly right | Cf is high for uplift (see extras). |
| 3.8 Phase cable ampacity | Roughly right | |
| 3.8 Al housing clearance | Correct | 11.5e-6 × 80 × 40 = 37 µm. |
| 3.8 PV checks and 1.5 × Isc fuse | Correct | |
| 3.8 6205 L10 | Correct | (14/0.7)³ Mrev ≈ 47,600 h. |

Total: 7 correct, 5 roughly right, 0 wrong.

## 4. Verdict quality
- **A** ("Do not build as drawn; redesign and re-review"): justified. The energy shortfall is quantified, robust across the input range and shown to be a sizing problem rather than a detail. Secondary high-severity items back it up. Required changes are stated.
- **B** ("Do not build as drawn. Build with changes"): justified on equally solid energy evidence plus an annual-hours check. The two-part wording is slightly muddled but means the same as A's: revise the design, then prototype.

## 5. Harmful or unsafe recommendations
None in either review.
- Both explicitly ban wet cleaning of the stones (K22).
- Neither recommends greasing the feed-spout bushes (K21).
- B suggests "greaseable" motor-pivot bushes in D13. On a dusty pivot that risks a dust paste, but B pairs it with "sealed against dust", so it is not counted as harmful.
- A's D19 wording "bring the trip down to the real quality limit" is odd, but it is paired with better heat removal and feed control, so it is not unsafe.

## 6. Totals
| | A | B |
|---|---|---|
| Key points (max 46) | 38 | 35 |
| Caught / partly / missed | 17 / 4 / 2 | 16 / 3 / 4 |
| Extras important / minor / wrong | 5 / 4 / 0 | 3 / 9 / 0 |
| Calcs correct / rough / wrong | 6 / 4 / 0 | 7 / 5 / 0 |
| Harmful recommendations | 0 | 0 |

## 7. Overall judgement
Both reviews answer "should this be built as drawn?" the same way, correctly and for the same decisive, well-calculated reason: the on-board PV supplies roughly half the energy the stated duty needs. Both identify most of the same hardware weaknesses (busbar joints, battery heat, enclosure heat and condensation, Sorel bond and furrows, gravity-tensioned belt in transport, bearings, false brinelling). Neither makes a wrong calculation or a harmful recommendation.

A is modestly better on "what must change." It covers more key items (38 vs 35), including pulley retention and soiling mitigation. It has more important extras, most notably the inadequate guarding and controller-dependent E-stop for a 1 kJ runner, and flour-temperature tripping.

B offers more breadth in minor items: SPD and fuses, pre-charge, dry-running, cable ampacity, and a better storage-wiring fix. It also gives a stronger parked-wind overturning case.

The edge goes to A, but the difference is small.