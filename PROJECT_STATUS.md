# Project Status - CE 393 Plate No. 2

**Last updated:** 2026-10-12  
**Repository:** [`justryan-n2d/plate_2_bsd`](https://github.com/justryan-n2d/plate_2_bsd)  
**Current base:** `main`  
**Latest design change:** user-reference layout revision 01 for A-02/A-03.

## Current position

**Phase 5 is in progress.** A-01 through A-07 preliminary SVG previews and a shared `data/building_model.json` are committed on `main`. A-02/A-03 now use the user-provided furnished layout references. Their visible arrangement is updated, but room dimensions and coordination with A-01/A-04-A-07 remain pending.

Phase 3 was merged by [PR #3](https://github.com/justryan-n2d/plate_2_bsd/pull/3). Phase 4 was merged by [PR #4](https://github.com/justryan-n2d/plate_2_bsd/pull/4). For the current Phase 5 revision, the A-01 to A-07 validator passed; the Phase 3 validation and the existing Phase 1 CAD validation also passed on that revision.

## Status by phase

| Phase | Current status | Main records / result | Remaining limitation |
|---|---|---|---|
| **1. Lot and site base** | Preliminary work completed and merged | `site/phase1_traverse_coordinates.csv`, `site/phase1_site_base.svg`, `site/phase1_site_analysis.md` | Adjusted area is 265.26 m² versus the assignment's approximate 300.00 m²; original survey, road/ROW geometry and parcel conditions still need confirmation. |
| **2. Site requirements and preliminary calculations** | **Pending; an important dependency** | `calculations/plate2_calculations.md`, C-04 through C-09 | Official site zoning, setbacks, buildable envelope, final footprint/floor areas/open space, occupant load, parking and other code requirements have not been fully determined. |
| **3. Space planning** | Preliminary programme and zoning package merged | `space_planning/space_requirement_table.csv`, `space_planning/adjacency_matrix.csv`, `space_planning/space_planning.md` and three SVG previews | Target dimensions and zoning are not final architectural dimensions. |
| **4. Stair planning** | Preliminary calculations and studies merged | `data/stair_design.json`, `space_planning/stair_design.md`, `space_planning/stair_plan.svg`, `space_planning/stair_section.svg` | Uses an assumed 3.000 m floor-to-floor rise; confirm actual levels and BP 344 applicability. Structural design and final building-section clearances remain open. |
| **5. Architectural plan set** | **Preliminary; layout revision 01 added** | A-01 to A-07 SVG previews; `data/building_model.json`; `space_planning/reference_layout_revision.md` | A-02/A-03 now follow the visual references. Room dimensions are not derived from the images. A-01/A-04-A-07, the shared model's legacy room targets, and the stair/roof/elevation/section geometry still need coordination. Model-driven SVG generation / architectural DXF export are not yet implemented. |
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

1. Run the Phase 5 SVG/data validation workflow and visually review the revised A-02/A-03 previews.
2. Resolve Phase 2 using official information: confirm survey/road ROW and local zoning/setbacks, then calculate the final buildable envelope and recompute floor areas, open space, occupant load, parking and code checks.
3. Dimension the reference layout, reconcile the legacy room targets with the actual room arrangement, and coordinate the ground/second-floor stair and balcony.
4. Update A-01 and coordinate A-04 through A-07 (roof, elevations, sections, details and schedules) to match the accepted layout.
5. Implement or finalize model-driven drawing generation and editable CAD export; inspect the outputs in compatible CAD software.
6. Proceed to Phase 6 specifications, Phase 7 documents, and Phase 8 presentation/print checks.

**Do not treat the project as ready for submission or construction yet.** The main current hold is Phase 2 verification and the resulting architectural coordination.


## Layout reference revision 01 (2026-10-12)

The student supplied furnished first- and second-floor images and selected them as the layout direction instead of the earlier simple room-box previews.

- **A-02:** TV console is shown in the living room, away from the entrance/foyer clearance area.
- **A-03:** gym and balcony are included; the karaoke room has one door on the circulation-hall side.
- `data/building_model.json` contains a new `reference_layout` section using SVG diagram units and automated checks for these two requirements.
- `space_planning/reference_layout_revision.md` records what changed and what remains open.

The visual layout is not a dimensioned plan. Existing room-size targets remain provisional and must be reconciled with the new arrangement. Site/setback confirmation and coordination of A-01/A-04-A-07 remain open.
