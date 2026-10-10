# CE 393 Plate No. 2

Project workspace for the proposed two-storey residential building plate.

## Current status

- Phase 1 site-base inputs and analysis are in the site folder.
- The academic plot closes by keeping courses 1-2 through 4-5 unchanged and using the documented adjusted P5-1 closing course.
- The assignment's 300.00 m² area is approximate. The adjusted closed polygon calculates to 265.26 m². Both values are documented; the plot is not forced to match the approximate figure.
- Drawing-generation and validation scripts, dependency documentation, folder notes, and a read-only GitHub Actions workflow are committed.
- GitHub Actions generates and validates the Phase 1 DXF/SVG output from the traverse data.
- Phase 3 now has a preliminary room requirement table, adjacency matrix, relationship diagram, and conceptual zoning diagrams for both floors. Phase 4 now adds a stair calculation/source-data package and plan/section previews. These are preliminary, not structural or construction drawings.
- Phase 5 A-01 to A-07 draft previews and the shared building model are merged into `main` through [PR #5](https://github.com/justryan-n2d/plate_2_bsd/pull/5); they remain preliminary and are not code-approved.
- Phase 2 now uses 265.26 m² as the working lot area, selects S-01 with uniform 2.00 m academic setbacks, and records the 5.00 m carriageway within the 8.00 m total ROW. See `site/phase2_site_requirements.md` and `PROJECT_STATUS.md`.
- The latest enhanced run passed: [view run and download artifact](https://github.com/justryan-n2d/plate_2_bsd/actions/runs/38008699847).
- Generated outputs are currently time-limited workflow artifacts, not automatically committed to the branch. Manual visual inspection in compatible CAD software remains required before accepting the drawing.

## Phase 1 site-base preview

![Preliminary Phase 1 site base](site/phase1_site_base.svg)

See the [site folder README](site/README.md) for source files, assumptions, and verification limits.

## Phase 2 setback scenario preview

S-01 (uniform 2.00 m setbacks) is the selected academic design basis. S-02 to S-04 remain comparison cases only. The site notes treat the 5.00 m carriageway as inside the 8.00 m total ROW.

![Phase 2 setback scenarios](previews/phase2_setback_scenarios.svg)

See [Phase 2 site requirements](site/phase2_site_requirements.md) and [scenario data](site/phase2_setback_scenarios.csv).

## Phase 3 space-planning previews

These SVGs are conceptual zoning diagrams, not dimensioned floor plans. The Phase 2 academic setback and buildable-envelope calculations are now recorded; the floor plans still need to be coordinated to them. The Phase 4 stair study uses an assumed 3.000 m floor-to-floor height that must match the final academic section.

### Adjacency / relationship diagram

![Preliminary adjacency diagram](space_planning/adjacency_diagram.svg)

### Ground-floor conceptual zoning

![Preliminary ground-floor zoning](space_planning/ground_floor_zoning.svg)

### Second-floor conceptual zoning

![Preliminary second-floor zoning](space_planning/second_floor_zoning.svg)

See the [Phase 3 space-planning notes](space_planning/space_planning.md), [room schedule](space_planning/space_requirement_table.csv), and [adjacency matrix](space_planning/adjacency_matrix.csv).

## Phase 4 stair study

The preliminary stair study is merged into `main`; it assumes a 3.000 m floor-to-floor rise and is not structural or construction documentation.

![Preliminary stair plan](space_planning/stair_plan.svg)

![Preliminary stair section study](space_planning/stair_section.svg)

See [stair calculations and code hold points](space_planning/stair_design.md).

## Phase 5 architectural draft previews

These A-01 to A-07 sheets are preliminary visual drafts for the student activity. Phase 2 uses 265.26 m² as the working lot area, a uniform 2.00 m setback on all five boundaries, and the 5.00 m carriageway inside the 8.00 m total ROW. The second-floor design now includes a required 3.00 m × 1.50 m balcony accessed from the master bedroom; its 4.50 m² is counted separately from enclosed floor area.

### A-01 - Site Development Plan

![A-01 preliminary site plan](previews/phase5_A01_site_development.svg)

### A-02 - Ground Floor Plan

![A-02 preliminary ground floor](previews/phase5_A02_ground_floor.svg)

### A-03 - Second Floor Plan

The second floor includes a required 3.00 m × 1.50 m balcony accessed from the master bedroom. The balcony area is 4.50 m² and is listed separately from enclosed floor area.

![A-03 preliminary second floor](previews/phase5_A03_second_floor.svg)

### A-04 - Roof Plan

![A-04 preliminary roof plan](previews/phase5_A04_roof_plan.svg)

### A-05 - Four Elevations

![A-05 preliminary elevations](previews/phase5_A05_elevations.svg)

### A-06 - Building Sections

![A-06 preliminary sections](previews/phase5_A06_sections.svg)

### A-07 - Details and Schedules

![A-07 preliminary details and schedules](previews/phase5_A07_details_schedules.svg)

See the [Phase 5 architecture notes](space_planning/phase5_architecture_notes.md), [shared building model](data/building_model.json), and [project status](PROJECT_STATUS.md).

## Project records

- [Project status](PROJECT_STATUS.md): what is finished, current phase, assumptions, blockers, and next steps.
- [Phase 2 site requirements and calculations](site/phase2_site_requirements.md): agreed academic assumptions, selected 2.00 m setbacks, ROW interpretation and completed preliminary calculations.
- [Setback scenario data](site/phase2_setback_scenarios.csv): four calculated offsets, with S-01 marked as the selected academic basis.
- [Project plan](plate2%20plan.md): assignment scope, required submissions, work plan, and drawing roadmap.
- [Shared preliminary building model](data/building_model.json): site/building geometry and assumptions for Phase 5 drafts.
- [Phase 5 architectural notes](space_planning/phase5_architecture_notes.md): drawing register and limitations.
- [Calculation worksheet](calculations/plate2_calculations.md): calculation methods, values, and checks.
- [Traverse coordinate CSV](site/phase1_traverse_coordinates.csv): original and adjusted course records, coordinates, and closure diagnostics.
- [Site analysis](site/phase1_site_analysis.md): supported site findings and items requiring further verification.
- [Site analysis matrix](site/phase1_site_analysis_matrix.csv): site topics, evidence, status, and follow-up actions.

## Planned CAD workflow

1. Validate the existing traverse CSV.
2. Generate editable DXF geometry and a matching SVG preview from the same numeric source.
3. Check course components, coordinate closure, perimeter, polygon area, CAD units, layers, and output consistency.
4. Open the DXF in compatible CAD software and inspect it visually.
5. Convert a reviewed DXF to DWG when needed, then inspect the converted file.
6. Prepare and check the required PDF sheets.

DXF is the editable CAD master in this workflow. DWG is a converted delivery copy. The source CSV and generation code are the traceable sources for plotted geometry.

## Folder guide

- **calculations/**: calculation work and results.
- **site/**: current Phase 1 source data, drawing, and analysis.
- **data/**: future shared building model and schedules. The building model file will be added after the layout is actually defined.
- **scripts/**: drawing generation and validation tools.
- **previews/**: generated project-wide SVG previews. The existing Phase 1 SVG remains in site/ to preserve current links.
- **drawings/**: generated editable DXF masters.
- **exports/pdf/** and **exports/dwg/**: reviewed deliverables.
- **.github/workflows/**: automated validation checks.

## Local commands

Use Python 3.11 or newer, from the repository root:

    python -m pip install -r scripts/requirements.txt
    python scripts/validate_site_base.py
    python scripts/generate_site_base.py

The generator writes drawings/phase1_site_base.dxf and previews/phase1_site_base_preview.svg. The workflow runs the source validator, generates both files, validates the generated DXF and SVG, and uploads them as the `plate2-phase1-cad-*` artifact for 14 days. See [GitHub Actions](https://github.com/justryan-n2d/plate_2_bsd/actions/workflows/validate-drawings.yml) and open the latest successful run to download the files. Generated CAD output remains preliminary until inspected in compatible CAD software.

## Limits

- The adjusted traverse is an academic plotting basis under the instructor's direction, not cadastral survey certification.
- The 5.0 m road width and 8.00 m right-of-way are separate stated values. No precise allocation of the remaining 3.0 m is assumed.
- Exact road/ROW edges, site levels, drainage, obstructions, setbacks, and parcel-specific hazard results are not inferred from the local coordinate plot.
- Automated checks do not establish code compliance, structural adequacy, permit readiness, or construction readiness.
