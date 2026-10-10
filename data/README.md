# Shared design data

This folder is reserved for machine-readable data introduced as the building design is defined.

## Planned data

- building_model.json: current preliminary source for Phase 5 site placement, nominal footprint, room rectangles, floor/roof assumptions, draft openings and drawing status. These values remain provisional.
- stair_design.json: preliminary Phase 4 stair calculation data. Its 3.00 m floor-to-floor rise is explicitly marked as an assumption and must be replaced if the accepted building levels differ.
- schedules.csv: future schedule data after the door, window, room/finish, and specification schedules have actual entries.

`building_model.json` is a draft rather than a final approved building layout. The Phase 5 drawings must be revised together when Phase 2 setbacks, access and floor-level assumptions are confirmed. Do not duplicate the Phase 1 traverse data here: `site/phase1_traverse_coordinates.csv` remains the source record for the current site base.

## Rules

- State units explicitly.
- Keep assignment-given values separate from calculated and design-selected values.
- Record the source and status of assumptions and pending values.
- Keep the Phase 5 SVG previews synchronized with this source as the model is revised. The automatic model-to-SVG generator and editable DXF export are still not complete.
