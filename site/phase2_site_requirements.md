# Phase 2 Site Requirements: Setback and Buildable-Envelope Screening

**Project:** CE 393 Plate No. 2, Lot 245-B, Barangay San Isidro, Palo, Leyte  
**Status:** Screening study only. The final setback decision and code calculations remain pending.

## 1. Purpose

Phase 2 must establish setbacks, the allowable buildable envelope, building footprint, floor areas, open space, occupant load, parking and other applicable dimensions. The repository currently has the academic closed traverse, but it does **not** have the approved survey plan, exact road right-of-way geometry or a confirmed Palo zoning classification for this parcel.

This note compares alternatives so the project does not silently treat the earlier uniform 2.00 m inset as the final setback.

## 2. Source information currently in the project

- Lot 245-B, Barangay San Isidro, Municipality of Palo, Province of Leyte.
- The assignment calls the lot area approximately **300.00 m²**.
- The closed academic traverse after the instructed P5-1 adjustment calculates to **265.2598 m²** (265.26 m²).
- Original five-course linear misclosure is **4.011967 m** before the instructed adjustment.
- The assignment describes a **5.0 m existing barangay road** along the southeast and southwest sides and separately states an **8.00 m road right-of-way**.
- In the course sequence, the road edges are provisionally interpreted as P2-P3 and P3-P4. Confirm this with the official survey plan.
- The planning model currently uses a **9.30 m × 7.90 m (73.47 m²) house rectangle** and a **2.80 m × 5.50 m (15.40 m²) carport rectangle** at one assumed location.

The road width and right-of-way are different measurements. Do not infer that the road pavement edge equals the legal ROW boundary or allocate the remaining 3.0 m without source evidence.

## 3. Code references and what they do / do not settle

### PD 1096, Section 708(a)

The Supreme Court E-Library reproduction of the National Building Code states that Group A dwellings are subject to a general minimum distance of 2 metres from the property line, subject to the provisions on easement of light and view, and limits building occupancy of inside and corner lots. This is the source basis for retaining the **uniform 2.00 m inset as a baseline screening case**, not a signed-off parcel setback.

Reference: [Supreme Court E-Library, Presidential Decree No. 1096, Section 708](https://elibrary.judiciary.gov.ph/thebookshelf/showdocs/26/53320).

### 2004 Revised IRR, Table VIII.2 (R-1 table-style comparison)

The published 2004 Revised IRR text includes an R-1 table with a 4.50 m front yard and 2.00 m side/rear yards, with a note that the listed Table VIII.2 setback requirements are for **newly-developed subdivisions**. The table is useful as a comparison, but its applicability to this particular lot is not established in the documents available to this project.

Reference copy: [2004 Revised IRR text hosted by IIBH](https://www.iibh.org/kijun/pdf/Philippines_02_IRR_of_NBC_of_the_Philippines.pdf). Confirm the adopted rules, amendments and local interpretation with the Palo Office of the Building Official / Municipal Planning and Development Office.

### Local ordinance and road-frontage classification

The parcel's zoning designation, development/subdivision status, which road-facing edge is legally considered the front yard, any dual-frontage requirement, the surveyed ROW line, easements, fire-separation conditions and any stricter local yard requirements have **not** been verified. Do not decide these by looking at the polygon alone.

## 4. Four screening scenarios

The areas below are computed from the documented adjusted academic traverse, by shifting each boundary line inward by its listed perpendicular distance and intersecting adjacent offset lines. They are the areas inside those **illustrative offset polygons**, not legal buildable-area certifications.

| ID | Scenario | P1-P2 | P2-P3 | P3-P4 | P4-P5 | P5-P1 | Screened envelope area |
|---|---|---:|---:|---:|---:|---:|---:|
| S-01 | Uniform 2.00 m screen | 2.00 | 2.00 | 2.00 | 2.00 | 2.00 | 152.4309 m² |
| S-02 | P2-P3 assumed front at 4.50 m | 2.00 | 4.50 | 2.00 | 2.00 | 2.00 | 128.9837 m² |
| S-03 | P3-P4 assumed front at 4.50 m | 2.00 | 2.00 | 4.50 | 2.00 | 2.00 | 128.8989 m² |
| S-04 | Both road edges at 4.50 m | 2.00 | 4.50 | 4.50 | 2.00 | 2.00 | 112.6268 m² |

The recorded fit flags in [`phase2_setback_scenarios.csv`](phase2_setback_scenarios.csv) test whether the **current Phase 5 house and carport rectangles at their current coordinates** are fully inside each offset polygon. A NO flag is not proof that no building can fit; it means the current rectangle must be moved, resized or redesigned before that scenario could be carried forward.

- S-01 fits the current house and carport rectangles at their present coordinates.
- S-02 fits the house rectangle, but the current carport position is outside the screened envelope.
- S-03 does not fit the current house rectangle at its present coordinates; the current carport also does not fit.
- S-04 does not fit either current rectangle at its present coordinates.

See [the setback-scenario preview](../previews/phase2_setback_scenarios.svg) for the four offset outlines and the current footprint overlays.

## 5. What can be recorded now

| Item | Current numerical result | Status |
|---|---:|---|
| Adjusted academic lot area | 265.2598 m² | Calculated from instructed closed traverse; survey verification still required |
| Assignment stated approximate area | 300.00 m² | Given approximate value |
| Uniform 2.00 m offset area | 152.4309 m² | Screening scenario only |
| Scenario envelope range | 112.6268-152.4309 m² | Depends on unconfirmed road-frontage/setback assumption |
| Current main-house rectangle | 9.30 × 7.90 = 73.47 m² | Concept placement, not a confirmed compliant footprint |
| Carport placeholder | 2.80 × 5.50 = 15.40 m² | One-car concept only; final parking rules/access pending |
| Combined house + carport covered area | 88.87 m² | Arithmetic only |
| Combined covered area ÷ adjusted lot area | about 33.5% | Arithmetic only, not the complete legal lot-occupancy/open-space check |
| Assignment occupants | 5-6 persons | Given intended household size, not the calculated code occupant load |

The general Group A dwelling lot-occupancy rule in PD 1096 Section 708(a) differs for inside vs corner lots, but the project's corner-lot / dual-frontage classification is not confirmed. Do not use the ratios above as a compliance finding.

## 6. Items that remain pending for Phase 2

1. Obtain / check the actual survey plan and resolve the 300.00 m² approximate area vs 265.26 m² computed academic traverse area.
2. Confirm the legal boundary of the 8.00 m ROW and the alignment/extent of both road edges.
3. Ask the Palo Office of the Building Official / Municipal Planning and Development Office to confirm the zoning classification, applicable residential type, yard classification for each boundary, adopted IRR / local rules, easements and any stricter setback.
4. Select the applicable scenario only after items 1-3 are verified. Revise A-01, building location and carport placement to fit it.
5. Calculate the final buildable envelope from confirmed offset lines and verify the chosen house/carport geometry is contained within it.
6. Measure the final exterior building footprint and ground-/second-floor areas from coordinated plans. The room programme totals and 15% wall allowance in Phase 3 are budgeting aids, not official floor-area outputs.
7. Compute the official open-space / lot-occupancy result using the adopted method and confirmed parcel category.
8. Confirm the parking requirement and required stall dimensions from the applicable official rule and local ordinance.
9. Identify the correct occupant-load method/factor, show the source, calculation and rounding.
10. Review applicable light, ventilation, sanitation, entrance/exit, fire-safety and accessibility rules for the revised plan.

## 7. Decision gate

**Phase 2 remains open.** The scenario calculation and geometry comparison are completed as preliminary research, but T-10 through T-19 must not be marked fully complete until official setbacks / ROW / classification and the dependent calculations are confirmed. For now, keep the Phase 5 preview drawings explicitly preliminary and revise them when those decisions are available.
