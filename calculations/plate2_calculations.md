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
| C-01 | Lot area | **265.26 m² from adjusted closed traverse; compare with approximate 300.00 m² stated area** |
| C-02 | Lot dimensions / boundary lengths | **Original courses recorded; adjusted perimeter = 64.1454 m** |
| C-03 | Traverse closure | **Closed by adjusting P5-1 only; original misclosure = 4.0120 m** |
| C-04 | Required setbacks | **PENDING** |
| C-05 | Buildable area | **PENDING** |
| C-06 | Building footprint | **PENDING** |
| C-07 | Floor areas | **73.47 m² per enclosed floor; 4.50 m² balcony additional; 151.44 m² total including balcony** |
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

### Phase 1 coordinate plot and closure adjustment

The closed preliminary graphic is in [site/phase1_site_base.svg](../site/phase1_site_base.svg), the course coordinate schedule including original and adjusted P5-1 records is in [site/phase1_traverse_coordinates.csv](../site/phase1_traverse_coordinates.csv), and the site analysis is in [site/phase1_site_analysis.md](../site/phase1_site_analysis.md).

These outputs use a local coordinate frame with P1 = (0, 0). They are not georeferenced. The instructor directed that the traverse be closed, so courses 1-2 through 4-5 remain unchanged and P5-1 is adjusted to N 06°02′11″ E, 15.7954 m. The original P5-1 value (N 08°10′ W, 16.35 m) is retained for transparency; the original unadjusted traverse misclosure is approximately 4.0120 m.

The adjusted perimeter is 64.1454 m and the closed-polygon area is 265.26 m². The assignment's approximate 300.00 m² area is 34.74 m² higher than this calculated result. Both values are documented without modifying courses 1-2 through 4-5 or forcing the calculated area to match the approximate area.

# C-04. Required Setbacks

**Adopted classroom assumption: 2.00 m inward from each of the five property boundaries.**

PD 1096 Section 708(a) gives a general minimum 2 m property-line distance for Group A dwellings. For this student activity, apply 2.00 m uniformly to P1-P2, P2-P3, P3-P4, P4-P5, and P5-P1 as the selected academic basis. Do not treat this as a real-site approval or as a substitute for a special requirement that the instructor may specifically assign.

| Boundary | Adopted academic setback |
|---|---:|
| P1-P2 | 2.00 m |
| P2-P3 | 2.00 m |
| P3-P4 | 2.00 m |
| P4-P5 | 2.00 m |
| P5-P1 | 2.00 m |

Road information to show on A-01: the **5.00 m carriageway is inside the 8.00 m total ROW**. The remaining 3.00 m is part of the total ROW outside the carriageway, but the assignment gives no exact allocation. Show both widths separately; do not subtract the carriageway again from the adopted 265.26 m² lot area.

Code reference: [PD 1096, Section 708, Supreme Court E-Library](https://elibrary.judiciary.gov.ph/thebookshelf/showdocs/26/53320).

**Result:** S-01 uniform 2.00 m offset selected for the academic design. S-02 to S-04 are retained as comparisons only.

---

# C-05. Buildable Area

Use the calculated area of the offset polygon for the selected S-01 scenario.

| Item | Value |
|---|---:|
| Adopted academic lot area | 265.26 m² |
| Setback | 2.00 m on each of five boundaries |
| Area inside the setback envelope | 152.4309 m² |
| Rounded academic buildable-envelope area | **152.43 m²** |

**Result:** 152.43 m² inside the uniform 2.00 m offset. This is the area used as the design envelope for this student activity.

---

# C-06. Building Footprint

## Main house footprint

```text
Footprint = width × depth
          = 9.30 m × 7.90 m
          = 73.47 m²
```

## Carport footprint

```text
Carport = 2.80 m × 5.50 m
        = 15.40 m²
```

## Combined covered ground area

```text
Combined covered area = 73.47 + 15.40
                      = 88.87 m²
```

The carport is treated as a separate open-sided covered area. The Phase 2 scenario geometry indicates that the current house and carport rectangles both fit within the selected S-01 offset envelope.

**Result:** Main-house footprint = 73.47 m²; carport = 15.40 m²; combined covered ground area = 88.87 m².

---

# C-07. Floor Areas

For this academic calculation, assume the enclosed part of both storeys uses the same 9.30 m × 7.90 m outer house envelope. The required second-floor balcony is an external area and must be listed separately from enclosed floor area.

## Ground-floor enclosed area

```text
Ground-floor area = 9.30 m × 7.90 m
                  = 73.47 m²
```

## Second-floor enclosed area

```text
Second-floor enclosed area = 9.30 m × 7.90 m
                           = 73.47 m²
```

## Required second-floor balcony

Adopt a 3.00 m width and 1.50 m projection from the master-bedroom wall.

```text
Balcony area = width × projection
             = 3.00 m × 1.50 m
             = 4.50 m²
```

The balcony is open to the exterior, attached to the master bedroom, and accessed through a nominal 0.90 m balcony door. Include a perimeter guardrail in the architectural concept. The balcony is within the plan's selected S-01 2.00 m academic setback envelope and is shown separately in A-03.

## Total floor area

```text
Total enclosed house floor area = ground-floor area + second-floor enclosed area
                                = 73.47 + 73.47
                                = 146.94 m²

Second-floor area including balcony = 73.47 + 4.50
                                    = 77.97 m²

Total floor area including balcony = 146.94 + 4.50
                                  = 151.44 m²
```

| Item | Academic result |
|---|---:|
| Ground-floor enclosed area | 73.47 m² |
| Second-floor enclosed area | 73.47 m² |
| Required balcony area | 4.50 m² |
| Second-floor total including balcony | 77.97 m² |
| **Total enclosed house floor area** | **146.94 m²** |
| **Total floor area including balcony** | **151.44 m²** |

The two totals are reported separately to avoid counting the open balcony as enclosed space. Recalculate if the final A-03 uses a different balcony size or second-floor outer outline.

# C-08. Remaining Open Space

For this calculation, count the main house and roofed carport as covered ground area.

```text
Uncovered area = lot area − combined covered ground area
               = 265.26 − 88.87
               = 176.39 m²
```

```text
Uncovered percentage = (176.39 ÷ 265.26) × 100
                     ≈ 66.5%
```

| Item | Area |
|---|---:|
| Adopted lot area | 265.26 m² |
| House + carport covered area | 88.87 m² |
| **Remaining uncovered area** | **176.39 m²** |
| **Uncovered percentage** | **66.5%** |

This is the arithmetic area not covered by the house and carport. Driveways and walkways may occupy part of it, so it should not automatically be described as all landscaped or permeable open space.

---

# C-09. Occupant Load

The assignment states that the proposed dwelling will accommodate **5-6 persons**. For planning, select the upper end of the stated range.

```text
Adopted academic design occupant count = 6 persons
```

**Result:** 6 persons for the preliminary residential layout. This uses the assignment's stated household size; it is not an assembly-occupancy factor calculation. If a floor-area method is specifically required by the instructor, use the assigned code table/factor and show its source rather than inventing a value.

---

# C-10. Stair Design Calculations

The Phase 4 stair study assumes a floor-to-floor height of 3.000 m. Carry these same values into Phase 2 and coordinate them with A-06.

## Total stair height

```text
H = second-floor FFL − ground-floor FFL
H = 3.000 m − 0.000 m = 3.000 m = 3000 mm
```

## Number of risers and riser height

```text
Number of risers = 18 total (9 per flight)
Riser height = 3000 mm ÷ 18
             = 166.7 mm
Check: 18 × 166.7 mm ≈ 3000 mm
```

## Tread depth and run

```text
Physical treads per flight = 9 risers − 1 = 8
Tread depth = 280 mm = 0.280 m
Run per flight = 8 × 0.280 m = 2.240 m
```

| Item | Result |
|---|---:|
| Floor-to-floor rise | 3.000 m (assumed) |
| Number of risers | 18, arranged 9 + 9 |
| Riser height | 166.7 mm |
| Tread depth | 280 mm |
| Run per flight | 2.240 m |
| Clear width per flight | 0.900 m |
| Intermediate landing depth | 0.900 m |
| Reserved stair-space envelope | 2.000 m × 3.200 m = 6.40 m² |

PD 1096 Section 708(h) states a minimum Group A stair clear width of 750 mm, maximum rise of 200 mm, and minimum run of 200 mm. The selected 900 mm width, 166.7 mm rise, and 280 mm tread exceed those basic dimensions. Headroom, openings, handrails and final section coordination still need to be shown on the architectural drawings.

Reference: [PD 1096, Section 708, Supreme Court E-Library](https://elibrary.judiciary.gov.ph/thebookshelf/showdocs/26/53320).

**Result:** Preliminary stair calculation completed under the assumed 3.000 m floor-to-floor height.

---

# C-11. Parking Requirement

For the academic single-family house design, provide **one off-street car space** in the planned carport.

```text
Number of proposed car spaces = 1
Carport dimensions = 2.80 m × 5.50 m
Carport area = 15.40 m²
```

A commonly cited NBCP Rule XIX passenger-car stall size is 2.40 m × 5.00 m. The proposed 2.80 m × 5.50 m carport is larger than those nominal dimensions. Use one space to match this plate's single-car carport concept.

**Result:** One proposed parking space, 2.80 m × 5.50 m. This is the selected classroom design assumption; use a different number/dimension if the instructor gave a specific parking table.

References: [PD 1096, Section 708, Supreme Court E-Library](https://elibrary.judiciary.gov.ph/thebookshelf/showdocs/26/53320); [Supreme Court E-Library decision quoting NBCP Rule XIX parking-slot dimensions](https://elibrary.judiciary.gov.ph/thebookshelf/showdocs/1/49990). The slot-size comparison is a cited baseline for this class exercise, not a claim that no later or instructor-specific table applies.

---

# C-12. Other Applicable Requirements

For the preliminary Group A dwelling, carry these code-related checks into the architectural plan set:

| Requirement | Phase 2 design treatment |
|---|---|
| Lot occupancy | Combined covered area ÷ lot area = 88.87 ÷ 265.26 = **33.5%** |
| Conservative occupancy comparison | 80% × 265.26 = **212.21 m²**; the 88.87 m² covered area is lower. The Section 708(a) inside/corner lot classification is not needed to make this classroom coverage comparison pass. |
| Entrance and exit | Show a main entrance and a separate exit path/opening in the coordinated plan, consistent with PD 1096 Section 708(i) |
| Light and ventilation | Locate room windows/openings on A-02/A-03 and review them against the room arrangement, consistent with Section 708(b) and the code's light/ventilation provisions |
| Sanitation | Include at least one toilet and bath, consistent with Section 708(c); detailed plumbing and sanitary-system design is excluded from this plate |
| Road / ROW labels | Label 5.00 m carriageway within 8.00 m total ROW; leave the remaining 3.00 m unallocated unless the assignment specifies its division |
| Other building services | Detailed plumbing, sanitary, electrical, mechanical, and fire-protection systems remain excluded by the assignment |

No detailed utility design is added in this plate because the instructor's project description explicitly reserves it for succeeding plates.

---

## Final Calculation Review Checklist

- [x] Lot area adopted as 265.26 m² for this academic exercise.
- [x] Lot boundary lengths and the adjusted traverse are recorded in the Phase 1 files.
- [x] Traverse closure and original misclosure are documented, including the adjusted P5-1 course.
- [x] Selected 2.00 m uniform academic setbacks recorded.
- [x] Buildable-envelope area calculated as 152.43 m².
- [x] Main-house footprint calculated as 73.47 m².
- [x] Carport footprint calculated as 15.40 m².
- [x] Ground-floor area calculated as 73.47 m² under the same-envelope assumption.
- [x] Second-floor enclosed area calculated as 73.47 m² under the same-envelope assumption.
- [x] Required second-floor balcony calculated as 3.00 m × 1.50 m = 4.50 m².
- [x] Total enclosed house floor area calculated as 146.94 m²; total including balcony = 151.44 m².
- [x] Remaining uncovered area calculated as 176.39 m² (approximately 66.5%).
- [x] Academic design occupant count adopted as 6 persons.
- [x] Stair width, risers, riser height, tread depth, landing dimensions and total rise recorded.
- [x] One-car parking space adopted, with a 2.80 m × 5.50 m carport.
- [x] Other preliminary Group A requirements identified for drawing coordination.
- [ ] Confirm that A-01 shows the 5.00 m road inside the 8.00 m total ROW and the selected setbacks.
- [ ] Confirm that A-02 and A-03 dimensions match the adopted footprint and area assumptions.
- [ ] Confirm that all values match the coordinated final drawings before printing.

**Phase 2 calculations are complete for the academic assumptions agreed by the student.** The required 4.50 m² second-floor balcony is reported separately from enclosed area. The remaining checks above are drawing-coordination tasks, not a requirement to obtain real-project approvals.
