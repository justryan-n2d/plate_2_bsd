#!/usr/bin/env python3
"""Validate Phase 2 setback screening scenarios against the repository's source data."""

from __future__ import annotations

import csv
import json
import math
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SITE_CSV = ROOT / "site" / "phase1_traverse_coordinates.csv"
SCENARIOS_CSV = ROOT / "site" / "phase2_setback_scenarios.csv"
MODEL_JSON = ROOT / "data" / "building_model.json"
PREVIEW_SVG = ROOT / "previews" / "phase2_setback_scenarios.svg"
EDGE_FIELDS = ("setback_1_2_m", "setback_2_3_m", "setback_3_4_m", "setback_4_5_m", "setback_5_1_m")
EXPECTED = {
    "S-01": (152.4309, "YES", "YES"),
    "S-02": (128.9837, "YES", "NO"),
    "S-03": (128.8989, "NO", "NO"),
    "S-04": (112.6268, "NO", "NO"),
}


def fail(message: str) -> None:
    raise ValueError(message)


def area(poly: list[tuple[float, float]]) -> float:
    return abs(sum(x1 * y2 - x2 * y1 for (x1, y1), (x2, y2) in zip(poly, poly[1:] + poly[:1])) / 2.0)


def cross(a: tuple[float, float], b: tuple[float, float]) -> float:
    return a[0] * b[1] - a[1] * b[0]


def load_traverse() -> list[tuple[float, float]]:
    if not SITE_CSV.is_file():
        fail(f"Missing source traverse CSV: {SITE_CSV}")
    with SITE_CSV.open("r", encoding="utf-8-sig", newline="") as handle:
        rows = {row["course"]: row for row in csv.DictReader(handle)}
    course_names = ("1-2", "2-3", "3-4", "4-5")
    if any(name not in rows for name in course_names):
        fail("The four unchanged traverse course rows are missing")
    first = rows["1-2"]
    points = [(float(first["start_easting_m"]), float(first["start_northing_m"]))]
    for course in course_names:
        row = rows[course]
        points.append((float(row["end_easting_m"]), float(row["end_northing_m"])))
    return points[:5]


def offset_polygon(poly: list[tuple[float, float]], setbacks: list[float]) -> list[tuple[float, float]]:
    """Intersect adjacent lines shifted inward by the perpendicular setback."""
    if len(poly) != len(setbacks) or len(poly) < 3:
        fail("Polygon/setback side counts do not match")
    orientation = 1.0 if sum(
        x1 * y2 - x2 * y1 for (x1, y1), (x2, y2) in zip(poly, poly[1:] + poly[:1])
    ) > 0 else -1.0
    lines: list[tuple[tuple[float, float], tuple[float, float]]] = []
    for i, p in enumerate(poly):
        q = poly[(i + 1) % len(poly)]
        dx, dy = q[0] - p[0], q[1] - p[1]
        length = math.hypot(dx, dy)
        if length <= 0:
            fail("Zero-length boundary segment")
        nx, ny = -dy / length * orientation, dx / length * orientation
        distance = setbacks[i]
        lines.append(((p[0] + distance * nx, p[1] + distance * ny), (dx, dy)))

    result = []
    for i in range(len(lines)):
        p, v = lines[(i - 1) % len(lines)]
        q, w = lines[i]
        denominator = cross(v, w)
        if abs(denominator) < 1e-10:
            fail("Adjacent offset lines are parallel; offset polygon is degenerate")
        qmp = (q[0] - p[0], q[1] - p[1])
        t = cross(qmp, w) / denominator
        result.append((p[0] + t * v[0], p[1] + t * v[1]))
    return result


def point_in_polygon(point: tuple[float, float], poly: list[tuple[float, float]]) -> bool:
    x, y = point
    inside = False
    for (x1, y1), (x2, y2) in zip(poly, poly[1:] + poly[:1]):
        if (y1 > y) != (y2 > y):
            x_cross = (x2 - x1) * (y - y1) / (y2 - y1) + x1
            if x < x_cross:
                inside = not inside
    return inside


def placement_fits(placement: dict, poly: list[tuple[float, float]]) -> bool:
    x = float(placement["southwest_easting_m"])
    y = float(placement["south_edge_northing_m"])
    width = float(placement["width_m"])
    depth = float(placement["depth_m"])
    corners = [(x, y), (x + width, y), (x + width, y + depth), (x, y + depth)]
    return all(point_in_polygon(corner, poly) for corner in corners)


def load_scenarios() -> list[dict[str, str]]:
    if not SCENARIOS_CSV.is_file():
        fail(f"Missing scenario CSV: {SCENARIOS_CSV}")
    with SCENARIOS_CSV.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        required = {
            "scenario_id", "scenario_name", *EDGE_FIELDS, "screening_envelope_area_m2",
            "current_house_rectangle_fits", "current_carport_rectangle_fits", "interpretation_limit",
        }
        missing = required - set(reader.fieldnames or [])
        if missing:
            fail(f"Scenario CSV is missing columns: {', '.join(sorted(missing))}")
        rows = list(reader)
    if len(rows) != len(EXPECTED):
        fail(f"Expected {len(EXPECTED)} scenarios; found {len(rows)}")
    return rows


def validate_scenarios(poly: list[tuple[float, float]], model: dict, rows: list[dict[str, str]]) -> None:
    seen = set()
    for row in rows:
        scenario_id = row["scenario_id"]
        if scenario_id not in EXPECTED or scenario_id in seen:
            fail(f"Unexpected or duplicate scenario id: {scenario_id}")
        seen.add(scenario_id)
        setbacks = [float(row[field]) for field in EDGE_FIELDS]
        if any(value < 0 for value in setbacks):
            fail(f"Negative setback in {scenario_id}")
        polygon = offset_polygon(poly, setbacks)
        calculated_area = area(polygon)
        target_area, expected_house, expected_carport = EXPECTED[scenario_id]
        if not math.isclose(calculated_area, target_area, rel_tol=0.0, abs_tol=0.05):
            fail(f"{scenario_id} area mismatch: calculated {calculated_area:.4f}, CSV {target_area:.4f}")
        if not math.isclose(calculated_area, float(row["screening_envelope_area_m2"]), rel_tol=0.0, abs_tol=0.05):
            fail(f"{scenario_id} CSV area does not match computed polygon")
        site = model["site"]
        house_fits = placement_fits(site["building_placement"], polygon)
        carport_fits = placement_fits(site["carport_placement"], polygon)
        if ("YES" if house_fits else "NO") != expected_house:
            fail(f"{scenario_id} house containment changed; revise the documented scenario table")
        if ("YES" if carport_fits else "NO") != expected_carport:
            fail(f"{scenario_id} carport containment changed; revise the documented scenario table")
        if row["current_house_rectangle_fits"] != expected_house or row["current_carport_rectangle_fits"] != expected_carport:
            fail(f"{scenario_id} CSV fit flag differs from the calculated containment result")
        if not row["interpretation_limit"].strip():
            fail(f"{scenario_id} has no explanatory limit")
    if seen != set(EXPECTED):
        fail("One or more expected scenario IDs are missing")


def validate_svg() -> None:
    if not PREVIEW_SVG.is_file():
        fail(f"Missing SVG preview: {PREVIEW_SVG}")
    try:
        root = ET.parse(PREVIEW_SVG).getroot()
    except ET.ParseError as exc:
        raise ValueError(f"Invalid SVG XML: {exc}") from exc
    if root.tag.rsplit("}", 1)[-1] != "svg":
        fail("Preview root must be an SVG element")
    text_values = [
        " ".join("".join(node.itertext()).split())
        for node in root.iter()
        if node.tag.rsplit("}", 1)[-1] in {"title", "desc", "text"}
    ]
    all_text = " ".join(text_values).lower()
    for scenario_id in EXPECTED:
        if scenario_id.lower() not in all_text:
            fail(f"Scenario preview is missing {scenario_id}")
    for phrase in ("screening only", "not a final", "house", "carport"):
        if phrase not in all_text:
            fail(f"Scenario preview is missing required disclaimer/label: {phrase}")


def main() -> int:
    model = json.loads(MODEL_JSON.read_text(encoding="utf-8"))
    poly = load_traverse()
    if not math.isclose(area(poly), float(model["site"]["adjusted_closed_traverse_area_m2"]), abs_tol=0.03):
        fail("Source traverse polygon area does not match the shared model area")
    rows = load_scenarios()
    validate_scenarios(poly, model, rows)
    validate_svg()
    print("PASS: source traverse area agrees with the shared model.")
    print("PASS: all four setback offset polygons and areas recalculate within tolerance.")
    print("PASS: current house/carport containment flags agree with polygon geometry.")
    print("PASS: setback scenario SVG parses and includes all scenario IDs and disclaimers.")
    print("NOTE: this checks geometry only; it does not determine the legally applicable local setbacks or certify code compliance.")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, ValueError, KeyError, TypeError, json.JSONDecodeError) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        raise SystemExit(1)
