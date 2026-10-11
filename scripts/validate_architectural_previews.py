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



def rectangles_overlap(a: dict[str, float], b: dict[str, float]) -> bool:
    return (
        float(a["x"]) < float(b["x"]) + float(b["width"])
        and float(a["x"]) + float(a["width"]) > float(b["x"])
        and float(a["y"]) < float(b["y"]) + float(b["height"])
        and float(a["y"]) + float(a["height"]) > float(b["y"])
    )


def rectangle_contains(outer: dict[str, float], inner: dict[str, float]) -> bool:
    return (
        float(inner["x"]) >= float(outer["x"])
        and float(inner["y"]) >= float(outer["y"])
        and float(inner["x"]) + float(inner["width"]) <= float(outer["x"]) + float(outer["width"])
        and float(inner["y"]) + float(inner["height"]) <= float(outer["y"]) + float(outer["height"])
    )


def validate_reference_layout(data: dict) -> None:
    layout = data.get("reference_layout")
    if not isinstance(layout, dict):
        fail("Missing reference_layout data for the furnished A-02/A-03 concept.")

    ground = layout.get("ground_floor", {})
    bounds = ground.get("room_bounds", {})
    tv_items = [item for item in ground.get("fixtures", []) if item.get("id") == "tv-console"]
    if len(tv_items) != 1:
        fail(f"Expected exactly one TV console in the first-floor reference layout, got {len(tv_items)}.")
    tv = tv_items[0]
    living = bounds.get("living-room")
    foyer = bounds.get("foyer")
    entry = ground.get("entry_clearance")
    if not living or not foyer or not entry:
        fail("Reference layout must define the living room, foyer and entrance-clearance bounds.")
    if tv.get("room_id") != "living-room" or not rectangle_contains(living, tv):
        fail("TV console must be inside the first-floor living room.")
    if rectangles_overlap(tv, foyer) or rectangles_overlap(tv, entry):
        fail("TV console overlaps the foyer or entrance-clearance route.")

    second = layout.get("second_floor", {})
    karaoke_doors = [door for door in second.get("doorways", []) if door.get("room_id") == "karaoke-room"]
    expected_doors = int(second.get("constraints", {}).get("karaoke-room", {}).get("door_count", 1))
    if len(karaoke_doors) != expected_doors or expected_doors != 1:
        fail(f"Karaoke room must have exactly one door in the second-floor model; found {len(karaoke_doors)}.")
    if "karaoke-room" not in second.get("room_bounds", {}):
        fail("The second-floor reference layout is missing the karaoke room bounds.")


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

        if filename == "phase5_A02_ground_floor.svg":
            tv_nodes = [el for el in root.iter() if el.attrib.get("id") == "tv-console"]
            if len(tv_nodes) != 1 or tv_nodes[0].attrib.get("data-room") != "living-room":
                fail("A-02 must show one TV console assigned to the living room.")
        if filename == "phase5_A03_second_floor.svg":
            karaoke_door_nodes = [
                el for el in root.iter()
                if el.attrib.get("data-room-door") == "karaoke-room"
            ]
            if len(karaoke_door_nodes) != 1:
                fail(f"A-03 must show exactly one karaoke-room door; found {len(karaoke_door_nodes)}.")


def main() -> int:
    if not MODEL_PATH.is_file():
        fail(f"Missing shared building model: {MODEL_PATH}")
    data = json.loads(MODEL_PATH.read_text(encoding="utf-8"))
    validate_model(data)
    validate_reference_layout(data)
    validate_svg_files()
    print("PASS: site area and 2 m screening geometry agree with the shared building model.")
    print("PASS: house/carport rectangles are contained by the screening polygon.")
    print("PASS: each room target area equals width x depth and fits the nominal footprint.")
    print("PASS: all seven A-01 to A-07 SVG sheets parse and are labelled preliminary.")
    print("PASS: A-02 TV console is inside the living room and clear of the foyer/entry route.")
    print("PASS: A-03 reference model and SVG each contain exactly one karaoke-room door.")
    print("NOTE: this verifies file/data consistency only, not setbacks, code compliance, design adequacy, or permit/construction readiness.")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, ValueError, KeyError, TypeError, json.JSONDecodeError) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        raise SystemExit(1)
