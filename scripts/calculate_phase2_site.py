#!/usr/bin/env python3
"""Calculate Phase 2 site metrics and clearly separated envelope scenarios.

The final applicable road-side yard remains unselected pending local zoning
confirmation. This script calculates explicit geometry-only scenarios without
promoting any one scenario to a final code-compliant building envelope.
"""
from __future__ import annotations

import argparse
import csv
import math
import sys
from pathlib import Path
from typing import Sequence

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_TRAVERSE = ROOT / "site" / "phase1_traverse_coordinates.csv"
DEFAULT_SETBACKS = ROOT / "site" / "phase2_setback_inputs.csv"
DEFAULT_REQUIREMENTS = ROOT / "site" / "phase2_code_requirements.csv"
EXPECTED_COURSES = ("1-2", "2-3", "3-4", "4-5", "5-1 adjusted to close")
TOLERANCE = 1e-5

Point = tuple[float, float]


def polygon_area(vertices: Sequence[Point]) -> float:
    """Return the absolute shoelace area in square units."""
    if len(vertices) < 3:
        raise ValueError("A polygon needs at least three vertices.")
    if any(not math.isfinite(value) for point in vertices for value in point):
        raise ValueError("Polygon coordinates must be finite numbers.")
    double_area = sum(
        x1 * y2 - x2 * y1
        for (x1, y1), (x2, y2) in zip(vertices, (*vertices[1:], vertices[0]))
    )
    area = abs(double_area) / 2.0
    if area <= TOLERANCE:
        raise ValueError("Polygon area must be greater than zero.")
    return area


def signed_polygon_area(vertices: Sequence[Point]) -> float:
    if len(vertices) < 3:
        raise ValueError("A polygon needs at least three vertices.")
    return sum(
        x1 * y2 - x2 * y1
        for (x1, y1), (x2, y2) in zip(vertices, (*vertices[1:], vertices[0]))
    ) / 2.0


def calculate_maximum_occupancy(area_m2: float, lot_kind: str) -> dict[str, float | str]:
    """Apply NBCP Section 708(a) lot-occupancy ceilings as scenarios."""
    if not math.isfinite(area_m2) or area_m2 <= 0:
        raise ValueError("Lot area must be a finite positive number.")
    factors = {"corner": 0.90, "inside": 0.80}
    if lot_kind not in factors:
        raise ValueError("lot_kind must be either 'corner' or 'inside'.")
    factor = factors[lot_kind]
    maximum = area_m2 * factor
    return {
        "lot_kind": lot_kind,
        "factor": factor,
        "maximum_occupancy_m2": maximum,
        "minimum_open_space_m2": area_m2 - maximum,
    }


def calculate_preliminary_parking_slots(area_m2: float) -> int | None:
    """Return the Table VII.4 preliminary slot count for a lot above 120 m².

    This scoped rule covers the project's current lot-area range only. It is
    not a complete replacement for the full table or local OBO review.
    """
    if not math.isfinite(area_m2) or area_m2 <= 0:
        raise ValueError("Lot area must be a finite positive number.")
    return 1 if area_m2 > 120.0 else None


def parking_slot_geometry(orientation: str = "perpendicular") -> dict[str, float | str]:
    """Return the 2004 NBCP Revised IRR minimum car-slot dimensions.

    Dimensions are the nominal slot rectangle only. They do not include a
    driveway, turning space, garage wall thickness, or access aisle.
    """
    options = {
        "perpendicular": {"width_m": 2.50, "length_m": 5.00},
        "diagonal": {"width_m": 2.50, "length_m": 5.00},
        "parallel": {"width_m": 2.15, "length_m": 6.00},
    }
    if orientation not in options:
        raise ValueError("orientation must be 'perpendicular', 'diagonal', or 'parallel'.")
    dimensions = options[orientation]
    return {
        "orientation": orientation,
        "width_m": dimensions["width_m"],
        "length_m": dimensions["length_m"],
        "area_m2": dimensions["width_m"] * dimensions["length_m"],
    }


def _validate_convex_polygon(vertices: Sequence[Point]) -> float:
    if len(vertices) < 3:
        raise ValueError("A polygon needs at least three vertices.")
    orientation = signed_polygon_area(vertices)
    if abs(orientation) <= TOLERANCE:
        raise ValueError("Polygon area must be greater than zero.")
    turns: list[float] = []
    for p0, p1, p2 in zip(
        vertices, (*vertices[1:], vertices[0]), (*vertices[2:], vertices[0], vertices[1])
    ):
        cross = (p1[0] - p0[0]) * (p2[1] - p1[1]) - (p1[1] - p0[1]) * (p2[0] - p1[0])
        if abs(cross) > TOLERANCE:
            turns.append(cross)
    if not turns or not (all(v > 0 for v in turns) or all(v < 0 for v in turns)):
        raise ValueError("Setback clipping currently requires a convex polygon.")
    return orientation


def inset_convex_polygon(vertices: Sequence[Point], offsets_m: Sequence[float]) -> list[Point]:
    """Clip a convex lot polygon by edge-parallel setback half-planes.

    Each offset is measured inward from the corresponding polygon edge.
    Vertices must be consistently ordered and offsets align with each edge.
    """
    if len(vertices) != len(offsets_m):
        raise ValueError("Provide exactly one setback offset for every polygon edge.")
    orientation = _validate_convex_polygon(vertices)
    for offset in offsets_m:
        if offset is None or not math.isfinite(float(offset)) or float(offset) < 0:
            raise ValueError("Setback offsets must be finite, non-negative numbers.")

    polygon = [(float(x), float(y)) for x, y in vertices]
    sign = 1.0 if orientation > 0 else -1.0
    for index, (edge_start, edge_end) in enumerate(zip(vertices, (*vertices[1:], vertices[0]))):
        ax, ay = edge_start
        bx, by = edge_end
        dx, dy = bx - ax, by - ay
        length = math.hypot(dx, dy)
        if length <= TOLERANCE:
            raise ValueError("Polygon contains a zero-length edge.")
        nx, ny = sign * (-dy / length), sign * (dx / length)
        offset = float(offsets_m[index])

        def signed_distance(point: Point) -> float:
            return (point[0] - ax) * nx + (point[1] - ay) * ny - offset

        if not polygon:
            break
        clipped: list[Point] = []
        start = polygon[-1]
        start_distance = signed_distance(start)
        start_inside = start_distance >= -TOLERANCE
        for end in polygon:
            end_distance = signed_distance(end)
            end_inside = end_distance >= -TOLERANCE
            if start_inside != end_inside:
                denominator = start_distance - end_distance
                if abs(denominator) > TOLERANCE:
                    fraction = start_distance / denominator
                    clipped.append((
                        start[0] + fraction * (end[0] - start[0]),
                        start[1] + fraction * (end[1] - start[1]),
                    ))
            if end_inside:
                clipped.append(end)
            start = end
            start_distance = end_distance
            start_inside = end_inside
        polygon = clipped

    if len(polygon) < 3:
        return []
    cleaned: list[Point] = []
    for point in polygon:
        if not cleaned or math.dist(point, cleaned[-1]) > TOLERANCE:
            cleaned.append(point)
    if len(cleaned) > 1 and math.dist(cleaned[0], cleaned[-1]) <= TOLERANCE:
        cleaned.pop()
    if len(cleaned) < 3 or polygon_area(cleaned) <= TOLERANCE:
        return []
    return cleaned


def resolve_buildable_envelope(
    vertices: Sequence[Point], offsets_m: Sequence[float | None]
) -> dict:
    """Calculate the working inset when all instructor-activity offsets are supplied."""
    if len(vertices) != len(offsets_m):
        raise ValueError("Provide one geometry offset for every boundary course.")
    missing = [
        index for index, value in enumerate(offsets_m)
        if value is None or str(value).strip() == ""
    ]
    if missing:
        return {
            "vertices": None,
            "area_m2": None,
            "status": f"Incomplete: missing final setback offsets for boundary edge(s) {', '.join(str(i + 1) for i in missing)}",
            "missing_edge_indices": missing,
        }
    envelope_vertices = inset_convex_polygon(vertices, [float(value) for value in offsets_m])
    if not envelope_vertices:
        return {
            "vertices": [],
            "area_m2": 0.0,
            "status": "No remaining envelope at the supplied setbacks",
            "missing_edge_indices": [],
        }
    return {
        "vertices": envelope_vertices,
        "area_m2": polygon_area(envelope_vertices),
        "status": "Working academic envelope calculated from all five supplied property-boundary offsets",
        "missing_edge_indices": [],
    }


def calculate_preliminary_envelope_scenarios(vertices: Sequence[Point]) -> list[dict]:
    """Calculate reproducible geometry scenarios while the applicable yard rule is unresolved.

    Offset order follows EXPECTED_COURSES: 1-2, 2-3, 3-4, 4-5,
    5-1 adjusted to close. Every offset is measured inward from the plotted
    parcel boundary, not from the roadway centerline.
    """
    definitions = [
        {
            "scenario_id": "A",
            "label": "2.00 m on all parcel edges (working baseline for Phase 3)",
            "offsets_m": [2.0, 2.0, 2.0, 2.0, 2.0],
        },
        {
            "scenario_id": "B",
            "label": "4.50 m candidate yard on road edge 3-4 only",
            "offsets_m": [2.0, 2.0, 4.5, 2.0, 2.0],
        },
        {
            "scenario_id": "C",
            "label": "4.50 m candidate yard on road edge 4-5 only",
            "offsets_m": [2.0, 2.0, 2.0, 4.5, 2.0],
        },
        {
            "scenario_id": "D",
            "label": "4.50 m candidate yards on both road edges",
            "offsets_m": [2.0, 2.0, 4.5, 4.5, 2.0],
        },
    ]
    results: list[dict] = []
    for definition in definitions:
        clipped = inset_convex_polygon(vertices, definition["offsets_m"])
        results.append({
            **definition,
            "vertices": clipped,
            "area_m2": polygon_area(clipped) if clipped else 0.0,
        })
    return results


def build_preliminary_envelope_scenarios_report(vertices: Sequence[Point]) -> str:
    """Build an auditable report for geometry scenarios, not a final setback ruling."""
    scenarios = calculate_preliminary_envelope_scenarios(vertices)
    lines = [
        "# Preliminary Building Envelope Scenarios",
        "",
        "**Project:** CE 393 Plate No. 2, Lot 245-B, Barangay San Isidro, Palo, Leyte  ",
        "**Status:** Geometry comparison only. No scenario below is adopted as the final legal setback rule.",
        "",
        "## 1. Confirmed project geometry",
        "",
        "- Adjusted closed-polygon area: 265.2598 m² (reported as 265.26 m²).",
        "- Road cross-section per instructor: 8.00 m total RROW = 1.50 m side strip + 5.00 m carriageway + 1.50 m side strip.",
        "- Road-frontage courses: 3-4 (southeast) and 4-5 (southwest).",
        "- Polygon vertex coordinates are local metres from P1=(0,0), not georeferenced survey coordinates.",
        "",
        "## 2. Preliminary setback geometry scenarios",
        "",
        "| Scenario | Edge 1-2 | Edge 2-3 | Road edge 3-4 | Road edge 4-5 | Edge 5-1 | Inset polygon area | Status |",
        "|---|---:|---:|---:|---:|---:|---:|---|",
    ]
    for scenario in scenarios:
        offsets = scenario["offsets_m"]
        if scenario["scenario_id"] == "A":
            status = "Selected working envelope for Phase 3"
        else:
            status = "Sensitivity comparison only"
        lines.append(
            f"| {scenario['scenario_id']} | {offsets[0]:.2f} m | {offsets[1]:.2f} m | "
            f"{offsets[2]:.2f} m | {offsets[3]:.2f} m | {offsets[4]:.2f} m | "
            f"{scenario['area_m2']:.2f} m² | {status} |"
        )
    lines += [
        "",
        "For this instructor-led activity, Scenario A is adopted as the working envelope for Phase 3. Scenarios B-D are retained only as sensitivity comparisons and are not used for the working room layout.",
        "",
        "### Inner polygon vertices for drafting comparison",
        "",
        "Each row is one vertex of the clipped inset polygon in sequence. The S1-S5 labels are local scenario vertices, not the original property monuments. Coordinates are in metres (x=easting, y=northing) and retain the Phase 1 local coordinate system.",
        "",
    ]
    for scenario in scenarios:
        lines += [
            f"#### Scenario {scenario['scenario_id']}: {scenario['label']}",
            "",
            "| Inset vertex | Local x (m) | Local y (m) |",
            "|---|---:|---:|",
        ]
        for index, (x, y) in enumerate(scenario["vertices"], start=1):
            lines.append(f"| S{index} | {x:.6f} | {y:.6f} |")
        lines.append("")
    lines += [
        "## 3. Working setback basis for this activity",
        "",
        "1. **PD 1096 Section 708(a):** use the Group A dwelling baseline of at least 2.00 m from the property line, subject to Civil Code easements of light and view. For this classroom activity, the same 2.00 m offset is used as the working setback on all five plotted parcel edges.",
        "2. **Road measurement reference:** all offsets in the scenario and the working envelope are measured inward from the plotted property boundaries. The road cross-section remains as given by the instructor: 8.00 m total RROW, comprising 5.00 m carriageway and 1.50 m strip on each side.",
        "3. **Alternative comparisons:** the 4.50 m values in Scenarios B-D are shown for comparison only. They are not used for the working Phase 3 envelope in this activity.",
        "4. **Lot geometry:** the working envelope follows the adjusted Phase 1 polygon, which preserves courses 1-2 through 4-5 and uses the instructor-directed adjusted closing course P5-1.",
        "",
        "The project will proceed using the instructor-provided assignment values and this documented 2.00 m working setback basis. The selected inset is an academic planning envelope, not a surveyed boundary or construction certification.",
        "",
        "## 4. Working envelope selected for Phase 3",
        "",
        "**Scenario A is selected as the working envelope for Phase 3.** The inset area is **152.43 m²** using a 2.00 m property-boundary offset on each of the five edges. The lot description gives road frontage on the southeast and southwest, so the 90% corner-lot occupancy scenario is used for the working comparison: 238.73 m² maximum occupied area, which is larger than the inset envelope. The building footprint will be placed within the 152.43 m² working envelope and may be smaller to accommodate parking, access, light, ventilation, and the required spaces.",
        "",
        "## 5. References",
        "",
        "- [PD 1096, National Building Code of the Philippines, Sections 704(a) and 708(a), Supreme Court E-Library](https://elibrary.judiciary.gov.ph/thebookshelf/showdocs/11/53320).",
        "- [DPWH Department Order No. 056, s. 2016, official PDF containing the Table VIII.2 note](https://www.dpwh.gov.ph/dpwh/sites/default/files/issuances/DO_056_s2016.pdf).",
        "- [2004 Revised IRR of PD 1096, PRBoA-hosted copy](https://www.architectureboard.com.ph/wp-content/uploads/2019/09/1.12-PD1096_-2004revIRR_PRBoA-unofcl-versnw08annotns.pdf). The 4.50 m comparison is not used as the working layout assumption in this activity.",
        "",
        "**Use limit:** Preliminary academic calculations only. The source traverse is an adjusted plotting basis, not a cadastral certification. Do not use these scenarios for setting out or construction.",
        "",
    ]
    return "\n".join(lines)


def _number(value: str, field: str, course: str) -> float:
    try:
        result = float(value)
    except (TypeError, ValueError) as exc:
        raise ValueError(f"Invalid numeric field {field!r} for course {course!r}.") from exc
    if not math.isfinite(result):
        raise ValueError(f"Non-finite numeric field {field!r} for course {course!r}.")
    return result


def load_traverse(traverse_path: Path) -> dict:
    if not traverse_path.is_file():
        raise FileNotFoundError(f"Traverse CSV not found: {traverse_path}")
    with traverse_path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        rows = list(reader)
        required = {
            "course", "distance_m", "start", "end", "start_easting_m",
            "start_northing_m", "end_easting_m", "end_northing_m",
        }
        if not reader.fieldnames or not required.issubset(reader.fieldnames):
            raise ValueError("Traverse CSV is missing required columns.")
    by_course = {row["course"].strip(): row for row in rows}
    missing = [course for course in EXPECTED_COURSES if course not in by_course]
    if missing:
        raise ValueError(f"Traverse CSV is missing required course(s): {', '.join(missing)}")
    ordered = [by_course[course] for course in EXPECTED_COURSES]
    vertices: list[Point] = []
    for row in ordered:
        vertices.append((
            _number(row["start_easting_m"], "start_easting_m", row["course"]),
            _number(row["start_northing_m"], "start_northing_m", row["course"]),
        ))
    for current, following in zip(ordered, ordered[1:]):
        end = (
            _number(current["end_easting_m"], "end_easting_m", current["course"]),
            _number(current["end_northing_m"], "end_northing_m", current["course"]),
        )
        next_start = (
            _number(following["start_easting_m"], "start_easting_m", following["course"]),
            _number(following["start_northing_m"], "start_northing_m", following["course"]),
        )
        if math.dist(end, next_start) > TOLERANCE:
            raise ValueError(f"Coordinate discontinuity between {current['course']} and {following['course']}.")
    closing = ordered[-1]
    final_point = (
        _number(closing["end_easting_m"], "end_easting_m", closing["course"]),
        _number(closing["end_northing_m"], "end_northing_m", closing["course"]),
    )
    if math.dist(final_point, vertices[0]) > TOLERANCE:
        raise ValueError("Adjusted traverse does not close at P1.")
    area = polygon_area(vertices)
    perimeter = sum(_number(row["distance_m"], "distance_m", row["course"]) for row in ordered)
    return {
        "rows": rows, "ordered_rows": ordered, "vertices": vertices,
        "area_m2": area, "perimeter_m": perimeter,
    }


def load_boundary_inputs(setback_path: Path) -> list[dict]:
    if not setback_path.is_file():
        raise FileNotFoundError(f"Setback input CSV not found: {setback_path}")
    with setback_path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        required = {
            "boundary_course", "adjacency", "edge_type", "code_clearance_m",
            "geometry_inset_m", "reference_line", "status", "basis", "notes",
        }
        if not reader.fieldnames or not required.issubset(reader.fieldnames):
            raise ValueError("Setback input CSV is missing required columns.")
        rows = [dict(row) for row in reader]
    if [row["boundary_course"] for row in rows] != list(EXPECTED_COURSES):
        raise ValueError("Setback input rows must match Phase 1 boundary-course order exactly.")
    for row in rows:
        raw_offset = row["geometry_inset_m"].strip()
        row["geometry_inset_m"] = (
            None if not raw_offset else
            _number(raw_offset, "geometry_inset_m", row["boundary_course"])
        )
        row["code_clearance_m"] = _number(
            row["code_clearance_m"], "code_clearance_m", row["boundary_course"]
        )
        if row["code_clearance_m"] < 0 or (
            row["geometry_inset_m"] is not None and row["geometry_inset_m"] < 0
        ):
            raise ValueError(f"Setback distances cannot be negative for course {row['boundary_course']}.")
    return rows


def load_code_requirements(requirements_path: Path) -> list[dict[str, str]]:
    """Validate the traceability CSV used to track supported and pending rules."""
    if not requirements_path.is_file():
        raise FileNotFoundError(f"Code requirements CSV not found: {requirements_path}")
    required_columns = {
        "requirement_id", "topic", "legal_or_assignment_basis",
        "requirement_or_given_value", "project_application",
        "calculation_or_action", "status", "source_url", "limitations",
    }
    with requirements_path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        if not reader.fieldnames or not required_columns.issubset(reader.fieldnames):
            raise ValueError("Code requirements CSV is missing required columns.")
        rows = list(reader)
    if not rows:
        raise ValueError("Code requirements CSV has no requirement rows.")
    seen: set[str] = set()
    for line_no, row in enumerate(rows, start=2):
        if None in row:
            raise ValueError(f"Code requirements CSV line {line_no} has extra unquoted fields.")
        if any(row.get(column) is None for column in required_columns):
            raise ValueError(f"Code requirements CSV line {line_no} has missing fields.")
        requirement_id = row["requirement_id"].strip()
        if not requirement_id:
            raise ValueError(f"Code requirements CSV line {line_no} has an empty requirement ID.")
        if requirement_id in seen:
            raise ValueError(f"Duplicate requirement ID in code requirements CSV: {requirement_id}")
        seen.add(requirement_id)
        if not row["topic"].strip() or not row["status"].strip():
            raise ValueError(f"Code requirements CSV line {line_no} must include topic and status.")
        if not row["source_url"].strip() and row["status"].strip().lower() != "pending":
            raise ValueError(f"Requirement {requirement_id} needs a source URL or a pending status.")
    expected_ids = {f"P2-{index:02d}" for index in range(1, 13)}
    missing_ids = sorted(expected_ids - seen)
    unexpected_ids = sorted(seen - expected_ids)
    if missing_ids:
        raise ValueError(f"Code requirements CSV is missing requirement ID(s): {', '.join(missing_ids)}")
    if unexpected_ids:
        raise ValueError(f"Code requirements CSV has unexpected requirement ID(s): {', '.join(unexpected_ids)}")
    return rows


def build_phase2_report(
    *, area_m2: float, stated_approximate_area_m2: float,
    perimeter_m: float, boundary_rows: Sequence[dict],
    corner_occupancy: dict, inside_occupancy: dict,
    envelope: dict, parking_slots: int | None = None,
) -> str:
    difference = stated_approximate_area_m2 - area_m2
    lines = [
        "# Phase 2 Site Requirements and Preliminary Calculations",
        "",
        "**Project:** Proposed Two-Storey Residential Building, CE 393 Plate No. 2  ",
        "**Status:** Preliminary code review and calculation workflow. This is not a permit determination or a surveyed site-development plan.",
        "",
        "## 1. Verified geometry inputs",
        "",
        "| Item | Result | Status |",
        "|---|---:|---|",
        f"| Approximate area stated in the assignment | {stated_approximate_area_m2:.2f} m² | GIVEN (approximate) |",
        f"| Area of adjusted, closed Phase 1 polygon | {area_m2:.2f} m² | CALCULATED from Phase 1 coordinate schedule |",
        f"| Difference (assignment approximate minus calculated polygon) | {difference:.2f} m² | RECORDED, not reconciled by changing the traverse |",
        f"| Adjusted closed-polygon perimeter | {perimeter_m:.4f} m | CALCULATED |",
        "",
        "The adjusted traverse remains an academic plotting basis under the instructor's direction. The first four courses are unchanged, and only P5-1 is adjusted. The approximate 300.00 m² brief value is preserved separately; it is not used to overwrite the calculated 265.26 m² polygon area.",
        "",
        "## 2. Setback review by boundary",
        "",
        "For this instructor-led academic activity, use the PD 1096 Section 708(a) Group A dwelling baseline of 2.00 m inward from each plotted property boundary. The instructor's road cross-section is 8.00 m total RROW = 5.00 m carriageway + 1.50 m strip on each side. The same 2.00 m property-boundary offset is used on road-facing courses 3-4 and 4-5 as the working drafting assumption for this plate.",
        "",
        "| Boundary | Adjoining feature | Code baseline | Geometry offset used? | Status / reason |",
        "|---|---|---:|---:|---|",
    ]
    for row in boundary_rows:
        code = f"{row['code_clearance_m']:.2f} m" if row["code_clearance_m"] is not None else "PENDING"
        offset = f"{row['geometry_inset_m']:.2f} m" if row["geometry_inset_m"] is not None else "NO"
        reason = row["notes"].replace("|", "\\|")
        lines.append(
            f"| {row['boundary_course']} | {row['adjacency']} | {code} | {offset} | "
            f"{row['status']}: {reason} |"
        )
    lines += [
        "",
        "**Working assumption for this activity:** use the 2.00 m property-boundary offset on all five courses for the preliminary envelope and Phase 3 layout. The 4.50 m variants remain comparison scenarios only and are not used in the working layout.",
        "",
        "## 3. Lot occupancy and minimum open-space scenarios",
        "",
        "For this activity, use the **265.26 m² adjusted-polygon area** for the occupancy comparison. The lot description gives road frontage along both the southeast and southwest edges, so use the corner-lot 90% occupancy scenario for the working comparison and retain the 80% inside-lot scenario for reference.",
        "",
        "| Classification scenario | Maximum occupancy factor | Maximum occupied area | Corresponding minimum open area |",
        "|---|---:|---:|---:|",
        f"| Corner lot (provisional) | {corner_occupancy['factor']:.0%} | {corner_occupancy['maximum_occupancy_m2']:.2f} m² | {corner_occupancy['minimum_open_space_m2']:.2f} m² |",
        f"| Inside lot (comparison only) | {inside_occupancy['factor']:.0%} | {inside_occupancy['maximum_occupancy_m2']:.2f} m² | {inside_occupancy['minimum_open_space_m2']:.2f} m² |",
        "",
        "These are occupancy ceilings, not the proposed building footprint. For the working site layout, the 152.43 m² inset envelope is the tighter geometric limit than the 238.73 m² corner-lot occupancy ceiling. Building footprint and remaining open space will be calculated after the room layout is arranged.",
        "",
        "## 4. Buildable-envelope calculation",
        "",
    ]
    if envelope["area_m2"] is None:
        lines += [
            "**WORKING ACADEMIC ENVELOPE NOT YET COMPUTED.** The instructor-provided cross-section (8.00 m total RROW = 5.00 m carriageway + 1.50 m strip on each side) is known and used in the site drawing. The project input table should contain the adopted 2.00 m working offset for all five property-boundary edges.",
            "",
            f"Envelope status: {envelope['status']}.",
            "",
            "Once all five working offsets are entered, this report reports the inset area for the Phase 3 layout. The instructor-provided 1.50 m / 5.00 m / 1.50 m RROW allocation is settled and is not a pending input.",
        ]
    elif envelope["area_m2"] == 0:
        lines += ["**NOT FEASIBLE at the supplied offsets.** The setback lines leave no polygonal buildable envelope."]
    else:
        lines += [
            f"Calculated inset-envelope area: **{envelope['area_m2']:.2f} m²**.",
            f"Envelope status: {envelope['status']}.",
            "This remains a geometric result for the supplied offsets, not a building permit or professional survey determination.",
        ]
    lines += [
        "",
        "## 5. Other preliminary requirements",
        "",
        "| Item | Current finding | Status |",
        "|---|---|---|",
        f"| Parking demand | {f'{parking_slots} off-street, on-site slot used as the working assumption for a single-family dwelling under Group A / Division A-1' if parking_slots is not None else 'Pending lot/use classification and current parking-table verification'} | PRELIMINARY ACTIVITY BASIS |",
        "| Standard car-slot size | 2.50 m × 5.00 m = 12.50 m² for perpendicular/diagonal parking; parallel option 2.15 m × 6.00 m = 12.90 m² | 2004 Revised IRR Rule VII, parking dimensions; slot must be outside RROW |",
        "| Driveway, maneuvering and garage clearances | Not included in the rectangle-area calculation | PENDING layout and applicable access checks |",
        "| Occupant load | Assignment gives 5–6 proposed occupants; code occupant load still requires the applicable floor area / method and occupancy classification | PENDING |",
        "| Building footprint | Must be selected after setback envelope and preliminary room arrangement are coordinated | PENDING |",
        "| Ground-floor area | Requires the dimensioned ground-floor plan | PENDING |",
        "| Second-floor area | Requires the dimensioned second-floor plan | PENDING |",
        "| Total floor area | Ground-floor area + second-floor area | PENDING |",
        "| Remaining open space after footprint | Adjusted lot area minus the final footprint; distinct from minimum open-space scenario above | PENDING |",
        "| Stair / other dimensions | Requires floor-to-floor height, building layout, and applicable code checks | PENDING |",
        "",
        "## 6. Code and reference basis",
        "",
        "1. [Presidential Decree No. 1096, National Building Code of the Philippines, Section 704(a) and Section 708(a)](https://elibrary.judiciary.gov.ph/thebookshelf/showdocs/11/53320). Section 708(a) supplies the Group A dwelling baseline distance and corner-/inside-lot occupancy ceilings; Section 704(a) supplies the street-centerline rule.",
        "2. [DPWH National Building Code Development Office documents](https://dpwh.architectureboard.com.ph/documents/), including the 2004 Revised Implementing Rules and Regulations of PD 1096, used here as the academic reference basis for the preliminary parking calculation.",
        "3. [DPWH Department Order No. 056, s. 2016 (official PDF)](https://www.dpwh.gov.ph/dpwh/sites/default/files/issuances/DO_056_s2016.pdf), Annex provision containing Table VIII.2; its note limits the listed residential setback table to newly developed subdivisions.",
        "4. [Civil Code of the Philippines, Article 670 and related easement provisions](https://elibrary.judiciary.gov.ph/thebookshelf/showdocs/2/53360).",
        "5. [2004 Revised Implementing Rules and Regulations of PD 1096, Rule VII parking requirements (copy hosted by the Professional Regulatory Board of Architecture)](https://www.architectureboard.com.ph/wp-content/uploads/2019/09/1.12-PD1096_-2004revIRR_PRBoA-unofcl-versnw08annotns.pdf). The parking table indicates at least one on-site off-street slot for a single-family dwelling lot above 120.00 m²; the slot dimensions are 2.50 m × 5.00 m for perpendicular/diagonal or 2.15 m × 6.00 m for parallel parking.",
        "",
        "## 7. Inputs still required before finalizing Phase 2",
        "",
        "- Proposed footprint, room dimensions, total floor areas, and remaining open space after the floor layout is developed.",
        "- Occupant-load and stair calculations using the coordinated floor plan and floor-to-floor height.",
        "- Parking-space placement, driveway, and garage/carport layout coordinated with the working envelope.",
        "- Final consistency check of site plan, floor plans, and the instructor's submission checklist.",
        "",
        "**Limit:** This academic worksheet is not a site survey, legal zoning determination, permit-ready design, or certification of code compliance. Do not use the provisional numbers to build.",
        "",
    ]
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--traverse", type=Path, default=DEFAULT_TRAVERSE)
    parser.add_argument("--setbacks", type=Path, default=DEFAULT_SETBACKS)
    parser.add_argument("--requirements", type=Path, default=DEFAULT_REQUIREMENTS)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--write-report", type=Path, help="Write the generated Markdown report to this path.")
    mode.add_argument("--check-report", type=Path, help="Fail if the report file differs from generated output.")
    scenario_mode = parser.add_mutually_exclusive_group()
    scenario_mode.add_argument(
        "--write-scenarios-report", type=Path,
        help="Write the generated preliminary envelope-scenarios Markdown report.",
    )
    scenario_mode.add_argument(
        "--check-scenarios-report", type=Path,
        help="Fail if the envelope-scenarios report differs from generated output.",
    )
    args = parser.parse_args()
    try:
        traverse = load_traverse(args.traverse)
        boundary_rows = load_boundary_inputs(args.setbacks)
        requirement_rows = load_code_requirements(args.requirements)
        offsets = [row["geometry_inset_m"] for row in boundary_rows]
        envelope = resolve_buildable_envelope(traverse["vertices"], offsets)
        corner = calculate_maximum_occupancy(traverse["area_m2"], "corner")
        inside = calculate_maximum_occupancy(traverse["area_m2"], "inside")
        parking_slots = calculate_preliminary_parking_slots(traverse["area_m2"])
        report = build_phase2_report(
            area_m2=traverse["area_m2"], stated_approximate_area_m2=300.0,
            perimeter_m=traverse["perimeter_m"], boundary_rows=boundary_rows,
            corner_occupancy=corner, inside_occupancy=inside,
            envelope=envelope, parking_slots=parking_slots,
        )
        scenarios_report = build_preliminary_envelope_scenarios_report(traverse["vertices"])
        if args.write_scenarios_report:
            args.write_scenarios_report.parent.mkdir(parents=True, exist_ok=True)
            args.write_scenarios_report.write_text(scenarios_report, encoding="utf-8")
            print(f"WROTE: {args.write_scenarios_report}")
        elif args.check_scenarios_report:
            if not args.check_scenarios_report.is_file():
                raise FileNotFoundError(f"Scenario report not found: {args.check_scenarios_report}")
            existing_scenarios = args.check_scenarios_report.read_text(encoding="utf-8")
            if existing_scenarios != scenarios_report:
                print(
                    f"FAIL: {args.check_scenarios_report} is out of date; regenerate it with --write-scenarios-report.",
                    file=sys.stderr,
                )
                return 1
            print(f"PASS: {args.check_scenarios_report} matches the current geometry and scenario rules.")
        if args.write_report:
            args.write_report.parent.mkdir(parents=True, exist_ok=True)
            args.write_report.write_text(report, encoding="utf-8")
            print(f"WROTE: {args.write_report}")
        elif args.check_report:
            if not args.check_report.is_file():
                raise FileNotFoundError(f"Report not found: {args.check_report}")
            existing = args.check_report.read_text(encoding="utf-8")
            if existing != report:
                print(f"FAIL: {args.check_report} is out of date; regenerate it with --write-report.", file=sys.stderr)
                return 1
            print(f"PASS: {args.check_report} matches the current source inputs.")
        else:
            print(report, end="")
        print(f"INFO: validated {len(requirement_rows)} traceable Phase 2 code/assignment requirements.")
        print(f"INFO: adjusted polygon area = {traverse['area_m2']:.4f} m²; perimeter = {traverse['perimeter_m']:.4f} m.")
        print(f"INFO: corner occupancy scenario = {corner['maximum_occupancy_m2']:.2f} m²; inside-lot scenario = {inside['maximum_occupancy_m2']:.2f} m².")
        envelope_text = "NOT CALCULATED (final road-side setbacks unresolved)" if envelope["area_m2"] is None else f"{envelope['area_m2']:.2f} m²"
        print(f"INFO: final buildable envelope = {envelope_text}.")
        for scenario in calculate_preliminary_envelope_scenarios(traverse["vertices"]):
            print(f"INFO: preliminary envelope scenario {scenario['scenario_id']} = {scenario['area_m2']:.2f} m² ({scenario['label']}).")
        return 0
    except (FileNotFoundError, ValueError, OSError) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
