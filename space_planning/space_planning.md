# Phase 3: Space Planning - Revision 02

**Project:** CE 393 Plate No. 2, Proposed Two-Storey Residential Building  
**Repository:** `justryan-n2d/plate_2_bsd`  
**Status:** Reopened for coordination with user reference layout revision 01. Conceptual room programme and relationships updated; dimensions and area budget remain pending.

## 1. Why Phase 3 is being revisited

The furnished first- and second-floor references selected for A-02 and A-03 change the room arrangement and add spaces not represented in the earlier Phase 3 programme. This revision brings the room schedule, adjacency matrix and diagrams into line with that direction before proceeding with further architectural coordination.

The reference is the **layout direction**, not a dimensioned drawing. Nothing in the supplied images supports calculating actual room sizes by pixel measurements.

## 2. Deliverables

- [Revised space requirement table](space_requirement_table.csv): required spaces, additional spaces shown in the reference, inherited target dimensions where available, and explicit dimension status.
- [Revised adjacency matrix](adjacency_matrix.csv): direct, near, buffered and conditional relationships with reasons.
- [Revised adjacency diagram](adjacency_diagram.svg): two-floor relationship overview.
- [Revised ground-floor zoning](ground_floor_zoning.svg): room positions and main circulation follow the first-floor reference.
- [Revised second-floor zoning](second_floor_zoning.svg): room positions and circulation follow the second-floor reference, including gym, robe, karaoke and balcony.
- [Space-planning validator](../scripts/validate_space_planning.py): checks programme fields, inherited arithmetic, adjacency references, SVG diagrams and the two explicit layout guardrails.

## 3. Room programme

### Ground floor

The required spaces remain entrance/foyer, living room, dining area, kitchen, toilet and bath, guest room, stairway, storage/service area and garage/carport. A general-circulation allowance remains as a provisional planning reserve, not as a separate physical room.

The reference places the guest room at the upper-left, toilet and bath below it, garage at the lower-left, dining and kitchen at the upper/right side, storage next to the stairway, and living room at the lower-right. The entrance/foyer is at the lower middle. The **TV console must stay inside the living room and must not obstruct the entrance/foyer route**.

### Second floor

The required spaces remain master bedroom, Bedroom 2, Bedroom 3, toilet and bath, family area and stair landing/circulation. The revision also records the additional spaces visible in the reference:

- Robe/wardrobe zone beside the master bedroom.
- Separate room labelled **Bathroom**.
- Separate room labelled **Toilet**.
- A further room labelled **Toilet and Bath**.
- Karaoke room, gym and balcony.

The three labelled wet-room spaces are kept separate in the programme because that is what the reference shows. Their exact intended uses, fixture contents and whether all three are to be retained should be confirmed during the next design review; they must not be merged without that decision. The karaoke room is reached from shared circulation and must have **exactly one door**. The gym also needs independent access from the shared circulation, without entry through a bedroom.

## 4. Dimension status and area budgeting

The dimension values still present in the CSV are **inherited provisional targets from the earlier Phase 3 programme**. They are retained for audit/history, not asserted as dimensions of the new reference layout. Every such row is marked `legacy-target-unverified`. The new rooms for which the reference supplies no usable dimensions are marked `not-dimensioned` and have blank size/area fields.

The earlier area-budget totals (including the 15% wall/structure allowance) are **superseded for this revised room arrangement**. They must not be presented as the revised plan's floor areas. No new room-area, gross-floor-area, coverage or open-space totals can be produced until the layout is measured and coordinated with Phase 2's confirmed buildable envelope.

| Item | Current status |
|---|---|
| Inherited room-size targets | Preserved in CSV, all marked unverified against revision 01 |
| Additional spaces from the reference | Recorded with no invented dimensions |
| Updated floor-area budget | Not calculated yet |
| Building footprint / setbacks | Awaiting Phase 2 confirmation |
| Final circulation and stair opening | Awaiting coordinated plan and section |
| Number of upstairs wet-room spaces | Three labels retained from the image; confirm whether all are intended |
| Karaoke-room door count | Exactly one, from shared circulation |
| TV console / entrance | TV kept inside the living-room zone, away from foyer clearance |

## 5. Adjacency and circulation decisions

### Ground floor

1. Maintain a clear route from the entrance into the living room; do not let the TV console, loose furniture or storage block the foyer.
2. Connect living and dining directly. Keep dining directly related to the kitchen and storage close to the kitchen.
3. Keep the guest room private and near the ground-floor toilet/bath.
4. Keep the stair easy to reach from the shared social/circulation area, with enough space for the approach and door swings after dimensioning.
5. Place the garage near the main approach but distinguish the pedestrian entry from vehicle movement. The drawing currently looks like an enclosed garage; decide whether the final design is a garage or covered-open carport.

### Second floor

1. Give the master bedroom, Bedroom 2 and Bedroom 3 independent doors to shared circulation.
2. Keep the robe connected to the master bedroom.
3. Keep the family area near the stair landing and separate it from direct exposure into the master bedroom.
4. Retain the separate bathroom, toilet and toilet/bath as separate schedule items until their functions and fixture layouts are confirmed.
5. Provide one karaoke-room door from the hall. Do not add a second door toward the stairway/family area.
6. Provide gym access from shared circulation, not through Bedroom 2 or any other bedroom.
7. Keep the balcony in the concept as shown, but inclusion and final size depend on setbacks, privacy, guardrail, weatherproofing, access and structural review.

### Cross-floor coordination

Keep the upper stair opening, landing and lower stair in the same coordinated design zone. Keeping the ground- and second-floor toilet/bath spaces close is a planning preference, not utility design. Verify stair headroom, landings and doors against the actual floor-to-floor height in Phase 4/5.

## 6. Relationship codes

- **direct:** place side by side or connect with a short direct path where practical.
- **near:** keep nearby with a short shared route; a door-to-door connection is not required.
- **buffered:** keep accessible but protect privacy or reduce direct exposure.
- **conditional:** use only if site, privacy, safety and applicable code checks permit it.

The matrix records the full reasoning. The SVG adjacency diagram highlights principal relationships and does not substitute for the matrix or the actual floor plan.

## 7. Updated Phase 3 outcome and hold points

The revised programme and diagrams now acknowledge the layout reference and its additional spaces. This is a **conceptual coordination milestone only**, not completion of the dimensioned plan.

- [ ] Confirm whether the three separate upstairs wet-room labels all represent intended rooms and establish what fixtures each contains.
- [ ] Confirm whether the ground-floor vehicle space will be enclosed garage or covered-open carport.
- [ ] Determine dimensions for all unmeasured spaces and test inherited targets against actual furniture, wall thickness, door swings and circulation.
- [ ] Confirm the final stair opening, landing and headroom against Phase 4 calculations and the building section.
- [ ] Recalculate room-area/floor-area totals after the measured layout and Phase 2 buildable envelope are known.
- [ ] Reconcile the balcony and gym extension with setbacks, footprint, elevations and roof plan.
- [ ] Review the room schedule, matrix and zoning diagrams again after those checks.

**Status:** Phase 3 has been reopened and updated to the reference layout. The conceptual programme is revised; final dimensions, area budgets, code checks and cross-sheet coordination remain pending.
