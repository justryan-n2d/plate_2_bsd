# Plate 2 - Reference Layout Revision 01

**Date:** 2026-10-12  
**Repository:** [justryan-n2d/plate_2_bsd](https://github.com/justryan-n2d/plate_2_bsd)  
**Status:** Preliminary visual layout adopted as the direction for the next design pass

## Design basis

The two furnished floor-plan images supplied by the student replace the earlier simple room-box previews as the visual direction for A-02 and A-03. The updated SVG previews are editable vector drawings with room fills, basic furniture, fixtures, door swings, windows and stair symbols.

## Changes in A-02 - First floor

- Keep the guest room at the upper-left, with toilet and bath below and the garage at the lower-left.
- Keep dining and kitchen in the upper part of the main house.
- Keep storage beside the stairway.
- Keep the living room at the lower-right, with the entrance/foyer along the lower middle.
- Place the TV console inside the living room, on the room side of the foyer. It must not overlap the foyer or the designated entrance-clearance rectangle.

## Changes in A-03 - Second floor

- Show Bedroom 2, the robe, master bedroom, Bedroom 3, bathroom, toilet, toilet-and-bath, gym, karaoke room, stairway, family area and balcony.
- The karaoke room must have **exactly one door**. This revision places that single door on its west wall, opening from the circulation hall.
- Keep the gym and balcony as visible parts of the reference layout.

## Automated guardrails

`scripts/validate_architectural_previews.py` checks that:

1. The shared reference model contains one TV console assigned to the living room.
2. The TV console lies inside the modeled living-room bounds and does not overlap the foyer or entrance-clearance bounds.
3. The second-floor reference model contains exactly one karaoke-room doorway.
4. A-02 contains one living-room TV console marker and A-03 contains exactly one SVG element marked as the karaoke-room doorway.
5. The existing numeric model checks and XML/SVG preview checks still pass.

These checks confirm the declared diagram layout and SVG markers only. They are not full architectural or building-code checks.

## Important limitations and next tasks

The reference images do not include readable room dimensions, a reliable scale, wall thicknesses, a verified building outline, or coordinated structural-grid information. The new layouts therefore use SVG diagram units only. Do not use them to measure construction dimensions.

The previous numerical room-size targets remain in the model as provisional data until they are reconciled with the revised design. The new floor plans also have not yet been coordinated with the lot buildable envelope or with the other sheets.

- [ ] Confirm official lot survey, road right-of-way and applicable zoning/setbacks.
- [ ] Dimension the revised floor plans and reconcile all room areas with the required space schedule.
- [ ] Confirm the stair opening, landing, headroom and floor-to-floor levels across A-02, A-03 and A-06.
- [ ] Coordinate balcony placement, guardrail, elevations, sections and roof projection.
- [ ] Reconcile the building footprint/carport with A-01 and the confirmed buildable envelope.
- [ ] Update A-04 through A-07 to match the accepted floor-plan geometry.
- [ ] Inspect all sheets visually in compatible CAD software before final export.
- [ ] Export editable CAD and print-review PDFs after dimensions and code checks are complete.

**Not for permit or construction use.** Site, structural, code and architectural coordination are still pending.


## Phase 3 Revision 02 coordination

Phase 3 has been reopened to reflect reference layout revision 01. See [revised space-planning notes](space_planning.md), [room schedule](space_requirement_table.csv), [adjacency matrix](adjacency_matrix.csv), [adjacency diagram](adjacency_diagram.svg), and the revised [ground](ground_floor_zoning.svg) and [second-floor](second_floor_zoning.svg) zoning diagrams. Dimensioned design and new area totals remain pending.
