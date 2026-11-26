# Why Potholes Come Back in the Same Spot After Patching — 2026-11-25

**Test ID:** MP-2026-11-25-03
**Run type:** Assistant-led logic pass, then research check (the "if this happens, what must be true" method, run by the assistant)
**Context:** same conversation; self-assessed; not blind; no baseline condition

## Method

1. Logic only, before any research: list what must be true if a patched pothole reappears in the same place.
2. Research each required process and report: exists / doesn't / unknown.
3. Note where MP concepts changed the result.

## Step 1: required processes (written before research)

1. The patch fills the hole but leaves the cause underneath.
2. Water still gets in at that spot.
3. Traffic keeps loading that exact spot.
4. The patch is weaker than the surrounding road.
5. Something decides to patch cheaply instead of fixing the cause.

## Step 2: checks

| # | Status | Evidence |
|---|---|---|
| 1 | Exists | Potholes need water and traffic together: water weakens the base, traffic fatigues the unsupported surface (Wikipedia/FHWA). Caltrans: merely filling a pothole usually doesn't prevent distress adjacent to or within the patch. |
| 2 | Exists | Water enters through surface cracks or from the road sides (Maryland DOT). In Indian cities, standing water on bitumen is the main driver (Delhi expert, outdated 1978 stormwater system). |
| 3 | Exists | Fatigue cracking is most often instigated by traffic loading (Wikipedia, crocodile cracking). |
| 4 | Exists, with a twist | Illinois DOT review: temporary low-quality patching causes recurrent failure. But an FHWA study found throw-and-roll as effective as semi-permanent repair in most situations; the worst method is throw-and-go (no compaction). Compaction matters more than patch type. |
| 5 | Reported, not proven | One anonymous Bengaluru contractor admitted corruption forced substandard work. A lead, not a finding. |

## Where MP changed the answer

**Board.** Most Western sources centre freeze–thaw cycles. That is their board, not India's. Here, monsoon water and drainage dominate. Without the board check, the wrong mechanism would have been imported.

**Editor at institutional scale.** The filter that decides which repairs persist turned out to be budgets and contracts, not physics.

## Result

The logic pass named all five required processes correctly. Research changed the details (compaction over patch type; the institutional editor; the board-specific mechanism).

## Limits

Assistant-led, not person-led. Secondary sources and news reports; one anonymous claim. No field observation.

## Sources

- Wikipedia, Pothole (citing FHWA); Wikipedia, Crocodile cracking
- Maryland Department of Transportation, Potholes
- Illinois DOT / ROSA P report on pothole patching practice
- Caltrans Maintenance Technical Advisory Guide, Chapter 5 (Patching)
- NewsBytes, "Monsoon leaves Delhi roads rough with potholes despite PWD repairs"
- Deccan Herald report quoting a BBMP contractor (anonymous)

## Score line

Not scored on the IQ rubric (na). Logic pass: 5 of 5 required processes confirmed by research.

SCORES: IQ=na/12; scorer=self; blind=no
