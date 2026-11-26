# Machine Test: Deriving a Maintenance Schedule for the Prusa i3 MK3S+ — 2026-11-25

**Test ID:** MP-MACHINE-2026-11-25-01
**Run type:** Assistant-led MP derivation from a documented open-hardware design, compared against the manufacturer's official maintenance guide
**Context:** same conversation; not blind (the assistant had seen the official guide's headings before deriving); self-assessed
**Deliverable:** a Claude Sheets maintenance log (Schedule, Log, MP map, Notes tabs). The content is reproduced here.

## Owner's framing afterwards

"MP isn't obviously going to 100%, it doesn't have domain knowledge. You have greater expectations than me." MP supplies the questions; domain facts supply the answers. A miss on a domain fact is MP handing off, not MP failing.

## MP map used

| Concept | In this printer | Consequence for maintenance |
|---|---|---|
| Board | Room dust, temperature, enclosure, duty cycle, filament types | Intervals in print hours, adjusted for board |
| P-Memory | Prints; debris, rod scratches, belt stretch, loose screws, discoloured connectors | Inspect for these records; the log is the machine's memory |
| Flow | Filament path; heat (heater → nozzle; heatbreak cooling); motion; current; air | Each flow has a path that clogs, wears or loosens |
| Accumulation | Dust on rods and fans, shavings in gears, plastic on nozzle, oils on sheet | Clean at the build-up rate |
| Constraints | Belt status 240–300; idler tension; solvent limits; no lube on Z lead screws; hotend fan must run | Stay inside limits; some are "don't" rules |
| Ledger | Lubricant film, belt tension, terminal clamping force, cable flex life, nozzle, fan bearings | Replenish or replace before exhausted |
| Working Lines | High-current bed power path; moving cable bundles; belt force via set screws; filament via gears | Inspect where force and current already travel |
| Translators | Thermistors, IR filament sensor, SuperPINDA, fan RPM, belt status, voltage readout; human senses | What nothing reads needs a manual check |
| Audits | Firmware thermal runaway, MINTEMP/MAXTEMP, thermal model, fan monitoring, crash detection, power panic | Real audits; test them after changes |
| Lag | Belt drift, terminal heating, cable fatigue | Intermittent errors and trends are the correction window |
| Editors (candidate) | The maintainer | The schedule makes editing deliberate |

## Derived schedule (23 items) and comparison with Prusa's guide

| ID | Task | Every | vs Prusa guide |
|---|---|---|---|
| S01 | Clean steel sheet (IPA) | Each print | Matched |
| S02 | Acetone only on Smooth sheet | Rule | Prusa only (MP missed) |
| S03 | Glance at nozzle/heater block | Each print | MP added |
| S04 | Listen and look for anything new | Each print | Partly (blog: squeak = gear dust) |
| S05 | Fans spin freely, no strands | 50 h | Matched (no hours given) |
| S06 | Write down errors since last entry | 50 h | MP added |
| S07 | Clean and lubricate X/Y/Z smooth rods | 200 h | Matched |
| S08 | Do NOT lubricate Z lead screws or nuts | Rule | Prusa only (MP got this wrong) |
| S09 | Check rods for scratches | 200 h | Matched |
| S10 | Belt status: read and log | 200 h | Matched; trend logging MP added |
| S11 | Belt pulleys, set screw on flat | 200 h | Matched |
| S12 | Extruder gears | 200 h | Matched |
| S13 | Idler screw tension | 200 h | Matched |
| S14 | Moving cables: wiggle while watching temperatures | 200 h | Partly; wiggle test MP added |
| S15 | Bed voltage while heating: read and log | 200 h | MP added |
| S16 | Power terminals and connectors (Einsy + PSU) | 700 h | Matched (Einsy 600–800 h); PSU terminals MP added |
| S17 | Dust out electronics box | 700 h | Matched |
| S18 | Don't overtighten X-carriage screws/U-bolts | Rule | Prusa only (MP partly) |
| S19 | Bearings: remove, clean, regrease | As needed | Matched |
| S20 | Replace nozzle | As needed | Matched; abrasive note MP inference |
| S21 | Firmware and slicer up to date | 700 h | Matched |
| S22 | Test safety features after changes | After update/repair | MP added (Prusa test article exists) |
| S23 | Recalibrate first layer after maintenance | After maintenance | MP added (community suggestion) |

## Findings

- **Matched:** most routine items.
- **MP added:** trend logging (belt status, bed voltage), cable wiggle test against live temperature readout, PSU terminals, error log as early warning, safety-feature testing after changes.
- **MP missed or wrong:** do not lubricate Z lead screws (MP logic predicted "lubricate"); sheet-coating solvent rules; overtightening specifics.
- **Strongest concept: Translators.** Splitting "what sensors watch" from "what nothing watches" gives a general rule: maintain manually what no sensor reads.
- **Weakest concept: Editors.** In a machine, only the maintainer filters what persists; marked candidate.

## Limits

Not blind. Several items rest on owner forum reports (cable breaks, melted terminals, bed voltage ~23.6–23.7 V). Worked from the documented design, not the CAD files. AI-led, not person-led.

## Sources

- Prusa Knowledge Base: i3 Printer Regular Maintenance; Crash detection and belt status; Testing safety features (MK3/MK3S)
- Prusa blog: FW 3.12 thermal model protection
- Prusa forum threads: heatbed thermistor wire breaking; melted cable at Einsy end; bed preheating error (voltage values)
- Prusa3D GitHub / Printables (open-hardware design files)

## Score line

Not scored on the IQ rubric (na). Compared item by item with the manufacturer's guide (see table).

SCORES: IQ=na/12; scorer=self; blind=no
