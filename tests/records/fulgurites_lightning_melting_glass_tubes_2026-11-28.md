# Fulgurites: Lightning, Melting and the Formation of Glass Tubes — 2026-11-28

**Test ID:** MP-2026-11-28-01  
**Run type:** Assistant-generated synthesis  
**Conditions:** single MP-guided condition; no baseline comparison  
**Context:** same-context · **Scorer:** self · **Blind:** no · **Execution:** literature research; no new physical experiment  
**Question:** How can a lightning strike turn ordinary sand or soil into glass-like structures, sometimes creating long branching tubes underground?

## Selective pre-interpretation inventory

| MP concept | What I identify in this query |
|---|---|
| Architecture | Mineral grains, pore spaces, moisture and the eventual fused glass structure. |
| Constraints | Electrical conductivity, soil composition, water content, heat transfer and discharge duration constrain where and how much material melts. |
| Board | The local soil profile, its moisture and mineral distribution, and the geometry of the discharge path. |
| P-Memory | The surviving glass structure preserves traces of the discharge path and material transformed. |
| Flow Under Constraint | Electrical current and heat move through a heterogeneous medium along available conductive paths. |
| Accumulation Patterns | Melted and fused grains form a connected tube or branching structure. |
| Stability | The molten wall must cool and solidify while retaining a tube-like geometry. |
| Ledger | Electrical energy must supply the heat needed for melting and fusion, while heat is lost to surrounding material; the available input and duration constrain the amount of glass that can form. |

## Mechanism and evidence

The central finding is that the brief, very high-current lightning impulse that initiates electrical breakdown is not necessarily enough to melt sufficient material to make a fulgurite. A 2023 laboratory study used volcanic ash from the Laacher See region and a controlled discharge system. A short impulse (about 100 microseconds in the described setup) initiated the conductive path; a lower-amplitude continuing current of 220–350 A was then applied for durations from 100 to 500 milliseconds. The impulse-only T0 experiment produced partial melting and sintering of particle clusters, while the continuing-current experiments produced fulgurites. The shortest continuing-current duration the apparatus could deliver was 100 ms, so the study does not establish that 100 ms is a universal physical threshold. [1]

The experiment produced tubular glassy structures with remnants of pristine material and partially melted crystals on their surfaces. The central void was variable; an open central void was reported only in the T200 specimen. Short apophyses/branches were observed in T100, T200 and T500. The T500 specimen differed in morphology from the other tube-like specimens. The authors state that the experimental setup did not permit direct observation of the fulgurite-forming process, so formation details were inferred from the imposed discharge conditions, videography and examination of the resulting structures. [1]

The material matters. A 2012 morphology study classified natural fulgurites into sand, clay, caliche and rock types, with an additional droplet form. Sand fulgurites tend to have thin glass walls; clay fulgurites thick, melt-rich walls; caliche fulgurites thick but relatively glass-poor walls; and rock fulgurites glass associated with largely unmelted surrounding rock. The authors estimated 1–30 MJ per metre of fulgurite and heating rates around 1,000 K/s for the studied material. These are morphology-based estimates, not universal requirements. [2]

The 2023 ash study discusses heterogeneity and conductive-path development as factors that can affect morphology and branching. The observed branches in its experiments are evidence that short secondary extensions can form under some tested conditions; they do not establish one universal branching mechanism for natural sand, clay, caliche and rock fulgurites. The final geometry reflects both the electrical discharge and the electrical, thermal and physical properties of the target material. [1][2]

The experiment also showed that longer continuing current did not simply produce a longer, more stable tube. At 500 ms the specimen departed from the tube-like morphology seen at shorter durations. The study discusses loss of structural integrity/collapse as a possible consequence of prolonged heating and changing porosity. This is a result of that experimental material and apparatus, not a general maximum-duration rule for lightning. [1]

## MP interpretation and findings

A fulgurite is a persistent structure left by an electrical discharge interacting with a particular material. Its architecture is not determined by current alone: the discharge waveform, duration, target composition, grain size and local conditions all matter.

The Ledger is essential here because the problem is explicitly an energy budget. Electrical energy is delivered over time; only part becomes heat in the target; heat is transferred into adjacent material and lost; and a sufficient thermal dose is needed to melt and fuse a continuous wall. This accounting is distinct from the movement of current and heat (Flow) and the formation of a connected residue (Accumulation Patterns).

The 2023 study's strongest contribution is the experimental separation between the short initiating impulse and the continuing current needed to produce substantial melting in its volcanic ash. It also provides a controlled series of continuing-current durations. The 2012 study supplies a broader natural morphology classification and energy estimates. These studies complement one another but do not establish a single universal recipe for all fulgurites.

## Limits and unresolved questions

- The 2023 laboratory target was prepared volcanic ash, not ordinary natural beach sand or garden soil.
- The minimum 100 ms continuing-current duration was constrained by the apparatus; shorter durations were not tested.
- The authors could not directly observe the complete formation process. The proposed mechanism is inferred from the setup and resulting specimens.
- The morphology and energy estimates from the 2012 study are not universal constants.
- The experiment did not establish a general causal law for natural branching across different soil types.
- No new experiment was run in this inquiry.

A useful future test would vary grain-size distribution, moisture and continuing-current duration independently, then measure melt fraction, wall thickness, branch frequency and whether the central void remains open. That would distinguish material effects from waveform effects rather than changing several at once.

## Sources

1. Çalışkanoğlu et al., “Experimental generation of fulgurite under realistic lightning discharge conditions,” *Scientific Reports* (2023): https://www.nature.com/articles/s41598-023-38781-8
2. Matthew A. Pasek, Kristin Block and Virginia Pasek, “Fulgurite Morphology: A Classification Scheme and Clues to Formation,” *Contributions to Mineralogy and Petrology* 164 (2012): https://doi.org/10.1007/s00410-012-0753-5

## Score sheet

**Run type:** assistant-generated synthesis **Conditions:** single MP-guided condition **Context:** same-context **Scorer:** self **Blind:** no **Execution:** literature

| Dim | MP-guided | Note (failure mode for any 0/1) |
|---|---:|---|
| IQ1 Engages the question | 2 | Directly explains how lightning produces glassy tubes and branches. |
| IQ2 Mechanism and evidence | 2 | Separates impulse from continuing current and distinguishes experimental ash from natural fulgurite classes. |
| IQ3 Evidence boundaries | 2 | Apparatus limits, lack of direct observation and material scope are explicit. |
| IQ4 Competing explanations | 1 | Material and waveform effects are identified, but alternative branching mechanisms are not given distinct predictions. |
| IQ5 Next question or action | 1 | A specific factorial experiment is proposed but not executed; no additional research step was carried out to resolve natural branching. |
| IQ6 Clarity and economy | 2 | The mechanism is explained in ordinary language without requiring MP knowledge. |
| **IQ total** | **10/12** | |

| MPF dimension | Score | Note |
|---|---:|---|
| MPF1 Inventory first and concrete | 2 | Inventory precedes interpretation and maps actual features. |
| MPF2 Proportionate selection | 2 | Relevant core concepts and lenses are used without forcing all seven. |
| MPF3 Concept fidelity | 1 | Ledger was omitted from the first user-facing inventory and added only in a later correction; the correction is preserved here. |
| MPF4 No unsupported mechanism | 2 | Branching mechanisms are qualified; no unsupported audit or editor is asserted. |
| MPF5 Source use | 2 | Framework checklist consulted; experimental and morphology claims are tied to the two studies. |
| MPF6 Reasoning audit actually used | 2 | The later correction explicitly restores Ledger and distinguishes energy accounting from Flow and Accumulation. |
| **MPF total** | **11/12** | |

**Integrity flags:** F1 No · F2 No · F3 No · F4 No · F5 No · F6 No.  
**Difference claimed?** No comparison condition was run.

**SCORES:** IQ_mp=10/12; MPF=11/12; scorer=self; blind=no

## Repository provenance

**Protocol retrieval (UTC):** 2026-11-28T08:40:42Z  
**Current main commit:** `436bef7071a93f083480c62ba9383902a19d05fb`

| File | Git blob SHA | SHA-256 |
|---|---|---|
| `tests/daily/README.md` | `04d295a20c67ff0774d89711c07a475616bf503e` | `d69d5220b45d68920d3cc9e1778dc1e0ff17d022dddcadac7ebb3770b09a8e74` |
| `tests/daily/SCORING.md` | `0b4f359fdeefdcdc55d55b94a94e8c8d801280a3` | `7f5045b4a3912ed1e951a79e6ac0b8b977fb70804074787d6454ab79d9bc9c79` |
| `tests/records/DEVELOPMENT_LOG.md` | `b46268bca9422f8156b5e84359b2a705f5abe392` | `62732e82c6e49046963ffd3eb7510a04f68de3c41b34a61d3def296f1f25b88a` |
