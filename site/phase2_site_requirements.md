# Phase 2: Site Requirements and Preliminary Calculations
## CE 393 Building System Design, Plate No. 2

**Project type:** Student academic activity for a proposed two-storey Group A dwelling  
**Working branch:** `phase2-site-requirements`  
**Status:** Academic calculation baseline completed using the agreed assumptions below. These are preliminary design calculations for the plate, not a real construction or permit submission.

## 1. Agreed project basis

Use these values consistently throughout Phase 2 and when revising the Phase 5 drawings.

| Item | Adopted value / treatment |
|---|---|
| Working lot area | **265.26 m²** from the adjusted, closed Phase 1 traverse |
| Lot geometry | Use the adjusted academic traverse already documented in `site/phase1_traverse_coordinates.csv` |
| Occupancy | Group A, two-storey residential dwelling |
| Household/design occupants | 5–6 stated in the assignment; use **6 persons** for the academic design |
| Road carriageway | **5.00 m** wide |
| Total road right-of-way | **8.00 m**, inclusive of the 5.00 m carriageway |
| Remaining ROW outside the carriageway | 3.00 m in total; its exact allocation is not specified, so do not invent separate shoulder/drainage widths |
| Working setback assumption | **2.00 m inward from each of the five lot boundaries**, using PD 1096 Section 708(a) as the classroom baseline for a Group A dwelling |
| Main house rectangle | 9.30 m × 7.90 m |
| Covered carport | 2.80 m × 5.50 m, for one car |
| Floor-to-floor height | 3.000 m, matching the Phase 4 stair-study assumption |
| Floor-area method | Use 73.47 m² enclosed area per floor; report the required 4.50 m² balcony separately from enclosed floor area |
| Parking assumption | One off-street parking space, represented by the planned single-car carport |

The 265.26 m² value is the chosen working area for this academic exercise. The assignment also calls the lot area approximately 300.00 m²; retain that as a source note, but do not treat the difference as a blocker or keep changing the working area.

### Road / ROW interpretation

The **5.00 m road is inside the 8.00 m total ROW**. Show the 5.00 m carriageway and the overall 8.00 m ROW as different dimensions on the site drawing. The remaining 3.00 m belongs to the ROW outside the carriageway in total. The assignment does not state whether it is split evenly, so no specific allocation to shoulders, drains, or margins is assumed.

For this student drawing, keep the technical-description lot boundary as the reference line for the 2.00 m inward academic setback. Do not subtract the 5.00 m carriageway from the lot area or count the ROW as additional lot area.

## 2. Academic code basis and limitations

- **PD 1096, Section 708(a):** the National Building Code text gives a general minimum 2 m distance from the property line for Group A dwellings, subject to its other provisions. Use 2.00 m on all boundaries as the selected classroom assumption. Source: [Supreme Court E-Library, PD 1096](https://elibrary.judiciary.gov.ph/thebookshelf/showdocs/26/53320).
- Section 708(a) also gives different maximum site-occupancy percentages for inside and corner lots. Because the assignment does not formally label this irregular two-road-frontage lot, compare the proposal with the **more conservative 80% ceiling** as a screening check. The proposed coverage is below both the 80% and 90% ratios, so this check does not control the footprint.
- For parking, the assignment's planned single-car carport is adopted as the academic proposal. The dimensions 2.80 m × 5.50 m are used for this plate.
- Other assumptions are identified as such and must not be represented as a legal survey, a signed design, or approval for construction.

This activity does not require obtaining an actual survey certification, a parcel-specific zoning letter, a building permit, or contractor-ready design. Use the given assignment values, the documented academic traverse, the referenced code provisions, and clearly stated assumptions.

## 3. Selected setback scenario

**Selected academic scenario: S-01, uniform 2.00 m offset on all five boundaries.**

| Boundary | Adopted setback |
|---|---:|
| P1–P2 | 2.00 m |
| P2–P3 | 2.00 m |
| P3–P4 | 2.00 m |
| P4–P5 | 2.00 m |
| P5–P1 | 2.00 m |

The two road-facing boundaries are provisionally identified as P2–P3 and P3–P4 from the assignment's boundary description. S-02 through S-04 remain comparison cases only. They are not additional approval gates for this classroom exercise.

### Calculated offset-envelope area

The uniform-offset polygon already calculated from the adjusted traverse gives:

**Academic buildable-envelope area = 152.4309 m² ≈ 152.43 m²**

This is the area inside the assumed setback offsets. It is smaller than the 265.26 m² lot area because the setback strips remain outside the assumed building envelope.

## 4. Building footprint and lot coverage

### Main house

```text
House footprint = width × depth
                = 9.30 m × 7.90 m
                = 73.47 m²
```

### Carport

```text
Carport area = 2.80 m × 5.50 m
             = 15.40 m²
```

### Combined covered ground area

```text
Combined covered area = house + carport
                      = 73.47 + 15.40
                      = 88.87 m²
```

### Lot coverage

```text
Coverage = (combined covered area ÷ lot area) × 100
         = (88.87 ÷ 265.26) × 100
         ≈ 33.5%
```

Conservative 80% coverage comparison:

```text
80% × 265.26 m² = 212.208 m² ≈ 212.21 m²
Actual covered area = 88.87 m² < 212.21 m²
```

The 88.87 m² covered area is within the selected 152.43 m² offset envelope according to the Phase 2 geometry check; both the house and carport fit at their current academic positions in S-01. Maintain that containment when revising the site plan.

## 5. Floor areas

For this preliminary calculation, use the same 9.30 m × 7.90 m main-house outer envelope for both storeys. The carport is open-sided and is not included in enclosed house floor area.

| Item | Calculation | Adopted area |
|---|---|---:|
| Ground-floor enclosed house area | 9.30 × 7.90 | **73.47 m²** |
| Second-floor enclosed house area | 9.30 × 7.90, same-envelope assumption | **73.47 m²** |
| Required second-floor balcony | 3.00 × 1.50 | **4.50 m²** |
| Second-floor total including balcony | 73.47 + 4.50 | **77.97 m²** |
| Total enclosed house floor area | 73.47 + 73.47 | **146.94 m²** |
| Total floor area including balcony | 146.94 + 4.50 | **151.44 m²** |
| Separate open-sided carport | 2.80 × 5.50 | 15.40 m² covered site area, not included above |

These are gross outer-envelope planning figures. If the final A-03 drawing later shows a smaller second-floor outline or an actual open-to-below area, recalculate the second-floor and total areas from that geometry.

## 6. Remaining open space / uncovered lot area

For the academic lot-coverage calculation, count both the house and roofed carport as covered ground area.

```text
Uncovered lot area = lot area − combined covered ground area
                   = 265.26 − 88.87
                   = 176.39 m²

Uncovered percentage = (176.39 ÷ 265.26) × 100
                     ≈ 66.5%
```

**Academic result:** 176.39 m², or approximately 66.5%, remains uncovered by the house and carport. This arithmetic does not mean every uncovered square metre is a landscaped or permeable area; driveway and walkway finishes will be decided in the site plan.

## 7. Occupant load

The assignment specifies a proposed household of 5–6 persons. For this single-family Group A dwelling activity, adopt the maximum stated household size:

**Design occupant count = 6 persons.**

```text
Adopted academic design occupants = max(5, 6) = 6 persons
```

This uses the stated household size as the planning basis. It is not an assembly-occupancy factor calculation. If the instructor specifically requires an area-factor method, add the prescribed factor and its source rather than inventing one.

## 8. Stair calculation carried forward from Phase 4

The assignment/repository uses a provisional 3.000 m floor-to-floor rise.

| Item | Calculation / adopted value |
|---|---|
| Total rise | 3.000 m = 3000 mm |
| Number of risers | 18 total, two flights of 9 |
| Riser height | 3000 ÷ 18 = **166.7 mm** |
| Treads per flight | 9 − 1 = 8 physical treads |
| Tread depth | **280 mm** |
| Horizontal run per flight | 8 × 0.280 = **2.240 m** |
| Clear stair width | **0.900 m per flight** |
| Intermediate landing depth | **0.900 m** |
| Reserved stair envelope | **2.000 m × 3.200 m = 6.40 m²** |

Against the general Group A stair values in PD 1096 Section 708(h), the selected 900 mm width exceeds 750 mm, the 166.7 mm riser is below 200 mm, and the 280 mm tread exceeds the 200 mm minimum run. The final drawing must still coordinate headroom, doors, railings, and floor thicknesses.

## 9. Parking

For this classroom proposal, provide **one off-street car space** through the single-car carport.

```text
Proposed carport = 2.80 m × 5.50 m = 15.40 m²
Proposed spaces = 1 car
```

A commonly cited NBCP Rule XIX passenger-car slot dimension is 2.40 m × 5.00 m; the proposed 2.80 m × 5.50 m carport exceeds those nominal width and length values. For this plate, use one space to match the proposed single-family house/carport concept. This is an academic choice, not a parcel-specific local parking determination.

Reference for the general Group A requirements: [PD 1096, Supreme Court E-Library](https://elibrary.judiciary.gov.ph/thebookshelf/showdocs/26/53320). The instructor's class reference takes precedence if a different parking-table version or required dimension was assigned.

## 10. Other applicable preliminary checks

| Requirement | Academic treatment |
|---|---|
| Group A occupancy | Use the stated single-family residential dwelling classification |
| Entrance and exit | Show a distinct main entrance and a separate exit path/opening in the coordinated ground-floor plan, consistent with the cited Section 708(i) baseline |
| Light and ventilation | Place windows/openings in the plans and elevations; review room ventilation when A-02/A-03 are coordinated |
| Sanitation | Include at least one toilet and bath as required by the assignment and noted in Section 708(c); detailed plumbing design remains excluded from this plate |
| Lot occupancy | 33.5% combined house/carport coverage; below both the 80% and 90% Section 708(a) comparison ceilings |
| Road access | Label 5.00 m carriageway within 8.00 m total ROW; show the 3.00 m difference as unallocated ROW width unless the drawing brief supplies an allocation |
| Detailed utilities | Excluded from Plate No. 2 by the assignment; do not design plumbing, sanitary, electrical, mechanical, or fire-protection systems in this phase |

## 11. Scenario comparison

The existing CSV and SVG retain S-01 to S-04 so the design decision is visible. S-01 is the selected academic basis; the other cases are comparisons only.

| Scenario | Setback assumption | Offset-envelope area | Use |
|---|---|---:|---|
| S-01 | 2.00 m on all boundaries | 152.4309 m² | **Selected academic design basis** |
| S-02 | 4.50 m on P2–P3; 2.00 m elsewhere | 128.9837 m² | Comparison only |
| S-03 | 4.50 m on P3–P4; 2.00 m elsewhere | 128.8989 m² | Comparison only |
| S-04 | 4.50 m on both road edges; 2.00 m elsewhere | 112.6268 m² | Comparison only |

## 12. Phase 2 completion checklist

- [x] T-10 / C-04: Adopt the 2.00 m setback assumption for the academic design.
- [x] T-11 / C-05: Calculate the selected 152.43 m² setback envelope.
- [x] T-12 / C-06: Record the 73.47 m² house footprint and 15.40 m² carport.
- [x] T-13 / C-07: Calculate the ground-floor area as 73.47 m² under the stated envelope assumption.
- [x] T-14 / C-07: Calculate the second-floor area as 73.47 m² under the same-envelope assumption.
- [x] T-15 / C-07: Calculate total enclosed house floor area as 146.94 m²; report 4.50 m² balcony separately for 151.44 m² total including balcony.
- [x] T-16 / C-08: Calculate uncovered lot area as 176.39 m² (66.5%).
- [x] T-17 / C-09: Adopt 6 persons as the academic design occupant count from the assignment's 5–6 person range.
- [x] T-18 / C-11: Adopt one car space in the 2.80 m × 5.50 m carport.
- [x] T-19 / C-12: Record the applicable preliminary Group A occupancy, entrance/exit, light/ventilation, and sanitation checks.
- [x] Carry Phase 4 stair calculations forward using the 3.000 m rise assumption.

**Phase 2 academic calculation baseline: complete using the agreed assumptions.** The required 3.00 m × 1.50 m balcony contributes 4.50 m² of external floor area and is reported separately from the enclosed area. Coordinate it into A-03 and show it in the relevant elevation before final plate issue. The remaining action is to coordinate these adopted values into A-01 to A-03 and the final plate sheets. This checklist does not claim real-site survey, permit, or construction approval.
