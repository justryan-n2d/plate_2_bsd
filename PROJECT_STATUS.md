# Project Status - CE 393 Plate No. 2

**Last updated:** 2026-10-10  
**Repository:** [`justryan-n2d/plate_2_bsd`](https://github.com/justryan-n2d/plate_2_bsd)  
**Main branch before the current Phase 2 revision:** `51efd88248d82da50dfb143c404044a02b4c53bc`  
**Current working branch:** `phase2-site-requirements`  
**Current review:** [Pull Request #6](https://github.com/justryan-n2d/plate_2_bsd/pull/6), open; contains the Phase 2 academic-assumption revision.

## Current position

This repository documents a **student academic plate**, not a real construction or permit project. Phase 2's working calculations have now been revised on the current branch based on the student's decisions and clearly labeled academic assumptions.

The A-01 to A-07 preliminary SVG package was merged into `main` through [PR #5](https://github.com/justryan-n2d/plate_2_bsd/pull/5). Phase 2's updated calculations, scenario status, model assumptions and project documentation are being delivered through PR #6. The drawings are still draft previews and require final coordination and presentation work for the class submission.

## Agreed academic assumptions

| Item | Adopted basis |
|---|---|
| Working lot area | **265.26 m²**, using the adjusted closed Phase 1 traverse |
| Original assignment area note | The brief says approximately 300.00 m²; keep as source information, not a blocker |
| Road and ROW | The **5.00 m carriageway is inside the 8.00 m total ROW** |
| Remaining ROW width | 3.00 m in total outside the carriageway; do not invent an exact split |
| Selected setback | **2.00 m on all five lot boundaries**, using PD 1096 Section 708(a) as the classroom baseline |
| Selected scenario | S-01; S-02 through S-04 are comparisons only |
| House footprint | 9.30 m × 7.90 m = 73.47 m² |
| Carport | 2.80 m × 5.50 m = 15.40 m²; one proposed car space |
| Floor areas | Ground 73.47 m²; second 73.47 m² under the same-envelope assumption; total 146.94 m² |
| Combined covered ground area | 88.87 m², or about 33.5% of the working lot area |
| Uncovered area | 176.39 m², or about 66.5%, after house + carport coverage |
| Academic design occupants | 6 persons, from the stated range of 5–6 persons |
| Stair | Carry forward Phase 4 calculation based on the assumed 3.000 m floor-to-floor rise |

The general Group A dwelling reference is [PD 1096, Section 708](https://elibrary.judiciary.gov.ph/thebookshelf/showdocs/26/53320). These are classroom assumptions used to complete the plate calculations, not representations of a real property survey, official zoning confirmation, permit review, or construction design.

## Status by phase

| Phase | Status | Main records | Remaining work |
|---|---|---|---|
| **1. Lot and site base** | Academic traverse and site-base package merged | `site/phase1_traverse_coordinates.csv`, `site/phase1_site_base.svg`, `site/phase1_site_analysis.md` | Carry the adopted 265.26 m² working area forward consistently; keep the source's approximate 300.00 m² note visible where useful |
| **2. Site requirements and calculations** | **Academic calculation baseline completed on current branch; PR #6 open** | `site/phase2_site_requirements.md`, `site/phase2_setback_scenarios.csv`, `previews/phase2_setback_scenarios.svg`, `calculations/plate2_calculations.md` | Coordinate selected assumptions into A-01 to A-03 and verify all sheet dimensions agree |
| **3. Space planning** | Preliminary programme and zoning package merged | `space_planning/space_requirement_table.csv`, `space_planning/adjacency_matrix.csv`, `space_planning/space_planning.md` and zoning previews | Recheck final room sizes and relationships after floor-plan coordination |
| **4. Stair planning** | Preliminary calculation and study package merged | `data/stair_design.json`, `space_planning/stair_design.md`, `space_planning/stair_plan.svg`, `space_planning/stair_section.svg` | Coordinate the assumed levels, headroom and handrails with final A-06 |
| **5. Architectural plan set** | Preliminary A-01 to A-07 SVG package merged | `previews/phase5_A01_site_development.svg` through `previews/phase5_A07_details_schedules.svg`, `data/building_model.json` | Show the 5.00 m road within the 8.00 m total ROW on A-01; align area assumptions; finish generation/editable CAD export and sheet coordination |
| **6. Preliminary specifications** | Not started | Checklist in `plate2 plan.md` | Prepare materials, workmanship requirements and specification schedule |
| **7. Required documentation** | Partially supported by earlier notes; not complete | Site analysis, calculations and Phase 3 records | Complete the final specification schedule, code-compliance checklist and design rationale |
| **8. Final review and presentation** | Not started | Submission checklist in `plate2 plan.md` | Coordinate title blocks, dimensions, scales, A3 sheets, long-bond calculations, final exports and print QA |

## Phase 2 results

| Calculation | Adopted academic result |
|---|---:|
| Uniform 2.00 m setback envelope (S-01) | **152.4309 m² ≈ 152.43 m²** |
| House footprint | 73.47 m² |
| Carport footprint | 15.40 m² |
| Total covered ground area | 88.87 m² |
| Ground-floor house area | 73.47 m² |
| Second-floor house area | 73.47 m² |
| Total house floor area | 146.94 m² |
| Uncovered lot area | 176.39 m² (66.5%) |
| Design occupant count | 6 persons |
| Proposed parking | 1 space, 2.80 m × 5.50 m |

S-01 contains the current house and carport rectangles. S-02 to S-04 remain in the scenario file and SVG for comparison, but the additional 4.50 m front-yard assumptions are not required blockers for the agreed classroom baseline.

## Next work, in order

1. Review/merge [PR #6](https://github.com/justryan-n2d/plate_2_bsd/pull/6) after checking the changed calculations and status records.
2. Revise A-01 to show the 5.00 m carriageway inside the 8.00 m total ROW and the selected 2.00 m academic setback. Do not assign the remaining 3.00 m to specific shoulder/drainage strips without a supplied drawing detail.
3. Check that the current 9.30 m × 7.90 m footprint, carport, floor-area assumptions, room layouts and stair agree across A-01, A-02, A-03 and A-06.
4. Finish the shared-source SVG generation and editable architectural DXF/DWG export; inspect the exports in compatible CAD software.
5. Complete Phase 6 specifications, Phase 7 documentation and Phase 8 sheet/print review.

**Phase 2 is considered complete for this academic exercise under the stated assumptions.** The final plate is not yet presentation-ready until the architectural sheets and final exports are coordinated. Nothing in this status claims real-site approval or construction readiness.
