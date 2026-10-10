# Phase 4: Stair Planning and Calculations

**Project:** CE 393 Plate No. 2, Proposed Two-Storey Residential Building  
**Status:** Preliminary stair study with a documented assumed floor-to-floor height. Not a construction or structural drawing.

## 1. Design decision and key assumption

Use a **U-shaped return stair with two parallel flights and an intermediate half-landing** as a compact starting arrangement. The assignment/repository does not yet state floor-to-floor height. For calculation only, this package assumes:

- Ground-floor finished floor: ±0.000 m.
- Second-floor finished floor: +3.000 m.
- Total vertical stair rise: **3.000 m**.
- Clear stair width per flight: **0.900 m**.
- Target riser: no more than **175 mm** by design preference, below the cited general NBCP maximum.
- Tread depth: **280 mm** as a preliminary selected dimension.

These are design assumptions, not facts from the assignment. Replace the assumed elevation difference if the instructor's floor levels or the later building section specify another height.

## 2. Code basis and applicability hold point

The official text of PD 1096 Section 708(h) gives Group A dwelling stair dimensions; the general stairway provisions in the NBCP set a maximum 200 mm rise, minimum 250 mm run, and at least 2.00 m headroom. The proposed **166.7 mm riser, 280 mm tread, and 900 mm clear width** are selected as conservative preliminary dimensions relative to these cited ordinary dwelling-stair limits. This is not a complete code-compliance determination.

Sources:
- [PD 1096 / National Building Code of the Philippines, Section 708](https://elibrary.judiciary.gov.ph/thebookshelf/showdocs/26/53320)
- [PD 1096, Senate Legislative Reference Bureau](https://ldr.senate.gov.ph/legislative%2Bissuances/Presidential%20Decree%20No.%201096%2C%20s.%201977)

**Accessibility hold point:** The NCDA's published [2024 revised IRR of BP 344](https://ncda.gov.ph/revised-2024-rules-and-regulations-implementing-batas-pambansa-344/) includes stricter dimensions for *accessible staircases*, including maximum 150 mm risers, minimum 300 mm treads, 1.50 m clear width and 1.50 m minimum landing depth, plus complementary ramps/lifts/escalators along accessible routes. This concept is a private Group A dwelling stair and is **not** being certified as an accessible staircase. The instructor / building official must confirm whether those provisions apply to this specific design. If they apply, redesign the stair and its envelope; the present 0.90 m flights and 0.90 m landing depth are insufficient for that accessibility specification.

## 3. Main calculation

### 3.1 Total stair height

```text
H = second-floor FFL - ground-floor FFL
H = 3.000 m - 0.000 m
H = 3.000 m
```

### 3.2 Number of risers and actual riser height

Choose 18 equal risers so that each rise is below the selected 175 mm design target.

```text
N = 18 risers
R = H / N
R = 3.000 m / 18
R = 0.1666667 m = 166.7 mm
Check: 18 x 166.6667 mm = 3000.0 mm
```

Split the stair into two balanced flights:

```text
Risers per flight = 9 + 9
Rise per flight = 9 x 166.6667 mm = 1500 mm = 1.500 m
```

The vertical distance between the ground floor and half-landing is 1.50 m, and between the half-landing and second floor is another 1.50 m. Both are below the 3.60 m maximum vertical distance between landings in the general stairway provision.

### 3.3 Tread depth and horizontal run

Use a preliminary tread depth of 280 mm. Each 9-riser flight has 8 physical treads before the next landing/floor level.

```text
Treads per flight = 9 risers - 1 = 8
Run per flight = 8 x 0.280 m = 2.240 m
Physical treads = 8 + 8 = 16
Combined physical tread run = 16 x 0.280 m = 4.480 m
```

The combined physical tread run is the sum of the two flight runs; it is not the overall plan length of the U-shaped stair. The stair footprint uses the **longer single-flight run** plus the intermediate landing depth.

A common comfort cross-check is:

```text
2R + T = 2(166.7 mm) + 280 mm
       = 613.4 mm (approximately)
```

This is recorded only as a design-comfort check, not as a substitute for code requirements.

## 4. Width, landing and stair-space envelope

| Item | Preliminary dimension | Check / explanation |
|---|---:|---|
| Clear width per flight | 0.900 m | Preliminary private-dwelling stair width; verify final code path and actual clear width after handrails/finishes |
| Riser height | 0.1667 m (166.7 mm) | 3.000 / 18; equal risers |
| Tread depth | 0.280 m (280 mm) | Above the cited general 250 mm minimum |
| Risers per flight | 9 | 1.500 m vertical rise per flight |
| Physical treads per flight | 8 | 8 x 280 mm = 2.240 m run |
| Intermediate landing depth | 0.900 m minimum in direction of travel | Matches one flight's 0.900 m clear width |
| Combined half-landing width | 2.000 m nominal | Spans both 0.900 m flights plus 0.200 m central separation allowance |
| Effective plan length | 2.240 + 0.900 = 3.140 m | Longest flight run plus landing |
| Nominal stair-space envelope | **2.000 m x 3.200 m** | Provides a nominal 60 mm length allowance beyond 3.140 m; wall/finish geometry still to be resolved |
| Nominal envelope area | 2.000 x 3.200 = **6.40 m²** | Planning reserve, not measured floor area |
| Minimum stair headroom | 2.000 m | Verify from tread-nosing plane to soffit at every point in the section |
| Target handrail height | 0.850 m above tread nosings | Within the NBCP's usual 0.800-0.900 m range; verify guard/handrail detail |

The 0.200 m central separation and the 60 mm planning allowance are envelope allowances only. They do not determine a central wall, handrail profile, stringer or structural thickness. Do not use this table as a fabrication or construction schedule.

## 5. Required safety and coordination checks

- Keep all risers and treads uniform within each flight. The general NBCP stair provision limits variation within a flight to 5 mm.
- Confirm a minimum 2.000 m clear headroom above the stair nosing line after beams, slabs, ceiling/soffit, finishes and landings are shown.
- Coordinate handrails on the final open sides and both sides where appropriate. The ordinary dwelling exception does not remove the need to guard open sides.
- Confirm that doors do not reduce landing clear width or swing across the clear landing route.
- Provide slip-resistant, durable tread finishes, adequate lighting and non-obstructed circulation.
- Recheck BP 344 accessibility applicability before freezing the geometry; the accessible-stair dimensions summarized above would require a larger redesign.
- This plate does not include structural sizing, reinforcement, stringer/beam sizing, vibration analysis, foundations or a full life-safety review.

## 6. Preview drawings

- [Stair plan study](stair_plan.svg): two flights, half-landing, plan envelope and principal dimensions.
- [Stair section / development study](stair_section.svg): vertical rise, riser/tread pattern, intermediate landing and headroom note.

The section file is a stair development schematic for calculation coordination. It is **not** the final building section A-06; Phase 5 must produce a coordinated building section through the actual stairway.

## 7. Phase 4 result

A preliminary stair arrangement and arithmetic set are now defined from a 3.000 m assumed floor-to-floor height: **18 risers at 166.7 mm; two flights of 9 risers; 16 physical treads of 280 mm; 2.240 m run per flight; 900 mm clear flight width; 900 mm landing depth; 2.000 m x 3.200 m nominal space envelope**.

**Hold before finalization:** instructor confirmation of floor-to-floor levels, accessibility-code applicability, stair structure, headroom and door/landing clearances. Revise all derived dimensions if the accepted height or applicable rules change.
