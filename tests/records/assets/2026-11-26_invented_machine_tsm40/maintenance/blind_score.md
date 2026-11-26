# Score: Checklists X and Y vs answer key (Sauravi TSM-40)

Scoring standard: rules 1-7 as given. Duty conversion: 1,000-1,400 h/yr; in season 4-7 h/day x 20-26 days, which is about 80-180 h/month (typically 100-130 h). So 250 h is about 2 months of season use, and weekly is about 25-40 h. Interval labels apply only to Caught items. When a checklist has several tasks for one item, the label goes by the task that matches the key's main interval.

## Fairness
All 23 key items are inferable from the spec sheet: each key item's 'spec basis' points to explicit spec text (materials, 'no insulating washers', 'no spindle lock or support', the stated Sorel-bond water sensitivity, 'bushes run dry', the sensor thresholds, and the standby currents). No item is UNFAIR, so the maximum is 46.

## Item-by-item

| Key ID | Item | Fair? | X score | X refs | X interval | Y score | Y refs | Y interval | Note |
|---|---|---|---|---|---|---|---|---|---|
| K01 | PV glass soiling | Yes | 2 | C08 | Accurate | 2 | C13 | Accurate | Both: soft brush/water, AR coating, 10 deg tilt, weekly-ish in dry season. Neither asks for hot-spot/cracked-glass inspection or names flour dust. |
| K02 | PV clamp galvanic corrosion + loosening | Yes | 2 | C35, Do-not 9 | Accurate | 2 | C29 | Accurate | Both inspect for white rust/pitting and retorque quarterly + post-monsoon. X also fits isolating pads (root-cause fix); Y adds frame-bond continuity test instead. |
| K03 | MC4/PV cabling (sensor gap: insulation test) | Yes | 2 | C36, C37, Sec.3 | Accurate | 2 | C30, Sec.3 item 7 | Accurate | Both check latch, heat marks, chafe, ties quarterly. Y explicitly says the insulation test does not show hot MC4s; X frames the gap as wake-up-only/after-breach. Both meet rule 4. |
| K04 | Enclosure condensation + vent clogging | Yes | 2 | C30, C31 | Too often | 2 | C15, C38 | Too often | Both: breathing/no drain/top vent/flour dust, gentle vent cleaning, yearly vent. Both weekly in monsoon, monthly otherwise (key: monthly / 3-monthly). Neither suggests desiccant or relocating vent/adding drain. |
| K05 | LiFePO4 heat ageing (sensor gap: BMS temp) | Yes | 2 | C28, C09, Sec.3 | Accurate | 2 | C27, C01, C14, C39, Sec.3 item 3 | Accurate | Both measure cabinet/outer-cell temps vs cell 8 monthly and shade parking. Y adds yearly capacity test (exactly half key's 6-month frequency, boundary-accurate); X has no capacity tracking. |
| K06 | Cell busbar joints | Yes | 2 | C26, Do-not 7 | Too often | 2 | C26, Do-not | Accurate | Both: Al creep, no spring washers, vibration, torque to cell maker, IR under load. X retorque monthly (key quarterly); Y 50 h then quarterly + rough tows. |
| K07 | Battery parasitic drain in storage | Yes | 2 | C33, Do-not 8 | Accurate | 2 | C44, C45 | Accurate | Both: partial SOC, open isolator, check/recharge every 4 weeks; both note the 12 mA BMS draw continues. X 60-70% SOC vs key 50-60% (close). |
| K08 | Motor controller terminals | Yes | 2 | C32 | Accurate | 2 | C28 | Accurate | Both retighten studs and cage terminals, fit ferrules, early first check, then quarterly (2x key frequency, within band). |
| K09 | Motor cable flex fatigue at swinging plate | Yes | 2 | C19 | Too often | 2 | C20, Do-not (loop) | Accurate | Both identify gland-exit fatigue and Hall cores failing first. X monthly (key 3-monthly); Y 250 h + each tow. Neither adds strain relief. |
| K10 | Motor TEFC cooling path | Yes | 2 | C10 | Accurate | 2 | C06 | Accurate | Both clean cowl/fins weekly, daily in heavy dust. X also checks fan for cracks. |
| K11 | Motor pivot pin/bushes | Yes | 2 | C18, Do-not 6 | Accurate | 2 | C12, C19, Do-not | Accurate | Both: light oil not grease, free-swing check. Y oils every 250 h (~half key frequency, boundary) with a weekly free-swing check and play check. |
| K12 | Poly-V belt (sensor gap: speed trip) | Yes | 2 | C07, C16, Sec.3 | Too often | 2 | C07, C12, C17, C37, C33, Sec.3 item 2 | Too rare | Both compare rpm to 440 each use and recognise the 250 rpm gap; replace at END. X rib inspection weekly (~25-40 h, key 100 h); Y rib inspection every 250 h (pointer weekly). Y adds alignment check. |
| K13 | Pulley set screw/key + taper-lock | Yes | 2 | C17 | Accurate | 2 | C18 | Accurate | Both check set screw, key, taper-lock. Y has early 20-50 h re-check and post-tow; X monthly, no run-in check. Neither mentions thread-locker. |
| K14 | Lower 30208 bearing grease/seals/preload | Yes | 2 | C11, C12, Do-not 4 | Accurate | 2 | C16, C32, C34, Do-not | Accurate | Both: measured 2-3 g H1 every 250 h, never pump to resistance, check play, reset locknut. X play check monthly (more often than key 500 h); Y adds yearly reseal/repack. |
| K15 | Upper bearing outer-ring creep in Al housing | Yes | 2 | C13 | Too often | 2 | C32, C35 | Accurate | Both state the Al/steel expansion creep mechanism and inspect the bore. Y dial-indicator check every 500 h matches key; X periodic check is monthly hand/IR feel, bore checked at stones-off service. Neither suggests retaining compound/sleeve. |
| K16 | Spindle bearing false brinelling in towing | Yes | 1 | C12, C45, Do-not 11-12 | n/a | 1 | C42, C43, Do-not | n/a | Both name false brinelling and do a post-tow hand-turn check; X adds moderate speed. Neither unloads/supports the runner stone before towing (the key preventive action), so Partly for both. |
| K17 | Millstone glazing/furrows/thickness | Yes | 2 | C21, C04 | Accurate | 2 | C21, C07 | Too rare | Both measure furrows and thickness vs 30 mm groove and dress/replace as pair. X monthly (~100-130 h) with dressing 300-600 h; Y every 250 h (key inspect 100 h). |
| K18 | Feed agitator cam + spring finger | Yes | 2 | C14 | Too often | 2 | C04 | Too often | Both compute ~2,600 flexes/min, note finger falls below the magnet. Both inspect daily/each use (key 100 h). |
| K19 | Hopper magnet | Yes | 2 | C01 | Accurate | 2 | C03 | Accurate | Both clean each use. |
| K20 | Chamber/sweeper/chute hygiene | Yes | 2 | C02, C24, C34 | Accurate | 2 | C05, C24, C44 | Accurate | Both dry-clean daily, inspect sweepers, clean before storage. |
| K21 | TRAP: lubricating UHMW-PE spout bushes | Yes | 1 | C15 (notes they run dry) | n/a | 2 | Do-not (UHMW-PE bushes/cam), C23 | Too rare | Y explicitly warns against lubricating them (abrasive paste, food path). X only notes they run dry; no warning, so not Caught per rule 3. Y bush inspection 250 h vs key 100 h. |
| K22 | TRAP: washing stones/chamber with water | Yes | 2 | Do-not 1, C02 | Accurate | 2 | Do-not 1, C05 | Accurate | Both explicit, citing the Sorel bond. |
| K23 | Protection function tests | Yes | 2 | C05, C06 | Too often | 1 | C11, C10, C07 | n/a | X tests E-stop, hopper 60 s stop, and NTC/rpm plausibility. Y tests E-stop and checks readings but only cleans the hopper sensor; no functional test of the 60 s stop, so Partly. |

## Totals

| Metric | X | Y |
|---|---|---|
| Points (max 46) | 44 | 44 |
| Caught / Partly / Missed | 21 / 2 / 0 | 21 / 2 / 0 |
| Traps caught (of 2) | 1 | 2 |
| Sensor-gap items caught (of 3: K03, K05, K12) | 3 | 3 |
| Intervals: Accurate / Too often / Too rare | 14 / 7 / 0 | 16 / 2 / 3 |
| Harmful advice | 0 | 0 |

## Harmful advice

None found in either checklist that would damage the machine or be unsafe. Concerns noted but not counted:
- X C11 converts 250 h to 'about every 2 to 3 weeks in season'. At this duty cycle 250 h is about 2 months. An owner who follows the calendar figure would grease about 3x as often, and the bearing has no relief port, so over-filling becomes a risk. The hour figure is correct and X's Do-not 4 warns against over-greasing, so this is an error rather than harmful advice. (Y's '250 h is roughly one month' is also optimistic, but it errs much less.)
- X Do-not 9 says to open the isolator before unplugging MC4s. That does remove the load current, but X does not say the array stays live at about 99 V in daylight. Y states this and says to cover the panels. This is incomplete safety advice, not harmful.
- Both grease the gap-screw guide posts with H1 grease (X C23, Y C22). Grease near flour can form paste. It is food-grade and outside the stone path, so it is not counted.

## Valuable extras (not in key)

**X:**
1. C23: free-lift test of the bed-stone relief and check of spring rust/free length (a seized post defeats the 6 mm relief).
2. C27: cell-spread check and periodic full charge to let the 60 mA passive balancer work and reset the coulomb-counted SOC.
3. C37: megger follow-up procedure when the MPPT reports an insulation fault.
4. C40-C43: trailer coupling, tyres (age-based replacement), hub bearings, leaf springs and U-bolts.
5. C22: runner hub nut and Sorel backing/efflorescence check.

**Y:**
1. C42: restrain the motor plate before towing, tagged 'REMOVE BEFORE START', to stop belt/hinge/cable shock loads.
2. C29: panel-frame bonding continuity test (a lost bond hides a frame fault from the MPPT insulation test).
3. C33: belt alignment check across the plate's arc of swing.
4. C34: yearly reseal and repack of the 30208 lower bearing to purge old grease, since there is no relief port.
5. Do-not list: no welding on the trailer with electronics connected, and no rewiring beyond 2 panels in series (MPPT 150 V limit).

## Verdict

No meaningful difference. Both checklists score 44/46 with 21 Caught, 2 Partly and 0 Missed, and both catch all 3 sensor-gap items. Neither contains harmful advice. Y is ahead on the traps (2/2 vs 1/2: only Y warns against lubricating the dry-running UHMW-PE feed bushes). Y's intervals are also closer to the key (16 Accurate vs 14). Y adds a pre-tow motor-plate restraint, a frame-bond continuity test and a yearly reseal of the lower bearing. X never sets an interval too rare (0 vs 3: Y's belt rib, stone and spout-bush inspections at 250 h are too rare). X also functionally tests the hopper sensor and fits isolating pads at the PV clamps. Its errors are all on the side of checking too often (7 items), plus a wrong hours-to-calendar conversion for greasing. An owner would be well served by either; these trade-offs roughly cancel out.