# Plate No. 2 Project Plan
## CE 393: Building System Design

**Project title:** Proposed Two-Storey Residential Building  
**Course activity:** Plate No. 2 in CE 393  
**Project repository:** `justryan-n2d/plate_2_bsd`  
**Plan purpose:** Track the work required by the instructor's Plate No. 2 document.

> **Basis and limit:** This plan is based only on the instructions in the provided *Plate No. 2 in CE 393: Building System Design* document. The task checklists organize the stated requirements; they do not add extra deliverables. Use the instructor's instructions when a drawing scale or other detail is left open.

---

## 1. Project objective

Prepare the preliminary design for a proposed two-storey residential building based on the lot description, applicable codes and regulations, user requirements, space-planning principles, and basic building-design considerations stated in the assignment.

The completed plate is intended to serve as the base building plan for the subsequent structural and utility systems described in the instructions.

## 2. Given project information

| Item | Information stated in the assignment |
|---|---|
| Project type | Two-storey residential building |
| Occupancy group | A |
| Initial construction type | Type V-A |
| Proposed occupants | 5–6 persons |
| Approximate lot area | 300.00 m² |
| Road right-of-way in project information | 8.00 m |
| Site condition | Generally level / grass land |
| Existing building | None |
| Building design | Required |
| Preliminary specifications | Required |
| Utility design | Excluded from Plate No. 2 |
| Lot number | 245-B |
| Survey plan | Psd-08-2026-XXX |
| Location | Barangay San Isidro, Municipality of Palo, Province of Leyte |

### Lot description given in the assignment

The property is bounded by Lot 245-A on the north, Lot 246 on the east, a stated existing 5.0 m barangay road on the southeast and southwest, and Lot 244 on the west.

| Line | Bearing | Distance |
|---|---|---:|
| 1–2 | N 78° 30' E | 15.20 m |
| 2–3 | S 12° 15' E | 11.80 m |
| 3–4 | S 48° 20' W | 8.75 m |
| 4–5 | S 83° 40' W | 12.60 m |
| 5–1 | N 08° 10' W | 16.35 m |

Use the instructor's clarified road cross-section: 8.00 m total RROW = 5.00 m existing barangay road + 1.50 m remaining RROW strip on each side. Show the 5.00 m carriageway and both 1.50 m strips separately on the preliminary site plan. The 3.00 m balance is therefore allocated symmetrically for this plate, not left unspecified.

---

## 3. Scope stated in the assignment

### Included

- Site base plan and site analysis.
- Space-requirement and adjacency/relationship analysis.
- Ground-floor and second-floor layouts.
- Roof plan.
- Four elevations.
- At least two building sections, including one through the stairway.
- Architectural details and schedules.
- Preliminary building specifications.
- The listed area, traverse, setback, occupant-load, stair, parking, and other applicable calculations.
- Code-compliance checklist and design rationale.
- Required drawings, calculations, documentation, and printed presentation.

### Excluded by the project description

Detailed utility systems are not to be designed in Plate No. 2. The assignment specifically names plumbing, sanitary, electrical, mechanical, fire-protection, and other building services as work for succeeding plates.

### Item listed in the submission checklist that needs attention

The required-submission list also includes column, footing and beam details/schedules, a foundation plan, and a second-floor framing plan, while the project description says the preliminary building plan will serve as the basis for later structural and utility systems. Keep these items in the submission checklist because they are explicitly listed. Follow the instructor's direction on how they are to be handled for this plate.

---

## 4. Required spaces

### Ground floor

- [ ] Entrance / foyer
- [ ] Living room
- [ ] Dining area
- [ ] Kitchen
- [ ] Toilet and bath
- [ ] Bedroom / guest room
- [ ] Stairway
- [ ] Storage / service area
- [ ] Garage / carport

### Second floor

- [ ] Master bedroom
- [ ] Bedroom 2
- [ ] Bedroom 3
- [ ] Toilet and bath
- [ ] Family area
- [ ] Stair landing / circulation
- [ ] Balcony, if appropriate

Additional spaces may be included when justified by the design.

---

## 5. Work plan

The order below is a practical way to track the stated requirements. The required outputs remain those listed in the assignment.

### Phase 1: Lot and site base

- [x] **T-01** Transcribe the lot bearings and distances from the technical description.
- [x] **T-02** Calculate the area from the closed traverse: 265.26 m² using adjusted P5-1. The difference from the approximate 300.00 m² stated in the brief (34.74 m²) is documented.
- [x] **T-03** Determine the property-boundary lengths and lot dimensions, with adjusted P5-1 documented separately from the original value.
- [x] **T-04** Plot and close the traverse by adjusting P5-1 only; retain the original value and show both values in the records.
- [x] **T-05** Prepare the preliminary site base using the technical description.
- [x] **T-06** Show property boundaries, course distances and bearings, north direction, road context, and adjacent properties in the preliminary site-base drawing.
- [x] **T-07** Complete the source-based site analysis and record evidence, limits, and site-verification items in `site/phase1_site_analysis.md` and `site/phase1_site_analysis_matrix.csv`. Exact access points, parcel-specific solar/shading, and existing-condition checks remain subject to field verification and later site-development planning.

#### Phase 1 implementation checkpoint (2026-10-10)

**Current status: The preliminary site-base traverse is closed by adjusting only P5-1 per the instructor's direction. Courses 1-2 through 4-5 remain exactly as given. The original P5-1 value is preserved for reference. The source-based site analysis is documented without beginning the house layout.**

Preliminary outputs are available in [the site base SVG](site/phase1_site_base.svg), [the traverse coordinate schedule](site/phase1_traverse_coordinates.csv), [the site-analysis note](site/phase1_site_analysis.md), and [the site-analysis evidence matrix](site/phase1_site_analysis_matrix.csv).

The original five listed courses produce a latitude sum of +0.4764 m, departure sum of -3.9836 m, and linear misclosure of approximately 4.0120 m. As directed, the first four courses are held unchanged and only P5-1 is adjusted from N 08°10′ W, 16.35 m to N 06°02′11″ E, 15.7954 m (about 15.80 m) so that it closes at P1. Both the original and adjusted P5-1 data are documented.

The adjusted closed traverse gives a perimeter of 64.1454 m and a polygon area of 265.26 m². The assignment's approximate 300.00 m² value is 34.74 m² higher than the calculated area, so both values are recorded. The 300.00 m² value is explicitly approximate. The 265.26 m² value is the calculated area of the adjusted closed polygon; the 34.74 m² difference is documented and accepted as a difference from the approximate figure, not a reason to force the traverse to match 300.00 m². The difference is therefore not a blocker by itself. If the original approved survey document or a later instructor direction becomes available, use it to confirm the source information rather than silently changing the remaining courses.

The 5.00 m carriageway and 8.00 m total RROW remain separately dimensioned. Per the instructor's clarification, the total includes a 1.50 m strip on each side of the 5.00 m carriageway. Use this known allocation in the academic road graphic; do not relabel the roadside strips as a specific sidewalk or drainage feature unless the assignment specifies that use.

The site analysis now records the eight requested topics: lot orientation, north direction, road access, solar orientation, vehicular access, pedestrian access, service access, and existing site conditions. It also includes a nearby regional climate reference from PAGASA's Tacloban City 1991-2020 normals and a link to HazardHunterPH for later location-based checking. These are contextual references only; they are not parcel-specific measurements or a completed hazard assessment.

**Still on hold before a final Site Development Plan:** use the instructor-provided road cross-section (8.00 m total RROW = 5.00 m carriageway + 1.50 m strip per side) in the site graphic, check actual site conditions if required, and establish the applicable final setbacks. The area difference is documented but is not treated as an error solely because the 300.00 m² figure is approximate. The adjusted traverse is an academic plotting basis under the instructor's direction, not a cadastral certification. Exact driveway, pedestrian entrance, and service-access positions remain deferred until the site development and house layout stages. No house layout has been started in this phase.

#### Repository status and verification record (2026-10-10)

The Phase 1 implementation was merged into `main` through [Pull Request #1](https://github.com/justryan-n2d/plate_2_bsd/pull/1). Merge commit: `2c5fea33b6e55260d0612cefbc2db38235db02f3`. The earlier statement that the pull request was still unmerged is no longer current.

The following checks were confirmed against the repository files now on `main`:

- Original P5-1, adjusted P5-1, and original closure gap remain separately recorded.
- Adjusted closing-course components return to P1; the closed traverse is reported with approximately 0.000000 m latitude and departure misclosure, based on the recorded component precision.
- Adjusted perimeter (64.1454 m), adjusted polygon area (265.26 m²), assignment approximate area (300.00 m²), and 34.74 m² difference are stated consistently in the site-base records.
- The road graphic uses the instructor's clarified allocation: 8.00 m total RROW = 5.00 m carriageway + 1.50 m strip on each side.
- CSV structure and field formatting, required site-analysis topics, cross-file references, and the explicit no-house-layout boundary were checked.

These are document and arithmetic consistency checks, not a professional survey certification. The difference between 265.26 m² and the approximate 300.00 m² figure is understood and documented; it is not a target to reconcile by changing the adjusted traverse. For this academic plate, the site layout will use the instructor-provided road cross-section and the 2.00 m working setback baseline adopted in Phase 2. House-layout work can now begin using the 152.43 m² working envelope; the adjusted plot remains an academic drawing based on the assignment's technical description.

### Phase 2: Site requirements and preliminary calculations

- [x] **T-10** Determine required setbacks using the instructor-activity baseline from PD 1096 Section 708(a): 2.00 m inward from each of the five plotted property boundaries.
- [x] **T-11** Determine the buildable area / allowable building envelope: Scenario A, a 2.00 m inset on all five edges, calculates to 152.43 m² and is selected as the working envelope for Phase 3.
- [ ] **T-12** Determine the proposed building footprint.
- [ ] **T-13** Calculate the ground-floor area.
- [ ] **T-14** Calculate the second-floor area.
- [ ] **T-15** Calculate the total floor area.
- [ ] **T-16** Determine the remaining open space.
- [ ] **T-17** Determine the applicable occupant load.
- [x] **T-18** Determine the preliminary parking requirement: use one on-site off-street slot as the activity basis for a single-family dwelling, with a 2.50 m × 5.00 m perpendicular/diagonal slot rectangle.
- [ ] **T-19** Identify and calculate remaining applicable code-based dimensions and requirements alongside the floor plan and stair design.

#### Phase 2 implementation checkpoint (2026-10-10)

**Status: Phase 2's site-envelope gate is complete for this instructor-led academic activity, and Phase 3 can proceed.** The Phase 2 site calculation report and the preliminary building-envelope scenario report record the adopted assumptions, numerical results, and coordinates. The calculation script validates the Phase 1 traverse, applies the 2.00 m working offset on all five edges, calculates the working inset area, and includes tested geometry functions.

The [Phase 2 code requirements register](site/phase2_code_requirements.csv) separates cited national-code provisions, assignment facts, provisional calculations, and local/site-specific items requiring verification.

- **T-10:** The working setback is adopted as 2.00 m inward from each plotted property boundary for this academic activity.
- **T-11:** Scenario A in [phase2_envelope_scenarios.md](calculations/phase2_envelope_scenarios.md) gives a working envelope of **152.43 m²**. Scenarios B-D are retained for comparison only.
- **T-18:** Use one on-site off-street parking slot as the preliminary activity basis. The slot rectangle is 2.50 m × 5.00 m for perpendicular/diagonal parking, or 2.15 m × 6.00 m for parallel parking.
- **Occupancy check:** Because the assignment describes road frontage on both southeast and southwest sides, use the 90% corner-lot scenario (238.73 m² maximum occupied area, 26.53 m² corresponding open area) for the working comparison. The 80% inside-lot values remain in the calculation report for reference.

The site-envelope basis is complete enough to proceed to Phase 3. The actual building footprint, floor areas, remaining open space, occupant-load calculation, stair geometry, and parking placement depend on the room layout and will be completed as the plans develop.

### Phase 3: Space planning

- [ ] **T-20** Make the space-requirement table for the proposed rooms and spaces.
- [ ] **T-21** Prepare an adjacency / relationship diagram showing functional relationships between the spaces.
- [ ] **T-22** Consider functional relationships, privacy, accessibility, convenience, service relationships, circulation, and safety.
- [ ] **T-23** Arrange the required ground-floor spaces.
- [ ] **T-24** Arrange the required second-floor spaces.
- [ ] **T-25** Review the building layout for functional space relationships and circulation.

### Phase 4: Stair planning and calculations

- [ ] **T-30** Determine the total stair height.
- [ ] **T-31** Determine the stair width.
- [ ] **T-32** Determine the number of risers.
- [ ] **T-33** Calculate the riser height.
- [ ] **T-34** Determine the tread depth.
- [ ] **T-35** Determine the landing dimensions.
- [ ] **T-36** Check that the stair layout and dimensions are shown consistently on plans and in at least one building section through the stairway.

### Phase 5: Architectural plan set

- [ ] **T-40 / A-01** Prepare the Site Development Plan.
- [ ] **T-41 / A-02** Prepare the Ground Floor Plan.
- [ ] **T-42 / A-03** Prepare the Second Floor Plan.
- [ ] **T-43 / A-04** Prepare the Roof Plan.
- [ ] **T-44 / A-05** Prepare four elevations: front, rear, left-side, and right-side.
- [ ] **T-45 / A-06** Prepare at least two building sections, with at least one passing through the stairway.
- [ ] **T-46 / A-07** Prepare architectural details and schedules.
- [ ] **T-47** Coordinate room names, dimensions, openings, stairs, floor levels, roof features, and other information shown across the drawings.
- [ ] **T-48 / D-01** Establish a code-driven, shared drawing-data source where practical so the SVG inspection previews and DXF drawing exports are generated from matching geometry and dimensions.
- [ ] **T-49 / D-02** Generate and review an SVG preview as each major 2D drawing is developed; use the preview to find layout, label, dimension, and coordination errors before final export.

### Phase 6: Preliminary specifications

- [ ] **T-50** Prepare the General Requirements section.
- [ ] **T-51** Prepare the Sitework section.
- [ ] **T-52** Prepare the Concrete and Masonry section.
- [ ] **T-53** Prepare the Roofing section.
- [ ] **T-54** Prepare the Doors and Windows section.
- [ ] **T-55** Prepare the Finishes section.
- [ ] **T-56** Prepare the Stair and Railings section.
- [ ] **T-57** Prepare the specification schedule required for submission.

### Phase 7: Required documentation

- [ ] **T-60** Complete the Space Requirement Table.
- [ ] **T-61** Complete the Adjacency Diagram.
- [ ] **T-62** Complete the Site Analysis.
- [ ] **T-63** Complete the Preliminary Building Specifications.
- [ ] **T-64** Complete the Specification Schedule.
- [ ] **T-65** Complete the Code Compliance Checklist.
- [ ] **T-66** Write the Design Rationale.

### Phase 8: Final review and presentation

- [ ] **T-70** Check that all drawings listed in the assignment are included.
- [ ] **T-71** Check that all required calculations are included.
- [ ] **T-72** Check that all required documentation is included.
- [ ] **T-73** Check that each sheet has the required identification and drawing information.
- [ ] **T-74** Check dimensions, labels, legends, symbols, and north arrows where applicable.
- [ ] **T-75** Set the drawing scales as appropriate for each drawing and follow the instructor's direction.
- [ ] **T-76** Prepare A3 drawing sheets.
- [ ] **T-77** Prepare calculations on long bond paper.
- [ ] **T-78** Inspect the sheets and calculations before printing the plate.
- [ ] **T-79** Keep the SVG preview files updated after meaningful drawing revisions and confirm that each preview reflects the current drawing data.
- [ ] **T-80** Inspect the SVG previews in GitHub/browser view and compare them against the drawing requirements, calculated dimensions, and related plans.
- [ ] **T-81** Export compatible DXF files for CAD editing and PDF sheets for review/printing; verify that the exported geometry and labels agree with the SVG previews.
- [ ] **T-82** Add a README.md preview section that embeds the committed SVG preview files once usable previews exist, and link the relevant drawing/export files.
- [ ] **T-83** Keep CSV files for supporting coordinate data, calculation values, area summaries, and schedules where tabular data is useful; check their units and values against the calculations and drawings.

---

## 6. Drawing requirements checklist

### A-01 – Site Development Plan

Show:
- [ ] Property boundaries
- [ ] Lot dimensions
- [ ] Bearings and distances
- [ ] North arrow
- [ ] Road
- [ ] Adjacent properties
- [ ] Required setbacks
- [ ] Building footprint
- [ ] Garage / carport
- [ ] Driveway
- [ ] Walkways
- [ ] Open spaces
- [ ] Landscaping, where applicable
- [ ] Other relevant site features

### A-02 – Ground Floor Plan

Show:
- [ ] Room names
- [ ] Dimensions
- [ ] Walls
- [ ] Doors
- [ ] Windows
- [ ] Stairs
- [ ] Furniture
- [ ] Space-planning fixtures
- [ ] Circulation
- [ ] Structural reference / grid lines, where appropriate

### A-03 – Second Floor Plan

Show:
- [ ] Room names
- [ ] Dimensions
- [ ] Walls
- [ ] Doors
- [ ] Windows
- [ ] Stairs
- [ ] Furniture
- [ ] Space-planning fixtures
- [ ] Circulation
- [ ] Structural reference / grid lines, where appropriate

### A-04 – Roof Plan

Show:
- [ ] Roof configuration
- [ ] Roof slopes
- [ ] Ridge lines
- [ ] Valleys
- [ ] Eaves
- [ ] Roof materials
- [ ] Roof framing concept
- [ ] Other architectural roof features

### A-05 – Elevations

Provide:
- [ ] Front elevation
- [ ] Rear elevation
- [ ] Left-side elevation
- [ ] Right-side elevation

Show:
- [ ] Building height
- [ ] Floor levels
- [ ] Roof form
- [ ] Doors
- [ ] Windows
- [ ] Exterior finishes
- [ ] Architectural features
- [ ] Ground line

### A-06 – Building Sections

Provide at least two sections, with at least one through the stairway.

Show:
- [ ] Ground line
- [ ] Floor levels
- [ ] Floor-to-floor heights
- [ ] Ceiling heights
- [ ] Roof
- [ ] Stair configuration
- [ ] Major building components
- [ ] Building heights

### A-07 – Architectural Details and Schedules

Provide:
- [ ] Door schedule
- [ ] Window schedule
- [ ] Room / finish schedule
- [ ] Stair detail
- [ ] Typical wall section
- [ ] Other necessary architectural details

---

## 7. Preliminary building specifications checklist

### A. General Requirements
- [ ] Quality of materials
- [ ] Workmanship
- [ ] Compliance with codes and standards

### B. Sitework
- [ ] Site clearing
- [ ] Earthwork
- [ ] Excavation
- [ ] Backfilling

### C. Concrete and Masonry
- [ ] Concrete
- [ ] Reinforcing steel
- [ ] Formwork
- [ ] Concrete hollow blocks / masonry
- [ ] Mortar
- [ ] Plastering

### D. Roofing
- [ ] Roof covering
- [ ] Roof framing
- [ ] Flashing
- [ ] Insulation, where applicable

### E. Doors and Windows
- [ ] Door materials
- [ ] Door frames
- [ ] Window materials
- [ ] Window frames
- [ ] Glazing
- [ ] Hardware
- [ ] Door and window dimensions

### F. Finishes
- [ ] Floor finishes
- [ ] Wall finishes
- [ ] Ceiling finishes
- [ ] Painting

### G. Stair and Railings
- [ ] Stair finish
- [ ] Handrails
- [ ] Guardrails

---

## 8. Required submission register

Keep all items below in the checklist because they appear in the assignment's required-submission section.

### A. Drawings
- [ ] Site Development Plan
- [ ] Ground Floor Plan
- [ ] Second Floor Plan
- [ ] Roof Plan / Roof Framing Plan
- [ ] Four Elevations
- [ ] Minimum Two Building Sections
- [ ] Architectural Details
- [ ] Door Schedule
- [ ] Window Schedule
- [ ] Column, Footing, Beam Details and Schedule
- [ ] Foundation Plan
- [ ] 2nd Floor Framing Plan
- [ ] Room / Finish Schedule

### B. Calculations
- [ ] Lot Area
- [ ] Lot Dimensions
- [ ] Traverse Closure
- [ ] Setbacks
- [ ] Buildable Area
- [ ] Building Footprint
- [ ] Floor Areas
- [ ] Open Space
- [ ] Occupant Load
- [ ] Stair Calculations
- [ ] Parking Requirement
- [ ] Other Applicable Calculations

### C. Documentation
- [ ] Space Requirement Table
- [ ] Adjacency Diagram
- [ ] Site Analysis
- [ ] Preliminary Building Specifications
- [ ] Specification Schedule
- [ ] Code Compliance Checklist
- [ ] Design Rationale

---

## 9. Presentation requirements

- [ ] Use **A3 paper** for the drawing sheets.
- [ ] Use **long bond paper** for calculations.
- [ ] Use manual drafting or CAD, as permitted by the assignment.
- [ ] Use an appropriate drawing scale based on the drawing and the instructor's direction.
- [ ] Prepare the required printed plate.

Each sheet must contain:
- [ ] University / school name
- [ ] Course / subject
- [ ] Plate number
- [ ] Plate title
- [ ] Student name
- [ ] Section
- [ ] Instructor
- [ ] Date
- [ ] Drawing title
- [ ] Scale
- [ ] North arrow, where applicable
- [ ] Dimensions
- [ ] Legends and symbols, where necessary

---

## 10. Calculation and drawing accuracy checks

Use these checks throughout the activity. They are review steps for the required work, not additional plate deliverables.

### A. Calculation checking

- [ ] Copy given values carefully from the assignment and keep their units.
- [ ] Label each calculation and separate **Given Data**, **Formula**, **Substitution**, **Working**, **Final Answer**, and **Check / Status**.
- [ ] Show the formula before substituting values.
- [ ] Recheck arithmetic independently before recording a final answer.
- [ ] Check angle conversion, quadrant/sign conventions, units, and rounding where relevant.
- [ ] Keep intermediate values at sufficient precision; round the reported result clearly and consistently.
- [ ] Compare related results. For example, the total floor area must equal the ground-floor area plus the second-floor area, and the stair rise must agree with the stated floor-level difference.
- [ ] Do not silently change a stated bearing, distance, dimension, or other value to make results agree. Mark discrepancies for checking against the assignment or instructor's direction.
- [ ] Mark a calculation **PENDING** when the needed dimensions or requirements have not yet been established.

Detailed working is kept in [calculations/plate2_calculations.md](calculations/plate2_calculations.md).

### B. Drawing checking

- [ ] Check that courses 1-2 through 4-5 use the stated bearings and distances unchanged, and that the closed academic plot uses the documented adjusted P5-1 only. Keep the original P5-1 value as source-reference data; do not label it as the adjusted boundary course or present the adjusted plot as a cadastral certification.
- [ ] Check dimensions, room names, door/window locations, furniture, stairs, circulation, and reference/grid lines against the corresponding drawing requirements.
- [ ] Compare the ground-floor plan, second-floor plan, roof plan, four elevations, and sections so that related dimensions and features agree.
- [ ] Check that the stair shown in the plans is consistent with the stair calculation and at least one section passes through the stairway.
- [ ] Check that roof form, floor levels, building heights, openings, and exterior finishes are consistent among the roof plan, elevations, sections, and specifications.
- [ ] Check that door/window schedules and room/finish schedules correspond to what is shown on the drawings.
- [ ] Check all dimensions, scale labels, north arrows where applicable, and legends/symbols where necessary.
- [ ] Inspect the final printed/exported sheets at the required A3 size, and inspect calculation pages on long bond paper for legibility and missing/cropped content.

### C. Final completion checklist

Before considering the activity ready for submission, verify that:

- [ ] Every required drawing in Section 8A is present.
- [ ] Every required calculation in Section 8B is present.
- [ ] Every required document in Section 8C is present.
- [ ] The required spaces appear in the ground and second floors.
- [ ] The site plan includes the site information listed for A-01.
- [ ] The roof plan, four elevations, sections, details, and schedules contain the items listed in the assignment.
- [ ] The preliminary specifications cover the listed categories.
- [ ] The calculations include the items specified in the brief and have been checked.
- [ ] Related drawings, calculations, schedules, and specifications agree with one another.
- [ ] Each sheet meets the presentation requirements.
- [ ] The drawing scales follow the instructor's direction.
- [ ] The submission is printed on the required paper sizes.

## 11. Note on unresolved instructions in the brief

The project description says detailed utility systems are excluded from this plate and describes the preliminary building plan as the base for succeeding structural and utility systems. However, the required-submission list includes structural drawings: column, footing, and beam details/schedules, a foundation plan, and a second-floor framing plan.

This plan keeps those structural items in the required-submission checklist because they are listed in the document. Follow the instructor's direction on their expected scope for Plate No. 2.


---

## 12. Agreed digital drawing and preview workflow

This section records the workflow agreed during project planning. It is intended to make inspection and revision easier; it does not change the instructor's required deliverables or override the assignment.

### 12.1 Working approach

- **ChatGPT + code** will be used to help prepare repeatable calculations, drawing geometry, dimensions, schedules, and exports. All calculated values and drawing outputs must still be checked against the assignment and applicable requirements.
- **SVG** will be a project output from the beginning, not an afterthought. It will act as a quick visual preview for checking the 2D drawings inside GitHub or a browser.
- **DXF** will be the generated, editable CAD master in compatible CAD software. Its geometry must come from the project's source data and generation code rather than from a separately hand-redrawn image.
- **DWG** will be a converted delivery copy when required. The conversion must be checked in compatible CAD software; corrections should normally be made in the source data/generator and regenerated, not only in the converted copy.
- **PDF** will be used for review, sheet arrangement, and printing/submission after dimensions, scales, labels, and page setup have been checked.
- **CSV** will store supporting tabular data where useful, such as lot coordinates, calculation results, area summaries, and schedules. CSV is supporting data, not the final architectural drawing format.
- **WalkMyPlan** will be used as a supplementary 3D visualization/inspection tool to review room arrangement, circulation, stairs, and the general spatial layout. It is a preview aid, not the source of truth for surveyed lot geometry, dimensions, code compliance, structural adequacy, or final 2D documentation.

### 12.2 Repository organization and implementation status

The initial scaffolding has been committed to the current main branch. The generator and both validation scripts now run successfully in GitHub Actions. A DXF and corresponding SVG are generated, validated, and uploaded as a 14-day workflow artifact. Generated outputs are not automatically committed to the branch; manual CAD-app review is still required before they are treated as accepted drawing deliverables.

```text
plate_2_bsd/
├── README.md                              [exists: project overview and current preview]
├── .gitignore                             [exists]
├── plate2 plan.md                         [exists]
├── calculations/
│   └── plate2_calculations.md             [exists]
├── site/                                  [exists: Phase 1 source files and outputs]
│   ├── README.md
│   ├── phase1_site_analysis.md
│   ├── phase1_site_analysis_matrix.csv
│   ├── phase1_site_base.svg
│   └── phase1_traverse_coordinates.csv
├── data/
│   └── README.md                          [exists; model/schedules deferred]
├── scripts/
│   ├── generate_site_base.py               [exists; generated outputs in CI]
│   ├── validate_site_base.py               [exists; passes in CI]
│   ├── validate_generated_dxf.py           [exists; DXF/SVG checks pass in CI]
│   └── requirements.txt                    [exists]
├── previews/
│   └── README.md                           [exists; generated SVG is a CI artifact]
├── drawings/
│   └── README.md                           [exists; generated DXF is a CI artifact]
├── exports/
│   ├── pdf/README.md                       [exists]
│   └── dwg/README.md                       [exists]
└── .github/
    └── workflows/
        └── validate-drawings.yml           [exists; successful end-to-end run]
```

**Deferred intentionally:** data/building_model.json and data/schedules.csv will be added when real layout geometry and schedule values exist. The existing site-coordinate CSV remains the Phase 1 source record; it is not duplicated in data/. The successful pipeline generates drawings/phase1_site_base.dxf and previews/phase1_site_base_preview.svg on the GitHub runner and uploads them as an artifact that expires after 14 days. These generated files are not committed to the repository automatically. Open the DXF in compatible CAD software for manual visual review before treating it as accepted.

### 12.3 GitHub SVG preview requirements

- [ ] Store committed preview files in `previews/`.
- [ ] Generate each preview from the current drawing data; avoid separately hand-editing the SVG in a way that makes it disagree with the DXF.
- [ ] Use descriptive titles, drawing names, dimensions, scale notes, and units when appropriate.
- [ ] Keep lines, labels, and dimensions readable when viewed on a phone as well as on a desktop.
- [ ] Use a clear visual hierarchy for property lines, walls, openings, dimensions, annotations, and furniture where applicable.
- [ ] Add or update a `README.md` section that embeds the available SVG previews using repository-relative image paths, for example:

```markdown
## Drawing Previews

### Ground Floor Plan
![Ground Floor Plan Preview](previews/ground-floor-plan.svg)
```

- [ ] Verify the SVG actually renders in GitHub; do not assume a file is viewable only because it was committed successfully.
- [ ] Treat the SVG as an inspection preview. Do not use on-screen appearance alone to certify dimensions or print scale.

### 12.4 Revision and inspection loop

1. **Read and confirm inputs.** Use the assignment's stated lot bearings, distances, requirements, and verified calculations. Record any discrepancy instead of silently altering source data.
2. **Calculate and structure.** Maintain named variables/data for coordinates, dimensions, room geometry, levels, openings, and schedules where practical.
3. **Generate previews and exports.** Produce SVG previews from the current drawing data. Generate corresponding DXF files from the same or consistently coordinated geometry where practical, and create CSV tables for supporting numeric data.
4. **Inspect the previews.** Review the SVGs in GitHub/browser view for missing or overlapping labels, incorrect layout, unclear dimensions, incomplete views, and cross-drawing inconsistencies.
5. **Inspect the spatial layout in 3D.** Recreate or inspect the arrangement in WalkMyPlan as a supplementary check. Record any layout concerns and revise the underlying drawing data, rather than treating a 3D image as the authoritative plan.
6. **Revise and regenerate.** Correct the source data or generation code, then regenerate affected SVG/DXF/CSV outputs. Recheck all drawings affected by the change.
7. **Prepare final sheets.** Arrange and export PDF sheets, confirm drawing scale and page size, inspect PDF output, and print using the assignment's A3 drawing-sheet and long-bond calculation-paper requirements.

### 12.5 What each format can and cannot prove

| Format/tool | Intended use | Important limitation |
|---|---|---|
| SVG | Quick 2D visual inspection inside GitHub/browser | Screen rendering does not prove real-world dimensions, CAD compatibility, or print scale |
| DXF | Editable 2D drawing geometry in compatible CAD software | Must be opened/checked in the intended CAD application and coordinated with the calculations |
| PDF | Review and print sheets | Must be checked for page size, scaling, missing/cropped content, and legibility |
| CSV | Supporting coordinates, numeric calculations, summaries, and schedules | Does not replace a dimensioned drawing sheet |
| WalkMyPlan | Supplementary 3D layout and circulation inspection | Does not replace checked 2D drawings, verified calculations, or instructor/code review |
| Source calculations and verified drawing data | Basis for dimensions and coordinated drawing outputs | Must be traceable to the assignment and checked; generated output is not automatically correct |

### 12.6 Consistency checks before an output is treated as ready

- [ ] SVG dimensions and labels match the verified drawing data.
- [ ] The corresponding DXF has been opened or otherwise validated in compatible CAD software.
- [ ] CSV units, signs, coordinates, and numerical values match the documented calculations.
- [ ] Related plans, elevations, sections, schedules, and details agree after revisions.
- [ ] The PDF uses the intended page size and print scale and has no clipped or unreadable content.
- [ ] Any unresolved course/instructor requirement is marked as pending rather than assumed resolved.
- [ ] Previews are labelled as preliminary until the checks above and the instructor's requirements are satisfied.


---

## 13. Repository implementation roadmap (before house-layout drafting)

This section turns the agreed digital workflow into an ordered implementation plan. The current site-base files are preserved. Initial repository scaffolding, generation scripts, validation scripts, dependency documentation, and the read-only GitHub Actions workflow are committed. The automated pipeline has now succeeded end-to-end: it generated the DXF and SVG, validated both against the existing Phase 1 source data, and uploaded the outputs as a 14-day artifact. Manual inspection of the DXF in a compatible CAD application remains pending.

### Stage R-1: Finalize the project plan

- [x] **R-01** Record the deliverables, source-of-truth rules, repository structure, generation workflow, and validation gates in this plan.
- [x] **R-02** Record the adjusted P5-1 course transparently and treat 300.00 m² as the assignment's approximate lot-area figure. Keep the 265.26 m² adjusted-polygon result documented; do not force the plotted area to equal the approximate figure.
- [x] **R-03** Cross-check this plan against the provided assignment. The required drawings, calculations, documentation, paper sizes, and scope exclusions remain represented; items whose expected detail is ambiguous are still flagged for instructor direction.

### Stage R-2: Add repository scaffolding

- [x] **R-10** Add a root README.md explaining the project, current phase, deliverables, drawing-generation workflow, limitations, and links to the current site files.
- [x] **R-11** Add scripts/ for deterministic drawing generation and validation code.
- [x] **R-12** Add drawings/ for editable DXF masters; the initial DXF is now generated and validated in CI as an artifact, but is not yet committed to the repository.
- [x] **R-13** Add previews/ for project-wide SVG previews. Preserve site/phase1_site_base.svg; the generated preview is validated in CI and available in the workflow artifact, not yet committed as a repository file.
- [x] **R-14** Add exports/pdf/ and exports/dwg/ with folder documentation for reviewed deliverables. Final exports are not yet present.
- [ ] **R-15** Define a machine-readable source format for the future building layout in data/building_model.json only when room geometry, levels, openings, and design parameters are ready to be recorded. Do not duplicate the Phase 1 coordinate CSV without a clear need.
- [x] **R-16a** Add Python dependency documentation and an initial read-only .github/workflows/validate-drawings.yml workflow.
- [x] **R-16b** Confirm that GitHub Actions validation succeeds. Successful runs are available in the [workflow history](https://github.com/justryan-n2d/plate_2_bsd/actions/workflows/validate-drawings.yml); the end-to-end run generates, validates, and uploads the DXF/SVG artifact.

### Stage R-3: Generate the first editable CAD file from Phase 1

- [x] **R-20** Implement scripts/generate_site_base.py to read site/phase1_traverse_coordinates.csv and build the closed lot from courses 1-2 through 4-5 plus the adjusted P5-1 row. The generator has run successfully in GitHub Actions.
- [x] **R-21** Ensure the original P5-1 and the diagnostic closure-gap row remain reference data only; the generator selects only the four stated courses and adjusted P5-1 for the boundary.
- [x] **R-22** Generate drawings/phase1_site_base.dxf with metre units, named layers, source-coordinate geometry, labels, and a closed parcel outline. The validated output is uploaded as a workflow artifact, not auto-committed.
- [x] **R-23a** Generate the SVG preview from the same source coordinates and validate its XML, polygon coordinates, vertex count, and required notes. The generated preview is included in the workflow artifact.
- [x] **R-23b** Visually inspect the rendered SVG preview. The parcel outline, vertex labels, course list, notes, north arrow, and graphic scale are visible and legible at preview size.
- [ ] **R-23c** Open the DXF in compatible CAD software and visually verify model-space units, layers, linework, text placement, extents, and plot behavior. SVG preview review does not replace this CAD-app check.
- [x] **R-24** Include notes for original and adjusted P5-1, approximate and calculated area, and the instructor-specified road cross-section: 5.00 m carriageway plus 1.50 m RROW strip on each side, 8.00 m total.
- [ ] **R-25** Keep the generated CAD output marked preliminary until the DXF has been opened and visually checked in compatible CAD software. The SVG preview has been visually reviewed, but that does not certify the DXF or drawing scale.

### Stage R-4: Validate the DXF/SVG generation pipeline

- [x] **R-30** Independently recompute the first four course components and confirm that adjusted P5-1 closes to P1 within a defined numerical tolerance.
- [x] **R-31** Check the five boundary vertices, course lengths, perimeter (64.145414 m), calculated closed-polygon area (265.2598 m²), and all source vertex coordinates against the CSV.
- [x] **R-32** Check DXF structural audit, metre units, required layers/entities, a single closed parcel polyline, and no extra entities on the property-boundary layer.
- [x] **R-33** Check that DXF vertex and course labels match source point names, bearings, and distances; check that key reference notes are present.
- [x] **R-34a** Visually review the rendered SVG preview for legibility, the plotted outline, labels, and notes; no obvious clipping or overlap was seen at the preview size.
- [ ] **R-34b** Open the DXF in compatible CAD software/viewer. Compare visible boundary linework, course labels, layers, units, extents, and plot behavior against the CSV and calculation notes.
- [x] **R-35** Add reproducible validation commands/scripts and verify successful runs in GitHub Actions. Passing automated checks do not certify a cadastral survey, code compliance, structural adequacy, or instructor approval.

### Stage R-5: GitHub automation and previews

- [x] **R-40a** Configure GitHub Actions to install the dependency, validate the source traverse, generate the DXF/SVG, validate both outputs, and upload them as an artifact.
- [x] **R-41** Keep CI read-only: generate and validate outputs without permission to commit to main or overwrite reviewed drawings.
- [x] **R-40b** Resolve the initial unsuccessful runs by rerunning the job, then verify successful end-to-end runs. The latest successful run includes stronger geometry and label checks.
- [ ] **R-42** Commit reviewed generated SVG previews and DXF outputs only after manual CAD-app inspection. Until then, keep generated outputs as expiring workflow artifacts.
- [x] **R-43** Add the root README with the existing site SVG embedded, links to source records, and directions for downloading the latest generated outputs from Actions.
- [x] **R-44** Add failure-reporting checks and upload successful DXF/SVG outputs as a 14-day workflow artifact. No automatic commits or large persistent build outputs are created.

### Stage R-6: Reuse the verified pipeline for the building plate

- [ ] **R-50** Define one shared building-geometry model for room outlines, walls, doors, windows, floor levels, stairs, roof geometry, and drawing annotations. Use it to generate related views where practical.
- [ ] **R-51** Plan and generate the site-development plan only after setbacks, buildable envelope, road/ROW assumptions, and site-access constraints have been worked through.
- [ ] **R-52** Generate ground-floor, second-floor, and roof-plan DXF/SVG drawings from the agreed geometry.
- [ ] **R-53** Coordinate elevations, building sections, stair dimensions, architectural details, and schedules with the same agreed dimensions and levels. Any view that requires separate geometry must still use documented common parameters.
- [ ] **R-54** Generate checked A3 PDF sheets and long-bond calculation pages in line with the assignment. Check the plot scale, sheet layout, dimensions, labels, and clipped content.
- [ ] **R-55** Convert final checked DXF files to DWG using a compatible converter. Inspect the resulting DWG; do not assume conversion preserves every annotation, dimension style, layer, or plot setting perfectly.

### 13.1 Source of truth and file ownership

- The instructor's assignment is the source of required deliverables and stated inputs.
- calculations/plate2_calculations.md records calculation methods, values, and their status.
- site/phase1_traverse_coordinates.csv is the machine-readable course/coordinate record for the current site base, including separate original and adjusted closing-course records.
- The drawing-generation code and its declared input files define generated SVG/DXF geometry. Generated output must be reproducible from those inputs.
- The closed academic plot uses the adjusted P5-1 course. The original assignment course is retained as source-reference information and must not be silently substituted or erased.
- A converted DWG is a delivery copy, not the independent source of truth. When a correction is needed, update the source data or generator, regenerate the DXF/SVG, validate them, and then reconvert.
- No drawing, calculation, or code-derived result should be described as professionally certified, permit-ready, or construction-ready merely because it passes automated checks.

### 13.2 Implementation acceptance gates

Do not advance to the next gate until its checks are met:

1. **Plan gate:** folder structure, source-of-truth rules, file ownership, and task order are recorded in this plan.
2. **Site CAD gate:** DXF is generated from the existing CSV and automated validation passes. Manual inspection in compatible CAD software is still required before this gate is complete.
3. **Site-requirements gate:** applicable setbacks and the buildable envelope are calculated and their assumptions are documented.
4. **Building-layout gate:** the room program, space-requirement table, and adjacency diagram are agreed before the detailed floor-plan geometry is treated as a design.
5. **Coordinated-drawing gate:** floor plans, roof plan, elevations, sections, details, and schedules agree on dimensions and levels.
6. **Submission gate:** checked PDF sheets, supporting calculations and documentation, and final DWG delivery copies are reviewed against the instructor's list.

The calculated area of the adjusted polygon is retained as 265.26 m². The 300.00 m² value remains the approximate lot area stated in the assignment. The project records both without forcing one to equal the other.
