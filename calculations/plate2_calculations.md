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
| C-04 | Required setbacks | **2.00 m inward-offset screening only; local zoning / road ROW confirmation pending** |
| C-05 | Buildable area | **152.43 m² screening polygon calculated; final legal envelope pending** |
| C-06 | Building footprint | **86.26 m² preliminary area-budget proxy; final outline pending** |
| C-07 | Floor areas | **86.26 m² ground / 83.48 m² second / 169.74 m² total planning proxies; final measured areas pending** |
| C-08 | Remaining open space | **179.00 m² lot-area subtraction proxy; formal open-space check pending** |
| C-09 | Occupant load | **PENDING** |
| C-10 | Stair design | **Preliminary calculation under assumed 3.000 m rise; level/code applicability pending** |
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

## Revised Phase 3 area-budget scenario (2026-10-12)

The room programme has been revised to retain the spaces in the selected reference images before preparing a dimensioned plan. The structured calculations are in [phase3_area_budget.csv](phase3_area_budget.csv).

| Planning check | Preliminary value | Status |
|---|---:|---|
| Lot area | 265.26 m² | Adjusted academic traverse |
| 2.00 m inward-offset screening polygon | 152.43 m² | Screening only, not a confirmed legal envelope |
| Ground-floor programmed clear area, including enclosed garage | 73.32 m² | Provisional target |
| Ground-floor gross-area proxy | 86.26 m² | 73.32 / 0.85 |
| Second-floor programmed clear area, excluding balcony | 70.96 m² | Retains 3 bedrooms and 3 labelled wet rooms; adds robe, karaoke, gym and shared circulation |
| Second-floor gross-area proxy | 83.48 m² | 70.96 / 0.85 |
| Total gross-area planning proxy | 169.74 m² | Not final C-07 floor area |
| Ground-footprint proxy / adjusted lot area | 32.52% | Planning comparison only |
| Lot area less footprint proxy | 179.00 m² | Not a formal open-space result |

The area budget assumes an **enclosed garage** because that is how the reference is shown. A 3.00 x 5.50 m clear bay is used to budget the space, but actual vehicle width, door swing, wall thickness and maneuvering should be checked. If changed to a covered-open carport, use the alternate row in the area-budget CSV and calculate enclosed floor area separately.

**Code and zoning hold point:** PD 1096 Section 708(a) gives general Group A dwelling criteria (including a 2 m property-line distance and a 90% maximum lot occupancy for corner lots). The lot description suggests two road-frontage sides, but exact local zone, official ROW/property lines, local frontage setbacks and other applicable conditions remain unverified. Official source: https://elibrary.judiciary.gov.ph/thebookshelf/showdocs/26/53320. Do not treat the 90% calculation or the 2 m screen as approval of the proposed footprint.

# C-04. Required Setbacks

## Assignment requirement

Determine applicable setbacks from the codes, regulations and local zoning information that actually apply to the site.

## Given data

- Calculated area from the adjusted closed traverse: 265.2598 m².
- The project information states an 8.00 m road right-of-way (ROW).
- The lot description states an existing 5.0 m barangay road along boundary courses P2-P3 and P3-P4. The existing paved road width and the full ROW are different measurements.
- The site description therefore suggests a lot with two road-frontage sides, but official parcel/ROW geometry and local zoning classification have not been supplied.

## National-code screening reference

PD 1096, National Building Code of the Philippines, Section 708(a), states that a Group A dwelling occupies not more than 90% of a corner lot or 80% of an inside lot and is at least 2 m from the property line, subject to the Civil Code provisions noted there. Official source: https://elibrary.judiciary.gov.ph/thebookshelf/showdocs/26/53320

The two described road-frontage edges support evaluating a corner-lot scenario, but this worksheet does **not** assert the parcel's final zoning/lot classification. The 2.00 m uniform offset stored in the building model is used only as a preliminary geometric screen. Applicable Palo zoning provisions, actual road ROW lines, easements, special frontage rules and instructor/building-official interpretation may impose different or additional requirements.

## Preliminary screening values

Corner-lot occupancy cap scenario, only if that classification and the cited provision are confirmed:

Theoretical coverage cap = 265.2598 m² x 0.90 = **238.7338 m²**

This is a theoretical percentage cap only. It is not the footprint target, does not override the setbacks, and does not prove that a footprint fits the irregular lot.

The current local-coordinate screening polygon uses an inward offset of 2.00 m at every lot edge. Its area is checked in C-05. This is **not a final approved setback plan**.

| Boundary / side | Screening offset | Final legal setback status |
|---|---:|---|
| North / P1-P2 | 2.00 m, screening only | PENDING |
| Road frontage / P2-P3 | 2.00 m, screening only | PENDING ROW and local frontage rule |
| Road frontage / P3-P4 | 2.00 m, screening only | PENDING ROW and local frontage rule |
| P4-P5 | 2.00 m, screening only | PENDING |
| P5-P1 | 2.00 m, screening only | PENDING |

**Result/status:** The 2.00 m screening offset is available for a preliminary fit study only. Confirm the approved land-use zone for Lot 245-B, the legal property/ROW line, and applicable local setback provisions before calling any value a required setback.

---

# C-05. Buildable Area

## Required inputs

- Adjusted academic lot polygon from C-01 to C-03.
- A provisional 2.00 m inward-offset polygon generated from the five lot boundary lines.
- Final local setbacks and ROW lines are still pending under C-04.

## Working: screening polygon area

The repository stores the provisional inward-offset vertices under site.setback_screening_polygon in data/building_model.json. Use the shoelace formula:

A = 1/2 x absolute value of sum(EᵢNᵢ₊₁ - Eᵢ₊₁Nᵢ)

The area of the stored 2.00 m uniform-offset polygon is:

**Screening-envelope area = 152.4309 m²**

Comparison to the lot and conditional occupancy scenario:

| Item | Area | Meaning |
|---|---:|---|
| Adjusted closed lot | 265.2598 m² | Academic traverse result |
| 90% corner-lot occupancy cap scenario | 238.7338 m² | Conditional PD 1096 Section 708(a) calculation, not a setback calculation |
| Uniform 2.00 m offset polygon | 152.4309 m² | Preliminary geometric screening envelope |
| Proposed ground-footprint planning proxy | 86.2588 m² | Early area-budget target, not dimensioned geometry |

For this study, the offset polygon is more restrictive by area than the 90% cap scenario. The footprint still must fit **geometrically** inside the polygon; subtracting areas alone is not sufficient to show compliance. The footprint may not use setbacks, frontage access or ROW space just because the total area arithmetic works.

**Result/status:** The 152.4309 m² screening polygon area is calculated. Final buildable area remains **PENDING** until the local zoning class, official ROW/property limits and applicable setbacks are verified and the actual footprint is drawn and checked.

---

# C-06. Building Footprint

## Basis

The furnished reference shows an attached/enclosed garage at the left side of the ground-floor arrangement. The previous model instead contained a 9.30 m x 7.90 m rectangular main-house target (73.47 m²) plus a 2.80 m x 5.50 m covered-open carport (15.40 m²). That older geometry is not coordinated to the reference and is kept only for comparison.

For the revised area budget, use the garage as enclosed unless a later design decision changes it to a covered-open carport. The space table now budgets a 3.00 m x 5.50 m clear garage area and preserves the inherited target areas for the other required ground-floor spaces.

## Ground-floor clear area budget

Previously scheduled ground-floor clear-space programme, including the 4.50 m² general circulation allowance: **56.82 m²**

Proposed garage clear target: 3.00 m x 5.50 m = **16.50 m²**

Total clear programmed area including garage: 56.82 + 16.50 = **73.32 m²**

Use the inherited rough 15% walls/structure allowance only for an early sizing check:

Gross footprint planning proxy = 73.32 / 0.85 = **86.2588 m² ≈ 86.26 m²**

This 15% allowance is an estimate carried forward from the prior planning worksheet, not a legal/code multiplier and not an actual outside-wall measurement. The existing model's house-plus-carport total is 88.87 m², which is close enough to retain as a candidate fit study, but the main footprint, garage geometry and openings must be redesigned to reflect the selected reference layout.

## Footprint checks still required

| Item | Result | Status |
|---|---:|---|
| Area-budget ground footprint proxy | 86.26 m² | Preliminary target |
| Existing main rectangle, 9.30 x 7.90 m | 73.47 m² | Legacy geometry only |
| Existing main rectangle + carport | 88.87 m² | Legacy geometry only; differs from reference garage |
| Legal setback / zoning fit | PENDING | Must use approved setback and ROW geometry |
| Reference layout outer-wall area | PENDING | Requires dimensioned plan |
| Garage enclosure, clearances and site access | PENDING | Final decision and driveway needed |

**Result/status:** The area budget now sets an initial target of about 86-90 m² for the combined ground-level footprint including an enclosed garage. Use this as a planning range, not a fixed approved footprint. Final C-06 is pending actual exterior dimensions and geometric site fit.

---

# C-07. Floor Areas

## Area-budget basis

The current reference adds a robe, a separate bathroom, a separate toilet, a karaoke room and a gym to the upstairs programme. These were not included in the earlier 44.23 m² second-floor room budget. The revised schedule has a provisional target for each, plus an 8.00 m² shared stair landing/circulation allowance. These target sizes are selected for area-budget planning only; they are not extracted from the image or code minimums.

| Second-floor space | Proposed clear-size target | Area target |
|---|---:|---:|
| Master bedroom | 3.20 x 3.40 m (inherited target) | 10.88 m² |
| Bedroom 2 | 2.80 x 3.00 m (inherited target) | 8.40 m² |
| Bedroom 3 | 2.80 x 3.00 m (inherited target) | 8.40 m² |
| Toilet and bath | 1.50 x 2.10 m (inherited target) | 3.15 m² |
| Family area | 2.80 x 3.00 m (inherited target) | 8.40 m² |
| Robe / wardrobe | 1.20 x 2.40 m (provisional) | 2.88 m² |
| Separate bathroom | 1.50 x 2.10 m (provisional) | 3.15 m² |
| Separate toilet | 1.20 x 1.50 m (provisional) | 1.80 m² |
| Karaoke room | 2.50 x 3.00 m (provisional) | 7.50 m² |
| Gym | 2.80 x 3.00 m (provisional) | 8.40 m² |
| Shared stair landing / hall circulation allowance | Area allowance, not a fixed rectangle | 8.00 m² |
| **Programmed second-floor clear-space budget** | | **70.96 m²** |
| Optional balcony | 1.20 x 3.00 m (provisional external space) | 3.60 m², excluded from enclosed proxy |

Second-floor gross-area planning proxy = 70.96 / 0.85 = **83.4824 m² ≈ 83.48 m²**

The total clear-space budget for the ground floor including the enclosed garage is 73.32 m², giving an 86.26 m² gross-area proxy with the same provisional factor.

Total floor-area planning proxy = 86.2588 + 83.4824 = **169.7412 m² ≈ 169.74 m²**

These are **area-budget proxies only**. The 15% allowance is a rough planning assumption, not a code factor. Actual gross floor areas must be measured from the dimensioned plan using the area-measurement convention required by the instructor and applicable rules. Stairwell voids, landings, walls, any garage classification, balcony and projections must be treated consistently.

**Result/status:** C-07 remains **PENDING for final floor areas**. The room programme now has a consistent provisional area budget to guide the next dimensioned design pass.

---

# C-08. Remaining Open Space

## Planning scenario

Use the adjusted closed traverse area and the ground-floor footprint proxy. This is a subtraction from the lot, not yet the formal zoning calculation of qualifying open or permeable space.

Remaining unbuilt lot area proxy = lot area - ground footprint proxy = 265.2598 - 86.2588 = **179.0010 m² ≈ 179.00 m²**

For comparison only, the 2.00 m setback-screening polygon has 152.4309 m². Subtracting the same footprint proxy gives:

Screening-polygon area remaining by subtraction = 152.4309 - 86.2588 = **66.1720 m² ≈ 66.17 m²**

The second value is an area comparison, **not proof that the footprint shape fits**. Both results exclude any later revisions to the main building outline, driveway, paving and detached structures. An area outside the footprint is not automatically qualifying open space under every applicable zoning/open-space rule.

| Item | Result | Status |
|---|---:|---|
| Adjusted closed lot area | 265.26 m² | Preliminary traverse calculation |
| Ground-floor footprint planning proxy | 86.26 m² | Provisional area budget |
| Unbuilt lot-area subtraction proxy | 179.00 m² | Preliminary |
| Uniform 2.00 m screen area | 152.43 m² | Geometric screening only |
| Screen area remaining by subtraction | 66.17 m² | Area-only comparison |
| Required / qualifying open space under local zoning | PENDING | Need exact zoning and measurement method |

**Result/status:** The planning subtraction has been calculated. C-08 remains **PENDING** until the final outline, confirmed zoning/setbacks, any required yard/open-space rules, and the drive/walk/paved areas are measured.

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

Determine stair width, number of risers, riser height, tread depth, landing dimensions and total stair height.

## Design assumption requiring confirmation

The assignment/repository does not yet provide final finished-floor elevations. The following preliminary computation therefore assumes a **3.000 m floor-to-floor rise**, from ground floor FFL ±0.000 m to second floor FFL +3.000 m. Change this input and recalculate if the instructor's building section specifies a different level difference.

## Working

### Total stair height

```text
H = second-floor FFL - ground-floor FFL
H = 3.000 m - 0.000 m = 3.000 m
```

### Number of risers and riser height

Choose 18 equal risers so that the rise remains below a 175 mm design target.

```text
N = 18 risers
R = H / N = 3.000 m / 18
R = 0.1666667 m = 166.7 mm

Check: 18 x 166.6667 mm = 3000.0 mm
```

Arrange two flights with 9 risers in each:

```text
Rise per flight = 9 x 166.6667 mm
                = 1500 mm = 1.500 m
```

### Tread depth and run

Select a 280 mm tread depth for the preliminary design. Each flight has 9 risers, 8 physical treads, and 2.240 m horizontal run.

```text
Treads per flight = 9 - 1 = 8
Run per flight = 8 x 0.280 m = 2.240 m
Physical treads = 8 + 8 = 16
Combined physical tread run = 16 x 0.280 m = 4.480 m
```

Comfort cross-check only:

```text
2R + T = 2(166.7 mm) + 280 mm
       = 613.4 mm (approximately)
```

The comfort expression is not a substitute for the applicable code requirements.

### Preliminary width and landing

| Item | Result | Check / note |
|---|---:|---|
| Floor-to-floor rise | 3.000 m | Assumed, not given |
| Number of risers | 18 | 9 per flight |
| Calculated rise | 166.7 mm | Uniform in both flights |
| Tread depth | 280 mm | Exceeds the cited general 250 mm minimum |
| Physical treads | 16 total | 8 per flight |
| Horizontal run per flight | 2.240 m | 8 x 280 mm |
| Clear width per flight | 0.900 m | Preliminary private-dwelling stair target |
| Intermediate landing depth | 0.900 m | At least one flight width |
| Combined half-landing width | 2.000 m nominal | Two 0.900 m flights plus a 0.200 m central separation allowance |
| Effective plan length | 3.140 m | 2.240 m run + 0.900 m landing |
| Nominal space envelope | 2.000 x 3.200 m | 6.40 m²; an allowance for coordination, not finished dimensions |
| Minimum headroom | 2.000 m | Must be checked in the coordinated section |
| Target handrail height | 0.850 m | Verify against the adopted rule and the final open-side guards |

## Code-basis notes

PD 1096 Section 708(h) states Group A dwelling stair requirements. The general NBCP stairway provisions include a maximum riser of 200 mm, minimum tread/run of 250 mm, 2.00 m minimum headroom, and landing/handrail provisions. The selected 900 mm clear flight width, 166.7 mm rise and 280 mm tread are preliminary choices checked against the cited ordinary stair criteria. The local building official/instructor must confirm the exact applicable rule set.

References:
- [PD 1096 / National Building Code of the Philippines](https://elibrary.judiciary.gov.ph/thebookshelf/showdocs/26/53320)
- [PD 1096, Senate Legislative Reference Bureau](https://ldr.senate.gov.ph/legislative%2Bissuances/Presidential%20Decree%20No.%201096%2C%20s.%201977)
- [NCDA: 2024 Revised IRR of BP 344](https://ncda.gov.ph/revised-2024-rules-and-regulations-implementing-batas-pambansa-344/)

**Accessibility hold point:** The design is not represented as an accessible staircase. Where the revised BP 344 accessible-stair provisions apply, the published values include a 150 mm maximum riser, 300 mm minimum tread, 1.50 m clear staircase width, landings at least 1.50 m deep, and complementary ramp/lift/escalator along accessible routes. This would require redesigning both stair geometry and reserved area; confirm applicability before finalizing.

## Checks still required in the final drawings

- Minimum 2.00 m clear headroom from a plane parallel to tread nosings to the soffit.
- Landing and door-swing clearances.
- Uniform tread/riser dimensions, finished surfaces and lighting.
- Handrails and guards at open sides.
- Slab, beam and finish depths at both levels.
- Structural sizing and detailing, outside the current stair geometry calculation.

**Result:** Preliminary calculation complete under the **assumed 3.000 m floor-to-floor rise**. These results must be revised if the accepted floor levels, code applicability or selected stair arrangement changes.

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
- [x] P5-1 adjustment to close the traverse is documented, and its original value is retained for reference.
- [x] Compare the calculated 265.26 m² polygon area against the approximate 300.00 m² area stated in the assignment; the 34.74 m² difference is recorded.
- [ ] Final required setbacks determined from the applicable local zoning classification and official property/ROW lines (2.00 m screen is only provisional).
- [x] Provisional 2.00 m offset screening polygon area calculated as 152.43 m²; final legal buildable area remains pending.
- [x] Revised ground-floor area-budget proxy calculated; actual exterior-wall footprint remains pending.
- [x] Provisional ground/second/total area-budget proxies calculated; final measured floor areas remain pending.
- [x] Provisional lot-area subtraction calculated; formal qualifying open space remains pending.
- [ ] Occupant load determined using the applicable method.
- [ ] Stair width, risers, riser height, tread depth, landings, and total stair height determined.
- [ ] Parking requirement determined.
- [ ] Other applicable requirements calculated if identified.
- [ ] All calculations use clear labels, consistent units, shown formulas, substituted values, and final results.
- [ ] Calculation values agree with the final drawings.

**Current status:** C-02 perimeter and C-03 traverse-closure arithmetic have preliminary results. The lot-area verification and remaining calculations are pending the information and design work required by the assignment.
