# Project Status - CE 393 Plate No. 2

**Last updated:** 2026-10-10  
**Repository:** [`justryan-n2d/plate_2_bsd`](https://github.com/justryan-n2d/plate_2_bsd)  
**Main branch after latest merge:** `d71de4f1d76af5b8317ff0421077aa7a8e24f0de`  
**Current working branch:** `phase5-architectural-plans`

## Current position

**Phase 5 is in progress.** Preliminary SVG previews have been created for A-01 through A-07 and a shared `data/building_model.json` records the current geometry and assumptions. The Phase 5 branch has not been merged into `main`.

Phase 3 was merged by [PR #3](https://github.com/justryan-n2d/plate_2_bsd/pull/3). Phase 4 was merged by [PR #4](https://github.com/justryan-n2d/plate_2_bsd/pull/4). The Phase 3, Phase 4 and existing Phase 1 CAD workflows passed in the previous verification cycle.

## Status by phase

| Phase | Current status | Main records / result | Remaining limitation |
|---|---|---|---|
| **1. Lot and site base** | Preliminary work completed and merged | `site/phase1_traverse_coordinates.csv`, `site/phase1_site_base.svg`, `site/phase1_site_analysis.md` | Adjusted area is 265.26 m² versus the assignment's approximate 300.00 m²; original survey, road/ROW geometry and parcel conditions still need confirmation. |
| **2. Site requirements and preliminary calculations** | **Pending; an important dependency** | `calculations/plate2_calculations.md`, C-04 through C-09 | Official site zoning, setbacks, buildable envelope, final footprint/floor areas/open space, occupant load, parking and other code requirements have not been fully determined. |
| **3. Space planning** | Preliminary programme and zoning package merged | `space_planning/space_requirement_table.csv`, `space_planning/adjacency_matrix.csv`, `space_planning/space_planning.md` and three SVG previews | Target dimensions and zoning are not final architectural dimensions. |
| **4. Stair planning** | Preliminary calculations and studies merged | `data/stair_design.json`, `space_planning/stair_design.md`, `space_planning/stair_plan.svg`, `space_planning/stair_section.svg` | Uses an assumed 3.000 m floor-to-floor rise; confirm actual levels and BP 344 applicability. Structural design and final building-section clearances remain open. |
| **5. Architectural plan set** | **Draft previews created on current branch** | The seven A-01 to A-07 SVG previews listed below; `data/building_model.json` | The shared model is present, but fully automated model-to-drawing generation / DXF export is not yet implemented. Draft geometry, site placement, doors/windows, elevations and roof assumptions need review and coordination. |
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

The shared source data is [`data/building_model.json`](data/building_model.json), and the explanation of assumptions is [`space_planning/phase5_architecture_notes.md`](space_planning/phase5_architecture_notes.md).

## Assumptions that must not be mistaken for verified facts

1. The A-01 drawing uses a **uniform 2.00 m inward screening offset** around the current academic plot. PD 1096 Section 708(a) includes a general minimum property-line distance for Group A dwellings, but the screening offset is **not the final setback decision**. Applicable zoning, R-1 rules where relevant, special road-frontage treatment, the 8.00 m ROW limits, fire separation and local requirements need confirmation. Reference: [Supreme Court E-Library, PD 1096](https://elibrary.judiciary.gov.ph/thebookshelf/showdocs/26/53320).
2. The house footprint currently shown is **9.30 m x 7.90 m = 73.47 m²**, plus a **2.80 m x 5.50 m** carport placeholder. Neither placement nor coverage is approved.
3. Stair and building level coordination still assumes **3.000 m from ground-floor FFL to second-floor FFL**.
4. The roof pitch, eave/ridge levels, door and window positions/sizes, and finish selections are provisional design choices.
5. The draft previews are SVG review drawings, not a signed design, a permit set, structural drawings, or construction documents.

## Next work, in order

1. Run and review the Phase 5 SVG/data validation workflow.
2. Complete Phase 2 from official source information: confirm survey/road ROW and local zoning/setbacks; calculate the final buildable envelope; then recalculate the footprint, floor areas, open space, occupant load, parking and code checks.
3. Revise the A-01 through A-03 plans and stair position to fit those confirmed constraints.
4. Implement or finalize the shared-source drawing generator and editable CAD export pipeline; compare generated outputs to the committed previews.
5. Coordinate roof, elevations, sections, opening schedules and dimensions; carry out visual inspection in compatible CAD software.
6. Proceed to Phase 6 specifications, Phase 7 documents, and Phase 8 presentation/print checks.

**Do not treat the project as ready for submission or construction yet.** The main current hold is Phase 2 verification and the resulting architectural coordination.
