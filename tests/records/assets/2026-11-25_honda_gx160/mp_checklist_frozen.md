# GX160 — Memory Prism checklist, frozen BEFORE reading Honda's schedule

Design facts used (from spec sheets only): air-cooled 4-stroke OHV single, cylinder inclined 25°, cast-iron sleeve; forced-air cooling by flywheel fan over fins; splash lubrication (no pump, no oil filter), ~0.6 L oil; Oil Alert low-level shutdown; transistorized magneto + spark plug; butterfly carburetor with fuel strainer; dual-element air cleaner; mechanical centrifugal governor; recoil starter; ~3 L fuel tank, unleaded / E10; optional spark arrester. No hour meter as standard.

Contamination note: I have general training knowledge of small-engine maintenance, so this is not a fully blind derivation. I have not opened the GX160 owner's manual or any maintenance page in this session.

## MP map
- Board: outdoor, dusty, hot (pumps, generators, tillers); intermittent use; long seasonal storage; often operated by non-specialists.
- Flows: intake air (filter → carb → cylinder); cooling air (fan → fins); fuel (tank → strainer → float bowl → jet); oil (splashed, no filter); spark (magneto → lead → plug); exhaust (muffler → arrester); motion (crank, governor linkage, recoil rope).
- Accumulation: dust in air filter; debris on fins/fan screen; carbon on plug, chamber, valves, arrester screen; sediment/water/varnish in tank, strainer, carb bowl; metal and soot in oil (oil change is the ONLY removal path — no filter); valve-clearance drift from wear.
- Ledger: small oil volume that lubricates AND cools, oxidises with heat; petrol degrades in storage (E10 takes up water); plug electrode erodes; filter holding capacity; rubber fuel line ages; recoil rope frays.
- Working Lines: heat path through fins (blockage → overheating); vibration path → fasteners loosen; fuel line (crack → leak/fire); governor linkage (sticky → hunting/overspeed).
- Translators: Oil Alert reads LEVEL only, not quality; human senses (sound, smoke colour, hard starting, oil colour, plug colour). Nothing reads: oil quality, filter clogging, valve clearance, fin blockage, fuel age, RUN HOURS (no meter).
- Audits: Oil Alert (detect low level → stop). Governor is a control loop holding speed, not an audit of engine health.
- Constraints: oil level band (check on level ground because cylinder is inclined); oil grade; fuel octane/ethanol limit; plug gap; valve clearance spec; max rpm.
- Lag: oil degradation, valve drift and fuel varnish are invisible until starting/running problems appear.
- No Sacred States: break-in — a new engine sheds metal early, so the first oil change should come early.

## Derived checklist (my intervals, from reasoning)
| ID | Task | When (MP estimate) | MP reason |
|---|---|---|---|
| M01 | Oil level on dipstick, engine level | Each use | Ledger; Oil Alert only catches low level |
| M02 | Air filter visual | Each use | Accumulation, dusty board |
| M03 | Air filter clean | ~25 h (sooner if dusty) | Accumulation |
| M04 | Air filter paper element replace | ~100–200 h or damaged | Ledger: holding capacity |
| M05 | Fuel level, leaks, fuel line cracks | Each use | Working line: fire risk |
| M06 | Cooling fins and fan screen clear | Each use | Working line: heat path |
| M07 | First oil change | ~5–10 h | No Sacred States: break-in particles |
| M08 | Oil change | ~50 h | No filter, small hot oil volume |
| M09 | Spark plug inspect, clean, gap | ~50–100 h | Accumulation (carbon), translator (plug colour) |
| M10 | Spark plug replace | ~200–300 h or yearly | Ledger: electrode erosion |
| M11 | Spark arrester screen clean (if fitted) | ~100 h | Accumulation |
| M12 | Fuel strainer / carb bowl sediment | ~100 h or each season | Accumulation |
| M13 | Storage: drain or stabilise fuel if idle >30 days | Before storage | Ledger: fuel degrades |
| M14 | Valve clearance check/adjust | ~300 h | Accumulation of wear; lag |
| M15 | Combustion chamber decarbon | ~500 h | Accumulation |
| M16 | Fasteners (mount, muffler, shroud) | ~50 h | Working line: vibration |
| M17 | Fuel line replace | ~2 years | Ledger: rubber ages |
| M18 | Recoil rope / starter check | ~100 h | Ledger: rope wear |
| M19 | Governor linkage free, no hunting | ~100 h | Working line |
| M20 | Oil Alert wire/connector check | ~100 h | Audit must itself be checked |
| M21 | Idle speed adjust | As needed / ~300 h | Constraint |
| M22 | Fit an hour meter or log run time | Once | Translator gap: no way to schedule by hours otherwise |
| M23 | Oil condition (colour, milky = water) | Each oil check | Translator for what Oil Alert can't read |
| M24 | Storage prep: fresh oil, cover, dry place | Before storage | Ledger: old oil is acidic in storage (inference) |
