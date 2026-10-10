# Phase 5 Architectural Draft - Design Notes

**Status:** Preliminary draft package only. See [Project Status](../PROJECT_STATUS.md) for the project-wide phase record.

## Drawing register

| Sheet | Preview | Current content |
|---|---|---|
| A-01 | [Site Development Plan](../previews/phase5_A01_site_development.svg) | Adjusted local lot polygon, 2.00 m inward screening line, concept house/carport placement, preliminary area budget and unresolved site constraints. |
| A-02 | [Ground Floor Plan](../previews/phase5_A02_ground_floor.svg) | Required ground-floor room targets, circulation band, schematic furniture and placeholder opening marks. |
| A-03 | [Second Floor Plan](../previews/phase5_A03_second_floor.svg) | Three bedrooms, shared bath, family area, stair opening and landing/circulation. |
| A-04 | [Roof Plan](../previews/phase5_A04_roof_plan.svg) | Gable roof, ridge, assumed pitch, eaves and conceptual slope arrows. |
| A-05 | [Four Elevations](../previews/phase5_A05_elevations.svg) | Front/rear/left/right schematic elevations with assumed storey and roof levels. |
| A-06 | [Building Sections](../previews/phase5_A06_sections.svg) | Stair vertical-development section study and general building section diagram. |
| A-07 | [Details and Schedules](../previews/phase5_A07_details_schedules.svg) | Typical wall/floor section concept, stair data, provisional door/window schedule and finish schedule. |

## Basis carried forward from Phases 1-4

- The Phase 1 adjusted traverse area is 265.2598 m² (rounded 265.26 m²). The assignment also states an approximate 300.00 m² area. Both values remain documented.
- Phase 3 room targets are in `space_planning/space_requirement_table.csv`.
- Phase 4 stair values are in `data/stair_design.json`: 18 risers at approximately 166.7 mm, 280 mm treads, 900 mm clear width per flight, 900 mm landing depth, and a 2.00 m x 3.20 m nominal stair zone.
- The building concept uses a 9.30 m x 7.90 m rectangular main footprint and a 2.80 m x 5.50 m single-car carport placeholder.

## Why A-01 is a screening study, not a final Site Development Plan

PD 1096 Section 708(a) states a general location / distance rule for Group A dwellings and discusses maximum lot occupancy for corner and inside lots. That does not settle all local conditions for this particular parcel. The current drawing applies a 2.00 m inward offset to the academic traverse as an initial screening polygon only.

The assignment describes an existing 5.0 m barangay road and separately states an 8.00 m right-of-way. Exact road edges, ROW lines, the classification of each road-side yard, local zoning, special setbacks and the approved survey plan are not verified. A local zoning ordinance or applicable IRR provision may require a larger yard. The current line must not be labelled or used as the final approved buildable envelope.

Reference: [Supreme Court E-Library - PD 1096](https://elibrary.judiciary.gov.ph/thebookshelf/showdocs/26/53320).

## Provisional geometry and arithmetic

| Item | Current draft value | Status |
|---|---:|---|
| Adjusted academic lot area | 265.26 m² | Preliminary; not cadastral certification |
| Area inside the uniform 2.00 m screening line | 152.43 m² | Geometric screening result only |
| House footprint | 9.30 x 7.90 = 73.47 m² | Concept rectangle |
| Carport placeholder | 2.80 x 5.50 = 15.40 m² | Position and code dimensions unconfirmed |
| Combined covered ground budget | 88.87 m² | Arithmetic only |
| Indicative combined coverage versus 265.26 m² | 33.5% | Arithmetic only; not a code certification |
| Lot area less house and carport areas | 176.39 m² | Arithmetic remainder only, not the final code open-space result |

## Floor plans and room coordination

The ground and second-floor room boxes are based on Phase 3 target sizes and are arranged inside the nominal 9.30 m x 7.90 m outline. In the drawings, boxes and opening markers are conceptual. Wall thickness, wall-centreline geometry, door swings, exact window positions, clear passage dimensions after finishes, furniture clearances, stairwell openings and structural grids require a proper coordinated design pass.

The second-floor plan places the stair opening/flight zone over the ground-floor stair zone and adds the Phase 4 landing allowance. This relationship is a starting arrangement only. Confirm exact landing geometry, stair direction, floor opening and headroom against the accepted vertical section.

## Levels, roof and elevations

The drawings reuse the Phase 4 assumption of a 3.000 m ground-to-second-floor rise. Eaves at +6.000 m, ridge at approximately +7.690 m and roof pitch of 20 degrees are new design assumptions. They need to be reconciled with the required ceiling heights, roof construction, elevations and stair headroom in the final sheets.

The draft opening schedule uses nominal placeholders: main entrance 0.90 x 2.10 m, bedroom door 0.80 x 2.10 m, bath door 0.70 x 2.10 m, typical window 1.20 x 1.20 m, living window 1.50 x 1.20 m, and bath window 0.60 x 0.60 m. These are not code-approved dimensions; final sizes and opening free areas must be checked against the selected room uses and applicable code.

## Shared model and validation limits

`data/building_model.json` now records site coordinates, the screening polygon, footprint placement, room boxes, level/roof assumptions, opening schedule and drawing status. `scripts/validate_architectural_previews.py` checks numerical consistency, containment within the screening polygon, area arithmetic, and basic SVG structure.

**Still incomplete:** the SVG geometry is not yet regenerated by a single committed drawing generator and the architecture has not yet been exported as an editable DXF/DWG set. The validator is a consistency check, not a full CAD geometry or design-code checker. After Phase 2 is resolved, update the shared model and regenerate/revise the drawings together.

## Explicit remaining checks

- Confirm official survey and road ROW geometry, and check the 265.26 m² vs approximate 300.00 m² discrepancy with the correct survey source.
- Confirm Palo zoning / residential type and the actual applicable setbacks, open space and lot occupancy rules.
- Recalculate buildable envelope and confirm proposed footprint/carport fit.
- Complete final occupant-load and parking calculations.
- Confirm floor levels and BP 344 applicability; redesign the stair if required.
- Coordinate doors/windows, ventilation, natural lighting, privacy, furniture clearances, structural reference lines and the roof drainage approach.
- Complete structural design only as required and directed by the assignment; the current typical wall section has no structural member sizing or reinforcement.
- Review all sheets visually, then export editable CAD and final A3/PDF sheets after dimensions are frozen.
