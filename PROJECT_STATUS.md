# Project Status - CE 393 Plate No. 2

**Last updated:** 2026-10-12  
**Repository:** [`justryan-n2d/plate_2_bsd`](https://github.com/justryan-n2d/plate_2_bsd)  
**Current base:** `main`  
**Current focus:** Phase 3 Revision 04 plus upper-floor lower-zone reference revision 02, retaining one combined upstairs Toilet and bath and documenting the requested gym/family/stair/balcony arrangement.

## Current position

**Phase 3 is now at Revision 04.** The user confirmed that the combined upstairs Toilet and bath stays, the separate upstairs Bathroom and Toilet are removed, and the ground-floor Toilet and bath stays. The enclosed-garage scenario budgets 73.32 m² of ground-floor clear space (86.26 m² gross proxy) and 66.01 m² of upper-floor clear space (77.66 m² gross proxy). The removed rooms release 4.95 m², which has not been reallocated. Exact local zoning/ROW setbacks and final measured floor areas remain pending.

Phase 3 was merged by [PR #3](https://github.com/justryan-n2d/plate_2_bsd/pull/3). Phase 4 was merged by [PR #4](https://github.com/justryan-n2d/plate_2_bsd/pull/4). For the current Phase 5 revision, the A-01 to A-07 validator passed; the Phase 3 validation and the existing Phase 1 CAD validation also passed on that revision.

## Status by phase

| Phase | Current status | Main records / result | Remaining limitation |
|---|---|---|---|
| **1. Lot and site base** | Preliminary work completed and merged | `site/phase1_traverse_coordinates.csv`, `site/phase1_site_base.svg`, `site/phase1_site_analysis.md` | Adjusted area is 265.26 m² versus the assignment's approximate 300.00 m²; original survey, road/ROW geometry and parcel conditions still need confirmation. |
| **2. Site requirements and preliminary calculations** | **Preliminary screening calculations updated** | `calculations/plate2_calculations.md`; `calculations/phase3_area_budget.csv` | The 2.00 m offset polygon area is 152.43 m², and 90% corner-lot cap is only a conditional scenario. Local Palo zoning classification, legal ROW/setback lines, final footprint/floor areas and qualifying open space remain pending. |
| **3. Space planning** | **Revision 04; upstairs wet-room simplification accepted** | Revised room schedule, adjacency matrix, zoning SVGs and `calculations/phase3_area_budget.csv` | Released 4.95 m² remains unallocated. Room sizes are targets, not image measurements or code minima. Final dimensions, footprint, floor area and formal open space remain pending. |
| **4. Stair planning** | Preliminary calculations and studies merged | `data/stair_design.json`, `space_planning/stair_design.md`, `space_planning/stair_plan.svg`, `space_planning/stair_section.svg` | Uses an assumed 3.000 m floor-to-floor rise; confirm actual levels and BP 344 applicability. Structural design and final building-section clearances remain open. |
| **5. Architectural plan set** | **Preliminary; lower upper-floor zone reference recorded** | A-01 to A-07 SVG previews; `data/building_model.json`; `calculations/phase3_area_budget.csv` | A-03 documents gym left, family area right, stairway along the upper-right edge, and a bottom-edge balcony with direct family-area access. Geometry remains conceptual and not dimensioned. The legacy 9.30 m x 7.90 m footprint/carport position is not coordinated to the new layout. A-01/A-04-A-07 and actual stair/roof/elevation/section geometry need the next design pass. Model-driven SVG regeneration / architectural DXF export are not yet implemented. |
| **6. Preliminary building specifications** | Not started | Planned specification sections in `plate2 plan.md` | Materials, workmanship requirements and specification schedule need to be written and coordinated. |
| **7. Required documentation** | Partially supported by earlier notes; not complete | Site analysis, calculations, Phase 3 records | Code compliance checklist, final space table, specification schedule and design rationale need final coordinated versions. |
| **8. Final review and presentation** | Not started | Checklist in `plate2 plan.md` | A3 sheets, long-bond calculations, final export, CAD inspection and print QA remain. |

## Phase 5 draft preview files

All are committed on the current `phase5-architectural-plans` branch:

- [A-01 Site Development Plan](previews/phase5_A01_site_development.svg)
- [A-02 Ground Floor Plan](previews/phase5_A02_ground_floor.svg)
- [A-03 Second Floor Plan](previews/phase5_A03_second_floor.svg)
- [A-04 Roof Plan](previews/phase5_A04_roof_plan.svg)
- [A-05 Four Elevations](previews/phase5_A05_elevations.svg)
- [A-06 Building Sections](previews/phase5_A06_sections.svg)
- [A-07 Details and Schedules](previews/phase5_A07_details_schedules.svg)

The shared source data is [`data/building_model.json`](data/building_model.json). See [`space_planning/reference_layout_revision.md`](space_planning/reference_layout_revision.md) and [`space_planning/phase5_architecture_notes.md`](space_planning/phase5_architecture_notes.md) for layout decisions and open checks.

## Assumptions that must not be mistaken for verified facts

1. The A-01 drawing uses a **uniform 2.00 m inward screening offset** around the current academic plot. PD 1096 Section 708(a) includes a general minimum property-line distance for Group A dwellings, but the screening offset is **not the final setback decision**. Applicable zoning, R-1 rules where relevant, special road-frontage treatment, the 8.00 m ROW limits, fire separation and local requirements need confirmation. Reference: [Supreme Court E-Library, PD 1096](https://elibrary.judiciary.gov.ph/thebookshelf/showdocs/26/53320).
2. The house footprint currently shown is **9.30 m x 7.90 m = 73.47 m²**, plus a **2.80 m x 5.50 m** carport placeholder. Neither placement nor coverage is approved.
3. Stair and building level coordination still assumes **3.000 m from ground-floor FFL to second-floor FFL**.
4. The roof pitch, eave/ridge levels, door and window positions/sizes, and finish selections are provisional design choices.
5. The draft previews are SVG review drawings, not a signed design, a permit set, structural drawings, or construction documents.

## Next work, in order

1. Dimension the revised Phase 3 layout, keeping only one combined upstairs Toilet and bath; do not use SVG coordinates as metres.
2. Decide how to allocate the released 4.95 m² after the measured room geometry is established, without double-counting the existing 8.00 m² circulation allowance.
3. Resolve Phase 2 using official information: survey/road ROW, zoning/setbacks and buildable envelope; then recalculate floor areas, open space, parking and code checks.
4. Dimension and coordinate the lower-zone layout, including the stair opening/landing and balcony door/projection, across A-02/A-03/A-04-A-07.
5. Implement or finalize model-driven drawing generation and editable CAD export; inspect the outputs in compatible CAD software.
6. Proceed to specifications, required documentation and presentation/print checks.

**Do not treat the project as ready for submission or construction yet.** The main current hold is Phase 2 verification and the resulting architectural coordination.


## Layout reference revision 01 (2026-10-12)

The student supplied furnished first- and second-floor images and selected them as the layout direction instead of the earlier simple room-box previews.

- **A-02:** TV console is shown in the living room, away from the entrance/foyer clearance area.
- **A-03:** gym and balcony are included; the karaoke room has one door on the circulation-hall side.
- `data/building_model.json` contains a new `reference_layout` section using SVG diagram units and automated checks for these two requirements.
- `space_planning/reference_layout_revision.md` records what changed and what remains open.

The visual layout is not a dimensioned plan. Existing room-size targets remain provisional and must be reconciled with the new arrangement. Site/setback confirmation and coordination of A-01/A-04-A-07 remain open.


## Phase 3 Revision 02 (2026-10-12)

Phase 3 was reopened after the student selected the furnished first- and second-floor reference images as the design direction. The revised room schedule, adjacency matrix, relationship diagram and both floor zoning diagrams now capture the same room arrangement and additional spaces.

- The first-floor TV is represented in the living-room zone, outside foyer/entry clearance.
- The second-floor karaoke room is assigned exactly one door from shared circulation.
- The separate Bathroom, Toilet and Toilet and bath labels remain separate pending confirmation.
- Room sizes shown from the earlier programme are retained only as unverified targets; undimensioned reference spaces have blank target fields. Previous room-area budget totals are superseded.

See [Phase 3 Revision 02](space_planning/space_planning.md) and [reference-layout revision record](space_planning/reference_layout_revision.md).


## Phase 3 area-budget coordination revision 03 (2026-10-12)

- The ground-floor space schedule now uses a proposed 3.00 x 5.50 m enclosed garage budget; clear programme total is 73.32 m² and gross-area proxy is 86.26 m².
- The second-floor room schedule now budgets the robe, separate Bathroom, separate Toilet, Toilet and bath, karaoke room, gym and 8.00 m² shared circulation; clear programme total is 70.96 m² and gross-area proxy is 83.48 m².
- Total gross-area planning proxy is 169.74 m², using a rough 15% wall/structure allowance. It is not the final measured GFA.
- The stored 2.00 m inward-offset polygon is 152.43 m². This is a screening assumption only. Parcel-specific zoning and road ROW/setback rules have not been verified.
- See `calculations/phase3_area_budget.csv` and `space_planning/space_planning.md` for formulas, assumptions and open checks.


## Phase 3 Revision 04 - user-confirmed upstairs wet-room simplification (2026-10-12)

- Keep the combined upstairs Toilet and bath.
- Remove the separate upstairs Bathroom and Toilet.
- Retain the ground-floor Toilet and bath.
- Revised second-floor clear-space programme: 66.01 m². Gross-area proxy: 77.66 m². Total gross-area planning proxy: 163.92 m².
- The removed rooms' provisional targets total 4.95 m²; this area is intentionally unallocated until the dimensioned layout is agreed.
- The second-floor zoning SVG and A-03 preview have been updated to show the wet-room decision. Re-check final layout geometry, room dimensions and cross-sheet coordination before marking Phase 3 or Phase 5 complete.


## Upper-floor lower-zone reference revision 02 (2026-10-12)

The latest user image confirms the lower section arrangement: gym left, family area right, stairway along the upper-right edge, and a balcony projecting from the bottom edge near the center of the overall upper-floor footprint. A single direct door leads from the family area to the balcony. The A-03 and Phase 3 zoning previews, shared model, documentation and validators now record this relationship. Dimensions, opening sizes, stair/landing coordination, balcony structural design and setback checks remain pending.
