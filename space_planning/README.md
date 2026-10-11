# Phase 3 Space Planning Files - Revision 02

This folder contains the revised concept-stage space programme for CE 393 Plate No. 2. Revision 02 aligns the room schedule, adjacency relationships and zoning diagrams with the furnished first- and second-floor reference selected for A-02/A-03.

## Files

- [`space_requirement_table.csv`](space_requirement_table.csv): assignment-required spaces plus additional spaces visible in the reference. Prior target sizes are kept as unverified inherited values; rooms without dimensions from the reference have blank size/area fields.
- [`adjacency_matrix.csv`](adjacency_matrix.csv): revised relationship labels and reasons for each floor and cross-floor coordination.
- [`adjacency_diagram.svg`](adjacency_diagram.svg): revised two-floor relationship view.
- [`ground_floor_zoning.svg`](ground_floor_zoning.svg): revised first-floor zoning; TV belongs in the living area and the foyer route stays clear.
- [`second_floor_zoning.svg`](second_floor_zoning.svg): revised second-floor zoning; includes robe, separate upstairs wet-room labels, gym, karaoke room, stairway and balcony, with exactly one karaoke-room door marker.
- [`space_planning.md`](space_planning.md): rationale, dimension-status policy, relationship decisions and open checks.
- [`reference_layout_revision.md`](reference_layout_revision.md): initial reference layout corrections and record.
- [`../scripts/validate_space_planning.py`](../scripts/validate_space_planning.py): programme, adjacency, diagram and layout guardrail checks.

## Important limits

The supplied images are a visual reference, not dimensioned drawings. Do not infer metres or room areas from SVG coordinates. The inherited dimension targets are not yet verified against this arrangement, the old area-budget totals are superseded, and no revised room/floor-area totals are claimed. Phase 2 site/setbacks and Phase 4 stair calculations remain dependencies. These files are not construction drawings or evidence of code compliance.

## Related Phase 4 stair study

- [Stair design calculations and code hold points](stair_design.md)
- [Stair plan preview](stair_plan.svg)
- [Stair section/development preview](stair_section.svg)
- [Structured stair values](../data/stair_design.json)
