# Daily Test: Why Metal Feels Colder Than Wood at the Same Temperature

**Test ID:** MP-2026-11-05-01  
**Date:** 2026-11-05  
**Track:** Normal daily test  
**Selection:** Assistant-selected independently of the user's recent conversations, projects, interests, and conceptual leads.  
**Question:** If a metal object and a wooden object have been in the same room for hours, why does the metal feel colder when touched?

## Protocol and limits

A paired qualitative comparison:
1. A conventional explanation in ordinary physics language.
2. An MP-guided explanation using the table-first response pattern.

Both drafts were produced by the same assistant in the same conversation. Topic selection was independent of the user's recent context, but the comparison was not blind or context-isolated. No independent scorer was available. This is a diagnostic exercise, not a controlled performance study.

## Evidence consulted

The American Physical Society explains that objects left in a room generally reach thermal equilibrium, yet metal feels colder because it transfers heat away from the hand more rapidly than wood. The University of Illinois Physics Van similarly notes that touch responds to the rate of heat transfer at the skin, not by directly reading an object's temperature.

A more complete contact-transfer description uses **thermal effusivity**, which combines conductivity, density, and heat capacity. Purdue's heat-transfer teaching resource notes that effusivity is the relevant property for how strongly a material draws heat from a contacting hand; conductivity alone is not the whole story.

Sources:
- American Physical Society, “Getting Warmer/Getting Colder”: https://www.aps.org/learning-resources/getting-warmer-colder
- University of Illinois Physics Van, “Why do Metals Feel Cold or hot to the Touch?”: https://van.physics.illinois.edu/ask/listing/44029
- Purdue University, “Conduction, convection, radiation”: https://web.ics.purdue.edu/~dchavas/teaching/interactive/heat-transfer.html

## Draft A — conventional explanation

If metal and wood have been sitting in the same room long enough, they are usually at approximately the same temperature. The metal is not necessarily colder.

Your hand is warmer than both objects, so heat flows from your skin into whichever object you touch. Metal conducts heat much more readily than wood, so it draws heat away from the contact area faster. Your skin cools more quickly, and that is what you experience as a colder sensation.

Wood is a poor conductor, so the surface under your finger warms up locally and the heat flow slows. Metal keeps carrying heat away from the contact area, so it continues to feel colder.

The fuller material property is thermal effusivity: how readily a material exchanges heat with another body at its surface. It depends on conductivity, density, and heat capacity, not conductivity alone.

If the objects are hotter than your skin, the same principle works in reverse: metal can feel hotter because it transfers heat into your skin more rapidly.

## Draft B — MP-guided explanation

### Pre-interpretation inventory

| MP concept | What I identify in this query |
|---|---|
| Board | The brief contact between a warm hand and an object at room temperature |
| Memory | Not relevant to this inquiry |
| Constraints | Initial temperature difference, contact area, contact duration, material properties, and heat capacity |
| Editors | Material properties filter the rate at which thermal energy moves from the skin into the object |
| Flow Under Constraint | Heat flows from the warmer skin into the cooler object; the rate differs by material |
| Audits | Not relevant to this inquiry |
| Identity | The perceived quality “feels colder” is the sensation to explain, not a direct measurement of object temperature |
| Working Lines | Not established by the query |
| No Sacred States | “Cold-feeling material” is not an intrinsic temperature category; the sensation depends on the contact conditions and direction of heat flow |
| Accumulation Patterns | Heat accumulates near the contact surface; wood warms locally more readily, while metal conducts energy away from that region |

### Explanation

The puzzle comes from treating touch as if it were a thermometer.

The object and the hand begin at different temperatures. Heat moves from the hand into the object. What differs is not necessarily the starting temperature but how quickly the contact changes the skin temperature.

Wood lets the contact surface warm up, reducing the temperature difference at the point of contact. Metal moves energy away from that point more effectively, so the skin continues losing heat.

This is why thermal effusivity is a better description of the initial tactile experience than temperature alone. Conductivity matters, but density and heat capacity also affect how the material behaves during contact.

The useful distinction is between:
- the object's actual temperature;
- the rate at which heat crosses the contact;
- the resulting temperature change in the skin;
- the sensation interpreted as cold or hot.

The sensation can reverse if the object is hotter than the hand. Metal then feels hotter for the same reason: it transfers energy faster.

## Comparison

| Criterion | Conventional answer | MP-guided answer |
|---|---|---|
| Corrects the temperature misconception | Yes | Yes |
| Explains heat flow direction | Yes | Yes |
| Explains why metal feels colder | Yes | Yes |
| Includes thermal effusivity nuance | Yes | Yes |
| Separates actual temperature from sensation | Yes | Makes the distinction explicit as separate elements |
| Adds a new physical mechanism | No | No |
| Useful next question | What determines the rate of heat transfer? | How do contact time, pressure, skin condition, and material effusivity alter the sensation? |

## Finding

The conventional answer already explains the phenomenon well. MP does not add a new physical mechanism or improve the basic explanation.

The inventory makes the distinction between actual object temperature, heat-transfer rate, skin response, and perceived coldness explicit. That may make the misconception easier to inspect, but it also adds a table to a question that can be answered simply.

**Provisional result:** no demonstrated content-quality gain. Possible organisational gain, but the extra structure may not be worth its overhead for a straightforward question. This is an important negative result: MP should not be invoked ritualistically.

## Limitations

- Same assistant and conversation; not blind or context-isolated.
- No independent scoring.
- The simple comparison assumes the objects have been in the same environment long enough to approach thermal equilibrium.
- Contact sensation also depends on surface finish, moisture, pressure, contact area, and duration; these are not exhaustively modelled here.

## Next probe

Compare objects with similar conductivity but different density and heat capacity, or vary contact duration, to test how well effusivity predicts the initial sensation. The everyday question is settled; the deeper measurement question is how the material and contact conditions combine.
