# Answer Key — Sauravi TSM-40 Towable Solar Stone Mill

1. **K01 — PV panel front glass (soiling)**
   - Mechanism: dry-season mineral dust and flour dust from the mill below settle on the panels. The 10° tilt is too shallow for wind or light rain to clear them. Soiling cuts PV output and charge, and uneven soiling can make cells run hot. Abrasive cleaning wears off the anti-reflective coating.
   - Action: clean with water and a soft brush or sponge, no abrasives. Look for cracked glass or hot-spot browning.
   - Interval: weekly in the dry season, plus after dust storms or long grinding runs; monthly otherwise.
   - Spec basis: 10° fixed tilt, AR-coated glass, canopy directly over the mill, dusty climate.

2. **K02 — Panel clamp points (galvanic corrosion + vibration loosening)**
   - Mechanism: anodized aluminium frames, A2 stainless clamps and bolts, and galvanized steel rails touch with no isolation. When monsoon moisture forms an electrolyte, the zinc and aluminium (both anodic to stainless) corrode at the contact points. You see white rust or pitting. Clamp preload drops, and towing vibration loosens the clamps further.
   - Action: inspect each clamp for white or powdery corrosion and pitting, retorque to spec, and fit EPDM/nylon isolating pads or washers. Apply a corrosion-inhibiting compound at the contacts.
   - Interval: every 3 months, after the monsoon, and after every 4–5 tows.
   - Spec basis: material list in Section 4, "no insulating washers", towing, monsoon humidity.

3. **K03 — MC4 connectors and PV cabling (sensor gap: insulation monitor)**
   - Mechanism: towing vibration, cable-tie wear and UV loosen or degrade the MC4 joints and chafe cable on canopy edges. A loose or corroded connector becomes a high-resistance joint that heats and can arc. The MPPT's insulation-resistance test only catches leakage to the frame once insulation is breached. It cannot see series resistance, a part-seated connector or early chafing.
   - Action: visually and by hand check every MC4 for full engagement, discoloration or melting. Check cable ties and look for chafing where cable crosses steel edges. An IR thermometer check under load is a bonus. Replace UV-brittle ties.
   - Interval: every 3 months and after every tow.
   - Spec basis: MC4s on a towed canopy, nylon ties, an insulation test that only measures resistance to frame.

4. **K04 — Electrical enclosure (condensation and vent clogging)**
   - Mechanism: in the monsoon, daily heating and cooling makes the sealed IP65 box "breathe" humid air through the ePTFE vent and past the gasket. That moisture condenses on cool nights and pools, because there is no drain. It corrodes terminals and boards. Flour dust from the grinding head next to the box also blinds the vent membrane. A blinded membrane lets pressure differentials build, which stresses the gasket and pulls moist air in past it instead.
   - Action: open the box and check for moisture, corrosion or tide marks. Place a desiccant pack. Clean the vent gently from outside (dry soft brush, no compressed air into the membrane) or replace it. Inspect the gasket. Consider moving the vent to the bottom face or adding a drain/breather.
   - Interval: monthly in the monsoon; every 3 months otherwise; replace the vent yearly.
   - Spec basis: IP65 polycarbonate, top-face ePTFE vent, no drain, mounted beside the grinding head, 100% RH.

5. **K05 — LiFePO4 capacity loss from heat (sensor gap: BMS temperature)**
   - Mechanism: a dark steel cabinet in the sun with passive vents only can sit at 40–50 °C for hours. Calendar ageing of LiFePO4 roughly doubles for every 10 °C or so above 25 °C, and worst at high SOC. The BMS only acts at 55/60 °C, so heat inside the normal range is not flagged. Its single sensor sits on the centre cell, so a hotter cell by the sunlit wall goes unseen.
   - Action: measure cabinet and cell surface temperatures on a hot afternoon. Track usable capacity (full-to-cutoff Ah, or hours of milling per full charge). Improve shading or paint the cabinet light, keep the vents clear, and avoid parking with the cabinet in the sun. Check the cell-voltage spread for weak cells.
   - Interval: temperature check monthly in the hot season; capacity check every 6 months.
   - Spec basis: dark cabinet partly outside the canopy shadow, no fan, one cell NTC, 46 °C ambient, 0–55 °C charge window.

6. **K06 — Cell busbar connections (thermal cycling + vibration + dissimilar metals)**
   - Mechanism: aluminium studs, nickel-plated copper busbars and zinc-plated steel nuts carry 45–55 A while milling. Aluminium creeps under bolt load. Daily thermal cycling and towing vibration then shed preload, and there are no spring washers to make up for it. Contact resistance rises, which heats the joint, which loosens it further. In humidity, galvanic attack hits the aluminium.
   - Action: isolate the battery. Check and retorque the busbar nuts to the cell maker's torque, and look for discoloration or corrosion. Under load, compare cell voltages or check joint temperatures. Clean and apply contact paste if needed.
   - Interval: every 3 months and after the first 50 h; also after rough towing.
   - Spec basis: Section 5 materials, no Belleville washers, transport, high continuous current.

7. **K07 — Battery during idle storage (parasitic drain)**
   - Mechanism: with the isolator closed, the 45 mA standby draw is about 7.5 Ah over 7 weeks. If PV charging can't keep up, or the isolator is open (BMS still draws 12 mA, about 2 Ah per week, with no charging), a pack left at low SOC can drop below the 2.60 V cutoff. Over-discharged cells may be damaged or refuse to charge. Storing at 100% SOC in the heat speeds up ageing.
   - Action: before storage, set about 50–60% SOC. Either keep the isolator closed with clean panels so PV maintains the pack, or open it and recharge every 4–6 weeks. Check SOC monthly.
   - Interval: before storage, and monthly during storage.
   - Spec basis: 45 mA / 12 mA draws, 6–12 week storage, isolator stops charging.

8. **K08 — Motor controller terminals (thermal-cycling loosening)**
   - Mechanism: the M6 brass stud nuts carry 55 A, and brass and copper expand more than the steel nut, so thermal cycling loosens them. Bare stranded wire in rising-cage terminals with no ferrules cold-flows and frays strands, and vibration works these joints loose. A loose power stud overheats. A loose Hall or thermistor wire causes intermittent stall trips or loss of thermal protection.
   - Action: isolate, then retorque the power stud nuts and check lugs for discoloration. Tug-test and retighten signal terminals, and fit ferrules.
   - Interval: after the first 50 h, then every 6 months and after rough towing.
   - Spec basis: Section 6 terminal details, "no ferrules fitted", high current, towing.

9. **K09 — Motor phase/Hall cable at the swinging motor (flex fatigue)**
   - Mechanism: the motor plate moves with belt vibration and swings up to 16° over the belt's life. The 300 mm unsupported cable flexes every run, plus towing bounce. The worst point is the rigid nylon gland exit, where strands fatigue and break. Fine 0.5 mm² Hall cores fail first and give intermittent commutation faults. The jacket can also crack.
   - Action: inspect the cable at the gland and the P-clip for jacket cracks, stiffness or kinking. Flex it by hand while watching for Hall faults. Add a strain-relief or bend-limiting gland and make sure there is a gentle service loop. Replace the cable if damaged.
   - Interval: every 3 months.
   - Spec basis: Section 7 pivot description, unsupported free length, fine Hall cores.

10. **K10 — Motor cooling path (dust clogging)**
    - Mechanism: flour and mineral dust pack the fan intake grille and the frame fins under the cowl. Flour is also combustible and holds moisture. Clogging cuts cooling. The winding NTC protects the winding, but it does so by derating: output and throughput fall, and the 6205 motor bearings and magnets run hotter than intended.
    - Action: dry-brush or vacuum the cowl intake and fins (low-pressure air from outside only), and check the fan for cracks.
    - Interval: weekly in use, or daily in heavy dust.
    - Spec basis: TEFC with external fan/cowl, finned frame, mounted beside the mill head.

11. **K11 — Motor pivot pin and bushes**
    - Mechanism: dust gets into the sintered bronze bushes and the oil dries out in the heat. The pivot stiffens or binds, so the motor's weight no longer sets belt tension: the belt slips, glazes and overheats. Worn bushes let the motor rock and misalign the belt.
    - Action: check that the plate swings freely by hand, belt off. Add a few drops of light oil and wipe off the excess, since grease would collect dust. Check for play and replace bushes when worn.
    - Interval: monthly.
    - Spec basis: gravity tensioning, oil-impregnated sintered bushes, dusty site.

12. **K12 — Poly-V belt (wear, stretch, slip; sensor gap: stone speed trip)**
    - Mechanism: heat and ozone age the EPDM, causing rib cracking. Dust abrades the ribs, the belt stretches, and glazing builds up from slip at start under load. Slip of 5–15% lowers throughput and heats the belt, but the speed sensor only trips below 250 rpm (about 43% slip). Moderate slip goes unalarmed unless someone compares stone rpm with 440.
    - Action: inspect the ribs for cracks, glazing, missing chunks or debris. Check the pointer on the NEW–END scale. Check pulley alignment and grooves. Compare the displayed stone rpm with 440 under load. Replace at END or on damage. Keep it free of oil.
    - Interval: inspect every 100 h; expect replacement at about 1,500–2,500 h.
    - Spec basis: EPDM poly-V, gravity tension pointer, speed sensor trip threshold, nominal 440 rpm.

13. **K13 — Motor pulley key/set screw and stone pulley taper-lock (fretting/loosening)**
    - Mechanism: a single set screw over a key on a plain-bore pulley lets micro-movement happen under cyclic belt load and torque pulses at start. The key and bore fret (red-brown "cocoa" oxide), the key wallows and the pulley walks or loosens. Taper-lock grub screws can also lose preload.
    - Action: check the set screw and taper-lock grub screws for tightness (thread-locker on the set screw). Look for fretting oxide and axial pulley movement, and check pulley alignment.
    - Interval: after the first 25 h, then every 250 h.
    - Spec basis: Section 7 pulley mounting details.

14. **K14 — Lower 30208 tapered roller bearing (grease, seals, preload)**
    - Mechanism: this bearing carries 38 kg plus spring-loaded grinding thrust. Dust gets past the lip seals and grease degrades in the heat. With no relief port, over-greasing can blow out the seals or churn and overheat the bearing. Preload drifts as the bearing wears, giving axial play and noise. No bearing temperature or vibration sensor exists.
    - Action: wipe the nipple, then add a small measured shot of H1 NLGI 2 grease. Do not pump until it resists. Check axial play and listen for noise. Inspect the seals and reset the locknut preload as needed.
    - Interval: grease every 250 h; check play every 500 h.
    - Spec basis: grease nipple, no relief port, H1 grease spec, tapered roller with locknut preload, no bearing sensing.

15. **K15 — Upper bearing in aluminium housing (outer-ring creep/fretting)**
    - Mechanism: aluminium expands about twice as much as steel. As the housing warms, the H7 fit loosens and the outer ring creeps and frets in the bore. Black/red oxide forms, the bore wears oversize and the spindle runs out, so stones run non-parallel and flour gets uneven. The inner ring press fit can also fret.
    - Action: during stone access, check spindle radial play and runout with a dial indicator. When the bearing is replaced, look for fretting marks or a polished bore. Use a bearing retaining compound, or sleeve the housing if the bore is worn.
    - Interval: check runout every 500 h; inspect the bore at bearing change.
    - Spec basis: cast aluminium housing, H7 bore, steel bearing, sealed bearing near heat and dust.

16. **K16 — Spindle bearings during towing (false brinelling)**
    - Mechanism: the 38 kg runner stays on the spindle with no support, so road vibration with the bearings stationary makes rolling elements oscillate in place. That wears grease out of the contact and leaves brinell-like marks on the raceways. It shows up as noise and roughness that appears soon after transport.
    - Action: before towing, take the stone's weight off the spindle (block or support the runner, or tighten the bed stone down onto shims in a controlled way). Turn the spindle by hand after transport and listen for roughness. Tow at moderate speed on rough roads.
    - Interval: each tow.
    - Spec basis: "no spindle lock or support", towing 1–4 times a month, leaf springs.

17. **K17 — Millstones (glazing, furrow wear, thickness)**
    - Mechanism: abrasion wears down the 3 mm furrows and glazes the faces, especially if the stones run with little grain between them. Output then falls, flour temperature rises and fineness changes. The stones also lose thickness.
    - Action: monitor throughput and flour temperature. Lift the lid and inspect the faces and furrow depth. Dress the stones (re-cut the furrows, roughen glazed faces) with a suitable dressing tool. Check thickness against the 30 mm groove and replace the pair at the limit.
    - Interval: inspect every 100 h; dress about every 300–500 h; thickness check at each dressing.
    - Spec basis: 3 mm furrows, 30 mm minimum mark, flour temperature display/trip.

18. **K18 — Feed agitator (UHMW cam and spring finger)**
    - Mechanism: at 440 rpm × 6 lobes, the finger flexes about 2,640 times a minute, roughly 160k per hour. The cam lobes wear flat and the finger can fatigue and break, causing feed to stop or bridge. A broken finger also drops a metal fragment toward the stones.
    - Action: inspect cam lobe height and the finger for cracks or set, and replace both as needed.
    - Interval: every 100 h.
    - Spec basis: Section 8 feed description.

19. **K19 — Hopper magnet (tramp iron)**
    - Mechanism: collected iron (nails, wire, a broken agitator finger) builds up and eventually washes into the stones. That chips the stones or lifts the bed and damages the springs.
    - Action: wipe the magnet clean.
    - Interval: each use (daily).
    - Spec basis: plate magnet in the hopper throat, village grain with tramp metal, 6 mm relief springs.

20. **K20 — Grinding chamber, sweepers, chute (hygiene and residue)**
    - Mechanism: flour residue in the drum, chute and spout absorbs monsoon humidity. It cakes, goes mouldy, attracts weevils and rodents, and can block the outlet. The sweeper rubber tips wear.
    - Action: dry-clean with a brush or vacuum after each day's milling, and run a small amount of clean grain to purge between customers if needed. Inspect the sweeper tips and replace when worn. Fully dry-clean before storage.
    - Interval: each use; before storage.
    - Spec basis: stainless drum with lid, sweeper blades, monsoon humidity, food product.

21. **K21 — TRAP: greasing or oiling the UHMW-PE feed-spout bushes**
    - Why it harms: the bushes are designed to run dry, and UHMW-PE is self-lubricating. Grease in the grain stream catches flour and dust, forming an abrasive, sticky paste that binds the spout and stops agitation. It also contaminates food with a non-food lubricant and attracts insects.
    - Correct action: keep dry, brush clean, and replace the bushes when worn.
    - Interval: inspect every 100 h along with K18.
    - Spec basis: "bushes run dry and sit directly in the grain stream".

22. **K22 — TRAP: washing the millstones or chamber with water**
    - Why it harms: the magnesium oxychloride (Sorel) bond is non-hydraulic and softens or leaches in liquid water. The grit then loosens, the face crumbles and the stone can crack. Wet residue also cakes and turns mouldy in the chamber.
    - Correct action: clean only dry (brush or vacuum). If the stones get wet, dry them thoroughly before use.
    - Interval: every cleaning.
    - Spec basis: stated stone bond and its water sensitivity, 14% grain moisture limit.

23. **K23 — Protection function tests (E-stop, hopper sensor, trips)**
    - Mechanism: flour dust coats the capacitive level sensor face, which can fool it into reading grain. Mushroom buttons and contacts can stick or corrode in humidity. A silently failed protection is only found when it is needed.
    - Action: test the E-stop (it must stop the mill and latch) and the hopper sensor's 60 s stop with the hopper emptied. Clean the sensor face. Confirm the flour NTC and stone-rpm readings are plausible.
    - Interval: monthly, and after transport or long storage.
    - Spec basis: Section 9 protections, capacitive sensor in a dusty hopper, humid climate.