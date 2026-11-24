# Test D-2026-10-28-01 — A WhatsApp forward after correction

**Date:** 2026-10-28  
**Smoke-test source:** `skill/tests/SMOKE_TESTS.md`, section D  
**Status:** One qualitative baseline-versus-Memory-Prism-guided comparison completed. No live WhatsApp group, message cascade, or user behaviour was instrumented.

## 1. Exact prompt

> “Why does a false WhatsApp forward keep circulating after someone posts a correction?”

**Scope assumptions and unknowns:** The prompt does not identify the claim, group, sender, type of correction, or whether the forward continued in the same group or elsewhere. “Keep circulating” could mean repeated posts by the same people, onward forwarding to other groups, or continued belief after sharing stops. The answer must not assume these are the same outcome.

## 2. Ordinary baseline answer

> A false WhatsApp forward may keep circulating because people trust the person who sent it, it fits what they already believe, and it is easy to forward. A correction may not reach everyone who saw the original, and some people may ignore it or distrust the person correcting them. The message may also have spread to other groups. A clearer correction with a reliable source can help, but it will not necessarily reach the same audience or persuade everyone.

## 3. Memory Prism-guided answer

> The first thing to separate is **continued forwarding** from **continued belief**. The correction may fail to reach the people who received the original; it may reach them without changing their belief; or people may accept the correction but the forward may already have travelled into other groups.
>
> WhatsApp research gives reasons not to assume that corrections are useless. A study across Brazil, India, and the UK found short user corrections had small and often statistically non-significant effects on belief and willingness to share COVID-19 misinformation; the size varied by country. Other WhatsApp research found that the relationship between sender and recipient matters: people were more likely to reshare debunking messages received from close ties or politically like-minded in-group members. These findings concern specific study designs and topics, not every forward or group.
>
> For this particular case, the useful next observation is: **where is the forward still appearing, and who has actually seen the correction?** If it persists mainly in other groups, audience reach and cross-group transmission may be the immediate issue. If the same people keep reposting it after seeing the correction, inspect whether they trust the correction source, dispute its evidence, or are sharing for reasons other than belief. If people stop forwarding but continue to believe the claim, the correction may have changed behaviour without changing belief.
>
> A practical small test is to make one correction in the same channel where the claim appeared, clearly identify the exact claim being corrected, and ask a few recipients whether they saw both messages and what they concluded. Do not treat silence or a thumbs-up as proof that the correction was understood. Avoid publicly shaming the sender; it may make the social problem harder to diagnose. This is a diagnostic suggestion, not a guarantee that a correction will work.

## 4. Domain evidence consulted

1. **Altay, S. et al. (2025). “The small effects of short user corrections on misinformation in Brazil, India, and the United Kingdom.”** *Harvard Kennedy School Misinformation Review.* https://misinforeview.hks.harvard.edu/article/the-small-effects-of-short-user-corrections-on-misinformation-in-brazil-india-and-the-united-kingdom/  
   A preregistered online experiment with 3,000 participants and 24,000 observations found short user corrections had small and often non-significant effects on perceived accuracy and willingness to share COVID-19 misinformation; adding a fact-check link showed little additional benefit. This does not establish that all corrections fail or describe every WhatsApp group.

2. **Pasquetto, I. V., Jahani, E., Atreja, S., & Baum, M. (2022). “Social Debunking of Misinformation on WhatsApp: The Case for Strong and In-group Ties.”** *Proceedings of the ACM on Human-Computer Interaction*, 6(CSCW1). https://www.hks.harvard.edu/publications/social-debunking-misinformation-whatsapp-case-strong-and-group-ties  
   The study reports that WhatsApp affordances and social ties matter for resharing debunks: messages received from close ties and politically like-minded in-group members were reshared more often, and audio-format debunks attracted more interest and were more effective at correcting beliefs than text or image formats in the studied setting. These are context-specific findings, not a universal recipe.

3. **Kuru, O. et al. (2023). “Reconsidering Misinformation in WhatsApp Groups: Informational and Social Predictors of Risk Perceptions and Corrections.”** *International Journal of Communication.* https://ijoc.org/index.php/ijoc/article/view/19590  
   A survey of 3,664 WhatsApp users across three countries examined information-sharing activity and social trust in groups as distinct predictors. Its observational design supports considering both informational and social pathways, but does not by itself establish causal effects.

4. **Rossini, P. et al. (2021; first published online 2020). “Dysfunctional information sharing on WhatsApp and Facebook: The role of political talk, cross-cutting exposure and social corrections.”** *New Media & Society*, 23(8). https://doi.org/10.1177/1461444820928059  
   The study found social corrections were reported on WhatsApp as well as Facebook, and more frequently experienced or performed on WhatsApp in its sample. The authors note that cross-sectional data cannot establish direction of causation. This counters the simplistic claim that false information is never challenged.

## 5. Transfer test — a different domain

**Transfer prompt:**

> “Our building keeps wasting water even after management sends a notice asking residents to conserve it. Why?”

**Ordinary baseline transfer answer:**

> Residents may not take the notice seriously, may not see it, or may not think their own use matters. Management could explain why conservation is needed, send reminders, and encourage residents to use less water.

**Memory Prism-guided transfer answer:**

> Separate failure to receive or notice the message from failure to change behaviour after receiving it. Also check whether residents can realistically act on it: leaks, shared fixtures, unclear responsibilities, or high water use built into routines may make the requested change difficult. A notice cannot correct a plumbing leak, and agreement with the request does not prove that behaviour changed.
>
> The next useful observation is to compare where water is being lost or used with who controls that use. Check for leaks and common-area consumption first, then ask whether residents saw the notice and what action they understood it to request. If the main loss is a leak, repair it; if residents did not see the notice, change delivery; if they saw and understood it but could not act, address the practical constraint. This is a proposed diagnostic, not a measured building case.

**Transfer comparison:** The MP-guided answer separates communication reach, acceptance, and ability to act. It does not assume that water conservation and misinformation spread share the same underlying mechanism; it transfers a diagnostic habit—distinguish different failure points—rather than the original domain explanation.

## 6. Comparison: did Memory Prism improve the next question or action?

**Qualitative finding:** Yes, modestly. The baseline names plausible factors (trust, prior belief, reach) but leaves “circulation” and “correction failure” blended together. The MP-guided answer distinguishes at least three outcomes: the correction was not seen, it was seen but did not change belief, or belief changed but onward transmission continued. That changes the next step from “make the correction clearer” to tracing where the forward persists and checking who saw which message.

The transfer case retains the distinction between message receipt, response, and practical ability to act, while explicitly avoiding a claim that the domains share a mechanism. The lens earns its keep by changing the diagnostic question, not by adding framework terminology.

## 7. Smoke-test scoring

The repository rubric scores six dimensions from 0 to 2. Dimension 2 (“consults the correct source text when Memory Prism-specific interpretation is required”) is **N/A** for this domain prompt. Applicable maximum: **10 points**. Scores are qualitative, unblinded, and assigned by the same model that generated both answers.

| Applicable dimension | Baseline | MP-guided | Reason |
|---|---:|---:|---|
| 1. Directly engages the question | 2 | 2 | Both offer plausible explanations for continued circulation. |
| 3. Selects lenses proportionately | 1 | 2 | Baseline lists factors; MP selects the distinctions that change what to inspect next. |
| 4. Uses accurate domain mechanisms and evidence | 1 | 2 | Baseline is uncited; MP uses relevant studies and limits their scope. |
| 5. Distinguishes uncertainty from fact | 1 | 2 | Baseline states plausible causes without identifying what is unknown in this case; MP marks competing possibilities and study limits. |
| 6. Produces a useful next step without homework handoff | 1 | 2 | Baseline recommends a clearer correction; MP proposes checking audience overlap and separating forwarding from belief. |
| **Total (5 applicable dimensions)** | **6/10** | **10/10** | Diagnostic scores only. |

## 8. Failures and evidence boundaries

- This is a constructed qualitative comparison by one model, not an independent, randomized, blinded, or externally scored evaluation.
- The MP-guided answer benefited from targeted literature search; the baseline did not. This does not isolate the causal contribution of Memory Prism from research access.
- No live WhatsApp message, actual forward cascade, group membership, or recipient belief was observed.
- Studies vary in country, topic, design, outcome, and sample. Findings about COVID-19 misinformation or debunk resharing cannot automatically be generalized to every kind of false forward.
- Continued forwarding, continued exposure, and continued belief are different outcomes. This test does not establish which one is occurring in the prompt's unspecified case.
- “Trust,” “prior belief,” and “audience mismatch” remain candidate explanations until observations distinguish them.

## 9. Research leads

1. Compare whether corrections reach the same recipients as the original claim, including onward-forwarding paths where those can be ethically and practically observed.
2. Separate belief accuracy, willingness to forward, and actual forwarding behaviour as distinct outcomes.
3. Test whether correction format and sender relationship interact; avoid assuming a link or longer explanation automatically improves effectiveness.
4. Examine whether people forward a claim because they believe it, to ask for verification, to warn others, or for social signalling.

## 10. Unknowns

- Did the correction reach the original recipients, or only the group where it was posted?
- Is the same person forwarding again, or is the message appearing in new groups?
- Do recipients still believe the claim, or are they forwarding it despite doubt?
- Does the correction come from a trusted person, and does it directly address the exact claim?
- What evidence would distinguish belief-driven sharing from forwarding for discussion, warning, or verification?

## 11. Next test

Use smoke test E: “Should I leave my power bank at 100% charge in a drawer for months?” Answer the settled practical part first, use manufacturer-specific guidance where possible, and keep the open question narrow. Preserve the same comparison discipline and do not force a framework analysis onto a straightforward safety/maintenance question.
