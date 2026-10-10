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
    if balcony.get("front_facade") != "east":
        fail("Balcony must be on the selected east/front facade")
    if not math.isclose(balcony_x, width, rel_tol=0.0, abs_tol=0.001):
        fail("Balcony must project from the east exterior wall")
    if balcony_y < 0 or balcony_y + balcony_width > depth + 1e-6:
        fail("Balcony span must fit along the east facade within the nominal house depth")
    if balcony.get("attached_to") != "Family area":
        fail("Balcony must be attached to the family area, not a bedroom")
    family = next((room for room in building["rooms"]["Second Floor"] if room["name"] == "Family area"), None)
    if family is None:
        fail("Second-floor model must include the family area")
    if not math.isclose(balcony_y, float(family["y_m"]), rel_tol=0.0, abs_tol=0.001):
        fail("Balcony alignment must start at the family-area facade edge")
    if not math.isclose(balcony_width, float(family["depth_m"]), rel_tol=0.0, abs_tol=0.001):
        fail("Balcony span must match the family-area length along the east facade")
    if not math.isclose(float(family["x_m"]) + float(family["width_m"]), width, rel_tol=0.0, abs_tol=0.001):
        fail("Family area must share the east/front exterior wall with the balcony")

    north_edge = float(site["building_placement"]["south_edge_northing_m"]) + float(site["building_placement"]["depth_m"])
    base_x = float(site["building_placement"]["southwest_easting_m"])
    east_edge = base_x + width
    balcony_north = north_edge - balcony_y
    balcony_south = balcony_north - balcony_width
    balcony_world = [
        (east_edge, balcony_north),
        (east_edge + balcony_projection, balcony_north),
        (east_edge + balcony_projection, balcony_south),
        (east_edge, balcony_south),
    ]
    if not all(point_in_polygon(point, screen) for point in balcony_world):
        fail("Balcony projection falls outside the selected S-01 academic setback envelope")

    area_assumptions = building.get("academic_floor_area_assumption", {})
    ground_gross = float(area_assumptions.get("ground_floor_gross_m2", 0))
    second_enclosed = float(area_assumptions.get("second_floor_enclosed_gross_m2", 0))
    second_with_balcony = float(area_assumptions.get("second_floor_total_with_balcony_m2", 0))
    total_enclosed = float(area_assumptions.get("total_enclosed_house_floor_area_m2", 0))
    total_including_balcony = float(area_assumptions.get("total_floor_area_including_balcony_m2", 0))
    if not math.isclose(ground_gross, calc_area, rel_tol=0.0, abs_tol=0.01):
        fail("Ground-floor area assumption does not match the main footprint")
    if not math.isclose(second_enclosed, calc_area, rel_tol=0.0, abs_tol=0.01):
        fail("Second-floor enclosed area assumption does not match the stated same-envelope basis")
    if not math.isclose(second_with_balcony, second_enclosed + balcony_area, rel_tol=0.0, abs_tol=0.01):
        fail("Second-floor total including balcony is inconsistent")
    if not math.isclose(total_enclosed, ground_gross + second_enclosed, rel_tol=0.0, abs_tol=0.01):
        fail("Total enclosed house floor area is inconsistent")
    if not math.isclose(total_including_balcony, total_enclosed + balcony_area, rel_tol=0.0, abs_tol=0.01):
        fail("Total floor area including balcony is inconsistent")

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
        if root.attrib.get("data-front-facade") != "east":
            fail(f"{filename} must use the shared east/front facade orientation")
        if root.attrib.get("data-balcony-access") != "family-area":
            fail(f"{filename} must share family-area access to the east/front balcony")
        for attr, expected in (("data-balcony-width-m", 3.0), ("data-balcony-projection-m", 1.5), ("data-balcony-offset-m", 4.9)):
            try:
                actual = float(root.attrib[attr])
            except (KeyError, ValueError):
                fail(f"{filename} is missing valid shared balcony metadata: {attr}")
            if not math.isclose(actual, expected, rel_tol=0.0, abs_tol=0.001):
                fail(f"{filename} balcony metadata mismatch for {attr}: {actual} != {expected}")
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
        geometry_ids = {
            "A-01": ("front-balcony-projection", "main-house-footprint"),
            "A-03": ("front-balcony-plan", "main-house-outline"),
            "A-04": ("front-balcony-projection", "main-roof-footprint"),
        }
        if drawing_no in geometry_ids:
            balcony_id, envelope_id = geometry_ids[drawing_no]
            balcony_shape = root.find(f".//*[@id='{balcony_id}']")
            envelope_shape = root.find(f".//*[@id='{envelope_id}']")
            if balcony_shape is None or envelope_shape is None:
                fail(f"{filename} must include both the house/roof outline and balcony geometry")
            try:
                bx = float(balcony_shape.attrib["x"])
                by = float(balcony_shape.attrib["y"])
                bw = float(balcony_shape.attrib["width"])
                bh = float(balcony_shape.attrib["height"])
                ex = float(envelope_shape.attrib["x"])
                ey = float(envelope_shape.attrib["y"])
                ew = float(envelope_shape.attrib["width"])
                eh = float(envelope_shape.attrib["height"])
            except (KeyError, ValueError):
                fail(f"{filename} balcony or envelope geometry has missing numeric coordinates")
            scale_x, scale_y = ew / 9.30, eh / 7.90
            expected = (
                ex + ew,
                ey + float(root.attrib["data-balcony-offset-m"]) * scale_y,
                1.50 * scale_x,
                3.00 * scale_y,
            )
            actual = (bx, by, bw, bh)
            for name, a, e in zip(("east-edge x", "family-area alignment y", "projection width", "facade span"), actual, expected):
                if not math.isclose(a, e, rel_tol=0.0, abs_tol=0.03):
                    fail(f"{filename} balcony {name} mismatch: {a} != {e}")
        if drawing_no == "A-03":
            if "balcony" not in desc or "balcony" not in visible_text.lower():
                fail("A-03 must describe and visibly show the required balcony")
            if "3.00 x 1.50 m" not in visible_text:
                fail("A-03 must label the balcony dimensions as 3.00 x 1.50 m")
            if "accessed from the family area" not in desc:
                fail("A-03 must state that the balcony is accessed from the family area")
            if "Family area" not in visible_text or "D-04" not in visible_text:
                fail("A-03 must show the family area and its D-04 balcony access")
            access_door = root.find(".//*[@id='family-area-balcony-door']")
            if access_door is None or access_door.attrib.get("data-access-space") != "family-area" or access_door.attrib.get("data-width-m") != "0.90":
                fail("A-03 D-04 must be a 0.90 m door from the family area")
            if any(local_name(el.tag) == "rect" and el.attrib.get("x") in {"417.35", "159.35"} and el.attrib.get("fill") == "#ffffff" for el in root.iter()):
                fail("A-03 contains opaque furniture boxes that can cover room labels")
        if drawing_no == "A-05":
            if "balcony" not in visible_text.lower() or "FRONT ELEVATION - ENTRY / CARPORT SIDE" not in visible_text:
                fail("A-05 must show the balcony on the east/front entry-carport elevation")
            front_balcony = root.find(".//*[@id='front-balcony-elevation']")
            if front_balcony is None:
                fail("A-05 must include the front-balcony elevation geometry")
            if front_balcony.attrib.get("data-span-m") != "3.00" or front_balcony.attrib.get("data-projection-m") != "1.50" or front_balcony.attrib.get("data-offset-m") != "4.90" or front_balcony.attrib.get("data-access-space") != "family-area":
                fail("A-05 balcony span/projection/position metadata must match the family-area location")
        if drawing_no == "A-06":
            front_section = root.find(".//*[@id='front-balcony-section']")
            if front_section is None:
                fail("A-06 must include a section through the front balcony")
            if front_section.attrib.get("data-span-m") != "3.00" or front_section.attrib.get("data-projection-m") != "1.50" or front_section.attrib.get("data-offset-m") != "4.90" or front_section.attrib.get("data-access-space") != "family-area":
                fail("A-06 balcony span/projection/position metadata must match the family-area location")
        if drawing_no == "A-07":
            if "Front/east balcony beside family area" not in visible_text or "D-04 Balcony door from family area: 0.90 x 2.10 m" not in visible_text:
                fail("A-07 balcony note and D-04 door schedule must match the front balcony")


def main() -> int:
    if not MODEL_PATH.is_file():
        fail(f"Missing shared building model: {MODEL_PATH}")
    data = json.loads(MODEL_PATH.read_text(encoding="utf-8"))
    validate_model(data)
    validate_svg_files()
    print("PASS: site area and 2 m screening geometry agree with the shared building model.")
    print("PASS: house/carport and family-area balcony fit within the S-01 academic envelope.")
    print("PASS: each room target area equals width x depth and fits the nominal footprint.")
    print("PASS: all seven A-01 to A-07 SVG sheets parse and are labelled preliminary.")
    print("PASS: A-01/A-03/A-04 balcony geometry aligns with the family area; A-05/A-06/A-07 match its location and D-04 access.")
    print("NOTE: this verifies file/data consistency only, not setbacks, code compliance, design adequacy, or permit/construction readiness.")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, ValueError, KeyError, TypeError, json.JSONDecodeError) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        raise SystemExit(1)
