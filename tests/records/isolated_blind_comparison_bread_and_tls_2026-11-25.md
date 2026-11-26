# Isolated, blind-scored comparison: plain answer vs Memory Prism skill — 2026-11-25

**Test ID:** MP-BLIND-2026-11-25-01
**Run type:** assistant-generated synthesis (bread) and documentation-grounded scenario with toy reproductions (cert)
**Design:** for each question, two fresh agents with no access to this conversation (one with no MP access, one told to apply `skill/memory-prism/SKILL.md`), identical other instructions, tools and word guidance. A third fresh agent scored both answers on the IQ rubric from `tests/daily/SCORING.md` (MP mentions stripped from the rubric), labels randomised, and was not told the study was about a framework. The scorer spot-checked two cited claims per answer.
**Context:** isolated · **Scorer:** second model instance (same model family) · **Blind:** partial (see limits) · **Execution:** literature + docs; both cert agents ran a local TLS reload check on their own

## Results (unblinded after scoring)

| Question | Plain | MP-guided | Difference |
|---|---:|---:|---:|
| Bread staling (MP was "B") | 7/12 | 11/12 | +4 |
| Certificate served after renewal (MP was "A") | 10/12 | 11/12 | +1 |

Per dimension (plain → MP):

| Dim | Bread | Cert |
|---|---|---|
| IQ1 Engages the question | 2 → 2 | 2 → 2 |
| IQ2 Mechanism and evidence | 1 → 2 | 2 → 2 |
| IQ3 Evidence boundaries | 1 → 2 | 1 → 2 |
| IQ4 Competing explanations | 0 → 2 | 1 → 2 |
| IQ5 Next question or action | 1 → 2 | 2 → 2 |
| IQ6 Clarity and economy | 2 → 1 | 2 → 1 |

## Reading

- By the repo's rule (≥3 points, each dimension justified, scorer and blinding stated), **bread shows a difference; cert does not**.
- The pattern held in both topics: MP-guided answers gained on evidence labelling (IQ3) and competing explanations (IQ4), and **lost a point on clarity (IQ6) both times**. Both scorers named the MP concept table as overhead that renamed things already in plain language.
- The gains map onto the skill's *behavioural rules* (separate fact/inference, keep rivals alive with predictions, propose a diagnostic test), not obviously onto the MP concepts. The bread scorer said the reader "could skip its framework table and lose nothing".
- Content: the MP bread answer surfaced a real scientific debate (crystals vs gluten network) and the amylose/amylopectin melting-point gap; the MP cert answer surfaced a current extra cause (May 2026 chain change) and mapped probe results to causes. Plain answers had one overstatement (bread) and one unlabelled inference (cert).

## Limits

- n = 2 questions, one scorer per question; one run each, no repeat sampling.
- Same model family for answerers and scorers.
- Blinding is partial: the MP answers are recognisable by their concept table, and the bread one names "Memory Prism". The scorer wasn't told the hypothesis, but could see the style.
- Some sources reached only as abstracts/snippets by the answering agents (they say so).

## Owner's response

"Me needs a checklist to understand what something does, why and the bigger picture. AI and human capabilities are not up for comparison but humanity having a legup in understanding things is the point here." The rubric scores an assistant's answer for an expert reader; the concept table it penalises (IQ6) may be the part a non-specialist needs. This test measured the AI-led half only.

## Most useful next test

Add a third condition: the skill's behavioural rules (evidence labels, competing explanations with predictions, diagnostic next step, no homework handoff) **without** the MP concepts or inventory table. If it matches MP-guided on IQ3–IQ5 and beats it on IQ6, the value is in the rules; if MP-guided still wins, the concepts are adding something. Also strip the inventory table before scoring to remove the style cue.

---

# Appendix: score_bread
# Blind review: bread staling (Answer A vs Answer B)

Question: Why does sealed bread still go stale, and why does warming a stale slice soften it only for a while? Audience: curious non-specialist.

## Scores

### Answer A

| Dim | Score | Justification |
|---|---|---|
| IQ1 | 2 | The settled answer comes first ("Stale is not the same as dry", Boussingault 1852) and keeps the user's framing (bag, warming, "only for a while"). Caveat: A presents everything as settled and never names an open part, though it doesn't narrow or delay the answer either. |
| IQ2 | 1 | Core mechanisms are correct and sourced (gelatinization, retrogradation, amylose fast and amylopectin slow, the fridge range). But it overstates what reheating resets: "The reheated crumb is back in the same unstable, disordered state it was in fresh from the oven." Amylose crystals melt at about 150 °C, so ordinary reheating does not reset them. A never mentions this, and it is part of why revival is partial. |
| IQ3 | 1 | Most claims carry citations. But inferences are stated as fact with no marking, e.g. "it makes things a bit worse each time" and "Each heating drives off real water ... so it can end up harder than before". Nothing says what is measured versus inferred, or what wasn't tested. |
| IQ4 | 0 | One story is defended (starch recrystallization plus water movement). There is no rival explanation, such as gluten or polymer-network firming versus amylopectin crystals, and no statement that nothing competes. |
| IQ5 | 1 | "Eat the slice while it's warm ... freeze it rather than refrigerating it". This is specific and useful, but it is advice, not diagnostic. It wouldn't separate any explanations. |
| IQ6 | 2 | Clear and well paced for a non-specialist. Technical terms (gelatinization, retrogradation, syneresis) are defined when first used. Length fits. |
| **Total** | **7/12** | |

### Answer B

| Dim | Score | Justification |
|---|---|---|
| IQ1 | 2 | The "Short answer" opens with the settled mechanism and covers both parts of the question. The open part is clearly marked ("The main uncertainty"; "[Open question] ... re-staling after reheating is *faster*"). The framework table comes after the answer, so it doesn't bury it (it is penalised under IQ6). |
| IQ2 | 2 | Mechanisms are accurate and traced to named sources, including primary studies (Aguirre et al. on storage temperature; Baik & Chinachoti on crumb-to-crust migration). It correctly adds the amylose (~150 °C) versus amylopectin (~50–60 °C) melting gap, which explains why revival is partial. It sets scope: "literature-based answer". |
| IQ3 | 2 | Explicit [Fact] / [Reasonable inference] / [Open question] labels. It flags a claim it couldn't trace ("about six times faster ... couldn't trace it to a primary study") and says what it didn't test ("I didn't run either test above"). |
| IQ4 | 2 | It keeps two accounts of firmness alive: crystals versus cross-linked network and water redistribution. It cites evidence that separates them (gluten-enriched bread "less starch retrogradation yet firmed more"). For why revival fades, it sets water loss against recrystallization and gives a test with a predicted outcome (Next move 1). |
| IQ5 | 2 | Next move 1 is concrete, doable at home and diagnostic: "If the wrapped slice stays soft longer, water loss during reheating is a big part of why the revival fades." The literature step was already done. Small flaw: toasting is hotter than 60–70 °C, so the two arms differ in temperature as well as water loss. |
| IQ6 | 1 | The body is clear, but the "Memory Prism inventory" table (P-Memory, Board, Ledger, Legacy, No Sacred States) is a framework layer a non-specialist didn't ask for. It relabels domain ideas (e.g. storage temperature becomes "Board") and repeats content from the body. Journal-style citations add some weight but are acceptable. |
| **Total** | **11/12** | |

## Accuracy spot-check

**Answer A**
1. *Boussingault (1852): sealed bread still goes stale; reheating to ~60 °C reverses it (McGee via ckbk).* **Confirmed.** The ckbk page says Boussingault "showed that bread could be hermetically sealed to prevent it from losing water" and "that staling is reversed by reheating the bread to 140°F/60°C." The excerpt I got back did not show the year 1852. That is likely an artefact of the excerpt, and B quotes the same passage with 1852 in it.
2. *Staling is "enhanced drastically" between −8 and 8 °C, and fridge bread stales faster (Wikipedia).* **Confirmed.** Retrogradation (starch): "At temperatures between −8 °C (18 °F) and 8 °C (46 °F), the aging process is enhanced drastically." Staling: "bread stored in a refrigerator will have increased staling rates." The Staling article also has the "not simply a drying-out process" quote and the line that heating to 60 °C "partially" restores freshness, as A says.

**Answer B**
1. *Retrogradation was fastest at 4 °C among 25, 4 and −18 °C. At −18 °C only existing crystals grew (AGRIS).* **Confirmed.** Abstract (Aguirre et al. 2011, *Stärke*): "At 4°C the rate of starch retrogradation is the highest for the studied conditions" and "at −18°C only crystal growth may occur, whereas at 25 and 4°C there would be not only growth" [but also new crystals forming].
2. *Retrograded amylopectin melts at ~50–60 °C and amylose at ~150 °C (Constraints row, Wikipedia).* **Confirmed.** Retrogradation (starch): "The crystal melting temperature of amylose is much higher (about 150 °C (302 °F)) than amylopectin (about 50–60 °C (122–140 °F))." B's quote that amylose recrystallizes faster also matches ("Amylose crystallization occurs much faster than crystallization of the amylopectin").

None of the checked claims was wrong, so none of the scores changed on accuracy grounds. A's IQ2 deduction is for leaving out the amylose point, not for a wrong citation.

## Totals

- Answer A: **7/12**
- Answer B: **11/12**

## Overall verdict

Both answers get the core science right, and every claim I checked held up. A curious reader would understand staling from either one. Answer A reads more smoothly and has no jargon. But it presents a single tidy story as fully settled, says reheating returns the crumb to its fresh-from-the-oven state (it can't, because amylose crystals survive at ordinary reheating temperatures), and doesn't separate sourced facts from inference. Answer B answers the question just as directly up front. It adds the amylose/amylopectin melting gap, which is the real reason revival is only partial. It labels what is established, inferred and open, flags a figure it couldn't trace, names the real debate over crystals versus network and water, and gives a home test that could tell the explanations apart. Its one real weakness is the "Memory Prism" table, which is extra framework that a non-specialist would skip. Overall, Answer B would serve the reader better: it is more accurate on the "only for a while" part and more honest about where the evidence stops. A reader should skip its framework table.

---

# Appendix: score_cert
# Review: cert.md (certbot reports success, users still see expired certificates)

## Answer A

| Dim | Score | Justification |
|---|---|---|
| IQ1 | 2 | The "Short answer" comes first and gives the settled part: certbot's success "doesn't tell you which certificate each TLS endpoint is actually sending". The user's "sometimes" framing is kept (cause 2), and "What remains uncertain" names the open part. The MP table comes after the answer, so it doesn't bury it. |
| IQ2 | 2 | The mechanisms are accurate and each one is cited: deploy hooks vs pre/post hooks, exit status, `live/` symlinks, the Gen Y chain change, the end of expiry emails, ARI. Scope is stated ("I haven't inspected your systems"). Two small overreaches: "all profiles" moved to Gen Y (the sources name tlsserver, shortlived and classic), and Windows working "because they build their own path" (the thread says the self-signed X2 root was in the Windows store). Neither changes the advice. |
| IQ3 | 2 | Claims carry explicit tags: [Fact], [Reasonable inference] ("Causes 1 and 2 together are the most common…"), and [Open question]. The method note separates documentation and community reports from the one local reproduction, and says plainly that no live system was inspected. Minor: cause 4 is tagged [Fact], but the thread disputes the exact server-side cause. |
| IQ4 | 2 | Five causes, ranked. The "How to tell them apart" section ties each one to a different observation: "Old leaf on every path → cause 1; some paths → cause 2; current leaf but expired chain cert → cause 4; disk expiry near → cause 5". It also gives distinguishing context: cause 4 "if errors started around late May 2026, or only affect certain client platforms". |
| IQ5 | 2 | The per-IP, per-SNI `openssl s_client` fingerprint sweep is concrete and diagnostic, since its result picks the cause. The answer already ran the researchable step itself (a local reproduction of the stale in-memory certificate). The fixes are specific, including `--run-deploy-hooks` for testing. |
| IQ6 | 1 | The body is clear, but the "MP concept" table adds jargon that isn't domain language ("P-Memory", "Editors (candidate)", "Translator", "Ledger", "Lag"). It mostly repeats the causes section, so it is avoidable overhead for an engineering team. |

**Total: 11/12**

## Answer B

| Dim | Score | Justification |
|---|---|---|
| IQ1 | 2 | The "Short answer" comes first, and its issued / deployed / served distinction directly answers "why". Cause 2 addresses the "sometimes" explicitly ("unrelated restarts hide the bug"). |
| IQ2 | 2 | The facts are accurate and cited: the exit-status quote, deploy hook semantics, `fullchain.pem`, the end of expiry emails, and lifetime dates (Feb 10 2027 for 64 days, Feb 16 2028 for 45 days, May 13 2026 for tlsserver), all verified. It keeps the issued, deployed and served states separate, which the rubric's software note asks for. One small omission: it doesn't cover the May 2026 Gen Y chain change, which can produce "expired" errors with a valid leaf. It only notes that a missing intermediate looks "untrusted". |
| IQ3 | 1 | It reports the local `openssl s_server` check, and most claims are cited. But inference isn't labelled: cause 2 ("unrelated restarts hide the bug") is a plausible story presented as the explanation. Nothing says that the reader's systems weren't inspected or what wasn't tested. |
| IQ4 | 1 | It lists six causes, but doesn't tie them to the different observations that would separate them. The probe script detects a mismatch without mapping the result back to a specific cause. |
| IQ5 | 2 | Runnable code: a validated deploy hook, and a probe script that compares served and on-disk fingerprints and checks `-checkend`. It adds an audit step (`certbot certificates`, `nginx -T`). It already ran the local reproduction. The "Don't use `--force-renewal`" warning is useful. |
| IQ6 | 2 | Plain domain language throughout. The issued / deployed / served terms earn their place, and the length suits an engineering audience. |

**Total: 10/12**

## Accuracy spot-checks

**Answer A**
1. *Exit code 0 when nothing is due, and a failing hook doesn't make it non-zero [1].* **Verified.** The Certbot User Guide says: "exit status will only be 1 if a renewal attempt failed" and "If a hook exits with a non-zero exit code, the error will be printed to stderr but renewal will be attempted anyway." It also confirms the 1/3-lifetime threshold, the advice to point servers at `live/` rather than copies, and `--run-deploy-hooks` with `--dry-run`.
2. *Gen Y move in May 2026, and an expired ISRG Root X2 cross-sign served by some operators [4][5].* **Mostly verified.** The community post confirms tlsserver and shortlived moved to YE/YR intermediates on May 20 and classic around May 27/28 ("now complete"). The X2 thread confirms an expired X2 cross-sign appeared in some servers' chains from about May 28. It was attributed to operators serving custom chains, and it broke clients without X2 in their trust store (Linux, Palo Alto). Two details are slightly off: "all profiles" (tlsclient isn't mentioned), and the Windows explanation (the thread credits the self-signed X2 being in the Windows store, not path building as such). These are minor imprecisions, not material errors.

**Answer B**
1. *A failing deploy hook still gives exit 0 [8].* **Verified.** In the thread, `certbot renew ... --deploy-hook "false"` returned "Got exit code: 0", and a responder confirmed that Certbot only prints a warning.
2. *Lifetime schedule [6]: classic moves to 64 days on Feb 10 2027 and 45 days on Feb 16 2028; tlsserver went to 45 days on May 13 2026; ARI recommended; fixed 60-day schedules won't do.* **Verified exactly** against the Let's Encrypt "From 90 to 45" post.

No material errors were found in either answer.

## Overall verdict

Both answers get the core mechanism right and back it with verified sources: certbot's success covers only the files on disk, not the certificate that is loaded or served. Both prescribe the right fixes: a validated reload as a deploy hook, and external monitoring of the served certificate. **Answer A serves the reader somewhat better.** Its differential-diagnosis section turns the fingerprint sweep into a decision procedure that maps each result to a cause. It labels what is fact, what is inference and what is open, and says plainly that no live system was inspected. It also catches a real, current alternative cause that B misses: the May 2026 Gen Y chain change, with expired X2 cross-signs that only some clients reject. Answer B is cleaner and more directly usable. Its runnable hook and probe scripts, the issued / deployed / served framing, and the "accidental restarts hide it" explanation for the "sometimes" are clear strengths. A's MP-concept table is jargon overhead that adds little for engineers. The gap is narrow (11 vs 10). A wins on diagnostic structure and evidence labelling, B on clarity.

---

# Appendix: answer bread_base
# Why sealed bread still goes stale, and why warming it only helps for a while

## Stale is not the same as dry

Most people assume stale bread is just dried-out bread. In 1852 the French chemist Jean-Baptiste Boussingault showed that bread could be **hermetically sealed so it lost no water and still go stale**. He also found that **reheating it to about 60 °C (140 °F)** made it fresh again, which is the temperature at which wheat starch gels [1]. Food scientists still treat this as the central fact: staling "is not simply a drying-out process caused by evaporation," and it happens even in humid conditions [2][8]. A bag stops water escaping from the loaf. It does nothing about what is happening to the water and starch inside.

## What actually happens: the starch re-crystallizes

Flour is mostly starch, and raw starch sits in tiny, tightly packed, partly crystalline granules. When dough bakes, those granules soak up water from the dough, swell and lose their ordered structure. This is called **gelatinization**, and it happens at roughly 60–65 °C. It is why fresh crumb is soft and springy [4].

The trouble is that this disordered state is not stable. Once the bread cools, the long starch molecules slowly line up again and pack into firm crystalline regions. This is **retrogradation**, and it is directly responsible for bread staling [5][4]. Starch comes in two kinds, and they behave differently:

- **Amylose** (straight chains) re-crystallizes quickly, mostly within the first hours as the loaf cools. That helps set the loaf's structure [6][5].
- **Amylopectin** (bushy, branched chains) re-crystallizes slowly, over the following days. This is the main driver of staling during storage [6].

Water moves around inside the loaf as this happens. Retrogradation squeezes water out of the starch network, a process called syneresis [5], and moisture shifts from the starch granules into the spaces between them and into the gluten [2][7][9]. Water also moves from the moist crumb out to the drier crust. So even when the loaf as a whole has lost no water, the crumb ends up **feeling** drier and crumblier while the crust goes soft and leathery [6]. In short, a sealed loaf hasn't lost its water. The water has been locked up and moved around, and the starch has turned stiff and crystalline.

### Why the fridge makes it worse

Starch re-crystallizes fastest at cool temperatures just above freezing. Bakerpedia puts the fastest crumb firming at about −5 to 10 °C [6], and Wikipedia says staling "is enhanced drastically" between −8 and 8 °C [5]. Bread kept in the refrigerator therefore stales noticeably *faster* than bread kept on the counter [2][4]. A home freezer at around −18 to −20 °C nearly halts the process, which is why freezing fresh bread works and refrigerating it doesn't [4][2]. (The fridge does slow mould. It just trades mould for staleness.)

## Why warming it softens it again

Starch crystals that formed at room temperature are fairly weak, and they "melt" at modest temperatures. Heat the crumb back above the gelation temperature, about 60 °C, and the crystalline regions break apart. Water molecules slip back between the starch chains, and the crumb becomes tender again [7]. Bakerpedia notes that crumb firming can be reversed by brief heating to about 50 °C or more [6], and Wikipedia describes heating to 60 °C in an oven or microwave as *partially* restoring freshness [2]. This only works if most of the water released by the starch is **still inside the bread**, sitting in the gluten network, so the starch can take it back up [7]. That is why the trick works on a sealed, stale-but-not-dried loaf but not on a rock-hard heel left out on the counter.

## Why the softness doesn't last

Reheating doesn't remove the underlying tendency to re-crystallize. It just resets the clock, and it makes things a bit worse each time:

1. **The starch re-crystallizes as soon as it cools.** The reheated crumb is back in the same unstable, disordered state it was in fresh from the oven, and as it cools the starch starts lining up again. Scientific American puts it this way: the network becomes "rigid at room temperature and below," and the change "is reversed with the introduction of heat" [3]. Take the heat away and the rigidity returns.
2. **Each heating drives off real water.** An oven, toaster or microwave evaporates some moisture, especially near the surface. After reheating, the bread has less water to hold its starch in the soft state. Now it really is drying out, on top of re-staling, so it can end up harder than before. This is why the trick works less well each time you repeat it [6], and why a loaf that is "too old" can no longer be revived [7].

So warming a stale slice is a genuine, physical reversal of staling, not an illusion. But it's a temporary one. Eat the slice while it's warm, and if you want bread to last, freeze it rather than refrigerating it.

## Sources

1. "Staling" (*On Food and Cooking*, Harold McGee, via ckbk) – https://app.ckbk.com/reference/food00011c10s001e005se006se001/staling
2. Staling – Wikipedia – https://en.wikipedia.org/wiki/Staling
3. "Why does food get stale?" – Scientific American – https://www.scientificamerican.com/article/experts-why-does-food-get-stale/
4. "The Complexities of Bread Staling" – IUFoST – https://iufost.org/iufostold/wp-content/uploads/2017/04/66-The-Complexities-of-Bread-Staling.pdf
5. Retrogradation (starch) – Wikipedia – https://en.wikipedia.org/wiki/Retrogradation_(starch)
6. Bread Staling – BAKERpedia – https://bakerpedia.com/processes/bread-staling/
7. "Reheating Reverses Staling" (*On Food and Cooking*, Harold McGee, via ckbk) – https://app.ckbk.com/reference/food00011c10s001e005se006se002/reheating-reverses-staling
8. "Why does bread go stale?" – BBC Science Focus – https://www.sciencefocus.com/science/why-does-bread-go-stale/
9. "Did you know breadboxes really did help keep bread fresh?" – McGill Office for Science and Society – https://mcgill.ca/oss/article/did-you-know-history/did-you-know-breadboxes-really-did-help-keep-bread-fresh

---

# Appendix: answer bread_mp
# Why sealed bread still goes stale, and why warming only revives it briefly

## Short answer

Staling is mostly not bread drying out. It is the starch inside the bread slowly **recrystallising**. Baking melts starch's natural crystalline order into a soft, water-swollen gel. As the loaf cools and sits, the starch molecules gradually pack back into ordered, crystal-like regions and squeeze water out of the gel. A sealed bag keeps water from leaving the loaf, but it can't stop water moving around inside it, and it can't stop the starch reorganising.

Warming a stale slice past about 60 °C melts most of those new crystals, so the crumb softens again. Nothing has changed the underlying tendency, though, so the crystals start re-forming as soon as the slice cools. Each reheating also costs some water. That's why the revival is temporary and gets less effective each time.

## How I'm mapping the question (Memory Prism inventory, open to correction)

| MP concept | What I identify in this query |
|---|---|
| P-Memory (Persistent Memory) | Two layers of persistent order in the crumb: (1) a fast-forming amylose network that sets within hours of baking, and (2) slowly re-forming amylopectin crystals that build up over days. Staleness is that order coming back. |
| Constraints | Thermodynamics: the soft gel made by baking is not the stable state at room temperature, so ordering is "downhill." The melting points differ: retrograded amylopectin melts at about 50–60 °C, amylose at about 150 °C. That gap sets what a toaster can and can't undo. |
| Board | Storage temperature: freezer, fridge or counter. Each changes the rate and type of crystal growth, without changing the chemistry. |
| Ledger | The loaf's water budget. Sealing keeps the total fixed but not where the water sits: it moves from crumb to crust and from starch to gluten. Every reheating spends water to evaporation, which can't be bought back. |
| Legacy (candidate) | The amylose network survives ordinary reheating. It sets a ceiling on how "fresh" a revived slice can get. |
| No Sacred States (lens) | "Fresh" is not bread's natural resting state. It's a temporary, heat-made state, and staling is the system relaxing out of it. |

## What's going on

**1. Sealing isn't enough, and this has been known since 1852.** [Fact] In 1852 Jean-Baptiste Boussingault showed that "bread could be hermetically sealed to prevent it from losing water," yet it still went stale (McGee, via ckbk). The modern account is that moisture moves from the starch granules into the spaces between them, degelatinizing the starch, while amylose and amylopectin realign and recrystallize, producing the hard, leathery texture (Wikipedia, *Staling*).

**2. There are two kinds of starch, working on two timescales.** [Fact] Amylose recrystallizes faster and drives initial firmness; amylopectin recrystallizes more slowly and "is responsible for development of the long-term crystallinity" (Wikipedia, *Retrogradation*). In lab measurements, the melting signal for recrystallised amylopectin in bread crumb falls in the region 40–80 °C (Cereal Chemistry, 1996). Ordinary bread crumb, at roughly 35–40% moisture, sits close to the water content that is optimal for recrystallization (Cereal Chemistry, 1986). Bread is almost ideally set up to stale.

**3. Water moves around inside the sealed bag.** [Fact] In hermetically sealed white bread, moisture migrated from the crumb to the crust. Bread stored with its crust became significantly firmer after a week and showed more amylopectin recrystallisation than crust-free bread (Baik & Chinachoti, 2000). The bag stops water leaving the loaf. It doesn't stop the crumb drying while the crust goes leathery.

**4. Warming works because the new crystals melt at a low temperature.** [Fact] Staling "can be reversed by heating the bread above the gelation temperature of wheat starch, 140°F/60°C". This works only "as long as much of the water released by the starch granules remains in the surrounding gluten" (McGee, via ckbk). That explains why sealing still matters: it keeps the water close enough to be reabsorbed when you reheat. Reheated bread firms up again as it cools (IUFoST), because "As soon as the bread re-cools the starches will re-crystalize" (Gizmodo).

**5. Why the revival fades, and fades faster with each round.**
- [Fact] The amylopectin crystals simply start forming again at room temperature.
- [Reasonable inference] Toasting or oven heat drives off water each time, so the slice has less water available on every cycle. And at about 150 °C, the amylose network isn't undone by normal reheating. Each revival starts from a worse baseline.
- [Open question] I didn't find a solid source showing that re-staling after reheating is *faster* than the original staling, as opposed to just starting drier. That's plausible (for example, leftover crystal seeds could speed regrowth), but I'm treating it as unestablished.

**6. Storage temperature changes the rate.** [Fact] Retrogradation was fastest at 4 °C among 25, 4 and −18 °C. At −18 °C only existing crystals grew, while at 25 °C and 4 °C new crystals also formed (storage-temperature study, AGRIS). Freezing (about −20 °C) is "sufficient to almost halt the recrystallization process" (IUFoST). So the fridge is the worst place for bread texture, and the freezer is the best. (A widely repeated figure says bread stales "about six times faster" in the fridge, but I couldn't trace it to a primary study.)

## The main uncertainty

Is staleness mostly *crystals*, or mostly *water and network rearrangement*? One study found gluten-enriched bread had **less** starch retrogradation yet **firmed more**. The authors concluded firmness depends more on a cross-linked polymer network than on amylopectin crystals alone (Cereal Chemistry, 1996). The textbook "it's starch crystals" story is right about the main driver and about why 60 °C works. How much of what you *feel* comes from the crystals, compared with water redistribution and gluten, is still debated.

## Next moves (all doable at home)

1. **Separate water loss from recrystallisation.** Take two equally stale slices. Warm one in a sealed bag or foil to about 60–70 °C, and toast the other uncovered. Let both cool for an hour. If the wrapped slice stays soft longer, water loss during reheating is a big part of why the revival fades.
2. **Test the temperature effect.** Store matching slices on the counter, in the fridge and in the freezer for two days, then compare texture before and after a brief warm-up.
3. **If you want to go deeper,** search for "amylopectin retrogradation DSC bread crumb" and "moisture redistribution gluten starch staling." The question there is how much firmness each mechanism accounts for.

*Scope note: this is a literature-based answer. I didn't run either test above.*

## Sources

- Staling — Wikipedia: https://en.wikipedia.org/wiki/Staling
- Retrogradation (starch) — Wikipedia: https://en.wikipedia.org/wiki/Retrogradation_(starch)
- Staling / Reheating Reverses Staling — Harold McGee, *On Food and Cooking* (via ckbk): https://app.ckbk.com/reference/food00011c10s001e005se006se001/staling and https://app.ckbk.com/reference/food00011c10s001e005se006se002/reheating-reverses-staling
- This Is Why Your Bread Goes Stale — Gizmodo: https://gizmodo.com/this-is-why-your-bread-goes-stale-1566737883
- The Complexities of Bread Staling — IUFoST: https://iufost.org/iufostold/wp-content/uploads/2017/04/66-The-Complexities-of-Bread-Staling.pdf
- Moisture redistribution and phase transitions during bread staling (Baik & Chinachoti, Cereal Chemistry 2000) — AGRIS: https://agris.fao.org/search/en/records/65df4ed90f3e94b9e5d739d5
- Effect of storage temperature on starch retrogradation of bread staling — AGRIS: https://agris.fao.org/search/en/records/65df4ed90f3e94b9e5d73a52
- Breadmaking/staling study (Cereal Chemistry, 1996, 73:32) — AACC: https://www.cerealsgrains.org/publications/cc/backissues/1996/Documents/73_32.pdf
- Water and retrogradation in wheat starch gels and bread crumb (Cereal Chemistry, 1986, 63:407) — AACC: https://www.cerealsgrains.org:443/publications/cc/backissues/1986/Documents/Chem63_407.pdf
- How bread goes stale — FoodCrumbles: https://foodcrumbles.com/how-bread-goes-stale/
- Bread Goes Stale About Six Times Faster in the Refrigerator — TodayIFoundOut: https://www.todayifoundout.com/?p=6163

---

# Appendix: answer cert_base
# Why "certbot renew: success" still ends in expired-certificate errors

## Short answer

Certbot's success message means one thing: the certificate *files on disk* are fine. It does **not** mean the certificate your users get during the TLS handshake is the new one. There are three separate states: **issued** (new files in `/etc/letsencrypt/live/...`), **deployed** (every process and node that terminates TLS has loaded those files), and **served** (what clients actually receive). Your job only reports the first. One monitoring write-up puts it this way: "Successful issuance is not successful deployment", so "Treat renewal, deployment, and live serving as three separate states." [5]

## Why it happens (most likely first)

1. **The TLS server never reloaded.** Nginx, Apache, HAProxy, Postfix, Java apps and the like read the certificate at startup or reload and keep it in memory. Certbot replaces the files, and the old certificate stays in use until something reloads the process. The Let's Encrypt forums are full of "renewed, but the site still shows not secure until I restart nginx" threads, and the standard fix is a deploy hook that reloads the service [3][4]. I checked this locally: I started `openssl s_server`, swapped the certificate file underneath it, and the handshake kept presenting the old certificate (expiring tomorrow) while the file on disk showed the new one (90 days).

2. **Why only "sometimes": unrelated restarts hide the bug.** Certbot renews early. Before 4.0 it renewed at a fixed 30 days before expiry. Since 4.0 it renews when less than a third of the lifetime remains [1], and with ARI support (Certbot 4.1+) usually at about two-thirds of the lifetime [7]. That leaves weeks between renewal and expiry. If a deploy, a package upgrade or a reboot restarts the server during that window, it picks up the new certificate by accident. You only see an outage when no restart happens in time. Expect this to get worse: certificate lifetimes are shrinking (see the last section).

3. **"Success" covers no-ops and hook failures.** "certbot renew exit status will only be 1 if a renewal attempt failed". It exits 0 when nothing was due, too [1]. A failing deploy hook doesn't change that. Certbot prints a warning ("Hook 'deploy-hook' reported error code 1") and still exits 0, even printing "Congratulations, all renewals succeeded" [8][9]. So a `systemctl reload nginx` that fails because of a config error is invisible to a job that only checks the exit code.

4. **Other copies of the certificate.** These include other nodes behind a load balancer, a cloud LB or CDN with its own uploaded certificate, containers with a baked-in or stale mounted file, or a script that copied the PEMs once. In these cases, some replicas may not be updated, a container may have a stale mounted file, the wrong RSA or ECDSA lineage may be in use, or a CDN may terminate TLS with its own certificate [5]. Certbot's docs say to point servers *directly* at the files in `live/` (or symlink to them) rather than copying, because `live/` is what gets updated on renewal [1].

5. **The config points at the wrong lineage or file.** Examples: a vhost referencing an old `example.com-0001` lineage that nothing renews any more, a path under `archive/` instead of `live/`, or `cert.pem` where `fullchain.pem` belongs. For nginx `ssl_certificate` (and Apache 2.4.8+), the file you want is `fullchain.pem` [1]. A missing intermediate shows up as "untrusted" rather than "expired", but it comes from the same blind spot: nobody checks what's actually being served.

6. **Nothing external will warn you any more.** Let's Encrypt stopped sending expiration-notification emails on June 4, 2025, and recommends a third-party monitor instead [2]. If those emails used to be your safety net, it's gone.

## How to stop it recurring

**1. Add a validated reload as a deploy hook, set once globally.** A deploy hook runs "once for each successfully issued certificate". Executables in `/etc/letsencrypt/renewal-hooks/deploy/` run for every lineage [1]:

```sh
#!/bin/sh
# /etc/letsencrypt/renewal-hooks/deploy/50-reload-nginx  (chmod +x)
set -e
nginx -t                 # refuse to reload a broken config
systemctl reload nginx
```

For multiple nodes, LBs or CDNs, the hook (or a pipeline it triggers) must push the new certificate to *every* termination point and reload each one. Copies are fine only if you treat distribution as a monitored step.

**2. Make hook failures loud.** Certbot won't fail the run for you [8][9], so have the hook alert on any non-zero step (curl a webhook, push a metric). Then test it end to end with `certbot renew --dry-run`, and afterwards check that the served certificate actually changed.

**3. Monitor the served certificate, not the file.** From outside, on every IP, region, listener and SNI name, compare the served certificate with the one on disk and alert on mismatch or low remaining days [5]:

```sh
served=$(echo | openssl s_client -connect "$IP:443" -servername "$HOST" 2>/dev/null \
         | openssl x509 -noout -fingerprint -sha256)
disk=$(openssl x509 -in /etc/letsencrypt/live/$NAME/fullchain.pem -noout -fingerprint -sha256)
[ -n "$served" ] && [ "$served" = "$disk" ] || alert "stale or unknown cert on $IP"
echo | openssl s_client -connect "$IP:443" -servername "$HOST" 2>/dev/null \
  | openssl x509 -noout -checkend $((14*86400)) || alert "served cert expires <14d"
```

Treat a failed probe or parse as a failure, never as a match [5]. Blackbox exporter, Uptime Kuma, or the third-party service Let's Encrypt suggests [2] can each do the remaining-days check.

**4. Audit what references which lineage.** Run `certbot certificates`, then `nginx -T | grep ssl_certificate` (or the equivalent for your server), and delete orphaned lineages and stray copies.

**5. Don't "fix" it with `--force-renewal`.** If the certificate on disk is already new, reissuing won't fix a loading or distribution problem, and it uses up rate limits [5].

## Why this is getting urgent

Let's Encrypt's default (`classic`) profile moves to **64-day certificates on Feb 10, 2027** and **45-day certificates on Feb 16, 2028**. The opt-in `tlsserver` profile went to 45 days on May 13, 2026. Let's Encrypt advises using ARI, not relying on fixed 60-day schedules, avoiding manual renewal, and monitoring renewals [6]. Shorter lifetimes shrink the window in which an accidental restart covers for a missing reload, so this intermittent failure will become a frequent one unless the reload and served-certificate checks above are in place. Make sure you're on Certbot 4.1+ so ARI-driven renewal timing applies [7][10].

## Sources

1. User Guide, Certbot documentation: https://eff-certbot.readthedocs.io/en/stable/using.html
2. Ending Support for Expiration Notification Emails, Let's Encrypt: https://letsencrypt.org/2025/01/22/ending-expiration-emails/ (and "Expiration notification service has ended": https://letsencrypt.org/2025/06/26/expiration-notification-service-has-ended)
3. Certificate is renewed but connection shows as not secure till you restart nginx, Let's Encrypt Community: https://community.letsencrypt.org/t/certificate-is-renewed-but-connection-shows-as-not-secure-till-you-restart-nginx/165695
4. Expired certificates detected after a renewal (Certbot, nginx), Let's Encrypt Community: https://community.letsencrypt.org/t/expired-certificates-detected-after-a-renewal-certbot-nginx/135107
5. How to alert when automated Let's Encrypt renewal succeeds but the service still serves the old certificate, OneUptime: https://oneuptime.com/blog/post/2026-08-26-how-to-alert-when-automated-lets-encrypt-renewal-succeeds-but-the-service-still-serves-the-old-certificate/view
6. Decreasing Certificate Lifetimes to 45 Days ("From 90 to 45"), Let's Encrypt: https://letsencrypt.org/2025/12/02/from-90-to-45
7. Certbot 4.1.0 Release, Let's Encrypt Community: https://community.letsencrypt.org/t/certbot-4-1-0-release/238369
8. Deploy hook failure doesn't make certbot renew command fail, Let's Encrypt Community: https://community.letsencrypt.org/t/deploy-hook-failure-doesnt-make-certbot-renew-command-fail/140367
9. Certbot deploy hook failure is hidden very well, Let's Encrypt Community: https://community.letsencrypt.org/t/certbot-deploy-hook-failure-is-hidden-very-well/199527
10. ACME Renewal Information (ARI), Let's Encrypt: https://letsencrypt.org/2026/03/17/acme-renewal-information-ari

---

# Appendix: answer cert_mp
# Certbot says "success", but users see expired certificates

**Short answer:** a successful `certbot renew` only tells you that the files under `/etc/letsencrypt/live/` are fine, or didn't need changing yet. It doesn't tell you which certificate each TLS endpoint is actually sending to users. Certbot's exit code is 0 when nothing was due for renewal, and a failing hook doesn't make it non-zero [1]. So "logs success every time" is consistent with users being served an old certificate. The fix is to treat deployment as its own step, check that step from the client side, and alert on what clients actually receive.

| MP concept | What I identify in this query |
|---|---|
| P-Memory (Persistent Memory) | The certificate a running process loaded at startup stays in its memory after the file on disk changes. The same goes for copied files, container snapshots, certificates uploaded to a CDN or load balancer, and hand-built chain files. |
| Constraints | The certificate's fixed `notAfter` date. The lifetime is getting shorter: 64 days from Feb 2027 and 45 days from Feb 2028 [2]. The client's trust store also limits which chains it will accept. |
| Editors (candidate) | Nothing replaces the stale copy unless a reload or redeploy happens. That depends on a hook that may be missing or broken. |
| Translator | Your success check reads certbot's exit code and logs. The user's TLS client reads the served certificate and chain. These two checks look at different things. |
| Ledger | The renewal margin is about one-third of the lifetime [1]. That is about 30 days now and about 15 days once certificates last 45 days. Every week a broken deployment goes unnoticed uses up part of it. |
| Lag | Issuing a certificate and serving it are separate steps. A stale copy causes no visible problem until its own expiry date arrives. |

## Why it happens (most likely first)

**1. The new certificate is on disk, but the server never loaded it.** [Fact] Pre- and post-hooks run on every renewal attempt. Deploy hooks run only after a successful renewal [1]. With `certonly --webroot` or `--standalone` and no deploy hook (or an empty `renewal-hooks/deploy/` directory), nothing tells nginx, HAProxy, Postfix or a Java app to reload. I tested this in a scratch experiment with a local TLS server. After the files were swapped, the server kept sending the old certificate (same SHA-256 fingerprint, old `notAfter`) until it was restarted. Only then did it send the new one. The server stays up, so nothing looks wrong for about 30 days, and then it starts sending an expired certificate.

**2. Some serving paths get the new certificate and others don't.** This fits the "sometimes" in your question. A deployment-focused write-up lists the usual causes [3]:
- Only one of several nodes runs certbot.
- A vhost points to a copied file instead of the `live/` symlink.
- A container has a stale bind mount or a certificate baked into the image.
- A CDN, load balancer or ingress terminates TLS with its own uploaded copy.
- An A or AAAA record points to an origin that was never updated.
- The RSA and ECDSA lineages have drifted apart.

Users who reach a stale path get errors. Everyone else is fine. Certbot's docs say to point servers directly at the `live/` files or symlinks, not at copies [1].

**3. The deploy hook ran and failed, and certbot still exited 0.** [Fact] A failing hook doesn't directly cause a non-zero exit [1][3]. Typical failures are a reload that hits a config error, a permissions error, or a copy step that fails partway through.

**4. The leaf certificate is current, but the chain is out of date.** [Fact] Let's Encrypt moved all profiles, including `classic`, to the new Generation Y intermediates in May 2026 [4]. Operators who serve a hard-coded or cached chain file ended up sending an **expired ISRG Root X2 cross-sign**. Clients that don't have X2 in their trust store reject it. Windows clients often work anyway because they build their own path, so only some users see the error [5]. Browsers usually report this as an "expired certificate" even though the leaf is valid. Always serve `fullchain.pem` exactly as ACME returns it.

**5. A renewal really did fail, and nobody was warned.** [Fact] Let's Encrypt stopped sending expiry-warning emails on June 4, 2025 [6][7]. If those emails were your safety net, you no longer have one.

[Reasonable inference] Causes 1 and 2 together are the most common explanation for "success logged, users hit expiry sometimes". Cause 4 is the main alternative if the errors started around late May 2026, or only affect certain client platforms.

## How to tell them apart (do this first)

For every IP address of every hostname (A and AAAA, each region, each SNI name), run:

```
openssl s_client -connect IP:443 -servername HOST -showcerts </dev/null
```

Compare the leaf's SHA-256 fingerprint with the leaf in `/etc/letsencrypt/live/HOST/fullchain.pem`. Compare fingerprints rather than dates [3].
- Old leaf on every path → cause 1.
- Old leaf on some paths → cause 2.
- Current leaf, but the chain includes an expired certificate → cause 4.
- `certbot certificates` shows the expiry date on disk is near → cause 5.

Then check `/var/log/letsencrypt/letsencrypt.log` to see whether a hook ran and what it returned.

## How to stop it recurring

1. **Make a reload part of renewal.** Put an executable script in `/etc/letsencrypt/renewal-hooks/deploy/` that runs `nginx -t && systemctl reload nginx` (or your equivalent) and exits non-zero on failure. If certificates are distributed to other nodes, CDNs, Kubernetes secrets or appliances, this script should push them there too. Test it with `certbot renew --dry-run --run-deploy-hooks` [1].
2. **Alert on what's served, not on certbot's exit code.** Run an external probe against every endpoint. Alert when the served fingerprint doesn't match what's on disk, when the served certificate has less than about a third of its lifetime left, or when the probe itself fails or goes stale [3]. Let's Encrypt points to external monitors such as Red Sift Certificates Lite as a replacement for its emails [7].
3. **Have one renewer per name, or one distribution step.** Don't let replicas renew independently or keep their own copies.
4. **Don't hard-code chains, and don't pin intermediates.** Let's Encrypt picks the intermediate at random on each issuance to discourage pinning [8].
5. **Get ready for shorter lifetimes.** Upgrade to Certbot 4.1 or later. It uses ACME Renewal Information (ARI) and renews at about two-thirds of the lifetime [9]. Remove any fixed "every 60 days" schedule, which won't work with 45-day certificates [2]. Run renewal at least daily.

## What remains uncertain

[Open question] I can't see your topology. Whether the errors line up with particular nodes, IP addresses or CDN edges (cause 2), or with particular client platforms (cause 4), is what separates the explanations. The per-IP fingerprint sweep above answers that within minutes.

*Method note: this is based on documentation and community reports, plus one local reproduction of cause 1. I haven't inspected your systems.*

## Sources
1. Certbot User Guide (hooks, renewal threshold, exit status, live directory) — https://eff-certbot.readthedocs.io/en/stable/using.html
2. Let's Encrypt, "Decreasing Certificate Lifetimes to 45 Days" — https://letsencrypt.org/2025/12/02/from-90-to-45
3. OneUptime, "Alert When Let's Encrypt Renews but a Service Uses the Old Certificate" — https://oneuptime.com/blog/post/2026-08-26-how-to-alert-when-automated-lets-encrypt-renewal-succeeds-but-the-service-still-serves-the-old-certificate/view
4. Let's Encrypt Community, "Upcoming Let's Encrypt Profile Changes On May 13, 20th, and 27th" — https://community.letsencrypt.org/t/upcoming-let-s-encrypt-profile-changes-on-may-13-20th-and-27th/247049
5. Let's Encrypt Community, "Possible expired ISRG Root X2 cert included in chain starting ~May 28th?" — https://community.letsencrypt.org/t/possible-expired-isrg-root-x2-cert-included-in-chain-starting-may28th/247784
6. Let's Encrypt, "Expiration notification service has ended" — https://letsencrypt.org/2025/06/26/expiration-notification-service-has-ended
7. Let's Encrypt, "Ending Support for Expiration Notification Emails" — https://letsencrypt.org/2025/01/22/Ending-Expiration-Emails
8. Let's Encrypt, "A New Generation of Roots and Intermediates (Gen Y)" — https://letsencrypt.org/2025/11/24/gen-y-hierarchy
9. Let's Encrypt Community, "Certbot 4.1.0 Release" — https://community.letsencrypt.org/t/certbot-4-1-0-release/238369

## Score line

Label-blind; partial blinding only (MP answers recognisable by style).

SCORES: IQ_bread_plain=7/12; IQ_bread_mp=11/12; IQ_tls_plain=10/12; IQ_tls_mp=11/12; scorer=independent agent; blind=yes