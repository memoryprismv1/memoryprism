# Why Bread Goes Stale Even in a Sealed Bag — and Why Warming Revives It (Briefly) — 2026-11-25

**Test ID:** MP-2026-11-25-02
**Run type:** Assistant-generated synthesis (literature-informed). No user-led inquiry; no bread was tested.
**Conditions:** conventional baseline vs MP-guided
**Context:** same-context (the baseline was written after the assistant had read the MP skill, so it is contaminated) · **Scorer:** self · **Blind:** no · **Execution:** literature

## Starting question

Why does bread go stale even when sealed in a bag so it can't dry out, and why does warming a stale slice make it soft again, but only for a while?

## Condition A — Conventional baseline

Staling is mostly not drying. During baking, starch granules absorb water and gelatinise into a soft, amorphous gel. As the loaf cools and sits, starch molecules (mainly amylopectin, more slowly than amylose) realign into partly crystalline regions. This is retrogradation, and it firms the crumb even in a sealed bag. Water also migrates from crumb to crust, which is why the crust goes leathery. Reheating melts the amylopectin crystallites and softens the crumb, but they re-form, faster than in fresh bread. The fridge speeds staling; the freezer nearly stops it. Commercial loaves use enzymes and emulsifiers to slow it.

## Condition B — MP-guided

### Selective inventory

| MP concept | What I identify in this query |
|---|---|
| P-Memory | The gelatinised starch–gluten network set by baking, and the growing amylopectin crystallites as residue of storage time |
| Constraints | Water content of the crumb; storage temperature relative to the range where retrogradation runs; amylopectin's branched structure, which slows its realignment |
| Flow | Water moving crumb → crust, and within the crumb from the gluten network into starch crystallites |
| No Sacred States | "Softness" isn't a property of the bread; it's a state that depends on temperature and on where the water sits |
| Stability / lag | Fresh softness is a temporary amorphous state; the firming begins as soon as baking ends |
| Translator (candidate) | Mouth and fingers read firmness and lost springiness as "dry," even when total water is unchanged |

Left out on purpose: **Editors** (I couldn't name an active filter beyond ordinary thermodynamics and kinetics, so I didn't invent one), **Ledger** (a loaf doesn't maintain itself, so there are no minimum payments; reheating is an energy input, not upkeep), and **Audits** (threshold-only: nothing detects or corrects).

### Mechanism and evidence

1. **Three candidate explanations, with different predictions**
   - *Evaporation:* firming should track mass loss, and a sealed loaf shouldn't stale.
   - *Amylopectin retrogradation:* firming should rise with crystallinity even when total water is constant, and heating above the crystallites' melting range should reverse it.
   - *Water redistribution:* with a crust present, crumb water should fall and firming should be worse than in crust-free crumb.

2. **What the evidence says** [Fact]
   - Staling is attributed to starch gradually moving from amorphous to partly crystalline, with amylopectin retrogradation central.
   - During storage, the soft gelatinised network is gradually transformed into a partly crystalline amylopectin network. Water bound into the crystallites can no longer plasticise the crumb or the gluten, so the crumb loses resilience (Goesaert et al. 2009).
   - Baik & Chinachoti (2000) stored white bread in hermetic pouches with and without crust. With crust, crumb moisture and water activity fell, and after seven days the bread was firmer and more recrystallised. Without crust, water stayed roughly unchanged. A thermal transition near 60 °C correlated with amylopectin recrystallisation.
   - So explanations 2 and 3 both operate and interact. Evaporation is a third, separate pathway for unwrapped bread, not the main story.

3. **Why reheating revives it, and why only briefly**
   - [Fact] The ~60 °C transition matches melting of amylopectin crystallites. Toasting or oven-warming reverses firmness because most water is still trapped in the crumb.
   - [Fact, secondary source] Reheated bread re-firms faster than fresh bread (America's Test Kitchen).
   - [Speculation] Why faster: candidate explanations are residual ordered regions acting as nuclei, and water lost during reheating. I found no primary source separating these.

4. **Fridge vs freezer** [Fact, secondary sources]
   Retrogradation runs faster at refrigerator temperature than at room temperature, while freezing nearly halts it. A Quadram Institute storage study compared room, fridge and freezer for sealed rolls. The often-repeated "six times faster" figure comes from a popular source; I couldn't trace it to a primary study, so I'm not stating it.

### Findings

- Sealed bread still stales because the starch network reorganises and water relocates *inside* the loaf. Total water can stay constant while the bread feels dry.
- The "dry" sensation is a translator reading: mouthfeel registers firmness and lost springiness, not water content.
- Warming works because the crystalline order melts near 60 °C. It doesn't add water, which is why it's temporary.

### Next diagnostic step

A home or lab test that separates the explanations: weigh a sealed loaf daily (mass ≈ constant ⇒ not evaporation), measure slice firmness, and reheat matched slices to below vs above ~60 °C core temperature. Retrogradation predicts that only the >60 °C slices soften. Adding a crust-removed sample tests the redistribution contribution.

## Comparison

Both conditions reach the same mechanism. MP-guided added:
- explicit competing explanations tied to predictions;
- the "feels dry ≠ is dry" distinction;
- a test that separates the explanations;
- marking the re-staling-speed explanation as speculation and declining to repeat an untraceable "6×" figure.

The last two came from evidence discipline in the skill rules more than from MP concepts as such. Cost: a longer answer and an inventory that a casual reader doesn't need.

## Limits

No experiment run. Several mechanism claims rest on abstracts and secondary sources (cooking sites, a patent). The baseline is contaminated by the assistant having read MP first, so the IQ difference is not a clean MP effect.

## Score sheet

**Run type:** assistant-generated synthesis **Conditions:** baseline, MP-guided **Context:** same-context **Scorer:** self **Blind:** no **Execution:** literature

| Dim | Baseline | MP-guided | Note (failure mode for any 0/1) |
|---|---:|---:|---|
| IQ1 Engages the question | 2 | 2 | |
| IQ2 Mechanism and evidence | 1 | 1 | Baseline: no sources. MP: abstracts/secondary sources for several claims |
| IQ3 Evidence boundaries | 1 | 2 | Baseline states "re-forms faster" and fridge claim without level |
| IQ4 Competing explanations | 0 | 2 | Baseline gives one story |
| IQ5 Next question or action | 0 | 2 | Baseline has none |
| IQ6 Clarity and economy | 2 | 1 | MP inventory and labels add overhead for an everyday question |
| **IQ total** | **6/12** | **10/12** | Self-scored, same context, unblinded |
| MPF1 Inventory first and concrete | n/a | 2 | |
| MPF2 Proportionate selection | n/a | 2 | Translator row marked candidate |
| MPF3 Concept fidelity | n/a | 2 | Ledger omission justified (no self-maintenance) |
| MPF4 No unsupported mechanism | n/a | 2 | Editor and audit explicitly not invented |
| MPF5 Source use | n/a | n/a | No MP-interpretation question arose |
| MPF6 Reasoning audit actually used | n/a | 2 | Audit removed the untraceable "6×" figure and flagged re-staling speed as speculation |
| **MPF total** | n/a | **10/10** | |

**Integrity flags:** F1 Yes. Several sources were read only as search snippets or abstracts, not full texts (cap IQ2 ≤ 1, applied). F2–F6 No.

**Reading:** the 4-point IQ gap meets the README's ≥3 threshold on paper, but the baseline was written by the same assistant, deliberately terse, after reading MP. Record as **no demonstrated difference**: the gain is plausibly from the evidence-discipline rules, not from MP concepts.

## Sources
- Baik & Chinachoti 2000, *Moisture redistribution and phase transitions during bread staling* (AGRIS record)
- Goesaert, Slade, Levine & Delcour 2009, *Amylases and bread firming – an integrated view* (AGRIS record)
- US Patent 6,635,289 (staling as starch crystallisation; amylopectin role)
- Quadram Institute, *What is the best way to store bread?* (2022)
- America's Test Kitchen, *How to revive stale bread*
- D. Mercer, University of Guelph, *The Complexities of Bread Staling* (IUFoST)

## Score line

SCORES: IQ_baseline=6/12; IQ_mp=10/12; MPF=10/10; scorer=self; blind=no