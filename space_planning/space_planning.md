# Phase 3: Space Planning

**Project:** CE 393 Plate No. 2, Proposed Two-Storey Residential Building  
**Repository:** `justryan-n2d/plate_2_bsd`  
**Status:** Preliminary space programme and conceptual zoning; not a dimensioned architectural plan.

## 1. Deliverables

- [Space requirement table](space_requirement_table.csv): required spaces, provisional clear-dimension targets, area targets and relationship notes.
- [Adjacency matrix](adjacency_matrix.csv): a text register explaining direct, near, buffered and conditional relationships.
- [Adjacency diagram](adjacency_diagram.svg): visual relationship diagram for the two floors.
- [Ground-floor zoning](ground_floor_zoning.svg): conceptual groupings for social, service, guest and vertical-circulation spaces.
- [Second-floor zoning](second_floor_zoning.svg): conceptual groupings for bedrooms, family area, bath and upper circulation.
- [Space-planning validator](../scripts/validate_space_planning.py): checks schedule fields and arithmetic, required spaces, adjacency references and SVG structure.

## 2. Important limits

Phase 2 has an adopted academic calculation baseline: 265.26 m² working lot area, S-01 with 2.00 m setbacks, and preliminary footprint/floor-area/open-space/occupant/parking calculations. The final room layouts still need drawing coordination. Therefore:

- All listed room dimensions are **provisional clear-dimension targets for planning**, not code minimums, final dimensions or construction instructions.
- The diagrams are **not to scale** and do not set the building orientation, lot position, driveway, vehicle gate, pedestrian gate, doors, windows or setbacks.
- The carport is a single-car planning placeholder. It does not establish the legal or code-required parking count or size.
- The balcony is required by the student's design direction. Use a 3.00 m × 1.50 m external balcony on the east/front entry-carport facade, directly beside and accessed from the family area; align its plan, elevation, section, roof projection and D-04/guardrail note across A-01/A-03/A-04/A-05/A-06/A-07.
- The stair footprint is a space allowance only. Stair width, risers, tread, landings, headroom and total stair height remain for Phase 4.
- Building utilities, including detailed plumbing and sanitary systems, remain excluded. Keeping the two bathrooms near each other vertically is only an architectural coordination preference.
- Room-area targets are not official ground-floor, second-floor or total floor-area calculations. Wall thicknesses, final circulation, stair/void treatment and the buildable envelope must be resolved in later phases.

The assignment gives an approximate lot area of 300.00 m²; the closed academic traverse currently calculates 265.26 m² after the documented P5-1 adjustment. Neither value is used here to claim that a particular footprint or setback is compliant.

## 3. Space requirement schedule

The schedule records the spaces named in the assignment and adds a separate circulation allowance for the ground floor. Dimensions are written as length x width in metres. The target area for dimensioned rows is length multiplied by width.

| Floor | Space | Target clear size | Target area | Planning intent |
|---|---|---:|---:|---|
| Ground | Entrance / foyer | 1.50 x 1.50 m | 2.25 m² | Buffer entry from the private rooms |
| Ground | Living room | 3.60 x 3.80 m | 13.68 m² | Public/social zone |
| Ground | Dining area | 2.80 x 2.80 m | 7.84 m² | Directly related to living and kitchen |
| Ground | Kitchen | 2.50 x 2.80 m | 7.00 m² | Adjacent to dining and storage/service |
| Ground | Toilet and bath | 1.50 x 2.10 m | 3.15 m² | Near guest room |
| Ground | Bedroom / guest room | 3.00 x 3.00 m | 9.00 m² | Private ground-floor sleeping space |
| Ground | Stairway | 2.00 x 3.20 m | 6.40 m² | Preliminary U-shaped return stair envelope; see Phase 4 study |
| Ground | Storage / service area | 1.50 x 2.00 m | 3.00 m² | Near kitchen |
| Ground | Garage / carport | 2.80 x 5.50 m | 15.40 m² | Covered-open single-car placeholder |
| Ground | General circulation allowance | Area allowance only | 4.50 m² | Reserve for routes and clearances |
| Second | Master bedroom | 3.20 x 3.40 m | 10.88 m² | Quieter and more private zone |
| Second | Bedroom 2 | 2.80 x 3.00 m | 8.40 m² | Independent access from shared circulation |
| Second | Bedroom 3 | 2.80 x 3.00 m | 8.40 m² | Independent access from shared circulation |
| Second | Toilet and bath | 1.50 x 2.10 m | 3.15 m² | Close to bedrooms |
| Second | Family area | 2.80 x 3.00 m | 8.40 m² | Connected to upper landing |
| Second | Stair landing / circulation | 2.00 x 2.50 m | 5.00 m² | Routes to rooms without crossing bedrooms |
| Second | Balcony | 3.00 x 1.50 m | 4.50 m² | Required external balcony accessed from family area through D-04; area tracked separately from enclosed floor area |

These figures are starting targets, not prescribed minimums. Furniture clearances, door swings, windows, ventilation, wall thickness and actual family needs may require different dimensions.

## 4. Preliminary area-budget cross-check

These are only programme-budget calculations for comparing the requested rooms with the likely scale of the concept. They do **not** complete calculation items C-06 or C-07.

| Budget check | Calculation | Preliminary value |
|---|---|---:|
| Ground-floor enclosed room targets | Sum of dimensioned enclosed ground-floor rows, excluding circulation allowance | 52.32 m² |
| Ground-floor circulation allowance | Separate planning allowance | 4.50 m² |
| Ground-floor programme target before wall/structure allowance | 52.32 + 4.50 | 56.82 m² |
| Approximate enclosed ground-floor budget | 56.82 / 0.85 using a provisional 15% gross-area allowance for walls/structure | 66.85 m² |
| Covered-open carport placeholder | 2.80 x 5.50 | 15.40 m² |
| Approximate ground-level covered budget including carport | 66.85 + 15.40 | 82.25 m² |
| Second-floor indoor programme target | Sum of dimensioned enclosed second-floor rows | 44.23 m² |
| Approximate enclosed second-floor budget | 44.23 / 0.85 using the same provisional 15% allowance | 52.04 m² |
| Required balcony target | 3.00 x 1.50 | 4.50 m² |

The 15% allowance is a rough planning assumption, not a code factor. These totals cannot replace a measured layout and must not be copied as official floor-area, coverage, open-space or code-compliance results. The final stair/opening treatment also needs to be resolved in the architectural plan set.

## 5. Adjacency, zoning and circulation decisions

### Ground floor

1. Place the foyer at the public approach and use it as a buffer before private rooms. The final pedestrian approach and door location depend on verified site conditions and Phase 2 setbacks.
2. Keep the living and dining spaces connected. The kitchen should directly relate to dining, with storage/service next to the kitchen.
3. Put the guest room in a quieter zone. Keep the ground-floor bath nearby, but avoid a bedroom door opening directly into the living room if the later geometry allows a short buffer.
4. Make the stair easy to find from the entry or living zone. The stair dimensions and safe headroom/landing configuration are still pending Phase 4.
5. Keep the carport near the general entry route while planning a separate pedestrian path so people do not have to walk through the vehicle manoeuvring area. The exact driveway and vehicle crossing are not selected in this phase.

### Second floor

1. Group the master bedroom and the two other bedrooms in the private zone, with individual access from shared circulation.
2. Place the family area near the stair landing so it works as shared space without making bedroom access pass through it.
3. Keep the common upstairs bath close to the bedrooms. If practical, keep it near the ground-floor bath location to support later coordination, without designing utilities in this plate.
4. Keep the master bedroom buffered from the stair/family area where possible.
5. Provide the required balcony beside the family area. For this academic concept, locate it on the east/right front side of the family-area zone, 3.00 m along the facade with a 1.50 m outward projection; include D-04 from the family area and a schematic perimeter guardrail.

### Accessibility, safety and privacy

- Do not route circulation through a bedroom or require access to one room through another room.
- Protect bathroom and bedroom privacy from the primary social space.
- Keep the main route legible and avoid placing furniture or storage in the stair approach.
- The room schedule does not prove accessibility compliance. Clear widths, door clearances, thresholds, ramps and other applicable requirements must be checked against the final plan and applicable code.
- Reserve exterior-wall opportunities for daylight and natural ventilation when the actual windows and elevations are designed. No window or door position is fixed by these zoning diagrams.

## 6. Relationship codes

The adjacency matrix uses these planning labels:

- **direct:** place side by side or connect with a short direct path where practical.
- **near:** keep nearby with a short shared route; a door-to-door connection is not required.
- **buffered:** keep functionally accessible but avoid a direct opening or immediate exposure between the spaces.
- **conditional:** use only if site, privacy, safety and code checks permit it.

The diagram highlights the main relationships. Use the CSV matrix for the full recorded rationale. Not every listed relationship must become a shared wall; the later plan must preserve circulation and privacy.

## 7. Phase 3 review outcome and hold points

The table, matrix and diagrams cover the required spaces and establish a preliminary arrangement for both floors. The arrangement is reviewed at the **conceptual adjacency and circulation** level only.

Before preparing dimensioned floor plans, return to Phase 2 to establish setbacks and the allowable building envelope. Then revise the programme and check the footprint, floor areas, open space, parking and other code-based requirements. Phase 4 must calculate the stair and verify that it fits the space reserved here. After that, coordinate walls, doors, windows, furniture, room dimensions, openings and the structural reference/grid approach across the plans and sections.

**Status:** Phase 3 preliminary space-planning package prepared. Final layout approval and code compliance remain pending later calculation and drawing checks.
