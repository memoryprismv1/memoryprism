# Experimental Test: Memory Prism Applied to Software Planning

**Test ID:** MP-EXP-SOFTWARE-PLANNING-2026-11-03-01  
**Date:** 2026-11-03  
**Status:** Initial planning pass recorded; user evaluation and follow-up not yet complete  
**Branch:** `experimental/software-planning-mp`  
**Type:** Assistant-invented project; exploratory software-planning test  
**Persistence:** Experimental branch only; not merged into the main test history

## Purpose

Test whether Memory Prism can contribute to software planning, rather than only helping explain unfamiliar phenomena or organise research questions.

The test should examine whether MP changes what the assistant notices, the order in which it plans, the dependencies and failure conditions it identifies, or the quality of the resulting plan.

The test must not equate more terminology, more detail, or more specialist knowledge with better planning. The central question is whether MP helps produce a more coherent and useful plan without adding conceptual baggage.

## Independence and provenance

The assistant invented the project, its fictional operating context, requirements, assumptions, and initial plan. It was not selected from the user's projects, recent conversations, or personal context. The user supplied no project requirements.

This is not an independent-model or context-isolated experiment: it was conducted within an ongoing conversation with access to the Memory Prism context. The assistant generated both the conventional planning perspective and the MP-guided perspective. No blind or external scoring has yet occurred.

## Fictional project brief

A small independent cinema operates one screen with 84 seats. Staff currently manage bookings through phone calls, a spreadsheet, and a paper seating chart. The cinema wants online booking while retaining box-office sales and walk-ins.

Initial requirements:

- Customers can view screenings, select seats, and pay online.
- Staff can sell tickets at the box office.
- Online and box-office sales share seat availability.
- Customers can cancel under a defined refund policy.
- Staff can cancel screenings or block seats.
- Customers receive booking confirmation and a ticket.
- Staff can retrieve a booking if a customer loses the ticket.

Explicit non-goals: memberships, loyalty, concessions, multiple venues, dynamic pricing, and marketing. No technology stack, payment provider, budget, or launch date was supplied.

## MP pre-interpretation inventory

| MP concept | What is identified in this project |
|---|---|
| Board | Each screening, with its own finite set of seats and operating period. |
| Memory | Persistent booking, payment, cancellation, and screening records. |
| Constraints | Seat capacity, screening times, payment confirmation, refund rules, and staff availability. |
| Editors | Booking rules, seat blocking, hold expiry, cancellation rules, and staff overrides. |
| Flow Under Constraint | Movement of seat availability, bookings, payments, and customer notifications. |
| Audits | Payment reconciliation and checking that booking records agree with actual sales. |
| Identity | A booking must be identifiable; a permanent customer account is not established as necessary. |
| Working Lines | Not established by the brief. |
| No Sacred States | A booking can change state or be cancelled; a seat assignment is not necessarily permanent. |
| Accumulation Patterns | Repeated bookings, cancellations, no-shows, and operational history may accumulate; future use is not established. |

## Initial planning result

### 1. Central invariant

For any given screening, a seat can have at most one active claim.

The project is therefore not merely a website with a booking form. It is a shared seat-allocation system with multiple sales channels. Online and box-office interfaces must use the same allocation authority.

### 2. Seat and booking lifecycle

A seat's status for a screening can be:

- Available
- Held (temporarily unavailable during checkout)
- Booked (payment or authorised box-office sale confirmed)
- Blocked (reserved by staff)

Relevant transitions include Held to Available on expiry or abandonment; Booked to Available after an accepted cancellation; Available to Blocked by staff; and Blocked to Available after staff release.

### 3. Payment/booking race condition

A critical failure case:

1. Customer A selects seat B7 and receives an eight-minute hold.
2. A begins checkout.
3. The hold expires.
4. Customer B buys B7 at the box office.
5. A's payment provider reports successful payment after B7 has been resold.

A successful payment event cannot by itself guarantee a successful booking.

Proposed handling:

- Hold the seat before checkout.
- Use a defined hold expiry.
- Treat the payment provider's confirmed event, not the browser success screen, as payment evidence.
- Finalise only if the hold remains valid.
- If payment succeeds after the seat has been released and resold, void or refund the payment and notify the customer.
- Make payment-event processing idempotent.

This is a core requirement, not a later enhancement.

### 4. Proposed system shape

A modular monolith is proposed for the single-venue MVP:

- Customer booking interface.
- Box-office interface.
- Staff administration.
- Shared booking and seat-allocation service.
- Relational database for screenings, seats, holds, bookings, payments, and audit history.
- External payment and email services.

The database, not just the user interface, must protect the no-double-allocation invariant through transactions and suitable locking or uniqueness constraints.

### 5. Implementation sequence

| Stage | Deliverable | Dependency/rationale |
|---|---|---|
| 0. Resolve operations | Seat map, sales rules, refund policy, staff workflow | Determines system rules. |
| 1. Screening and seat administration | Create screenings, configure seats, block seats | Establishes saleable inventory. |
| 2. Shared allocation engine | Holds, expiry, booking states, concurrency protection | Both sales channels depend on it. |
| 3. Online booking and payment | Selection, checkout, payment confirmation, tickets | Depends on reliable allocation. |
| 4. Box-office sales | Staff sales, cash/card recording, lookup, cancellation | Reuses shared allocation. |
| 5. Operational readiness | Reconciliation, failure handling, backups, training | Verifies real operating readiness. |

### 6. Decisions still open

- Whether seats are always numbered and the layout fixed.
- Whether customers can book multiple seats in one transaction.
- Hold duration.
- Cancellation and refund cutoff.
- Complimentary-ticket permissions.
- Internet outage procedure during sales.
- Whether scanning hardware is required or staff lookup is sufficient.

Provisional MVP assumptions: guest checkout, online card payment, cash or card at the box office, email tickets, and staff lookup rather than dedicated scanning hardware.

### 7. Risks surfaced

- Duplicate sale: one allocation authority and database enforcement.
- Payment succeeds but booking fails: explicit payment/booking reconciliation.
- Abandoned checkout leaves seats unavailable: automatic hold expiry.
- Staff override causes conflict: permission checks and audit trail.
- Email delivery fails: booking remains valid and ticket can be retrieved.
- Internet outage: defined sales-pause procedure; no unsafe offline allocation in MVP.
- Refund and seat release disagree: explicit cancellation state and reconciliation.

## Preliminary assessment: what MP appears to have contributed

The MP pass made the screening-level boundary and finite seat inventory explicit before selecting architecture. This helped make the shared allocation authority the centre of the plan rather than treating online booking and box-office sales as separate feature areas.

The mapping also made several distinctions visible:

- A temporary hold is not a confirmed booking.
- A payment is not identical to a booking.
- A customer account is not automatically required just because a booking needs an identity.
- Payment reconciliation is an operational check, not merely a reporting feature.
- The system must preserve a seat-allocation invariant across multiple interfaces.

These observations materially shape the proposed design and sequencing.

## Limitations and competing explanation

This is not evidence that MP uniquely generated these insights. Domain-driven design, state modelling, transaction design, and ordinary software architecture practice can also identify shared resources, lifecycle transitions, concurrency hazards, and reconciliation requirements.

The next comparison should ask whether MP changed the plan in a demonstrable way relative to a conventional requirements-first plan, and whether any improvement is useful rather than simply more elaborate.

No claim of superiority is made at this stage. The assistant authored the plan and this preliminary assessment; user evaluation is pending. No external reviewer, blind scoring, implementation, or operational validation has occurred.

## Next evaluation

Inspect whether the MP-guided plan has:

1. Found a consequential dependency or failure condition that a conventional feature-first plan might miss.
2. Sequenced implementation around the actual operating invariant.
3. Avoided unnecessary architecture and requirements.
4. Left the right decisions open rather than silently inventing answers.
5. Produced a plan that is easier to act on, not merely more intellectually elaborate.

The user will assess the usefulness of the plan and may challenge assumptions or identify omissions. Record that feedback before claiming an outcome.
