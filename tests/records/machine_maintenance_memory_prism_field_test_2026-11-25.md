# Machine Maintenance: Memory Prism Across Physical Systems

**Record date:** 2026-11-25  
**Record type:** Cross-case field-test synthesis  
**Status:** Completed desk-based application; not a controlled performance evaluation  
**Scope:** Nine machine cases spanning workshop equipment, industrial machinery, pumps, engines, compressors and CNC equipment.

## Why this record exists

Memory Prism was applied repeatedly to machine-maintenance problems. The requested output began as a practical maintenance checklist and log. Across the cases, the inquiry repeatedly had to go beyond a list of scheduled tasks: it had to preserve machine state, operating context, dependencies, intervention consequences, evidence and obligations that remained open.

This record captures the cross-case findings. It does not redefine the Framework, add mandatory stages, or claim that every concept must appear in every maintenance investigation.

## Cases examined

| Machine / system | Main maintenance question exposed |
|---|---|
| PROXXON TBM 115 precision bench drill press | Basic scheduled care, operating-hour ledger, source discrepancies and unknown machine-specific details |
| Grizzly G0640X bandsaw | Mixed-frequency maintenance, preparation dependencies and cleaning before lubrication |
| Haas HAC30-VS compressor | Multiple service clocks, first-service exceptions and recurring intervals |
| Beisler 1281/5-1 sewing unit | Multiple subsystems and contamination whose rate depends on material and use |
| KSB HPK pump | Condition-based monitoring, baselines, temperature-dependent oil intervals and limits of available thresholds |
| Cummins QSK60G generator | One oil-analysis finding propagating into several evidence-led investigations |
| SANY SY19E electric excavator | Maintenance interventions creating new contamination, bleeding, flushing and verification obligations |
| Atlas Copco GA15–GA26 compressor | Distinguishing symptom disappearance, provisional recovery and durable correction; recurrence history |
| Haas VF/VM CNC machining centre | Separating mechanical repair, calibration, geometric verification and restored production capability |

The individual case packs contain the machine-specific checklists, logs, source notes and unresolved details. This synthesis should be read alongside them, not as a replacement for them.

## Cross-case findings

### 1. A checklist is a snapshot; the Ledger is the continuing account

A checklist says what should be checked or done at a point in time. It does not, by itself, preserve what is still owed, why it is owed, what evidence would close it, or what happens if it is deferred.

The Ledger proved useful as a continuing account of:
- operating hours, calendar time, cycles and other service clocks;
- first-service exceptions and subsequent intervals;
- resources, consumables, parts and maintenance capacity;
- observations and measurements against baselines;
- unresolved defects, deferred work and conditional obligations;
- evidence required for verification and closure.

This distinction appeared in simple scheduled servicing and in complex condition-based work. The Ledger is not merely a place to write down completed maintenance. It carries obligations across time and interventions.

### 2. The machine's architecture determines the inquiry

A generic checklist cannot adequately describe every machine. The bandsaw's blade, wheels, guides and tensioning system; the sewing unit's head, controls, suction and pneumatic maintenance; and the generator's oil, cooling, intake and engine systems create different dependency structures.

The useful inquiry starts from the actual Board and its relationships. The framework transferred across machines because it helped construct a question-specific inquiry, not because the same maintenance questions were mechanically copied to every machine.

### 3. Maintenance is itself a state-changing intervention

The SANY excavator case made this especially visible. Opening hydraulic lines can introduce air and contamination. A filter replacement can expose debris that changes the investigation. Flushing, bleeding, running checks and shutdown inspections are not administrative extras: the intervention has changed the machine and generated new obligations.

The same pattern appears elsewhere: cleaning changes what can be inspected; lubrication depends on prior cleaning; replacing a component can require checks of connected surfaces and systems. A task may therefore create child obligations that must be tracked before the parent intervention can be closed.

### 4. One finding can propagate through a dependency network

The Cummins oil-analysis case showed that a single signal can generate several distinct checks across connected systems. The correct response is not to treat the finding as a diagnosis. It is to preserve the signal, identify plausible sources, gather discriminating evidence and keep the parent concern open while its branches are investigated.

This also clarifies the Translator's role: observation is not diagnosis, diagnosis is not a decision, and a decision is not proof that the intervention worked.

### 5. Repair, restoration and durable correction are different states

The cases exposed several false closure points:
- a symptom disappears, but recurrence has not been ruled out;
- a component is repaired, but system capability has not been verified;
- mechanical movement is restored, but CNC positioning or geometry remains unverified;
- a machine runs, but the required operating performance has not been demonstrated.

The Atlas Copco compressor and Haas CNC cases made this distinction particularly clear. Closure should be tied to the claim being made and the evidence that supports it. “Repaired”, “running”, “verified”, “restored” and “durably corrected” are not interchangeable labels.

### 6. Evidence needs its operating context

A reading without context can mislead. Useful evidence may need its measurement location, operating condition, load, baseline, instrument, calibration status, machine configuration, method and timestamp.

The KSB pump case showed why a temperature threshold or trend must be interpreted in the manufacturer's stated context. The Haas CNC case showed why measurement results must remain attached to configuration, compensation state, instrument and test method. Missing thresholds must remain unknown; they must not be invented to make a checklist look complete.

### 7. History is part of present machine state

Wear, prior repairs, adjustments, substitutions, configuration changes, recurring defects and deferred work affect what the machine can currently do and what a new observation means.

Memory and P-Memory preserve more than a narrative service history: they provide the prior states against which present observations are interpreted. Legacy is not simply age. It is the accumulated consequence of previous states and interventions.

### 8. Different clocks and conditional rules must coexist

The cases included operating-hour intervals, calendar intervals, cycle-based conditions, first-service exceptions, temperature bands, material-dependent contamination and condition-triggered work. Flattening these into one generic “next due” date loses important structure.

The Ledger must retain the actual trigger and the rule that generated the obligation. A conditional task is not equivalent to a fixed interval.

## Memory Prism concepts that did useful work

These are observations about how the concepts functioned in these cases, not a prescribed mapping for all maintenance work.

- **Board:** The machine and its interacting subsystems, including external operating context where relevant.
- **Constraints:** Manufacturer limits, safe-work boundaries, operating conditions, dependencies and permissible interventions.
- **Editors:** Operators, technicians, maintainers, control systems and interventions that change machine state.
- **Translator:** The work of turning observations into interpretations, decisions, actions and checks of the resulting state.
- **Memory / P-Memory:** Prior observations, states, readings, interventions and unresolved consequences.
- **Legacy:** Accumulated wear, repairs, settings, substitutions and historical decisions that shape present behaviour.
- **Ledger:** Resources, service clocks, reserves, obligations, deferred work, evidence and closure.
- **Viability:** Whether the machine can continue to perform its required function within its constraints.
- **Correction window:** The remaining opportunity to intervene before deterioration or accumulated consequences make recovery harder or impossible.

No concept needed to be forced into every individual case. The mapping became useful where the machine and the question gave it work to do.

## What this exercise supports — and what it does not

### Supported by the exercise

1. The same framework can help construct materially different maintenance inquiries across several machine types without imposing one universal checklist.
2. Ledger-based obligation tracking is useful beyond recording completed tasks: it preserves open work, dependencies, conditional triggers and closure evidence.
3. Interventions can generate new obligations, so maintenance records need to represent changes caused by maintenance itself.
4. A finding can initiate a network of investigations without being prematurely promoted to a diagnosis.
5. The distinction between repair, operational return, verification, restoration and durable correction is practically important.
6. Evidence quality depends on preserving context, not merely storing values.

### Not established

- This was a desk-based exercise using manufacturer documentation and constructed maintenance records, not inspections of the physical machines.
- No maintenance was performed and no real service history was observed.
- The exercise was not a blinded comparison against conventional maintenance planning or a controlled test of answer quality, cost, downtime or reliability.
- It does not establish that Memory Prism improves maintenance outcomes, prevents failures or replaces engineering judgement, OEM instructions, statutory inspection or site safety procedures.
- The cases do not yet deeply test conflicting evidence, severe resource scarcity, or several simultaneously deteriorating subsystems with competing correction priorities.
- Machine-specific manuals, revisions, serial ranges, nameplates and site requirements remain authoritative. Where source material was ambiguous or incomplete, the packs recorded the uncertainty rather than resolving it by assumption.

## Next useful tests

The next tests should challenge the boundaries that this batch did not adequately exercise:

1. **Conflicting evidence:** operator report, sensor trend and inspection result disagree. How is uncertainty retained without prematurely selecting one account?
2. **Resource-constrained maintenance:** the correct parts, labour or downtime are unavailable. How does the Ledger represent competing obligations, deferred risk and the shrinking correction window?
3. **Interacting deterioration:** two subsystems are deteriorating and an intervention on one may worsen or mask the other. How are dependencies and sequencing represented?
4. **Actual history import:** take a real, anonymised service log and test whether the framework can reconstruct current state and outstanding obligations without inventing missing events.

These are proposed follow-up tests, not conclusions from the present batch.

## Overall finding

The output evolved from a maintenance checklist into a representation of machine state and the history of interventions that change that state.

The strongest result was not that Memory Prism generated paperwork. It was that it repeatedly exposed what must remain connected for a machine to remain viable: architecture, constraints, flows and resources, history, observations, interventions, dependencies, evidence and unfinished obligations.

The framework did not need to become a maintenance framework to do this. It supplied a way to construct the inquiry; machine-specific knowledge supplied the mechanisms, limits and evidence.
