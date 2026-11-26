# Smoke Test G — Ledger Is Core, and Dormancy Defers Payment — 2026-11-25

**Test ID:** MP-SMOKE-G-2026-11-25-01
**Test:** `tests/smoke/SMOKE_TESTS.md` § G
**Run type:** Assistant-generated, literature-informed, single condition (MP skill in use)
**Context:** same conversation; self-scored; not blind; no seeds tested
**MP sources consulted:** Framework (The ledger; Dead, alive, maybe-dead, and never alive), Audits essay (Dormancy and Mode Shift), `references/concepts.md`

## Prompt

> A dormant seed can germinate after years. Is it 'off'? What does it still owe, and is Ledger just an optional lens here?

## Answer produced

**Short answer:** It's not off, and Ledger is not optional. Ledger is one of the Framework's original concepts, not one of the seven essay lenses. The Framework says dormant seeds "pause metabolism but retain open ledgers. They defer payment, not close accounts." The literature adds a refinement: in a *dry* seed, the account isn't just paused. Damage keeps accruing as a debt that is paid, if it can be, on rehydration.

| MP concept | What I identify in this query |
|---|---|
| Ledger | Stored reserves (starch, oils, storage proteins), a non-renewable stock of small antioxidants, and an accumulating repair bill (DNA, lipid and protein damage) |
| Living matter | Open account: no closure until the embryo can no longer repair and germinate |
| Viability band / correction window | Seed longevity: how long damage can accrue before repair at imbibition can no longer clear it |
| Constraints | Moisture content and temperature set cytoplasm state (glassy vs fluid) and so the rate of deterioration; oxygen availability |
| Flow (kept separate) | Water uptake at imbibition, which reopens enzymatic activity |
| Audit (candidate, scoped) | DNA-damage checkpoints that delay germination in aged seeds; active only once hydrated, not in the dry state |

**1. Two different "dormant" states, two ledgers** [Fact, with scope noted]
- *Dry, quiescent orthodox seed.* The cytoplasm solidifies into a glass that restricts molecular motion and slows deterioration. Enzymes are largely inactive, so damage isn't repaired. Reactive oxygen species still form, and small antioxidants (glutathione, tocopherols) are consumed. That is a reserve drawn down with no income. Longevity rises as moisture content and temperature fall, and hypoxia prevented lipid peroxidation in glassy-state seeds in one study.
- *Imbibed but dormant seed (e.g. in a soil seed bank).* DNA repair is active in imbibed dormant seeds, preserving genome integrity during long stasis in soil. Here the seed is paying maintenance continuously from stored reserves.

**2. What it owes when it wakes** [Fact]
On imbibition, repair activities clear damage accumulated during quiescence. The DNA-damage response and repair start early, hours before the cell cycle begins. Aged seeds delay germination to deal with accumulated DNA damage. Repair capacity and accumulated damage are major determinants of seed vigour and viability. After that, the reserves must fund germination and early growth until the seedling can photosynthesise.

**3. What happens when payments can't be met** [Fact + inference]
Aged seeds germinate more slowly, produce weaker seedlings, or fail. In *Arabidopsis*, the checkpoint regulator SOG1 triggers cell death after germination in response to accumulated DNA damage. [Reasonable inference] The debt can exceed what the reserves and repair machinery can pay inside the window, which is the Framework's "cost exceeds intake → failure enforced," at the timescale of storage.

**Refinement to the Framework's wording.** "Pause metabolism… defer payment" is right about the account staying open. For dry seeds, though, "defer" undersells it: the liability grows during the pause, and part of the reserve (antioxidants) is spent without metabolism. A more exact phrasing: *the account stays open, payment is deferred, and the balance owed keeps rising at a rate set by moisture, temperature and oxygen.* [Reasonable inference from the sources]

**On the Audits essay's "mode shift is audit-driven":** for seeds, entry into the dry state is mainly a developmental maturation programme rather than a response to detected deviation. I did not find evidence that seeds "audit" in the dry glassy state. The clearly supported audit-like mechanism, DNA-damage checkpoints, operates after hydration. [Open question: whether the essay's general claim fits orthodox seed maturation.]

**Next diagnostic question:** For one species, does the length of the pre-germination lag after imbibition scale with storage age and storage humidity? If the repair-debt reading is right, it should lengthen with both, and DNA-repair mutants should show steeper longevity loss. Published *Arabidopsis* mutant work already points this way.

## Smoke score (self, unblinded)

| Dimension | Score | Note |
|---|---:|---|
| 1 Engages the question | 2 | Not off; Ledger core; stated first |
| 2 Consults correct source | 2 | Framework living-matter and Audits dormancy passages used |
| 3 Proportionate lenses | 2 | No essay lenses forced; Audits used only to test its own claim |
| 4 Domain accuracy | 1 | Sourced, but mostly *Arabidopsis* and orthodox seeds. Recalcitrant seeds and true physiological dormancy mechanisms (ABA/GA) not covered. Several sources are search snippets, not full papers. |
| 5 Uncertainty vs fact | 2 | Labels used; essay claim flagged as open |
| 6 Useful answer, no handoff | 2 | Concrete ledger items plus a diagnostic test |
| **Total** | **11/12** | |

**Finding worth keeping:** the run surfaced a substantive nuance (debt accrual during dry quiescence) and a possible overreach in the Audits essay ("mode shift is audit-driven") for seeds. Both are candidates for owner review, not edits.

## Sources
- Waterworth et al. 2019, *Seeds and the Art of Genome Maintenance*, Front. Plant Sci. 10:706 (PMC6554324)
- Waterworth et al. 2022, *Seed DNA damage responses promote germination and growth in Arabidopsis thaliana*, PNAS (PMC9335332)
- Waterworth et al. 2016, DNA repair in the soil seed bank (PMC5003248)
- Gerna et al. (bioRxiv 2020.12.11.421446), glassy state, hypoxia and lipid peroxidation
- *Antioxidant depletion during seed storage under ambient conditions*, Seed Science Research (Cambridge)

## Score line

Not scored on the IQ rubric (na). Smoke-test score: 11/12 (self, unblinded).

SCORES: IQ=na/12; scorer=self; blind=no
