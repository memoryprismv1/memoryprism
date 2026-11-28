# Wheel Design Structural Tests — 2026-11-28

**Test collection:** MP-WHEELS-2026-11-28  
**Run type:** Assistant-led, user-directed exploratory case analysis with later show-and-tell validation  
**Conditions:** Two batches; structural analysis followed by selected historical/source checks  
**Context:** Same conversation · **Scorer:** none · **Blind:** no · **Execution:** desk analysis and source review; no physical tests  
**Purpose:** Examine whether MP can identify useful constraints, dependencies, operating-envelope limits and plausible failure modes across different wheel/vehicle architectures.

## Method and evidence boundary

The assistant selected cases and performed the initial structural inquiry. The user asked for a harder second batch and then requested the historical reveals ("show and tell"). The second batch was therefore not a blind prospective test: the designs were assessed before their identities and outcomes were discussed, but the subsequent validation was retrospective and conducted in the same conversational context.

The first batch is recorded as structural analysis, not as source-verified historical findings. The second batch includes source checks for selected historical cases. This collection is an exploratory record of MP use, not a controlled comparison against an unassisted baseline and not evidence that MP predicts design success or failure.

## Batch 1 — initial structural analysis

| Design | Structural observations |
|---|---|
| Spoked bicycle wheel | Tensioned spokes distribute load around a rim; spoke tension, rim stiffness, geometry and maintenance interact. A wheel is not simply a set of spokes independently carrying compression. |
| Michelin Tweel airless wheel | Removes the pneumatic puncture mode, but transfers demands to compliant spokes/web, shear bands and materials. Heat build-up, cyclic fatigue, load and speed become important operating constraints. Specialised success rather than a universal replacement for pneumatic tyres. |
| Mecanum wheel | Angled rollers enable omnidirectional movement through a coupled set of wheel forces. Performance depends on floor surface, roller contact, load distribution and coordinated control; intermittent contact, vibration and slip constrain use. |
| Solid rubber industrial tyre | Eliminates air-loss/puncture failure and can be robust at low speeds, but transmits more shock and can accumulate heat under sustained load or speed. The operating duty cycle matters. |
| Square wheel on an inverted-catenary track | The wheel cannot be evaluated independently of its track. The coupled geometry can produce a smooth ride when the track profile is matched to the wheel; the system-level architecture, not the wheel alone, makes it work. |

These are mechanism-level assessments. No comparative measurements or historical outcome audit was performed for this batch.

## Batch 2 — harder cases and source checks

### A. Penny-farthing (high-wheel bicycle)

**Initial diagnosis:** Large driven wheel increases distance travelled per pedal revolution, but raises the rider's centre of mass and makes a forward fall ("header") consequential. The architecture has a narrow safety envelope on uneven ground and under sudden braking or loss of balance.

**Historical check:** The Science Museum Group describes the large wheel's gearing advantage and the high saddle (over 1.5 m in some designs), and records the safety bicycle's eventual displacement of the ordinary. The safety bicycle combined more accessible geometry with chain drive and similarly sized wheels.

**Assessment:** Strong structural fit. The design's speed/efficiency benefit was coupled to a high consequence of falling and limited accessibility.

Source: Science Museum Group, [Penny Farthing Bicycle](https://collection.sciencemuseumgroup.org.uk/objects/co8421051/penny-farthing-bicycle-bicycle).

### B. Buckminster Fuller's Dymaxion car

**Initial diagnosis:** A three-wheeled vehicle with a single rear steering wheel may offer an exceptionally small turning circle, but rear steering changes the relationship between steering input and vehicle response. Directional stability, crosswind response, steering feedback and tail swing require careful treatment. A manoeuvrability advantage at low speed does not establish safe controllability at road speed.

**Historical check:** The Dymaxion's rear steering did provide extraordinary manoeuvrability. The *BuckyWorks* account describes twitchy handling in gusty crosswinds despite changes to steering cables and rear-wheel swivel geometry; it also notes that a sharp steering input could swing the tail beyond the front wheels' tracks. The car was not developed into a production vehicle. The 1933 fatal crash should not be treated as proof that the steering design caused the accident: contemporary accounts report that the investigation cleared the Dymaxion of responsibility.

**Assessment:** Strong diagnosis of the manoeuvrability/controllability trade-off. The main concern is not simply "three wheels"; it is the combination of rear steering, long body, steering response, aerodynamic forces and ordinary road conditions.

Sources:
- [BuckyWorks: Buckminster Fuller's Ideas for Today](https://www.buckyverse.org/en/buckyworks/buckyworks.pdf).
- [HISTORY: First Dymaxion car produced](https://www.history.com/this-day-in-history/july-12/first-dymaxion-car-produced).
- [The Dymaxion World of Buckminster Fuller](https://www.buckyverse.org/en/the_dymaxion_world_of_buckminster_fuller/the_dymaxion_world_of_buckminster_fuller.pdf).

### C. Michelin PAX run-flat system

**Initial diagnosis:** The support ring allows continued movement after pressure loss, but changes the service system. The tyre, wheel and support ring form a specialised assembly; repairability, replacement parts, equipment, trained technicians and service-network coverage become part of the product's viability.

**Historical check:** Michelin's own FAQ says PAX repair requires special mounting equipment, replacement parts and technical training, and directs repairs to authorised servicing dealers. Contemporary reporting described customer complaints about replacement cost and difficulty finding appropriate repair facilities, and reported Michelin's decision to phase out OEM supply in 2008.

**Assessment:** Strong structural diagnosis of ecosystem/service dependency. The technology may solve a tyre-level problem while creating a support-network constraint. This is not proof that service issues alone caused the system's commercial retreat.

Sources:
- [Michelin Canada PAX System FAQ](https://www.michelin.ca/en/auto/assistance/faq).
- [Tyrepress: Michelin Phasing Out OEM Supply of PAX](https://www.tyrepress.com/2008/04/michelin-phasing-out-oem-supply-of-pax/).

### D. Firestone ATX / Wilderness AT tyre failures

**Initial diagnosis:** A generic tyre-separation scenario suggested interacting risks involving construction, heat, inflation, load, speed and vehicle behaviour. This initial framing was too generic to identify the actual defect and its production scope.

**Historical check:** NHTSA's investigation concerned particular Firestone ATX, ATX II and Wilderness AT tyres. Firestone recalled approximately 14.4 million tyres in August 2000; the agency documented tread separations associated with crashes, fatalities and injuries. The investigation considered tyre construction and production codes, and the relationship between tyre failures and vehicle consequences.

**Assessment:** The initial MP diagnosis identified a plausible family of interacting mechanisms but did not, by itself, identify the actual affected products, production population or defect. This is an important limit: a generic mechanism inventory is not a substitute for component-level evidence and investigation.

Source: [NHTSA, Final Report on the Firestone tyre investigation](https://www.nhtsa.gov/sites/nhtsa.gov/files/firestonereport.pdf).

### E. Goodyear G159 tyres used on motorhomes

**Initial diagnosis:** A tyre designed around one duty cycle may be exposed to a different one when fitted to a motorhome: sustained highway operation, vehicle loading, inflation practice and heat exposure may differ from the original commercial-vehicle use. Application mismatch can create a risk even where the tyre's original intended use was different.

**Historical check:** NHTSA opened investigation PE17-009 into G159 tyres installed on Class A motorhomes. Its 2022 recall alert states that more than 170,000 tyres were recalled after a high rate of failures on RVs compared with similar tyres. Goodyear's own statement disputed an inherent tyre defect and described the risk in relation to underinflated or overloaded use on Class A motorhomes. That disagreement should remain visible rather than being collapsed into a single definitive causal claim.

**Assessment:** Strong identification of application/duty-cycle mismatch as a question to investigate. The evidence supports concern about the RV application and operating conditions; it does not justify simplifying the history to "a truck tyre was automatically unsuitable for a motorhome."

Sources:
- [NHTSA: Consumer Alert — Goodyear Issues Recall for Select Tires Used on RVs](https://www.nhtsa.gov/press-releases/goodyear-recall-tires-rvs).
- [NHTSA: ODI Resume, PE17-009](https://static.nhtsa.gov/odi/inv/2017/INOA-PE17009-5650.PDF).
- [Goodyear: Statement on G159 275/70R22.5](https://news.goodyear.com/2022-06-07-Goodyear-Statement-on-G159-275-70R22-5).

### F. Monocycle (rider inside the wheel)

**Initial diagnosis:** Placing the rider inside the wheel lowers the centre of gravity relative to a unicycle, but does not make the system statically stable. Balance, steering, acceleration/braking and rider control remain demanding.

**Historical check:** An IEEE Control Systems Magazine paper on monocycle stability states that both unicycles and monocycles are statically unstable. The lower centre of gravity may make a monocycle potentially easier to ride than a unicycle, but piloting remains challenging.

**Assessment:** Appropriate classification is experimental/niche architecture with substantial control challenges, not a failed mass-market product.

Source: [IEEE: A history of the monocycle stability and control from inside the wheel](https://ieeexplore.ieee.org/abstract/document/1700041).

## Cross-case findings

The most useful MP observations in this collection were:

1. **Coupled systems:** The square wheel only makes sense with its matched track; the Mecanum wheel depends on floor and control conditions; PAX depends on a specialised service ecosystem.
2. **Operating-envelope mismatch:** A design can work in a narrow regime but become unsuitable when speed, load, surface, weather, duty cycle or road geometry changes.
3. **Benefits can create new liabilities:** Puncture resistance can shift risk to heat and material fatigue; extreme manoeuvrability can complicate high-speed controllability; a lower centre of gravity does not remove dynamic instability.
4. **Accumulated dependencies:** Service equipment, trained technicians, replacement parts and repair locations can become essential accumulated infrastructure around a technical design.
5. **Evidence specificity matters:** The Firestone case exposed a weakness in the initial generic diagnosis. A plausible mechanism family does not identify a particular manufacturing defect, affected population or causal chain without more specific evidence.
6. **Outcome categories must remain distinct:** A design can be mechanically functional, commercially niche, operationally constrained, superseded or withdrawn. These are not interchangeable meanings of "failure."

## User-supplied observational transfer: long vehicles turning

The user connected the Dymaxion discussion to repeated real-world observations of long cargo-hauler trucks negotiating turns on ordinary roads. Long vehicles demonstrate several visible geometric effects:

- rear-wheel off-tracking: the trailer or rear axle follows a tighter path than the front axle;
- front/rear path divergence and the need for a wider turning envelope;
- outward tail swing at the opposite end of the vehicle;
- increased difficulty where road width, kerbs, parked vehicles and other traffic constrain the manoeuvre.

This is relevant observational evidence for the general proposition that vehicle length and geometry interact with the available turning space. It is **not** evidence that the Dymaxion had the same mechanism as an articulated truck. The Dymaxion's rear-wheel steering and directional response are distinct design features. The analogy is useful at the level of operating-envelope fit, not as a one-to-one mechanical explanation.

## Overall interpretation

This collection provides additional examples of MP being used to organise structural inquiry across different engineering designs. Its value here is in surfacing dependencies, coupled constraints, operating-envelope mismatches and plausible failure modes, then identifying what evidence is needed to distinguish among them.

It does **not** establish predictive accuracy, universal reliability or superiority over an unassisted analysis. The second batch's historical checks were retrospective and the interaction was not blind. A stronger future evaluation would freeze an evidence packet before outcome disclosure, keep the outcome record separate, and have independent reviewers assess whether the structural diagnosis identifies the relevant mechanisms without being given the historical answer.

No change to the Memory Prism framework, skill, checklist or core doctrine is proposed by this record.
