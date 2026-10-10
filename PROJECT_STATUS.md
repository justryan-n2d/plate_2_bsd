# Project Status - CE 393 Plate No. 2

**Last updated:** 2026-10-10  
**Repository:** [`justryan-n2d/plate_2_bsd`](https://github.com/justryan-n2d/plate_2_bsd)  
**Main branch after latest merge:** `51efd88248d82da50dfb143c404044a02b4c53bc`  
**Current working branch:** `phase2-site-requirements`  
**Current review:** [Pull Request #6](https://github.com/justryan-n2d/plate_2_bsd/pull/6), open and awaiting review.

## Current position

**Current work is Phase 2: site requirements and setback confirmation.** A-01 to A-07 preliminary SVG previews, the shared draft model and the initial Phase 5 notes were merged into `main` through [PR #5](https://github.com/justryan-n2d/plate_2_bsd/pull/5). The drawings are still preliminary, not code-approved or construction-ready.

Phase 3 space planning merged through [PR #3](https://github.com/justryan-n2d/plate_2_bsd/pull/3), Phase 4 stair planning through [PR #4](https://github.com/justryan-n2d/plate_2_bsd/pull/4), and Phase 5 preliminary drawing previews through [PR #5](https://github.com/justryan-n2d/plate_2_bsd/pull/5). The latest Phase 5 revision passed the Phase 5 SVG/data validator, Phase 3 validator and existing Phase 1 CAD validation. Phase 2 now compares four setback screening cases; no final legal setback has been chosen.

## Status by phase

| Phase | Status | Main records | Remaining limitation |
|---|---|---|---|
| **1. Lot and site base** | Preliminary work completed and merged | `site/phase1_traverse_coordinates.csv`, `site/phase1_site_base.svg`, `site/phase1_site_analysis.md` | Adjusted area is 265.26 m² vs the assignment's approximate 300.00 m²; official survey/ROW/site conditions need confirmation. |
| **2. Site requirements and calculations** | Four setback screening scenarios and validator added; official decisions pending | `site/phase2_site_requirements.md`, `site/phase2_setback_scenarios.csv`, `previews/phase2_setback_scenarios.svg`, calculations C-04-C-09 | Local zoning, legal road/ROW limits, front-yard classification, final envelope, occupant load, parking, open space and official floor areas remain unconfirmed. |
| **3. Space planning** | Preliminary package merged | `space_planning/space_requirement_table.csv`, `space_planning/adjacency_matrix.csv`, `space_planning/space_planning.md` and three SVG previews | Target room sizes/zoning are not final architectural dimensions. |
| **4. Stair planning** | Preliminary calculation package merged | `data/stair_design.json`, `space_planning/stair_design.md`, `space_planning/stair_plan.svg`, `space_planning/stair_section.svg` | Assumes 3.000 m floor-to-floor rise; confirm levels and BP 344 applicability. Structural design and final section clearance checks remain. |
| **5. Architectural plan set** | Preliminary A-01-A-07 SVG package merged | `previews/phase5_A01_site_development.svg` through `previews/phase5_A07_details_schedules.svg`, `data/building_model.json` | Drawings need revision after Phase 2; automatic model-to-SVG generation and editable architectural DXF/DWG export are not complete. |
| **6. Preliminary specifications** | Not started | Checklist in `plate2 plan.md` | Materials, workmanship requirements and specification schedule need to be written/coordinated. |
| **7. Required documentation** | Partial source notes exist; final documents pending | Site analysis, calculations and Phase 3 records | Final space table, specification schedule, code compliance checklist and design rationale need completion. |
| **8. Final review and presentation** | Not started | Submission checklist in `plate2 plan.md` | Final CAD/DWG/PDF, A3 sheets, long-bond calculations, visual inspection and print QA remain. |

## Phase 2 screening results

All four areas were calculated by offsetting the adjusted academic traverse inward by the stated distances. They are **screening polygons, not legally approved buildable envelopes**.

| Scenario | Offset assumptions | Calculated screen area | Current house placement fits | Current carport placement fits |
|---|---|---:|---|---|
| S-01 | 2.00 m from all boundaries | 152.4309 m² | Yes | Yes |
| S-02 | P2-P3 at 4.50 m, other edges 2.00 m | 128.9837 m² | Yes | No |
| S-03 | P3-P4 at 4.50 m, other edges 2.00 m | 128.8989 m² | No | No |
| S-04 | Both road-side edges at 4.50 m, other edges 2.00 m | 112.6268 m² | No | No |

"No" tests the current rectangle at its current position only. It means move/redesign the current layout if that scenario is accepted; it does not prove that no house can fit in the envelope.

## Important assumptions / blockers

1. The assignment's 300.00 m² lot area is approximate; the adjusted academic traverse calculates to 265.2598 m². The original approved survey plan still needs checking.
2. The assignment describes a 5.0 m existing road and separately states an 8.00 m ROW. The legal ROW line and exact road-frontage geometry are not provided.
3. PD 1096 Section 708(a) supplies a general Group A dwelling property-line-distance baseline; the published 2004 Revised IRR Table VIII.2 includes R-1 front/side/rear yard dimensions for newly-developed subdivisions. Applicability, the local Palo zoning and which road boundary is the legal front yard must be confirmed. See [PD 1096, Supreme Court E-Library](https://elibrary.judiciary.gov.ph/thebookshelf/showdocs/26/53320) and [the 2004 Revised IRR reference copy](https://www.iibh.org/kijun/pdf/Philippines_02_IRR_of_NBC_of_the_Philippines.pdf).
4. The current 9.30 m × 7.90 m house and 2.80 m × 5.50 m carport are concept placements. The A-01 uniform 2.00 m inset is not the final legal setback.
5. Phase 4 assumes a 3.000 m floor-to-floor rise; the instructor / actual sections must confirm it.
6. The SVG previews are for draft review. They are not permits, structural drawings or construction documents.

## Next work

1. Obtain confirmation of survey/ROW lines, local Palo zoning, applicable yard classification and setbacks from the appropriate local office / instructor.
2. Select the applicable scenario only after that confirmation; recalculate the final envelope and revise A-01 and the carport / house placement.
3. Recalculate the actual footprint, measured floor areas, code-defined open space, occupant load, parking and other applicable requirements in C-04 through C-09.
4. Confirm floor levels and stair/accessibility rules; coordinate openings, roof, elevations and actual building sections.
5. Implement the shared-source drawing generator and editable CAD export; inspect generated drawings in compatible CAD software.
6. Finish Phase 6 specifications, Phase 7 documentation and Phase 8 final review / printing.

**Do not treat the project as ready for submission or construction yet.** Phase 2 official site/code confirmation is the current main dependency.
