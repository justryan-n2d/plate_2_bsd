# Plate No. 2 Calculations
## CE 393: Building System Design

**Project:** Proposed Two-Storey Residential Building  
**Repository:** `justryan-n2d/plate_2_bsd`  
**Source:** Instructor-provided *Plate No. 2 in CE 393: Building System Design*  
**Purpose:** Organized worksheet for every calculation required in the assignment.

> **Important:** This file follows the assignment instructions. Values stated in the brief are labelled as given data. Values calculated from the given bearings and distances are labelled preliminary. Items requiring dimensions, a plotted plan, or an applicable code requirement are marked **PENDING**. Do not invent missing values or silently change the assignment data.

---

## Calculation Index

| No. | Required calculation | Status |
|---|---|---|
| C-01 | Lot area | **PENDING verification** |
| C-02 | Lot dimensions / boundary lengths | Given boundary distances listed below; plot/check pending |
| C-03 | Traverse closure | **Calculated from the given values; closure gap shown without adjustment** |
| C-04 | Required setbacks | **PENDING** |
| C-05 | Buildable area | **PENDING** |
| C-06 | Building footprint | **PENDING** |
| C-07 | Floor areas | **PENDING** |
| C-08 | Remaining open space | **PENDING** |
| C-09 | Occupant load | **PENDING** |
| C-10 | Stair design | **PENDING** |
| C-11 | Parking requirement | **PENDING** |
| C-12 | Other applicable requirements | **PENDING as identified during design** |

### Status labels

- **GIVEN:** directly stated in the assignment.
- **CALCULATED:** arithmetic shown in this file using stated inputs.
- **PENDING:** cannot be completed from the assignment information currently recorded.
- **CHECK:** result needs to be checked against the source information or the completed drawing.

---

# C-01. Lot Area

## Given data

- Approximate lot area stated in the assignment: **300.00 m²**.
- Lot boundary bearings and distances are given in the technical description.
- Following the instructor's direction, only P5-1 is adjusted to close the traverse; courses 1-2 through 4-5 remain unchanged.

## Working: area from the adjusted closed traverse

Use the closed coordinates in the local east-north coordinate system:

| Point | Easting (m) | Northing (m) |
|---|---:|---:|
| P1 | 0.000000 | 0.000000 |
| P2 | 14.894856 | 3.030393 |
| P3 | 17.398552 | -8.500934 |
| P4 | 10.862083 | -14.317898 |
| P5 | -1.661019 | -15.707836 |
| P1 (closed) | 0.000000 | 0.000000 |

Use the coordinate / shoelace formula:

```text
Area = 1/2 × |Σ(EᵢNᵢ₊₁ - Eᵢ₊₁Nᵢ)|
```

Substitution using the unrounded coordinates from the course components:

```text
Area ≈ 265.2598 m²
```

**Calculated area from the adjusted closed traverse: 265.26 m²**

| Comparison | Area |
|---|---:|
| Approximate area stated in the assignment | 300.00 m² |
| Area calculated from the adjusted closed traverse | 265.26 m² |
| Difference (calculated minus stated approximate area) | -34.74 m² |

The calculated area is about **34.74 m² lower** than the stated approximate area. Keep both values visible; do not adjust other courses just to make the area equal to 300.00 m².

**Result/status:** Area calculated from the closed plot. It is based on the documented adjustment to P5-1, while 300.00 m² remains the approximate area stated in the assignment.

---

# C-02. Lot Dimensions / Boundary Lengths

## Given data from the technical description

| Boundary line | Bearing | Distance |
|---|---|---:|
| 1–2 | N 78° 30' E | 15.20 m |
| 2–3 | S 12° 15' E | 11.80 m |
| 3–4 | S 48° 20' W | 8.75 m |
| 4–5 | S 83° 40' W | 12.60 m |
| 5–1 | N 08° 10' W | 16.35 m |

## Working: original and adjusted perimeter

Original total using all five distances as written in the assignment:

```text
Original total = 15.20 + 11.80 + 8.75 + 12.60 + 16.35
               = 64.70 m
```

For the closed plot, keep the first four distances unchanged and use the calculated adjusted closing course P5-1:

```text
Adjusted perimeter = 15.20 + 11.80 + 8.75 + 12.60 + 15.795414
                   = 64.145414 m
                   ≈ 64.1454 m
```

| Item | Bearing | Distance |
|---|---|---:|
| Original P5-1 value from assignment | N 08°10′ W | 16.35 m |
| Adjusted closing course used in plot | N 06°02′11″ E | 15.7954 m (about 15.80 m) |

The original total of **64.70 m** is retained as the sum of the instructor's five stated distances. The perimeter of the adjusted closed plot is **64.1454 m**. The original P5-1 value remains recorded separately in the CSV.

---

# C-03. Traverse Closure

## Purpose

The assignment provides five boundary courses. The instructor directed that the traverse should be closed. For this plot, courses **1-2 through 4-5 are held unchanged** and only the final course **P5-1** is adjusted to return to P1.

The original P5-1 value is kept in the calculations and coordinate schedule so the adjustment is transparent.

## Formula and sign convention

For a course with distance (D) and bearing angle (\theta), measured from north or south:

```text
Latitude  = D × cos(θ)
Departure = D × sin(θ)
```

Use the bearing quadrant for the signs:

| Bearing quadrant | Latitude sign | Departure sign |
|---|---:|---:|
| N ... E | + | + |
| S ... E | - | + |
| S ... W | - | - |
| N ... W | + | - |

## Step 1: Calculate courses 1-2 through 4-5 without adjustment

| Line | Bearing | Distance (m) | Latitude (m) | Departure (m) |
|---|---|---:|---:|---:|
| 1-2 | N 78°30′ E | 15.20 | +3.030393 | +14.894856 |
| 2-3 | S 12°15′ E | 11.80 | -11.531327 | +2.503697 |
| 3-4 | S 48°20′ W | 8.75 | -5.816964 | -6.536469 |
| 4-5 | S 83°40′ W | 12.60 | -1.389938 | -12.523102 |
| **Sum of first four courses** | | **48.35** | **-15.707836** | **-1.661019** |

## Step 2: Check the original P5-1 as written in the assignment

Original value: **N 08°10′ W, 16.35 m**.

```text
Latitude  = +16.184195 m
Departure = -2.322568 m

Original traverse latitude sum  = -15.707836 + 16.184195
                                = +0.476359 m

Original traverse departure sum = -1.661019 - 2.322568
                                = -3.983587 m

Original linear misclosure = √[(0.476359)² + (-3.983587)²]
                           ≈ 4.011967 m
                           ≈ 4.0120 m
```

The original five-course data does not close. The following adjustment changes only the last course in order to close the plotted traverse, as instructed.

## Step 3: Calculate the adjusted P5-1 closing course

To close the traverse, P5-1 must cancel the sums from the first four courses:

```text
Required latitude  = -(-15.707836) = +15.707836 m
Required departure = -(-1.661019)  = +1.661019 m
```

Calculate the closing distance:

```text
Distance = √[(15.707836)² + (1.661019)²]
         ≈ 15.795414 m
         ≈ 15.80 m
```

Calculate the bearing angle from north:

```text
θ = tan⁻¹(|departure| / |latitude|)
  = tan⁻¹(1.661019 / 15.707836)
  ≈ 6.036287°
  ≈ 6°02′11″
```

Both components are positive, so the closing bearing is in the northeast quadrant.

**Adjusted P5-1 for the closed plot: N 06°02′11″ E, 15.7954 m (about 15.80 m).**

## Step 4: Check the adjusted closed traverse

Using the adjusted closing course:

```text
Sum of latitudes    ≈ 0.000000 m
Sum of departures   ≈ 0.000000 m
Linear misclosure   ≈ 0.000000 m
```

The adjustment is limited to P5-1. The source value **N 08°10′ W, 16.35 m** is preserved in this worksheet and the CSV as the original assignment data, while the adjusted value is used to close the plotted shape.

**Result/status:** The plotted traverse is closed using the adjusted P5-1 course as directed. The calculated closed-polygon area is recorded in C-01. This is a documented academic adjustment, not a claim that the original technical description itself closes.

---

### Phase 1 coordinate plot and source-data status

The preliminary graphic is in [site/phase1_site_base.svg](../site/phase1_site_base.svg), and the course coordinate schedule is in [site/phase1_traverse_coordinates.csv](../site/phase1_traverse_coordinates.csv). The related site notes are in [site/phase1_site_analysis.md](../site/phase1_site_analysis.md).

These outputs use a local coordinate frame with P1 = (0, 0). They are not georeferenced. The fifth course ends at P1*, approximately 4.0120 m from P1; the gap is shown as a closure diagnostic only, not as an added parcel boundary. The source bearings and distances remain unchanged. Keep C-01 lot-area verification pending because the stated 300.00 m² area is approximate and the courses do not close.

# C-04. Required Setbacks

## Assignment requirement

Determine applicable setbacks based on the relevant codes and regulations.

## Given data available

- Approximate lot area: 300.00 m².
- Road right-of-way in the project-information table: 8.00 m.
- The lot description states an existing 5.0 m barangay road width; the project information separately gives an 8.00 m right-of-way.

## Calculation worksheet

| Boundary / side | Applicable setback | Source / basis | Status |
|---|---:|---|---|
| North | PENDING | PENDING | Not determined |
| East | PENDING | PENDING | Not determined |
| Southeast road side | PENDING | Road boundary and applicable requirement need to be determined | Not determined |
| Southwest road side | PENDING | Road boundary and applicable requirement need to be determined | Not determined |
| West | PENDING | PENDING | Not determined |

Treat the 5.0 m road width and 8.00 m total right-of-way as separate measurements. The remaining 3.0 m may accommodate shoulders, drainage, or other road-related spaces depending on the road plan. Do not assume a particular split or allocation because the assignment does not specify one. Do not fill in setback distances until the applicable requirement and the boundary used for measurement have been identified.

**Result:** **PENDING**. Complete this section after the lot is plotted and the applicable requirements are determined.

---

# C-05. Buildable Area

## Assignment requirement

Determine the allowable building envelope.

## Required inputs

- Verified lot geometry from C-01 to C-03.
- Applicable setbacks from C-04.
- Setback lines plotted from the correct property/road boundaries.

## Working procedure

1. Plot the verified property boundary.
2. Draw the applicable setback lines.
3. Identify the area inside the lot and outside the required setback areas.
4. Measure or calculate the resulting buildable envelope.

| Item | Result |
|---|---:|
| Verified lot area | PENDING |
| Setbacks confirmed | PENDING |
| Buildable envelope area | **PENDING** |

**Result:** **PENDING** until the lot geometry and setbacks are confirmed.

---

# C-06. Building Footprint

## Assignment requirement

Determine the proposed ground-floor building footprint.

## Required inputs

- Buildable envelope from C-05.
- Proposed ground-floor layout.
- Dimensions of the outside building walls.

## Working

After the ground-floor plan is prepared, calculate its footprint from the dimensions of the proposed building outline. If the outline has multiple parts, show the separate area calculations and their sum.

```text
Building footprint = area enclosed by the proposed ground-floor
                     building outline
```

| Item | Result |
|---|---:|
| Proposed exterior building dimensions | PENDING |
| Proposed building footprint | **PENDING** |
| Check against buildable envelope | PENDING |

**Result:** **PENDING** until the building footprint is designed and dimensioned.

---

# C-07. Floor Areas

## Assignment requirement

Calculate the ground-floor area, second-floor area, and total floor area.

## Required inputs

- Dimensioned ground-floor plan.
- Dimensioned second-floor plan.
- Consistent area-measurement method for both floors.

## Working

Record the area of the proposed ground floor and second floor from the completed drawings. If the plan is divided into simpler shapes, label each part, show its formula, and add the partial areas.

```text
Ground-floor area = sum of the measured areas on the ground floor

Second-floor area = sum of the measured areas on the second floor

Total floor area   = Ground-floor area + Second-floor area
```

| Floor area | Result |
|---|---:|
| Ground floor | PENDING m² |
| Second floor | PENDING m² |
| **Total floor area** | **PENDING m²** |

**Result:** **PENDING** until both floor plans are dimensioned.

---

# C-08. Remaining Open Space

## Assignment requirement

Determine the remaining open space.

## Required inputs

- Lot area calculated from the verified lot geometry.
- Proposed building footprint.

## Working worksheet

```text
Remaining open space = lot area - area occupied by the building footprint
```

Substitution:

```text
Remaining open space = [verified lot area] - [building footprint]
                      = PENDING m²
```

| Item | Result |
|---|---:|
| Verified lot area | PENDING m² |
| Building footprint | PENDING m² |
| Remaining open space | **PENDING m²** |

**Result:** **PENDING**. Use the area values from C-01 and C-06 when they are completed.

---

# C-09. Occupant Load

## Assignment requirement

Determine the applicable occupant load.

## Given data

- Proposed occupants: **5–6 persons**.
- Occupancy group stated in the assignment: **A**.

The proposed number of occupants is not automatically the same as a code-calculated occupant load. Complete the calculation using the applicable requirement identified for this activity.

## Calculation worksheet

| Input / step | Value |
|---|---|
| Area used for the occupant-load calculation | PENDING |
| Applicable occupant-load factor or method | PENDING: determine from the applicable requirement |
| Formula / method | PENDING until the applicable method is identified |
| Calculated occupant load | **PENDING persons** |

Record the formula, units, substituted values, rounding method, and source of the applicable requirement once determined. Do not invent an occupant-load factor.

---

# C-10. Stair Design Calculations

## Assignment requirements

Determine:
- Stair width
- Number of risers
- Riser height
- Tread depth
- Landing dimensions
- Total stair height

## Required inputs

- Floor-to-floor height shown in the building design.
- Proposed stair arrangement.
- Applicable dimensions/requirements for the stair.

## Calculation worksheet

| Item | Symbol / method | Result |
|---|---|---|
| Total stair height | Difference between the two floor levels served | PENDING m |
| Number of risers | Determine from total rise and selected permitted riser height, then use a whole number | PENDING |
| Riser height | Total stair rise ÷ number of risers | PENDING m |
| Tread depth | Determine from the stair design and applicable requirement | PENDING m |
| Stair width | Determine from the stair design and applicable requirement | PENDING m |
| Landing dimensions | Determine from the stair layout and applicable requirement | PENDING m |
| Total stair height check | Confirm calculated rise matches the floor-level difference | PENDING |

## Working template

```text
Total stair rise             = [floor-to-floor height] = PENDING m
Selected number of risers    = PENDING
Calculated riser height      = total stair rise ÷ number of risers
                             = PENDING m
Tread depth                  = PENDING m
Stair width                  = PENDING m
Landing dimensions           = PENDING
```

**Result:** **PENDING** until the floor heights and stair design are established.

---

# C-11. Parking Requirement

## Assignment requirement

Determine the applicable parking requirement.

## Design elements named in the assignment

- Garage / carport on the ground floor.
- Driveway on the site development plan.

## Calculation worksheet

| Item | Result |
|---|---|
| Applicable parking requirement | PENDING |
| Required number of parking spaces | PENDING |
| Proposed garage / carport dimensions | PENDING |
| Proposed driveway arrangement | PENDING |
| Check against the site plan | PENDING |

Determine the applicable requirement using the relevant code/regulation identified for the activity. Do not assume a required number or dimension where the assignment does not provide it.

**Result:** **PENDING**.

---

# C-12. Other Applicable Requirements

The assignment also requires calculations for other applicable code-based dimensions and requirements.

For each additional calculation, use this labeled format:

### C-12.__ [Name of requirement]

**1. Requirement from assignment:**  
[Write the applicable item.]

**2. Given data:**  
- [Input and unit]
- [Input and unit]

**3. Formula / method:**  
```text
[Write the formula or method]
```

**4. Substitution and working:**  
```text
[Show the input values substituted into the formula]
```

**5. Result:**  
[Value and unit]

**6. Source / basis:**  
[Applicable code/regulation or instructor-provided direction]

**7. Status:**  
[Given / Calculated / Pending / Check]

---

## Final Calculation Review Checklist

- [ ] Lot area determined and checked.
- [ ] Lot dimensions/boundary lengths recorded.
- [ ] Traverse closure shown, including latitude and departure sums and linear misclosure.
- [ ] Any discrepancy in the source data checked before finalizing lot geometry.
- [ ] Required setbacks determined and their basis recorded.
- [ ] Buildable area calculated from the plotted setback envelope.
- [ ] Building footprint calculated from the proposed ground-floor plan.
- [ ] Ground-floor, second-floor, and total floor areas calculated.
- [ ] Remaining open space calculated.
- [ ] Occupant load determined using the applicable method.
- [ ] Stair width, risers, riser height, tread depth, landings, and total stair height determined.
- [ ] Parking requirement determined.
- [ ] Other applicable requirements calculated if identified.
- [ ] All calculations use clear labels, consistent units, shown formulas, substituted values, and final results.
- [ ] Calculation values agree with the final drawings.

**Current status:** C-02 perimeter and C-03 traverse-closure arithmetic have preliminary results. The lot-area verification and remaining calculations are pending the information and design work required by the assignment.
