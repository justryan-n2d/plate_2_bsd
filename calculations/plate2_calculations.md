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
| C-03 | Traverse closure | **Preliminary result calculated; requires checking against source data** |
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
- The assignment also provides five boundary bearings and distances.

## Required work

The assignment asks us to determine and verify the lot area from the technical description.

## Working

A verified area should be calculated from the plotted and checked lot geometry. The traverse-closure check in **C-03** indicates that the listed courses do not currently return to their starting point. Therefore, a final area based on those courses should not yet be reported as verified.

| Item | Value |
|---|---:|
| Approximate area stated in brief | 300.00 m² |
| Area calculated from a verified, closed traverse | **PENDING** |
| Difference from the stated approximate area | **PENDING until area is calculated** |

**Result/status:** The only area currently available is the assignment's stated approximate area of **300.00 m²**. Verification is pending until the traverse data is checked.

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

## Working: Total boundary length / perimeter

```text
Perimeter = sum of all five boundary distances

          = 15.20 + 11.80 + 8.75 + 12.60 + 16.35
          = 64.70 m
```

**Calculated total boundary length:** **64.70 m**

The five listed distances are the boundary-course lengths provided in the assignment. Verify them against the source description before treating the plotted lot dimensions as final.

---

# C-03. Traverse Closure

## Purpose

The assignment requires checking the closure of the plotted traverse.

## Formula and sign convention

For a boundary course with distance (D) and bearing angle (	heta), measured from the north or south direction:

```text
Latitude increment  = D × cos(θ)
Departure increment = D × sin(θ)
```

Apply signs from the bearing quadrant:

| Bearing quadrant | Latitude sign | Departure sign |
|---|---:|---:|
| N ... E | + | + |
| S ... E | - | + |
| S ... W | - | - |
| N ... W | + | - |

These signs are used to calculate the north-south and east-west components of each course.

## Step 1: Calculate each latitude and departure

The values below are calculated from the bearings and distances supplied in the assignment. Values are rounded to four decimal places.

| Line | Bearing | Distance (m) | Latitude calculation/result (m) | Departure calculation/result (m) |
|---|---|---:|---:|---:|
| 1–2 | N 78° 30' E | 15.20 | (+15.20cos78.5^circ = +3.0304) | (+15.20sin78.5^circ = +14.8949) |
| 2–3 | S 12° 15' E | 11.80 | (-11.80cos12.25^circ = -11.5313) | (+11.80sin12.25^circ = +2.5037) |
| 3–4 | S 48° 20' W | 8.75 | (-8.75cos48.3333^circ = -5.8170) | (-8.75sin48.3333^circ = -6.5365) |
| 4–5 | S 83° 40' W | 12.60 | (-12.60cos83.6667^circ = -1.3899) | (-12.60sin83.6667^circ = -12.5231) |
| 5–1 | N 08° 10' W | 16.35 | (+16.35cos8.1667^circ = +16.1842) | (-16.35sin8.1667^circ = -2.3226) |
| **Sum** | | **64.70** | **+0.4764 m** | **−3.9836 m** |

## Step 2: Find the latitude and departure misclosures

```text
Sum of latitudes    = +0.4764 m
Sum of departures   = -3.9836 m
```

For a closed traverse, both sums should be zero, subject to the accuracy and rounding of the source measurements.

## Step 3: Calculate linear misclosure

Formula:

```text
Linear misclosure = √[(sum of latitudes)² + (sum of departures)²]
```

Substitution:

```text
Linear misclosure = √[(0.4764)² + (-3.9836)²]
                  ≈ 4.0120 m
```

**Preliminary linear misclosure:** **approximately 4.0120 m**

## Step 4: Calculate the preliminary relative closure

Using the sum of the listed boundary distances:

```text
Perimeter = 64.70 m

Relative closure denominator = Perimeter ÷ Linear misclosure
                             = 64.70 ÷ 4.0120
                             ≈ 16.13

Approximate closure ratio = 1 : 16.13
```

## Result and action required

**CHECK REQUIRED:** The supplied bearings and distances produce a preliminary linear misclosure of approximately **4.0120 m**. This is not a zero closure and should be checked against the original assignment values.

- [ ] Recheck all bearings, distances, quadrant signs, and arithmetic against the assignment.
- [ ] Ask the instructor for clarification or corrected data if the values are confirmed to be inconsistent.
- [ ] Do not silently alter a bearing or distance to force closure.
- [ ] Recalculate the coordinates and lot area after the source data is clarified.

This result is a mathematical check of the numbers transcribed above, not an assertion about what the intended survey data should have been.

---

### Phase 1 coordinate plot and source-data status

The preliminary graphic is in [site/phase1_site_base.svg](../site/phase1_site_base.svg), and the course coordinate schedule is in [site/phase1_traverse_coordinates.csv](../site/phase1_traverse_coordinates.csv). The related site notes are in [site/phase1_site_analysis.md](../site/phase1_site_analysis.md).

These outputs use a local coordinate frame with P1 = (0, 0). They are not georeferenced. The fifth course ends at P1*, approximately 4.0120 m from P1; the gap must not be treated as a parcel boundary or silently adjusted. Keep C-01 lot-area verification pending until the source courses are checked. The stated 300.00 m² remains an approximate area from the assignment, not an area verified from the open traverse.

# C-04. Required Setbacks

## Assignment requirement

Determine applicable setbacks based on the relevant codes and regulations.

## Given data available

- Approximate lot area: 300.00 m².
- Road right-of-way in the project-information table: 8.00 m.
- The lot description also refers to an existing 5.0 m barangay road.

## Calculation worksheet

| Boundary / side | Applicable setback | Source / basis | Status |
|---|---:|---|---|
| North | PENDING | PENDING | Not determined |
| East | PENDING | PENDING | Not determined |
| Southeast road side | PENDING | Road boundary and applicable requirement need to be determined | Not determined |
| Southwest road side | PENDING | Road boundary and applicable requirement need to be determined | Not determined |
| West | PENDING | PENDING | Not determined |

Do not fill in setback distances until the applicable requirement has been identified from the relevant code/regulation and the site/road boundary used for measurement has been determined.

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
