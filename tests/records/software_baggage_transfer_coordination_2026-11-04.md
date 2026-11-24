# Software Daily Test: Baggage-Transfer Exception Coordination

**Test ID:** MP-SOFTWARE-2026-11-04-01  
**Date:** 2026-11-04  
**Track:** Software daily test  
**Selection:** Assistant-selected scenario, not derived from the user's projects or recent conversations.  
**Test type:** Comparative software-planning exercise: conventional planning vs MP vs MP plus critical challenge.

## Purpose

Continue the software-planning test track begun on 2026-11-03. The question is whether MP changes how a software problem is framed and planned, and whether a separate challenge pass exposes weaknesses that neither planning approach catches.

This is a constructed scenario, not a real airport procurement or implementation proposal.

## Scenario brief

A medium-sized transfer hub handles checked baggage for multiple airlines and ground-handling companies. Existing departure-control, baggage-reconciliation, and sorting systems will remain in place.

The airport wants a new operational coordination layer to help staff identify bags at risk of missing connecting flights and decide where human intervention may help.

Known conditions:
- Bags move through multiple airlines, airport systems, and ground handlers.
- Connections have deadlines; some are short and disrupted by late-arriving aircraft.
- Tracking events arrive from multiple systems and may be delayed, duplicated, missing, or out of order.
- Some observations are automated; some require manual scans.
- Staff need to see a bag's latest known location, event freshness, intended onward flight, and transfer risk.
- The system may notify staff and record actions, but it must not autonomously hold or delay an aircraft.
- The system must preserve a traceable history of events and interventions.

Non-goals:
- Replacing the airport's baggage handling or reconciliation systems.
- Controlling sorters or conveyor machinery.
- Replacing airline departure-control systems.
- Building a passenger-facing baggage-tracking app.
- Making autonomous flight departure decisions.

No technology stack, budget, delivery date, or vendor has been specified.

## External domain evidence consulted

IATA Resolution 753 defines four core baggage tracking points: acceptance, loading, transfer, and arrival. Its implementation guide describes data exchange and operational scenarios, including a late-arriving transfer bag that has entered the sorter but has not yet reached the makeup area. The guide describes how knowing its injection time and location can support a better depart/wait decision. This is a human operational decision, not a software system's authority to make the decision.

Source: IATA Resolution 753 Implementation Guide, Issue 4.0 (November 2023), https://www.iata.org/contentassets/5c4aa8b8b3b1432697d2bf3301450684/reso753-implementation-guide---2023_issue-4.0.pdf

IATA's Baggage Information eXchange (BIX) is a newer event-oriented messaging standard intended to improve interoperability across airlines, airports, ground handlers, and technology providers. IATA describes the custodian airline as the source of truth for its baggage information and supports partner publish/subscribe exchange.

Source: IATA, Baggage Information eXchange (BIX), https://www.iata.org/en/programs/ops-infra/baggage/baggage-information-exchange-bix/

IATA reports that 41% of baggage mishandling occurs during transfers, and that Resolution 753 requires tracking at four points. These are industry-level figures and requirements, not assumed performance figures for this fictional hub.

Source: IATA, Baggage Tracking, https://www.iata.org/en/programs/ops-infra/baggage/baggage-tracking/

## Condition A — conventional software-planning pass

### Problem framing

Build an operational dashboard and alerting service that aggregates baggage events and helps staff intervene before connecting bags miss their onward flights.

### Main workstreams

1. **Requirements and user workflows**
   - Identify users: transfer coordinators, ground handlers, airline operations staff, supervisors.
   - Define views for at-risk bags, flight cutoffs, bag history, and manual intervention.
   - Define notification and escalation rules.

2. **Integrations**
   - Connect to existing baggage-reconciliation, departure-control, sorting, and tracking feeds.
   - Support multiple airline and handler interfaces.
   - Normalise incoming event formats.

3. **Data model**
   - Bag and tag identifiers.
   - Passenger and itinerary associations where permitted.
   - Flights, connections, handling locations, events, and interventions.
   - Event timestamps and source systems.

4. **Risk and alerting**
   - Compare expected progress with connection deadlines.
   - Identify missing transfer events and bags with stale status.
   - Prioritise bags by departure time and connection risk.

5. **Operations interface**
   - Search and filter bags.
   - Show current known status and event history.
   - Allow staff to acknowledge, assign, and record interventions.

6. **Security and access**
   - Role-based access.
   - Audit logs.
   - Data-sharing boundaries between airlines and handlers.

7. **Testing and rollout**
   - Simulate delayed, duplicated, and missing events.
   - Test airline/handler integration differences.
   - Pilot with a limited set of flights and handlers.
   - Measure alert accuracy and operational usefulness.

### Preliminary architecture

A modular service with event ingestion, normalisation, a baggage/flight association store, a risk evaluation component, an operational API, and a staff dashboard. A durable event log supports traceability and replay.

### Main risks identified

- Integration differences between systems.
- Missing or stale scans.
- Incorrect bag-to-flight association.
- False-positive alerts and alert fatigue.
- Privacy and cross-airline access.
- Staff ignoring or misunderstanding alerts.
- Network or integration outages.

## Condition B — MP-guided planning pass

### Pre-interpretation inventory

| MP concept | What I identify in this query |
|---|---|
| Board | The time-bounded transfer operation: a bag must move through a physical handling process before its onward flight closes |
| Memory | The persistent event history for each bag and its itinerary associations |
| Constraints | Flight cutoffs, physical handling time, sorter capacity, connection windows, data-sharing permissions, and incomplete observations |
| Editors | Operational rules that classify bags for attention and prioritise interventions; they filter which cases receive scarce staff attention |
| Flow Under Constraint | Physical baggage movement and the information flow between airline, airport, and handler systems |
| Audits | Event history and intervention records that allow staff to reconstruct what was known and done |
| Identity | Bag identity/tag, current itinerary association, and the distinction between a bag and its current intended flight |
| Working Lines | Candidate operating routes and handling paths; exact paths are not established by the brief |
| No Sacred States | “At risk,” “transferred,” and “loaded” are operational states supported by observations, not permanent truths; later events may revise the picture |
| Accumulation Patterns | Repeated delays, scan gaps, and transfer bottlenecks can accumulate into recurring operational pressure |

### Central organising idea

This is not primarily a dashboard project. It is a coordination problem between a physical process and several partial information systems.

A bag has:
- an intended itinerary,
- a physical location that may be only partially observed,
- a history of events,
- and a time window in which it must reach the onward flight.

Those are related but not interchangeable.

### Proposed core invariant

**The system must never present an old or inferred event as proof of a bag's current physical location or custody.**

Every displayed status should retain its source, event time, receipt time, and freshness. A bag's intended onward flight can change without its physical location changing; its observed location can change without its itinerary being updated.

### Lifecycle and state handling

Avoid one simplistic linear status field. Keep separate dimensions:
- **Journey association:** current intended flight/itinerary.
- **Physical observations:** last confirmed scan/location and its source.
- **Operational assessment:** normal, at risk, exception, or unknown.
- **Intervention:** unassigned, acknowledged, action underway, resolved, or escalated.

A bag can be at a known physical location but have an uncertain onward-flight association. It can be operationally at risk while its latest scan is technically valid but stale.

### Proposed sequence

1. Verify which event feeds and data rights actually exist.
2. Map bag identifiers, flight associations, locations, event semantics, and clock behaviour.
3. Build a durable event-ingestion and normalisation layer.
4. Preserve source and timing metadata; handle duplicate and late events.
5. Create a read-only operational picture with explicit freshness and uncertainty.
6. Add risk prioritisation and human intervention workflows.
7. Pilot against historical and live operational data before tuning thresholds.
8. Add analytics for recurring bottlenecks only after event quality is understood.

### MP-specific planning shift

The key shift is from “build an alert dashboard” to “preserve the distinction between what the bag is supposed to be doing, what was last observed, and what staff should do next.”

This changes the data model, status semantics, and order of implementation. The dashboard becomes a view over a trustworthy operational history rather than the system's organising centre.

## Condition C — MP plus critical challenge pass

The challenge pass asks whether the MP-guided plan rests on assumptions that have not been earned.

### Challenges and corrections

1. **Can the system see enough to make useful predictions?**
   - A dashboard cannot create visibility where no scan or system event exists.
   - Before promising prediction, measure feed coverage, scan latency, event loss, and the proportion of bags with usable transfer observations.
   - “Unknown” must be a first-class result, not silently converted into “late” or “missing.”

2. **Is a risk score actionable?**
   - Knowing that a bag is at risk does not guarantee that it can be retrieved, rerouted, or loaded before cutoff.
   - Risk should be paired with the last confirmed physical location, estimated remaining handling time where evidence supports it, and available intervention options.
   - Avoid presenting a numerical probability as calibrated unless validated against historical outcomes.

3. **What does a timestamp mean?**
   - Event time and system-receipt time are different.
   - Clocks may drift; events can arrive out of order.
   - A late-arriving event must not overwrite a newer physical observation merely because it was processed later.
   - Preserve original source timestamps and receipt timestamps; define ordering and correction rules.

4. **What if the bag is rebooked or the passenger is re-routed?**
   - The original onward flight association may become obsolete.
   - Maintain itinerary/flight-association history rather than mutating the bag into a single current state with no trace.
   - Re-evaluate risk when flight associations change.

5. **Who owns the event and who may correct it?**
   - BIX's custodian-airline model is a useful standards direction, but this fictional hub may have legacy feeds and bilateral arrangements.
   - Define authoritative sources per event type and a correction/dispute process.
   - Do not assume all partners can publish directly into one shared store.

6. **Could alerts make operations worse?**
   - Excessive false positives can distract staff from genuinely recoverable bags.
   - Measure precision, recall, lead time, and the percentage of alerts with a feasible intervention—not just alert volume.
   - Allow staff feedback, but do not let unreviewed feedback silently rewrite authoritative event history.

7. **Is the system allowed to make departure decisions?**
   - No. The brief explicitly excludes autonomous aircraft holds.
   - The product should present evidence and options to authorised operational staff. Decision authority remains in existing operational procedures.

8. **Is the proposed system duplicating an existing product?**
   - Before implementation, inventory current BRS, sorter, DCS, and vendor capabilities. The project may be an integration/configuration effort rather than a wholly new platform.
   - This is a discovery gate, not a reason to abandon the stated coordination-layer objective.

### Revised recommendation

Do not begin with predictive alerts. Begin with an evidence-quality and operational-observability pilot:
- ingest a bounded set of existing event feeds;
- preserve source, event time, receipt time, and correction history;
- display last confirmed observation and freshness;
- replay known transfer failures;
- measure whether staff can identify actionable cases earlier than they can today.

Only add risk scoring after the pilot establishes adequate data coverage and a useful intervention window.

## Comparative matrix

| Dimension | Conventional planning | MP-guided | MP + critical challenge |
|---|---|---|---|
| Initial framing | Dashboard and alerting product | Coordination between physical baggage flow and partial information systems | Verify whether sufficient reliable data exists to coordinate anything usefully |
| Main organising structure | Workstreams and features | Transfer operation, bag history, constraints, observations, interventions | Evidence quality, authority, uncertainty, and actionability |
| Core data model | Bag, flight, event, alert | Separate itinerary association, physical observation, operational assessment, intervention | Preserve event time vs receipt time, source authority, corrections, and history |
| State handling | Status and alert workflow | Multiple independent state dimensions | Unknown/stale/conflicting observations must remain explicit |
| Failure handling | Missing/duplicate events and integrations | Stale observations and divergence between intended and observed state | Out-of-order events, clock drift, rebooking, conflicting sources, no actionable intervention |
| Operational safety | Role-based access and no autonomous control | Human intervention is explicit | Decision authority and limits are explicit; alerts cannot imply control |
| Delivery sequence | Integrate, model, score, dashboard, pilot | Establish event history and observation quality before operational views | Evidence-quality pilot before predictive scoring |
| Key contribution | Comprehensive feature/workstream coverage | More accurate representation of the baggage's operational reality | Challenges whether the proposed prediction and intervention capability is supportable |

## Findings

### What changed between the passes?

- The conventional pass produced a plausible and recognisable software plan. It did not ignore event quality or operational risks.
- MP changed the organising structure: the system is about maintaining the distinction between intended itinerary, observed physical state, and operational response.
- The critical challenge pass questioned whether data coverage and operational lead time justify prediction at all. It moved the first delivery milestone from “risk alerts” to “evidence-quality pilot.”

### What can be attributed to MP?

The separation of intended itinerary, physical observation, and operational assessment emerged in the MP-guided framing. This is a useful planning distinction.

The critical challenge pass added the more severe questions about event-time ordering, authority, clock drift, data coverage, actionability, and whether the system should predict at all. Those findings belong to the challenge pass, not uniquely to MP.

### Provisional assessment

MP appears to help expose the real-world process underneath a software feature list and to organise the data model around that process. The challenge pass then tests whether the proposed system can know enough to act usefully.

This is promising but not proof that MP outperforms conventional software planning. The same assistant generated all three passes in the same conversation, with prior exposure to the scenario and earlier outputs. There was no blind scoring, independent architect review, or context-isolated baseline.

## Evaluation criteria for future software tests

Use the same criteria across future software cases:
1. Did the approach identify the actual operating invariant?
2. Did it distinguish real-world state from recorded/assumed state?
3. Did it expose dependencies and authority boundaries?
4. Did it identify failure modes and recovery paths?
5. Did it improve implementation sequencing?
6. Did it question whether the proposed software capability is technically and operationally supportable?
7. Did it reduce unnecessary cognitive load without replacing useful domain detail with framework jargon?

Do not score a test as an MP success merely because its answer is longer, more technical, or more diagnostic.

## Sources

- IATA Resolution 753 Implementation Guide, Issue 4.0 (2023): https://www.iata.org/contentassets/5c4aa8b8b3b1432697d2bf3301450684/reso753-implementation-guide---2023_issue-4.0.pdf
- IATA Baggage Information eXchange (BIX): https://www.iata.org/en/programs/ops-infra/baggage/baggage-information-exchange-bix/
- IATA Baggage Tracking: https://www.iata.org/en/programs/ops-infra/baggage/baggage-tracking/

## Next probe

For a future software test, choose a different software problem and retain the three-condition comparison. Prefer a scenario where the need for a software intervention is already established, so the exercise tests planning quality rather than being dominated by a build-versus-buy debate.
