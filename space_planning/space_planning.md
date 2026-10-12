# Phase 3: Space Planning - Revision 04 (Wet-Room Simplification)

**Project:** CE 393 Plate No. 2, Proposed Two-Storey Residential Building  
**Repository:** justryan-n2d/plate_2_bsd  
**Status:** User-confirmed upstairs wet-room simplification and revised preliminary budget; released area allocation, dimensions, legal site envelope and final floor areas remain pending.

## 1. Design basis

Use the furnished floor-plan images supplied by the student as the arrangement reference. Treat those images as a design direction, not measured drawings. Phase 3 now gives the rooms a provisional area budget before the dimensioned layout is prepared. No SVG pixel measurement is used as a real dimension.

The area-budget source of record is [phase3_area_budget.csv](../calculations/phase3_area_budget.csv). The room programme is in [space_requirement_table.csv](space_requirement_table.csv), and relationships are recorded in [adjacency_matrix.csv](adjacency_matrix.csv).

## 2. Site and code constraints affecting the budget

The repository's adjusted academic traverse calculates 265.2598 m², while the assignment's area remains an approximate 300.00 m². Use 265.2598 m² for preliminary arithmetic and keep the difference documented.

The current uniform 2.00 m inward-offset polygon has a calculated area of 152.4309 m². This is a **geometric screening scenario**, not an approved buildable envelope. PD 1096 Section 708(a) gives general Group A dwelling criteria that include a minimum 2 m from a property line and a 90% maximum occupancy scenario for corner lots. The project description says road frontage occurs along two sides, but actual official ROW/property-line geometry and local zoning classification remain to be verified. Official code source: https://elibrary.judiciary.gov.ph/thebookshelf/showdocs/26/53320

Do not assume a local zone classification such as R-1 without the parcel's zoning certification or authenticated zoning map. A 90% area cap does not override a setback or prove that a footprint fits the irregular site. Confirm Palo's applicable zoning provisions, road setbacks, setbacks measured from the correct ROW line, and other local requirements before finalizing A-01.

## 3. Area budget

The area budget uses inherited clear-space targets where available and proposed targets for new rooms shown in the reference. These are planning targets only, not code minimums. A provisional 15% wall/structure allowance (divide programmed clear area by 0.85) is carried forward only for early budgeting; it is not a code factor.

| Check | Preliminary value | How it is used |
|---|---:|---|
| Lot area | 265.26 m² | Adjusted academic traverse |
| 2.00 m inward-offset screening polygon | 152.43 m² | Preliminary fit screen only |
| Ground-floor programmed clear area, including enclosed garage | 73.32 m² | 56.82 m² previous programme + 16.50 m² garage target |
| Ground-floor gross-area proxy | 86.26 m² | 73.32 / 0.85 |
| Second-floor programmed clear area, excluding balcony | 66.01 m² | Retains 3 bedrooms and one combined Toilet and bath; adds robe, karaoke, gym and shared circulation |
| Second-floor gross-area proxy | 77.66 m² | 66.01 / 0.85 |
| Total gross-area planning proxy | 163.92 m² | 86.26 + 77.66; not final C-07 floor area |
| Ground-footprint proxy / adjusted lot area | 32.52% | Planning comparison only |
| Lot area less footprint proxy | 179.00 m² | Not proof of formal qualifying open space |

The preliminary budget assumes an **enclosed garage** because that is how the reference is shown. A 3.00 x 5.50 m clear bay is used to budget the space, but actual vehicle width, door swing, wall thickness and maneuvering should be checked. If changed to a covered-open carport, use the alternate row in the area-budget CSV and calculate enclosed floor area separately.

## 4. Ground-floor planning

Retain the intended arrangement: guest room at the upper-left, ground-floor toilet and bath nearby, garage on the left/front side of the concept, dining and kitchen in the open social zone, storage beside the stair, and living room at the lower/right part of the plan with the entrance/foyer along the lower middle.

- Keep the TV console inside the living-room zone, outside the foyer/entry-clearance path.
- Keep direct connections between dining and kitchen; storage should be near kitchen use.
- Make the pedestrian entry identifiable and separate from the vehicle maneuvering area.
- Use the 56.82 m² pre-garage clear programme only as the room target budget; keep the 4.50 m² circulation reserve separate from any actual measured hall unless it is reconciled in the plan.
- The enclosed garage clear-area target is 16.50 m². Verify that the selected vehicle fits and occupants can open doors; do not let the garage door, foyer or driveway route conflict.

## 5. Second-floor planning

Keep the master bedroom, Bedroom 2, Bedroom 3, family area and stair/common circulation. Retain the robe, one combined Toilet and bath, karaoke room, gym and optional balcony. The user confirmed removal of the separate upstairs Bathroom and Toilet.

| Additional / adjusted space | Proposed clear-size target | Budget area |
|---|---:|---:|
| Robe / wardrobe | 1.20 x 2.40 m | 2.88 m² |
| Karaoke room | 2.50 x 3.00 m | 7.50 m² |
| Gym | 2.80 x 3.00 m | 8.40 m² |
| Shared stair landing / hall circulation allowance | 8.00 m², area allowance only | 8.00 m² |
| Balcony, optional external area | 1.20 x 3.00 m | 3.60 m², outside this enclosed floor-area proxy |

The 8.00 m² upstairs circulation allowance replaces the older 5.00 m² target so the shared hall can independently serve the bedrooms, the single combined toilet and bath, gym and karaoke room. Do not add the old 5.10 m² schematic hall as a separate area on top; it is legacy layout data. Stair opening and upper landing still need to be dimensioned against the Phase 4 stair study.

### Access and privacy rules

- All bedrooms require independent doors to the shared hall.
- The gym must be reached from shared circulation, not through Bedroom 2 or Bedroom 3.
- The karaoke room must have **exactly one door** from shared circulation. Do not add an entry toward the stairway/family area.
- Keep the master bedroom private from the family/karaoke area.
- Keep only the combined upstairs Toilet and bath. The separate Bathroom and Toilet have been removed; retain the ground-floor Toilet and bath.
- The balcony remains conditional on legal projection/setback, guardrails, privacy, waterproofing and structural coordination.

## 6. Stair, site and cross-sheet coordination

The Phase 4 stair still assumes a 3.000 m floor-to-floor rise, 18 risers at about 166.7 mm, 280 mm tread and a nominal 2.00 x 3.20 m stair envelope. These values are preliminary. Confirm the floor levels and applicable stair/accessibility provisions; if a stricter accessible-stair requirement applies, the current stair budget must be redesigned and the room programme rebalanced.

Before finalizing the layout, coordinate:
1. the actual room dimensions and door/furniture clearances;
2. garage footprint, vehicle entry and pedestrian route;
3. the stair flight, upper opening and 8.00 m² shared circulation allowance;
4. the balcony/gym outline and roof/elevation projections;
5. the final building footprint inside the official setback/ROW envelope.

## 7. Hold points

- [ ] Obtain the parcel-specific zoning classification / authenticated zoning map and confirm local setback/ROW requirements.
- [ ] Confirm whether the separately labelled Bathroom, Toilet and Toilet and bath are all intended and list the fixtures for each.
- [ ] Confirm enclosed garage versus covered-open carport.
- [ ] Measure final outside walls and revise the room targets based on actual fit and furniture.
- [ ] Recalculate C-06 footprint, C-07 floor areas and C-08 qualifying open space from the dimensioned plans.
- [ ] Coordinate the upper-level stair opening, landing, door swings and headroom with Phase 4 and A-06.
- [ ] Update A-01 and A-04 through A-07 after the measured layout and official site envelope are agreed.

**Status:** The preliminary budget now leads the concept. The reference layout remains viable as a direction, but neither its precise dimensions nor its local zoning/code compliance has been established.

## Phase 3 Revision 04 - user-confirmed wet-room arrangement (2026-10-12)

The user confirmed this arrangement:

- Keep the combined upstairs Toilet and bath.
- Remove the separate upstairs Bathroom and separate Toilet.
- Keep the ground-floor Toilet and bath.

The former upstairs Bathroom target (3.15 m²) and Toilet target (1.80 m²) release 4.95 m² from the prior clear-space programme. This 4.95 m² is currently unallocated and is not counted as a new bedroom, hall, or gym expansion until the layout is dimensioned. The revised second-floor clear-space programme is 66.01 m²; its gross-area planning proxy is 77.66 m² using the same rough 0.85 factor. The combined gross-area proxy is 163.92 m², not final measured GFA.

The separate-room labels and their doors must be removed from A-03 and the Phase 3 zoning/relationship records. The single combined bathroom still needs a checked fixture layout, door swing and ventilation. Phase 3 remains open for T-25: dimensioning, area measurement and cross-floor coordination.