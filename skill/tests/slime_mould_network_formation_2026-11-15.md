# Slime Mould Network Formation — 2026-11-15

## Test type
Normal daily test. Topic selected independently of recent conversation topics and projects.

## Question
How does *Physarum polycephalum* form useful transport networks, and does its behaviour demonstrate optimisation?

## Observation
*Physarum polycephalum* is a plasmodial slime mould. Its visible network consists of tubes through which material circulates. When food sources are available at different locations, the organism explores its environment and develops connections between them.

A key mechanism is flow-dependent tube adaptation:
- Tubes carrying greater flow tend to strengthen or widen.
- Tubes carrying less flow tend to narrow.
- The network is continually remodelled as resource distribution and flow change.

This local feedback can generate network-level organisation without a central controller calculating a complete route map.

## The Tokyo railway comparison
A 2010 *Science* study placed oat flakes at locations corresponding to cities around Tokyo and observed the network formed by the slime mould. Researchers compared the resulting networks with the Tokyo rail system using measures including construction cost, transport efficiency and fault tolerance.

The slime mould generated economical networks with useful transport properties. However, the comparison was not a demonstration that it universally outperformed human engineering: the real railway network showed stronger resilience to some single-link failures, and biological outcomes varied between trials.

## What the experiment establishes — and what it does not
Supported:
- Local physical feedback can generate useful global network structure.
- The organism remodels connections as flow changes.
- The resulting networks can be compared quantitatively with engineered networks.

Not established:
- That the organism computes shortest paths in a human-like sense.
- That it always finds a global optimum.
- That its solutions are superior to engineered networks across all objectives.
- That a biological mechanism can be transferred directly into infrastructure software without accounting for domain-specific constraints.

The organism balances competing considerations such as network extent, transport and robustness. “Efficiency” is therefore not a single self-evident objective.

## Memory Prism inventory
| MP concept | What I identify in this query |
|---|---|
| Board | Physical environment containing food sources, substrate and barriers. |
| Memory | Existing tubes persist and influence subsequent circulation and remodelling. |
| Constraints | Food locations, distance, substrate, physical barriers and growth/maintenance costs. |
| Editors | Flow-dependent reinforcement and constriction of tubes. |
| Flow Under Constraint | Nutrient circulation and network growth through available routes. |
| Audits | Tube structure and measured network performance provide observable evidence of adaptation. |
| Identity | The organism remains one connected plasmodium despite its distributed network. |
| Working Lines | Local feedback rules produce a network-level outcome. |
| No Sacred States | A route useful earlier can weaken or disappear when conditions change. |
| Accumulation Patterns | Repeated flow reinforces selected pathways over time. |

## Critical Thinking examination
- Distinguish a useful network from a mathematically optimal network.
- Identify which objective is being optimised: length, efficiency, resilience or a weighted combination.
- Do not infer intention or route calculation from the visual outcome.
- Ask whether the comparison uses equivalent constraints and failure conditions.
- Treat biological variability as evidence, not merely experimental noise to ignore.

## Findings
The interesting property is not intelligence in a human sense. It is the production of useful network structure through local feedback acting on a persistent physical network. The structure both records past flow and changes the routes available for future flow.

The engineering lesson is conditional: decentralised adaptation may be useful where conditions change and local information is more available than a complete central picture. It does not remove the need to define objectives, constraints and failure tolerance.

## Limits and unresolved questions
- Different experimental layouts and resource distributions may produce different network structures.
- Performance depends on the chosen objective and metric.
- The biological system's ability to adapt does not automatically establish robustness under all disturbances.
- Translating the mechanism into an algorithm requires explicit treatment of constraints, costs and recovery behaviour.

## Sources
- Tero et al. (2010), “Rules for Biologically Inspired Adaptive Network Design,” *Science*: https://www.science.org/doi/10.1126/science.1177894
- Review and related work on *Physarum* network adaptation: https://pubmed.ncbi.nlm.nih.gov/?term=Physarum+network+adaptation+flow+tube+diameter

## Provenance
Prepared from the 2026-11-15 daily test research and analysis in this conversation. This is a research synthesis, not a new experiment.
