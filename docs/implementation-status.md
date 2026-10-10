# Repository Implementation Status

**Project:** CE 393 Building System Design, Plate No. 2  
**Building:** Proposed two-storey residential building  
**Status date:** 2026-10-10  
**Working branch:** `phase-2-site-calculations`  
**Review:** [Pull Request #2](https://github.com/justryan-n2d/plate_2_bsd/pull/2)  
**Latest recorded full validation:** [GitHub Actions run 50](https://github.com/justryan-n2d/plate_2_bsd/actions/runs/38023516564)

This document records what has been implemented, the selected assumptions for the classroom activity, and the remaining work. The instructor's assignment and clarifications are the project source of truth. Room dimensions introduced in Phase 3 are proposals for planning, not instructor-given dimensions.

## 1. Current status at a glance

| Area | Status | What is done |
|---|---|---|
| Phase 1: site base | Implemented; CAD-app inspection remains | Lot traverse records, adjusted closing course, area/perimeter calculations, site analysis, SVG site preview, DXF/SVG generation and automated checks |
| Phase 2: site envelope | Complete enough to proceed | Instructor's 8.00 m road cross-section recorded; 2.00 m working inset adopted for all five lot edges; 152.43 m² working envelope calculated |
| Phase 3: space planning | Started | First-draft room-area table and ground-/second-floor adjacency diagrams recorded |
| Floor-plan layout | Not done yet | Need to arrange rooms and parking in dimensioned plans within the working site envelope |
| Final drawing package | Not done yet | Roof plan, elevations, sections, details, schedules, specifications, PDFs/DWGs and final coordination remain |

## 2. Source project information

The assignment describes a two-storey Group A residential building, initial construction type V-A, for 5-6 occupants, at Lot 245-B, Barangay San Isidro, Palo, Leyte. The stated area is approximately 300.00 m².

The adjusted closed Phase 1 polygon calculates to **265.26 m²**, with an adjusted perimeter of approximately **64.1454 m**. The **34.74 m²** difference from the assignment's approximate area is documented rather than corrected by changing more traverse courses. The first four boundary courses are retained, and the instructor-directed adjustment is confined to the closing course P5-1. The coordinates are a classroom plotting basis, not a cadastral survey.

## 3. Phase 1 work completed

- Transcribed the technical-description courses into the site coordinate records and preserved the original closing-course information alongside the adjusted closure record.
- Calculated and documented the adjusted area, perimeter, and difference from the approximate area in the assignment.
- Prepared the preliminary site-base SVG and automated DXF/SVG generation and validation scripts.
- Added a read-only GitHub Actions workflow that checks the source traverse, unit tests, reports, generated drawing geometry, labels, and SVG preview.
- Recorded the required site-analysis topics and the instructor's road cross-section in the site files.

**Still pending for Phase 1 drawing acceptance:** open the generated DXF in compatible CAD software and visually check units, layers, linework, labels, extents, and plot behavior. Passing automated checks does not replace that manual CAD-app inspection.

## 4. Phase 2 work completed

### 4.1 Instructor-specified road cross-section

The working site drawing uses the instructor's clarification:

**8.00 m total RROW = 1.50 m side strip + 5.00 m barangay road/carriageway + 1.50 m side strip.**

This allocation is settled for the classroom activity. It is not recorded as an unresolved input.

### 4.2 Working setback and envelope

For this activity, the selected working assumption is a **2.00 m inward inset from each of the five plotted property boundaries**. The calculation uses the adjusted closed lot polygon and yields a **152.43 m² working envelope**, referred to as Scenario A.

| Scenario | Working offsets on edges 1-2, 2-3, 3-4, 4-5, 5-1 | Inset area | Use |
|---|---|---:|---|
| A | 2.00 m on every edge | 152.43 m² | Selected working envelope for Phase 3 |
| B | 2.00 m, 2.00 m, 4.50 m, 2.00 m, 2.00 m | 128.90 m² | Comparison only |
| C | 2.00 m, 2.00 m, 2.00 m, 4.50 m, 2.00 m | 125.02 m² | Comparison only |
| D | 2.00 m, 2.00 m, 4.50 m, 4.50 m, 2.00 m | 112.29 m² | Comparison only |

The 4.50 m alternatives are kept for comparison and are not used as the selected classroom layout basis.

### 4.3 Other preliminary figures

- Corner-lot occupancy scenario: 90% of 265.2598 m² = **238.73 m²** maximum occupied area, with **26.53 m²** as its corresponding open-area balance.
- Inside-lot comparison: 80% = **212.21 m²** maximum occupied area, with **53.05 m²** as the corresponding open-area balance.
- Preliminary parking basis: one on-site off-street car slot for the assumed single-family dwelling activity. The standard slot rectangle used for the first draft is **2.50 m × 5.00 m = 12.50 m²** for perpendicular/diagonal parking. The parallel option in the calculation record is 2.15 m × 6.00 m.
- The occupancy ceilings are not the building footprint. The actual footprint and residual open space must be calculated from the dimensioned plan.

### 4.4 Phase 2 implementation files

- [Phase 2 calculation report](../calculations/phase2_site_calculations.md)
- [Building-envelope scenarios and local inset coordinates](../calculations/phase2_envelope_scenarios.md)
- [Per-boundary working setback inputs](../site/phase2_setback_inputs.csv)
- [Traceable code requirements register](../site/phase2_code_requirements.csv)
- [Calculator, validation logic, and tests](../scripts/calculate_phase2_site.py)

## 5. Phase 3 work started

The first-draft [space program and adjacency document](../design/phase3_space_program.md) records the required spaces and a proposed set of room-size targets for early planning.

It includes:
- Ground-floor spaces: entrance/foyer, living room, dining area, kitchen, toilet and bath, guest bedroom, stairway, storage/service area, and garage/carport slot.
- Second-floor spaces: master bedroom, two additional bedrooms, toilet and bath, family area, stair landing/circulation, and optional balcony.
- Proposed dimensions and target areas, explicitly identified as design proposals.
- Ground-floor and second-floor adjacency diagrams.
- Preliminary priorities for privacy, circulation, kitchen/service connections, pedestrian access, and parking access.

**No dimensioned floor-plan layout has been completed yet.** The next task is to arrange the space blocks inside the selected 152.43 m² working envelope, then coordinate the two floor plans, stair location, bathroom/service areas, parking, driveway, doors, windows, and circulation.

## 6. Remaining work

### Phase 3
- Fit and revise the ground-floor room layout inside the working site envelope.
- Develop the second-floor plan and coordinate stairs and wet areas between floors.
- Recalculate gross floor areas, total floor area, actual footprint, and remaining open space from the dimensioned layout.
- Position parking and driveway/access without using the road right-of-way for the parking slot.
- Calculate occupant load and other requirements that depend on the chosen floor area and occupancy.
- Review circulation, privacy, light and ventilation, door/window placement, furniture clearances, and functional relationships.

### Later phases and final submission
- Finish stair geometry and show it consistently in plans and a section through the stairway.
- Prepare roof plan, four elevations, at least two building sections, architectural details, schedules, and preliminary building specifications.
- Complete the required Space Requirement Table, Adjacency Diagram, Site Analysis, specifications, specification schedule, Code Compliance Checklist, and Design Rationale.
- Coordinate all drawings and calculations; prepare the requested A3 drawing sheets and long-bond calculation pages.
- Generate and review final SVG/DXF files, inspect CAD files in a compatible application, and prepare checked PDF and DWG delivery files where required by the assignment.

## 7. Validation and GitHub status

The latest recorded full automated validation is [run 50](https://github.com/justryan-n2d/plate_2_bsd/actions/runs/38023516564), which passed:
1. Python compilation checks.
2. Phase 1 traverse validation.
3. Phase 2 unit tests.
4. Verification that the committed Phase 2 report matches the calculation script.
5. Verification that the envelope scenario report matches the calculation script.
6. DXF/SVG generation and validation.
7. Upload of the generated DXF and SVG as a workflow artifact.

The workflow's drawing artifacts are temporary (14-day retention); the generator does not automatically commit generated CAD files. Review the latest successful Actions run to download them.

**GitHub PR status:** [Pull Request #2](https://github.com/justryan-n2d/plate_2_bsd/pull/2) remains open as a draft. These changes are on `phase-2-site-calculations`; this documentation does not claim the branch has been merged into `main`.

## 8. Important file map

| Path | Purpose |
|---|---|
| `plate2 plan.md` | Assignment scope, deliverable checklist, phased work plan, and drawing roadmap |
| `site/phase1_traverse_coordinates.csv` | Source coordinate/course records and closing-course information |
| `site/phase1_site_analysis.md` | Narrative site analysis and supported/pending observations |
| `site/phase1_site_analysis_matrix.csv` | Site topics, evidence, status, and actions |
| `site/phase1_site_base.svg` | Existing preliminary site-base preview |
| `scripts/generate_site_base.py` | DXF/SVG generation from source data |
| `scripts/validate_site_base.py` | Source traverse validation |
| `scripts/validate_generated_dxf.py` | Generated CAD/SVG checks |
| `scripts/calculate_phase2_site.py` | Phase 2 calculations and reproducible report generation |
| `tests/test_phase2_site.py` | Phase 2 geometry and report consistency tests |
| `calculations/phase2_site_calculations.md` | Site geometry, occupancy, setback assumptions, parking basis, and remaining layout calculations |
| `calculations/phase2_envelope_scenarios.md` | Working envelope, alternatives, and inset polygon coordinates |
| `design/phase3_space_program.md` | Initial room program and adjacency diagrams |
| `.github/workflows/validate-drawings.yml` | Automated validation workflow |

## 9. Limitations

This is a classroom design workflow. Automated checks verify internal consistency and calculation reproducibility; they do not certify the property survey, professional code compliance, structural adequacy, permit readiness, or construction readiness. Use the instructor's activity requirements for this plate, and revise proposed room dimensions as the plans develop.
