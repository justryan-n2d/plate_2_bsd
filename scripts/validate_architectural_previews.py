#!/usr/bin/env python3
"""Validate Phase 5 preliminary architectural preview files and shared data."""

from __future__ import annotations

import json
import math
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODEL_PATH = ROOT / "data" / "building_model.json"
PREVIEW_DIR = ROOT / "previews"
DRAWINGS = {
    "phase5_A01_site_development.svg": "A-01",
    "phase5_A02_ground_floor.svg": "A-02",
    "phase5_A03_second_floor.svg": "A-03",
    "phase5_A04_roof_plan.svg": "A-04",
    "phase5_A05_elevations.svg": "A-05",
    "phase5_A06_sections.svg": "A-06",
    "phase5_A07_details_schedules.svg": "A-07",
}


def fail(message: str) -> None:
    raise ValueError(message)


def local_name(tag: str) -> str:
    return tag.rsplit("}", 1)[-1]


def signed_area(points: list[tuple[float, float]]) -> float:
    return sum(
        x1 * y2 - x2 * y1
        for (x1, y1), (x2, y2) in zip(points, points[1:] + points[:1])
    ) / 2.0


def point_in_polygon(point: tuple[float, float], polygon: list[tuple[float, float]]) -> bool:
    x, y = point
    inside = False
    for (x1, y1), (x2, y2) in zip(polygon, polygon[1:] + polygon[:1]):
        if (y1 > y) != (y2 > y):
            x_cross = (x2 - x1) * (y - y1) / (y2 - y1) + x1
            if x < x_cross:
                inside = not inside
    return inside


def polygon_area_from_json(items: list[dict[str, float]]) -> float:
    points = [(float(p["easting_m"]), float(p["northing_m"])) for p in items]
    if len(points) < 3:
        fail("The site geometry must have at least three vertices")
    return abs(signed_area(points))


def validate_model(data: dict) -> None:
    site = data["site"]
    building = data["building"]
    foot = building["footprint"]
    width = float(foot["width_m"])
    depth = float(foot["depth_m"])
    if width <= 0 or depth <= 0:
        fail("Building footprint dimensions must be positive")

    actual_lot = polygon_area_from_json(site["polygon_vertices"])
    recorded_lot = float(site["adjusted_closed_traverse_area_m2"])
    if not math.isclose(actual_lot, recorded_lot, rel_tol=0.0, abs_tol=0.02):
        fail(f"Building model lot-area mismatch: polygon={actual_lot:.4f}, recorded={recorded_lot:.4f}")

    screen = [(float(p["easting_m"]), float(p["northing_m"])) for p in site["setback_screening_polygon"]]
    screen_area = abs(signed_area(screen))
    if not math.isclose(screen_area, 152.43, rel_tol=0.0, abs_tol=0.05):
        fail(f"Unexpected 2 m screening polygon area: {screen_area:.4f} m²")

    for label, key in (("house", "building_placement"), ("carport", "carport_placement")):
        placement = site[key]
        x = float(placement["southwest_easting_m"])
        south = float(placement["south_edge_northing_m"])
        w = float(placement["width_m"])
        d = float(placement["depth_m"])
        corners = [
            (x, south),
            (x + w, south),
            (x + w, south + d),
            (x, south + d),
        ]
        if not all(point_in_polygon(c, screen) for c in corners):
            fail(f"Preliminary {label} footprint extends outside the 2 m screening polygon")

    calc_area = width * depth
    if not math.isclose(calc_area, float(site["main_footprint_area_m2"]), rel_tol=0.0, abs_tol=0.01):
        fail("Main footprint area does not match width x depth")
    carport_area = float(site["carport_placement"]["width_m"]) * float(site["carport_placement"]["depth_m"])
    if not math.isclose(carport_area, float(site["carport_area_m2"]), rel_tol=0.0, abs_tol=0.01):
        fail("Carport area does not match width x depth")
    combined = calc_area + carport_area
    if not math.isclose(combined, float(site["combined_covered_ground_area_m2"]), rel_tol=0.0, abs_tol=0.01):
        fail("Combined ground coverage arithmetic is inconsistent")

    # The balcony is an external projection, so validate it separately from enclosed room boxes.
    balcony = building.get("balcony")
    if not isinstance(balcony, dict) or balcony.get("status") != "required":
        fail("The shared model must include a required second-floor balcony")
    balcony_width = float(balcony["width_m"])
    balcony_projection = float(balcony["projection_m"])
    balcony_area = float(balcony["area_m2"])
    balcony_x = float(balcony["x_m"])
    balcony_y = float(balcony["y_m"])
    if min(balcony_width, balcony_projection, balcony_area) <= 0:
        fail("Balcony dimensions and area must be positive")
    if not math.isclose(balcony_width * balcony_projection, balcony_area, rel_tol=0.0, abs_tol=0.01):
        fail("Balcony area does not match width x projection")
    if not math.isclose(balcony_y, -balcony_projection, rel_tol=0.0, abs_tol=0.001):
        fail("Balcony should project outward from the upper edge of the second-floor plan")
    if balcony_x < 0 or balcony_x + balcony_width > width + 1e-6:
        fail("Balcony attachment span must fit along the nominal house facade")
    if balcony.get("attached_to") != "Master bedroom":
        fail("Balcony must be attached to the master bedroom for the current plan")

    north_edge = float(site["building_placement"]["south_edge_northing_m"]) + float(site["building_placement"]["depth_m"])
    base_x = float(site["building_placement"]["southwest_easting_m"])
    balcony_world = [
        (base_x + balcony_x, north_edge),
        (base_x + balcony_x + balcony_width, north_edge),
        (base_x + balcony_x + balcony_width, north_edge + balcony_projection),
        (base_x + balcony_x, north_edge + balcony_projection),
    ]
    if not all(point_in_polygon(point, screen) for point in balcony_world):
        fail("Balcony projection falls outside the selected S-01 academic setback envelope")

    for floor, rooms in building["rooms"].items():
        names: set[str] = set()
        for room in rooms:
            name = room["name"]
            if name in names:
                fail(f"Duplicate room name on {floor}: {name}")
            names.add(name)
            x, y = float(room["x_m"]), float(room["y_m"])
            rw, rd = float(room["width_m"]), float(room["depth_m"])
            area = float(room["target_area_m2"])
            if min(rw, rd, area) <= 0:
                fail(f"Nonpositive room dimensions/area: {floor} / {name}")
            if x < 0 or y < 0 or x + rw > width + 1e-6 or y + rd > depth + 1e-6:
                fail(f"Room box is outside the nominal building footprint: {floor} / {name}")
            if not math.isclose(rw * rd, area, rel_tol=0.0, abs_tol=0.011):
                fail(f"Room area mismatch: {floor} / {name}: {rw} x {rd} != {area}")
            if not room.get("dimension_note"):
                fail(f"Missing dimension note for {floor} / {name}")


def validate_svg_files() -> None:
    for filename, drawing_no in DRAWINGS.items():
        path = PREVIEW_DIR / filename
        if not path.is_file():
            fail(f"Missing required preview: {filename}")
        try:
            root = ET.parse(path).getroot()
        except ET.ParseError as exc:
            raise ValueError(f"Malformed SVG in {filename}: {exc}") from exc
        if local_name(root.tag) != "svg":
            fail(f"{filename} root element is not svg")
        title = " ".join(
            " ".join("".join(el.itertext()).split())
            for el in root.iter()
            if local_name(el.tag) == "title"
        )
        desc = " ".join(
            " ".join("".join(el.itertext()).split()).lower()
            for el in root.iter()
            if local_name(el.tag) == "desc"
        )
        visible_text = " ".join(
            " ".join("".join(el.itertext()).split())
            for el in root.iter()
            if local_name(el.tag) == "text"
        )
        if drawing_no not in title:
            fail(f"{filename} title does not contain {drawing_no}")
        if "preliminary" not in desc or "not" not in desc:
            fail(f"{filename} description must state that it is preliminary and not final/construction-ready")
        if drawing_no not in visible_text:
            fail(f"{filename} visible sheet title does not contain {drawing_no}")
        if drawing_no == "A-03":
            if "balcony" not in desc or "balcony" not in visible_text.lower():
                fail("A-03 must describe and visibly show the required balcony")
            if "3.00 x 1.50 m" not in visible_text:
                fail("A-03 must label the balcony dimensions as 3.00 x 1.50 m")
        if drawing_no == "A-05" and "balcony" not in visible_text.lower():
            fail("A-05 should show the balcony on the assumed front elevation")


def main() -> int:
    if not MODEL_PATH.is_file():
        fail(f"Missing shared building model: {MODEL_PATH}")
    data = json.loads(MODEL_PATH.read_text(encoding="utf-8"))
    validate_model(data)
    validate_svg_files()
    print("PASS: site area and 2 m screening geometry agree with the shared building model.")
    print("PASS: house/carport rectangles and required balcony are contained by the S-01 academic envelope.")
    print("PASS: each room target area equals width x depth and fits the nominal footprint.")
    print("PASS: all seven A-01 to A-07 SVG sheets parse and are labelled preliminary.")
    print("PASS: A-03 shows a dimensioned 3.00 m x 1.50 m balcony; A-05 includes the balcony on the assumed front facade.")
    print("NOTE: this verifies file/data consistency only, not setbacks, code compliance, design adequacy, or permit/construction readiness.")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, ValueError, KeyError, TypeError, json.JSONDecodeError) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        raise SystemExit(1)
