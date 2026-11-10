# Automaticity Stress Test — Gecko Adhesion and Release

**Test ID:** AUTO-2026-11-10-01  
**Date:** 2026-11-10  
**Skill under test:** Automaticity — [canonical SKILL.md](https://github.com/memoryprismv1/cognitive-interface-ai-skills/blob/main/automaticity/SKILL.md)  
**Skill revision:** blob `2964f0894e2b163e5aecdb413b4b6ada8b14d6d4`  
**Visible signal:** `[Automaticity used]`  
**Method:** Same-content writing stress test: a deliberately dense AI-pasta comparator followed by an Automaticity rewrite. Both versions were produced by the same assistant in the same context. This is not a blind test, an independently scored test, or a true skill-disabled baseline.

## Question

How do geckos stick to walls and ceilings, then let go?

## Test design

The existing [gecko test record](gecko_toe_pad_adhesion_detachment_2026-11-10.md) provides a research-backed fact base. This test reuses its core explanation so the comparison focuses on language rather than introducing a new scientific topic.

The first version is deliberately written in an AI-pasta style. It is a stress-test comparator, not a claim about what an unassisted model would always produce. The second version applies Automaticity. Both should preserve the same core ideas.

## Version A — AI-pasta comparator

Gecko attachment to vertical and inverted surfaces is enabled by a hierarchical adhesive architecture in the toe pads, where microscopic setae branch into nanoscale spatulae that collectively maximise effective contact area. This extensive interface allows individually weak van der Waals interactions to combine into substantial dry adhesion and friction, without reliance on adhesive secretions or suction-based attachment. The animal modulates engagement through active toe placement and rolling movements; detachment is achieved by reversing toe orientation and progressively peeling the adhesive structures away from the substrate. Resulting performance remains contingent on substrate roughness, contamination, interfacial water films, and morphological differences between species, so adhesion is not uniform across all surfaces or environmental conditions.

## Version B — Automaticity

[Automaticity used]

Geckos can cling to walls and ceilings because their toe pads make very close contact with a surface.

Each toe pad has tiny hairs called setae. Each hair branches into even smaller tips called spatulae. Together, those tips touch a large area of the surface.

In the species studied, this close contact lets many weak attractions add up to strong dry adhesion. These attractions are called van der Waals forces. The toe structures also help create grip and friction. Geckos do not need glue or suction cups.

**The gecko controls the grip with its toes.** It presses and rolls them onto the surface to attach. To let go, it changes the angle and peels the tips away, much like lifting tape from one edge.

The grip depends on the surface. Roughness, dirt, water films and differences between species can change how well it works. Water can weaken the grip when a thin film separates the tips from the surface. Wet performance varies.

## Content-preservation check

| Content in the comparator | Preserved in Version B? | How |
|---|---|---|
| Hierarchical toe-pad structure | Yes | Hairs (setae) branch into smaller tips (spatulae). |
| Large close-contact area | Yes | Explained as many tiny tips touching a large surface area. |
| Van der Waals dry adhesion | Yes | The weak attractions are named and their combined effect is stated. |
| Adhesion and friction | Yes | Both grip and friction are retained. |
| No glue or suction | Yes | Stated directly in familiar words. |
| Active toe placement and rolling | Yes | Pressing and rolling the toes is explicit. |
| Peeling detachment | Yes | Angle change and progressive peeling are retained, with a tape analogy. |
| Surface and species limits | Yes | Roughness, dirt, water films and species differences remain. |
| Wet-condition qualification | Yes | Water-film separation and variable wet performance remain. |

## Findings

**Reading friction:** Version B breaks the noun-heavy opening into a sequence the reader can follow: toe structure → close contact → combined attraction → controlled attachment and release → limits. It replaces phrases such as “hierarchical adhesive architecture”, “effective contact area” and “interfacial water films” with familiar words and explicit actions.

**Idea preservation:** The comparison retained all of the listed content points. The technical terms were not erased; setae, spatulae and van der Waals forces remain, but their roles are explained in ordinary language.

**Causal clarity:** The most useful change is making the gecko's active control visible. It presses and rolls to attach, then changes the angle and peels to release. The tape comparison makes the release motion easier to picture without replacing the physical explanation.

**Selective emphasis:** One bold sentence promotes the key action: the gecko controls its grip with its toes. The formatting does not carry information that is missing from the prose.

**Length:** Version B is not necessarily shorter. It uses more sentences and spells out relationships that Version A compresses into technical phrases. This is consistent with the skill's rule: reduce processing friction, not substance.

## Result

**Provisional positive result for this writing probe.** Automaticity produced a more accessible explanation while retaining the comparator's core claims and qualifications. The gain is in the form and the visibility of the causal sequence, not in a new scientific mechanism.

This does not establish that readers will understand or remember Version B better. No reader timing, comprehension test, recall measure, blind comparison, or independent assessment was conducted. The comparator was intentionally made dense, so this test does not measure the size of the effect against ordinary unassisted model output.

## Next test

Use a naturally occurring answer that is already AI-pasta-heavy, rather than a deliberately constructed dense comparator. Rewrite it with Automaticity and check whether the simpler form preserves distinctions, conditions and uncertainty without adding unnecessary length or losing technical precision.

## Source basis

- [Prior gecko explanation and its evidence references](gecko_toe_pad_adhesion_detachment_2026-11-10.md)
- [Automaticity — canonical skill instructions](https://github.com/memoryprismv1/cognitive-interface-ai-skills/blob/main/automaticity/SKILL.md)
