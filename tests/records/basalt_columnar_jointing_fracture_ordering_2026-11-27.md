# Basalt Columnar Jointing: Fracture Networks and Polygon Ordering — 2026-11-27

**Test ID:** MP-2026-11-27-01  
**Run type:** Assistant-generated synthesis  
**Conditions:** single MP-guided condition; no baseline comparison  
**Context:** same-context · **Scorer:** self · **Blind:** no · **Execution:** literature research; no new physical experiment  
**Question:** How does cooling lava develop columnar joints, and why do the resulting columns so often have roughly polygonal, especially hexagonal, cross-sections?

## Selective pre-interpretation inventory

| MP concept | What I identify in this query |
|---|---|
| Architecture | A solidifying lava body is divided by a connected network of contraction fractures into columns. |
| Constraints | Thermal gradients, cooling rate, rock tensile strength, elastic properties, flow geometry and boundary conditions constrain fracture initiation and propagation. |
| Board | The cooling boundaries and interior of a lava flow have different thermal histories; the local environment changes the fracture and cooling conditions. |
| P-Memory | The persistent fracture network and striae preserve structural traces of the cooling and fracture history. |
| Flow Under Constraint (candidate) | Heat transfer through the rock and, after fractures open, possible fluid circulation along the cracks influence the thermal field. |
| Accumulation Patterns (candidate) | Individual cracks connect into a network; their junction geometry and spacing determine the polygonal columns. |
| Stability | The solidifying rock accommodates contraction by fracture once tensile stress exceeds the material's resistance. |

## Mechanism and evidence

Columnar joints are contraction fractures that propagate through cooling lava. As the material cools and solidifies, thermal contraction creates tensile stress. Once the local stress exceeds the rock's tensile strength, a fracture can form and propagate with the moving thermal/solidification front. The fracture surfaces can preserve step-like markings called striae, which record incremental crack advance. Goehring and Morris's field study and modelling of the Columbia River Basalt Group relates column radius and stria size to cooling and fracture dynamics. [1]

The columns are not poured into hexagonal moulds. Their polygonal geometry is an emergent property of a crack network. The 2008 study describes a contrast between irregular surface patterns, which commonly contain many T-junctions and polygons of varied area, and more ordered interior colonnades, where cracks more often meet at Y-junctions with approximately 120-degree angles and polygon areas become more similar. Much of the observed ordering occurs within roughly one or two metres of the flow margin. Even well-ordered formations such as the Giant's Causeway retain pentagons, heptagons and other departures from a hexagonal ideal. The authors explicitly identify the detailed cause of this ordering as an open problem. [1]

Column size is related to cooling and fracture advance, but the relationship should not be reduced to a universal one-variable rule. In the studied Columbia River Basalt Group flows, column radius and stria size were found to be inversely related to cooling rate. The authors also note that crack-enhanced heat transfer couples column scale, fracture advance and cooling rate, making the causal relationship more subtle than a simple cooling-rate dial. Their model is most directly applicable to the thick type II/III flows studied, not every possible lava geometry. [1]

A separate 2018 thermo-mechanical experiment directly examined fracture initiation in basalt from Eyjafjallajökull, Iceland. For that material, the estimated solidus was 980 °C, while the experiment observed localised macroscopic tensile failure at 890–840 °C, below the solidus. The authors measured tensile stress build-up and a subsequent nonlinear increase in permeability as fractures opened during further cooling. These temperatures and measurements belong to the tested basalt and experimental conditions; they are not universal constants for all lavas. [2]

The two studies address different parts of the problem:
- The 2018 experiment constrains the temperature window and mechanics of fracture initiation for its tested basalt.
- The 2008 field study addresses fracture propagation, column scale and the evolution of ordering in particular large basalt flows.

They should not be collapsed into one experiment or treated as if either fully solves the origin of hexagonal ordering.

## Findings and interpretation

The regular columns arise from a moving fracture network, not from a pre-existing hexagonal template. Thermal contraction supplies the stress; fracture mechanics controls initiation and propagation; local cooling conditions influence spacing; and the network becomes more ordered as it develops into the interior in the field examples studied.

The visible hexagons are therefore a statistical tendency within a fracture system, not a rigid geometrical rule. The persistent rock structure is a P-Memory of the process, but the final geometry alone does not reveal every detail of the thermal history.

The crack network also changes the system it forms in: once open, fractures increase permeability and can permit fluid movement. The 2008 paper discusses water/steam convection as a proposed heat-transfer mechanism in lower colonnades but notes the absence of direct evidence for that mechanism there. The 2018 experiment independently demonstrates increased permeability after fracture formation; it does not establish that the same fluid-circulation regime operates in every natural colonnade. [1][2]

## Limits and unresolved question

The detailed mechanism that drives the transition from irregular surface cracks to more ordered interior columns remains incompletely understood. The 2008 study identifies this as an open problem and cautions that regularity is often overstated.

A useful future discriminating study would compare fracture-network evolution under controlled changes in cooling-front speed and boundary geometry, measuring junction transitions, polygon-area distributions, stria spacing and crack-front speed together. That would test whether ordering is mainly a consequence of local crack interactions, cooling-front dynamics, or their coupling. No such experiment was performed in this run.

## Sources

1. Lucas Goehring and Stephen W. Morris, “Scaling of columnar joints in basalt,” *Journal of Geophysical Research: Solid Earth* 113, B10203 (2008). Field observations, fracture striae, column scaling, ordering and model limitations: https://doi.org/10.1029/2007JB005018
2. Anthony Lamur et al., “Disclosing the temperature of columnar jointing in lavas,” *Nature Communications* 9, 1432 (2018). Thermo-mechanical basalt experiments, sub-solidus tensile failure and permeability change: https://doi.org/10.1038/s41467-018-03842-4

## Score sheet

**Run type:** assistant-generated synthesis **Conditions:** single MP-guided condition **Context:** same-context **Scorer:** self **Blind:** no **Execution:** literature

| Dim | MP-guided | Note (failure mode for any 0/1) |
|---|---:|---|
| IQ1 Engages the question | 2 | Directly explains formation and polygon ordering without treating hexagons as mandatory. |
| IQ2 Mechanism and evidence | 2 | Fracture mechanics, field observations and thermo-mechanical experiment are distinguished and sourced. |
| IQ3 Evidence boundaries | 2 | Experimental temperatures are scoped to the tested basalt; unresolved ordering and untested fluid circulation are stated. |
| IQ4 Competing explanations | 1 | Multiple processes are identified, but their distinct predictions are not fully developed into a comparison. |
| IQ5 Next question or action | 1 | A specific experiment is proposed, but no researchable follow-up was executed in this run. |
| IQ6 Clarity and economy | 2 | Mechanism and evidence are explained without requiring MP vocabulary. |
| **IQ total** | **10/12** | |

| MPF dimension | Score | Note |
|---|---:|---|
| MPF1 Inventory first and concrete | 2 | Selective inventory precedes interpretation and names features of this system. |
| MPF2 Proportionate selection | 2 | Uses structural concepts and two candidate lenses; does not force all lenses. |
| MPF3 Concept fidelity | 2 | Ledger omitted because ongoing resource maintenance is not explanatory here; P-Memory is not narrowed to a database. |
| MPF4 No unsupported mechanism | 2 | Fluid circulation is labelled as a limited proposal, not an established universal mechanism. |
| MPF5 Source use | 2 | Framework protocol consulted; domain claims tied to the two studies. |
| MPF6 Reasoning audit actually used | 1 | Scope corrections and the separation of fracture initiation from ordering are visible, but the audit did not produce a fully diagnostic competing-hypothesis test. |
| **MPF total** | **11/12** | |

**Integrity flags:** F1 No · F2 No · F3 No · F4 No · F5 No · F6 No.  
**Difference claimed?** No comparison condition was run.

**SCORES:** IQ_mp=10/12; MPF=11/12; scorer=self; blind=no

## Repository provenance

**Protocol retrieval (UTC):** 2026-11-27T10:23:16Z  
**Current main commit:** `c4405ba7a2c1572dee6ddb3cce151048e86cad39`

| File | Git blob SHA | SHA-256 |
|---|---|---|
| `tests/daily/README.md` | `04d295a20c67ff0774d89711c07a475616bf503e` | `d69d5220b45d68920d3cc9e1778dc1e0ff17d022dddcadac7ebb3770b09a8e74` |
| `tests/daily/SCORING.md` | `0b4f359fdeefdcdc55d55b94a94e8c8d801280a3` | `7f5045b4a3912ed1e951a79e6ac0b8b977fb70804074787d6454ab79d9bc9c79` |
| `tests/records/DEVELOPMENT_LOG.md` | `3e3f6913242cac552580caf556051003090041dd` | `77d70016210a6bcf64058184634db3b0f69c12a61aec149cec24d5b5f7d42a0b` |
