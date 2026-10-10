# Phase 2 Site Requirements and Preliminary Calculations

**Project:** Proposed Two-Storey Residential Building, CE 393 Plate No. 2  
**Status:** Preliminary code review and calculation workflow. This is not a permit determination or a surveyed site-development plan.

## 1. Verified geometry inputs

| Item | Result | Status |
|---|---:|---|
| Approximate area stated in the assignment | 300.00 m² | GIVEN (approximate) |
| Area of adjusted, closed Phase 1 polygon | 265.26 m² | CALCULATED from Phase 1 coordinate schedule |
| Difference (assignment approximate minus calculated polygon) | 34.74 m² | RECORDED, not reconciled by changing the traverse |
| Adjusted closed-polygon perimeter | 64.1454 m | CALCULATED |

The adjusted traverse remains an academic plotting basis under the instructor's direction. The first four courses are unchanged, and only P5-1 is adjusted. The approximate 300.00 m² brief value is preserved separately; it is not used to overwrite the calculated 265.26 m² polygon area.

## 2. Setback review by boundary

PD 1096 Section 708(a) states that Group A dwellings shall be at least 2.00 m from the property line, subject to the Civil Code provisions on easements of light and view, and shall occupy not more than 90% of a corner lot or 80% of an inside lot. Section 704(a) also states that the center line of an adjoining street or alley is considered an adjacent property line. The project therefore cannot place road-frontage setback lines accurately until the street-centerline / right-of-way relationship is confirmed.

| Boundary | Adjoining feature | Code baseline | Geometry offset used? | Status / reason |
|---|---|---:|---:|---|
| 1-2 | Lot 245-A | 2.00 m | 2.00 m | provisional baseline: Use only as the statutory starting point; confirm Palo zoning and any larger requirement. |
| 2-3 | Lot 246 | 2.00 m | 2.00 m | provisional baseline: Use only as the statutory starting point; confirm Palo zoning and any larger requirement. |
| 3-4 | Existing barangay road on southeast | 2.00 m | NO | geometry pending: The adjoining street centerline is treated as an adjacent property line; its exact relation to this polygon and the 8.00 m RROW is not established. |
| 4-5 | Existing barangay road on southwest | 2.00 m | NO | geometry pending: The adjoining street centerline is treated as an adjacent property line; its exact relation to this polygon and the 8.00 m RROW is not established. |
| 5-1 adjusted to close | Lot 244 | 2.00 m | 2.00 m | provisional baseline: Use only as the statutory starting point; confirm Palo zoning and any larger requirement. |

**Important distinction:** the 2.00 m statutory baseline is not confirmation that every final yard is exactly 2.00 m. The local zoning ordinance, zoning classification, actual road centerline / RROW, and any more restrictive applicable rules must be checked with the Municipality of Palo's competent offices. NBCP Table VIII.2's R-1 residential-yard values (front 4.50 m, side and rear 2.00 m) are specifically noted as applying to newly developed subdivisions in the table note, so they are not silently applied as the final rule here.

## 3. Lot occupancy and minimum open-space scenarios

For a transparent preliminary comparison, Section 708(a)'s caps are calculated using the **265.26 m² adjusted-polygon area**, not the approximate area from the brief. The site has two stated adjoining road-frontage edges, so the corner-lot scenario is shown first, but final lot classification and local restrictions must be confirmed.

| Classification scenario | Maximum occupancy factor | Maximum occupied area | Corresponding minimum open area |
|---|---:|---:|---:|
| Corner lot (provisional) | 90% | 238.73 m² | 26.53 m² |
| Inside lot (comparison only) | 80% | 212.21 m² | 53.05 m² |

These are code-ceiling scenarios, not the calculated buildable envelope and not the proposed footprint. Actual setbacks, local zoning, light-and-ventilation requirements, and other applicable limitations can require a smaller building and more open space.

## 4. Buildable-envelope calculation

**NOT CALCULATED.** A final inset polygon is intentionally not generated because one or more roadway geometry offsets are missing. This avoids treating the boundary line as the road centerline or inventing an allocation of the stated 5.00 m road width and 8.00 m RROW.

Envelope status: Incomplete: missing geometry offsets for boundary edge(s) 3, 4.

The geometry engine and tests are in place. Once the survey / site reference identifies the applicable road-centerline or RROW lines and the Municipality's setbacks are verified, populate the geometry-offset inputs and regenerate this report.

## 5. Other preliminary requirements

| Item | Current finding | Status |
|---|---|---|
| Parking | 1 off-street/on-site slot indicated as a preliminary minimum | PRELIMINARY; verify at local OBO |
| Occupant load | Assignment gives 5–6 proposed occupants; code occupant load still requires the applicable floor area / method and occupancy classification | PENDING |
| Building footprint | Must be selected after setback envelope and preliminary room arrangement are coordinated | PENDING |
| Ground-floor area | Requires the dimensioned ground-floor plan | PENDING |
| Second-floor area | Requires the dimensioned second-floor plan | PENDING |
| Total floor area | Ground-floor area + second-floor area | PENDING |
| Remaining open space after footprint | Adjusted lot area minus the final footprint; distinct from minimum open-space scenario above | PENDING |
| Stair / other dimensions | Requires floor-to-floor height, building layout, and applicable code checks | PENDING |

## 6. Code and reference basis

1. [Presidential Decree No. 1096, National Building Code of the Philippines, Section 704(a) and Section 708(a)](https://elibrary.judiciary.gov.ph/thebookshelf/showdocs/11/53320). Section 708(a) supplies the Group A dwelling baseline distance and corner-/inside-lot occupancy ceilings; Section 704(a) supplies the street-centerline rule.
2. [DPWH National Building Code Development Office documents](https://dpwh.architectureboard.com.ph/documents/), including the 2004 Revised Implementing Rules and Regulations of PD 1096. Verify Table VII.4 parking requirements against the current official text and local Building Official interpretation before finalizing the design.
3. [DPWH Department Order No. 056, s. 2016 (official PDF)](https://www.dpwh.gov.ph/dpwh/sites/default/files/issuances/DO_056_s2016.pdf), Annex provision containing Table VIII.2; its note limits the listed residential setback table to newly developed subdivisions.
4. [Civil Code of the Philippines, Article 670 and related easement provisions](https://elibrary.judiciary.gov.ph/thebookshelf/showdocs/2/53360).

## 7. Inputs still required before finalizing Phase 2

- Municipal zoning classification and applicable Palo zoning ordinance requirements for this parcel.
- A reliable road-centerline / RROW line for both road-frontage boundaries and confirmation of the measured road/ROW relationship.
- Confirmation whether the Municipality applies a specific corner-lot classification and any additional yard / site-occupancy rules.
- Applicable parking table and exact parking-space dimensions confirmed for the adopted use classification.
- Later, a coordinated preliminary floor plan and floor-to-floor height to calculate footprint, floor areas, occupant load, stair geometry, and residual open space.

**Limit:** This academic worksheet is not a site survey, legal zoning determination, permit-ready design, or certification of code compliance. Do not use the provisional numbers to build.
