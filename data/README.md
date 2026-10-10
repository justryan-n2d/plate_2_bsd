# Shared design data

This folder is reserved for machine-readable data introduced as the building design is defined.

## Planned data

- building_model.json: future single source for agreed room outlines, walls, openings, floor levels, stairs, roof parameters, and drawing annotations.
- schedules.csv: future schedule data after the door, window, room/finish, and specification schedules have actual entries.

These files are intentionally not created yet. A blank model would imply that the building layout has already been defined. Do not duplicate the Phase 1 traverse data here: site/phase1_traverse_coordinates.csv remains the source record for the current site base.

## Rules

- State units explicitly.
- Keep assignment-given values separate from calculated and design-selected values.
- Record the source and status of assumptions and pending values.
- Generate drawing geometry from data rather than maintaining conflicting copies.
