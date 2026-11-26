# Sauravi TSM-40 Towable Solar Stone Mill — Owner's Specification Sheet

## 1. Purpose

The TSM-40 is a trailer-mounted flour mill for grinding dry cereals and pulses. It is towed between villages and runs without grid power from an on-board photovoltaic array and battery.

## 2. Duty Cycle and Operating Environment

- Typical use: 4–7 h/day, 20–26 days/month in post-harvest seasons; about 1,000–1,400 h/year.
- Throughput: 40–60 kg/h (maize, medium-fine setting).
- Grain input: moisture 14% wet basis or lower.
- Design ambient: 10–46 °C; RH 20–100%; mineral dust in the dry season, sustained rain and humidity in the monsoon. Sunlit deck surfaces can exceed 55 °C.
- Transport: towed up to 40 km/h on paved and unpaved roads, typically 1–4 times per month.
- Storage: may be parked unused 6–12 weeks between seasons.

## 3. Overall Layout

A single-axle hot-dip galvanized trailer (leaf springs, 13-inch wheels) carries the mill head and drive mid-deck, a battery cabinet at the drawbar end, an electrical enclosure on the mill frame, and a fixed galvanized canopy carrying the PV array and shading the mill. Mass approximately 640 kg.

## 4. Photovoltaic Array

- 4 × 410 W monocrystalline panels, glass-backsheet, anti-reflective coated front glass, anodized aluminium frames. Wired 2-series × 2-parallel; array open-circuit voltage approximately 99 V.
- Panels are clamped to hot-dip galvanized steel C-section rails with A2 stainless steel mid- and end-clamps, M8 A2 stainless bolts and serrated stainless flange nuts. No insulating washers or pads are fitted between the aluminium frames, the stainless clamps and the galvanized rails.
- Canopy tilt fixed at 10° toward the drawbar.
- Panel interconnection: factory MC4-type connectors on 4 mm² solar cable. Homerun: 6 mm² double-insulated solar cable, fixed to the canopy legs with UV-stabilized nylon cable ties, entering the electrical enclosure through a cable gland.

## 5. Battery System

- Chemistry: lithium iron phosphate (LiFePO4), 16 prismatic cells, 3.2 V 105 Ah each, configured 16S1P: 51.2 V nominal, 5.4 kWh.
- Cell terminals: aluminium threaded studs, M6. Cells are joined by nickel-plated copper busbars, retained with plain steel zinc-plated flange nuts. No spring or Belleville washers.
- Battery management system (BMS), mounted inside the cabinet:
  - measures each of the 16 cell voltages;
  - measures pack current with a shunt;
  - one NTC temperature sensor bonded to the side of cell 8 (centre of the pack) and one NTC on the BMS MOSFET heatsink;
  - charge permitted 0–55 °C cell temperature; discharge permitted −20 to 60 °C;
  - over-voltage cutoff 3.65 V per cell, under-voltage cutoff 2.60 V per cell;
  - passive cell balancing, 60 mA, active above 3.40 V per cell;
  - state of charge by coulomb counting;
  - standby self-consumption 12 mA.
- Battery cabinet: 1.5 mm powder-coated steel, dark green, at the drawbar end, partly outside the canopy shadow morning and evening. Passive ventilation through two louvres (low front, high rear) with washable polyester filter mats. No fan.
- 125 A Class-T fuse; 35 mm² copper cables with crimped lugs.
- 63 A two-pole rotary DC isolator on the cabinet door. With the isolator closed and the mill stopped, the system draws approximately 45 mA from the battery (BMS, controllers on standby, display).

## 6. Electrical Enclosure

- Polycarbonate enclosure, IP65 rated, with neoprene door gasket. Mounted vertically on the mill frame 1.1 m above the deck, beside the grinding head.
- One ePTFE membrane pressure-equalisation vent (M12), fitted in the enclosure's top face. No drain.
- Contents:
  - **MPPT solar charge controller**, 48 V, 60 A, 150 V maximum PV input. Measures PV voltage and current, battery voltage, and its own heatsink temperature. Performs a PV array insulation-resistance test at each morning wake-up and refuses to start charging if insulation resistance from either PV conductor to the frame is below 100 kΩ. Communicates with the BMS over CAN.
  - **BLDC motor controller**, 48 V, 70 A peak, 55 A continuous, sensored (Hall) commutation. Power connections: M6 brass studs with nuts for battery positive/negative and for the three motor phases (crimped lugs). Signal connections (Hall sensors, motor thermistor, start/stop, speed sensor, hopper sensor, flour thermistor): rising-cage screw terminal blocks, 0.5–1.5 mm² conductors, no ferrules fitted.
  - Two 15 A gPV string fuses, earth bar.
- Door panel: display, START/STOP buttons, latching emergency-stop, fault LED.

## 7. Drive Motor and Belt

- Motor: 48 V, 2.2 kW (S1), 2,800 rpm, brushless DC, inner rotor, IP54, totally enclosed fan-cooled (TEFC): external shaft-mounted plastic fan under a steel cowl blowing axially across a finned aluminium frame. Rotor bearings: 6205-2RS sealed. Embedded NTC winding thermistor.
- Motor shaft: 24 mm with 8 mm parallel key. Motor pulley: steel, plain bore, 63 mm pitch diameter, keyed and secured by one M8 set screw over the key.
- Motor mounting (gravity tensioning): the motor is bolted to a steel plate that hinges on a 20 mm hardened steel pin through two oil-impregnated sintered bronze bushes. The weight of the motor and plate hangs on the belt and sets its tension; no tensioning screw is fitted. As the belt lengthens, the plate swings downward; a painted pointer on the plate moves along a scale marked "NEW" and "END" welded to the frame. Plate swing range approximately 16°.
- Motor phase cable: 3 × 6 mm² plus 6-core 0.5 mm² Hall/thermistor cable, H07RN-F rubber-sheathed, leaving the motor terminal box through a nylon cable gland. Free, unsupported length of 300 mm between the gland on the swinging motor and a fixed P-clip on the frame.
- Belt: poly-V, PJ section, 10 ribs, EPDM compound, 1,600 mm effective length. Belt runs dry, over unlubricated pulley grooves.
- Driven (stone) pulley: cast iron, 400 mm pitch diameter, on a taper-lock bush (two grub screws) on the spindle. Ratio 6.35:1; nominal stone speed 440 rpm.

## 8. Mill Head

- **Arrangement:** vertical-axis stone mill. The lower ("runner") stone rotates. The upper ("bed") stone is stationary and moves vertically to set the grinding gap.
- **Stones:** 400 mm diameter, 60 mm thick when new. Composition: fused corundum and flint grit in a magnesium oxychloride (Sorel cement) bond. This bond is non-hydraulic: it softens and leaches under prolonged contact with liquid water. Grinding faces have 12 cast-in radial furrows, 3 mm deep when new. Minimum usable thickness 30 mm, marked by a groove around the stone edge. Each stone is set in a steel ring with a filled cement backing. Runner stone with ring and hub: 38 kg.
- **Spindle:** 40 mm, carbon steel (C45), vertical. Runner stone hub fixed to its upper end with a taper and central nut.
- **Upper spindle bearing:** 6208-2RS deep-groove ball bearing, sealed and grease-filled for life. Inner ring press fit (k5) on the spindle. Outer ring in a cast aluminium alloy housing, H7 bore, retained axially by a circlip. Located 150 mm below the stone face, inside the dust zone below the grinding chamber.
- **Lower spindle bearing:** 30208 tapered roller bearing (carries the runner stone weight plus downward grinding thrust) in a cast iron housing with double nitrile lip seals and one grease nipple. No grease relief port. Preload set by a locknut and tab washer. Factory fill: NSF H1 food-grade lithium-complex grease, NLGI 2.
- **Gap adjustment:** the bed stone frame is carried on three guide posts and pulled down toward the runner by a central M24 trapezoidal-thread screw with a handwheel and graduated dial (0.05 mm per division). Three steel compression springs (zinc-plated) under the guide-post nuts allow the bed stone to lift up to 6 mm if a hard object passes through.
- **Stone housing:** 304 stainless steel drum around the stones, with a hinged lid (two over-centre latches) for access. Flour is swept by two rubber-tipped sweeper blades on the runner rim to a tangential outlet into a 304 stainless chute.
- **Hopper and feed:** 45 litre food-grade HDPE hopper with a slide gate. A neodymium plate magnet sits across the hopper throat. Grain falls through a 304 stainless feed spout into the eye of the bed stone. The feed spout swings on a 10 mm stainless steel pin in two UHMW-PE bushes; the bushes run dry and sit directly in the grain stream. The spout is shaken by a spring-steel wire finger riding on a six-lobed UHMW-PE cam on the runner-stone hub nut.
- **Frame:** welded mild steel, painted, bolted to the deck on rubber mounts.

## 9. Sensors, Indicators and Protections

| Device | What it measures / does |
|---|---|
| Motor winding NTC | Winding temperature; controller derates current above 110 °C, stops at 130 °C |
| Motor controller | Phase current (limit 55 A continuous, 70 A for 10 s), bus voltage, own heatsink temperature; stall trip if no Hall transitions for 2 s after a start command |
| Stone speed sensor | Inductive proximity sensor reading four bolt heads on the stone pulley; shows stone rpm on display; trips the motor if stone speed is below 250 rpm for 5 s while the motor is commanded on |
| Hopper level sensor | Capacitive sensor 60 mm above the hopper throat; stops the motor 60 s after grain falls below it |
| Flour temperature | NTC in the outlet chute; value shown on display; trips motor at 55 °C |
| BMS | Cell voltages, pack current, one cell temperature, MOSFET temperature; disconnects pack outside limits in Section 5 |
| MPPT controller | PV insulation resistance at wake-up; PV/battery voltage and current; heatsink temperature |
| Emergency stop | Latching mushroom button, removes controller enable |
| Display | SOC, battery voltage, PV power, motor current, stone rpm, flour temperature, operating hours, fault codes |

No temperature or vibration sensing is fitted to the spindle bearings, the belt, the battery cabinet air, or the electrical enclosure interior.

## 10. Consumable and Replaceable Parts

Belt; stones (matched pair); spindle and motor bearings; lip seals; sweeper tips; UHMW-PE bushes and cam; agitator finger; ePTFE vent; filter mats; pivot bushes; fuses; panel clamps; individual LiFePO4 cells.

## 11. Controls and Operation

Close the isolator, set the gap with the handwheel, fill the hopper, open the gate, press START (4 s soft-start ramp). STOP or the hopper sensor ends the run. Charging is automatic when PV is available and the isolator is closed; with it open, the battery is disconnected from both controllers and charging stops.