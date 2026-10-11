#!/usr/bin/env python3
"""Validate the revised Phase 3 room programme, relationships, SVGs, and layout guardrails."""

from __future__ import annotations

import csv
import json
import math
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPACE_DIR = ROOT / "space_planning"
SCHEDULE_PATH = SPACE_DIR / "space_requirement_table.csv"
MATRIX_PATH = SPACE_DIR / "adjacency_matrix.csv"
MODEL_PATH = ROOT / "data" / "building_model.json"

REQUIRED_BY_FLOOR = {
    "Ground Floor": {
        "Entrance / foyer", "Living room", "Dining area", "Kitchen",
        "Toilet and bath (ground floor)", "Bedroom / guest room", "Stairway",
        "Storage / service area", "Garage / carport",
    },
    "Second Floor": {
        "Master bedroom", "Bedroom 2", "Bedroom 3",
        "Toilet and bath (second floor)", "Family area",
        "Stair landing / circulation",
    },
}
REFERENCE_SPACES_BY_FLOOR = {
    "Ground Floor": {"General circulation allowance"},
    "Second Floor": {
        "Robe / wardrobe (master bedroom)", "Bathroom (second floor)",
        "Toilet (second floor)", "Karaoke room", "Gym", "Balcony (if appropriate)",
    },
}
VALID_STATUSES = {"required", "additional", "optional", "conditional", "allowance"}
VALID_TYPES = {"enclosed", "vehicle-area", "allowance", "optional-external", "support-zone", "circulation"}
VALID_RELATIONSHIPS = {"direct", "near", "buffered", "conditional"}
VALID_DIMENSION_STATUS = {"legacy-target-unverified", "legacy-allowance-unverified", "not-dimensioned"}


def fail(message: str) -> None:
    raise ValueError(message)


def read_csv(path: Path, required_columns: set[str]) -> list[dict[str, str]]:
    if not path.is_file():
        fail(f"Required CSV not found: {path}")
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        missing = required_columns - set(reader.fieldnames or [])
        if missing:
            fail(f"{path.name} missing columns: {', '.join(sorted(missing))}")
        rows = [dict(row) for row in reader]
    if not rows:
        fail(f"{path.name} has no data rows")
    return rows


def numeric(value: str, field: str, space: str) -> float:
    try:
        result = float(value)
    except (TypeError, ValueError) as exc:
        raise ValueError(f"Invalid {field} for {space!r}: {value!r}") from exc
    if not math.isfinite(result):
        fail(f"Non-finite {field} for {space!r}")
    return result


def validate_schedule() -> tuple[dict[str, set[str]], set[str], int]:
    rows = read_csv(SCHEDULE_PATH, {
        "floor", "space", "requirement_status", "space_type",
        "target_length_m", "target_width_m", "target_area_m2",
        "area_basis", "dimension_status", "zone", "preferred_relationships", "planning_notes",
    })
    names_by_floor: dict[str, set[str]] = {}
    all_names: set[str] = set()
    seen: set[tuple[str, str]] = set()
    legacy_target_count = 0
    undimensioned_count = 0

    for row in rows:
        floor, space = row["floor"].strip(), row["space"].strip()
        status, space_type = row["requirement_status"].strip(), row["space_type"].strip()
        dimension_status = row["dimension_status"].strip()
        if not floor or not space:
            fail("Every schedule row must name a floor and a space")
        key = (floor, space)
        if key in seen:
            fail(f"Duplicate space row: {floor} / {space}")
        seen.add(key)
        all_names.add(space)
        names_by_floor.setdefault(floor, set()).add(space)

        if status not in VALID_STATUSES:
            fail(f"Invalid requirement_status for {space!r}: {status!r}")
        if space_type not in VALID_TYPES:
            fail(f"Invalid space_type for {space!r}: {space_type!r}")
        if dimension_status not in VALID_DIMENSION_STATUS:
            fail(f"Invalid dimension_status for {space!r}: {dimension_status!r}")

        length_text, width_text, area_text = (
            row["target_length_m"].strip(),
            row["target_width_m"].strip(),
            row["target_area_m2"].strip(),
        )
        basis = row["area_basis"].strip()

        if dimension_status == "legacy-target-unverified":
            if space_type in {"allowance", "support-zone"}:
                fail(f"{space!r} cannot be dimensioned as a legacy enclosed target with type {space_type!r}")
            if not length_text or not width_text or not area_text:
                fail(f"Legacy target {space!r} requires length, width and area values")
            length = numeric(length_text, "target_length_m", space)
            width = numeric(width_text, "target_width_m", space)
            area = numeric(area_text, "target_area_m2", space)
            if min(length, width, area) <= 0:
                fail(f"Legacy target values must be positive for {space!r}")
            if not math.isclose(length * width, area, rel_tol=0.0, abs_tol=0.011):
                fail(f"Legacy area mismatch for {space!r}: {length} x {width} != {area}")
            if basis != "legacy target; unverified":
                fail(f"{space!r} must clearly mark its values as a legacy, unverified target")
            legacy_target_count += 1

        elif dimension_status == "legacy-allowance-unverified":
            if space_type != "allowance":
                fail(f"{space!r} is marked as a legacy area allowance but is not type 'allowance'")
            if length_text or width_text or not area_text:
                fail(f"Area allowance {space!r} must have blank dimensions and a positive area only")
            if numeric(area_text, "target_area_m2", space) <= 0:
                fail(f"Area allowance must be positive for {space!r}")
            if basis != "legacy planning allowance; unverified":
                fail(f"{space!r} must identify its legacy area allowance as unverified")

        else:
            if length_text or width_text or area_text:
                fail(f"Not-dimensioned space {space!r} must have blank length, width and area fields")
            if basis != "not dimensioned from reference image":
                fail(f"{space!r} must state that no dimensions were taken from the reference image")
            undimensioned_count += 1

        if not row["planning_notes"].strip():
            fail(f"Missing planning note for {space!r}")

    for floor, required in REQUIRED_BY_FLOOR.items():
        missing = required - names_by_floor.get(floor, set())
        if missing:
            fail(f"{floor} is missing assignment-required spaces: {', '.join(sorted(missing))}")
    for floor, required in REFERENCE_SPACES_BY_FLOOR.items():
        missing = required - names_by_floor.get(floor, set())
        if missing:
            fail(f"{floor} is missing spaces shown in the selected reference: {', '.join(sorted(missing))}")

    return names_by_floor, all_names, legacy_target_count


def validate_adjacency(names_by_floor: dict[str, set[str]], all_names: set[str]) -> int:
    rows = read_csv(MATRIX_PATH, {"floor", "space_a", "space_b", "relationship", "reason"})
    seen_pairs: set[tuple[str, str, str]] = set()
    for row in rows:
        floor = row["floor"].strip()
        a, b = row["space_a"].strip(), row["space_b"].strip()
        relationship = row["relationship"].strip()
        if a not in all_names:
            fail(f"Adjacency matrix references unknown space: {a!r}")
        if b not in all_names:
            fail(f"Adjacency matrix references unknown space: {b!r}")
        if a == b:
            fail(f"Adjacency pair cannot reference the same space twice: {a!r}")
        if floor not in {"Ground Floor", "Second Floor", "Cross-floor"}:
            fail(f"Unrecognized floor value in adjacency matrix: {floor!r}")
        if floor != "Cross-floor":
            if a not in names_by_floor.get(floor, set()) or b not in names_by_floor.get(floor, set()):
                fail(f"{floor} adjacency has a space on a different floor: {a!r} / {b!r}")
        if relationship not in VALID_RELATIONSHIPS:
            fail(f"Invalid relationship label: {relationship!r}")
        if not row["reason"].strip():
            fail(f"Adjacency pair has no reason: {a!r} / {b!r}")
        key = (floor, *sorted((a, b)))
        if key in seen_pairs:
            fail(f"Duplicate adjacency pair: {floor} / {a} / {b}")
        seen_pairs.add(key)
    return len(rows)


def local_name(tag: str) -> str:
    return tag.rsplit("}", 1)[-1]


def validate_svg(path: Path, required_names: set[str]) -> ET.Element:
    if not path.is_file():
        fail(f"Required SVG not found: {path}")
    try:
        root = ET.parse(path).getroot()
    except ET.ParseError as exc:
        raise ValueError(f"Invalid SVG XML in {path.name}: {exc}") from exc
    if local_name(root.tag) != "svg":
        fail(f"{path.name} root element must be <svg>")
    desc = " ".join("".join(el.itertext()) for el in root.iter() if local_name(el.tag) == "desc")
    normalized_desc = " ".join(desc.lower().split())
    if "not to scale" not in normalized_desc:
        fail(f"{path.name} must declare that the diagram is not to scale")
    for name in required_names:
        if name.lower() not in normalized_desc:
            fail(f"{path.name} description does not include required space {name!r}")
    if not any(local_name(el.tag) == "text" for el in root.iter()):
        fail(f"{path.name} contains no visible text")
    return root


def rectangles_overlap(a: dict, b: dict) -> bool:
    return (
        float(a["x"]) < float(b["x"]) + float(b["width"])
        and float(a["x"]) + float(a["width"]) > float(b["x"])
        and float(a["y"]) < float(b["y"]) + float(b["height"])
        and float(a["y"]) + float(a["height"]) > float(b["y"])
    )


def rectangle_contains(outer: dict, inner: dict) -> bool:
    return (
        float(inner["x"]) >= float(outer["x"])
        and float(inner["y"]) >= float(outer["y"])
        and float(inner["x"]) + float(inner["width"]) <= float(outer["x"]) + float(outer["width"])
        and float(inner["y"]) + float(inner["height"]) <= float(outer["y"]) + float(outer["height"])
    )


def validate_layout_guardrails(model: dict) -> None:
    layout = model.get("reference_layout")
    if not isinstance(layout, dict):
        fail("Shared building model is missing reference_layout")

    ground = layout.get("ground_floor", {})
    room_bounds = ground.get("room_bounds", {})
    tv_items = [item for item in ground.get("fixtures", []) if item.get("id") == "tv-console"]
    if len(tv_items) != 1:
        fail(f"Expected exactly one TV console in the reference model, found {len(tv_items)}")
    tv = tv_items[0]
    living = room_bounds.get("living-room")
    foyer = room_bounds.get("foyer")
    entry = ground.get("entry_clearance")
    if not living or not foyer or not entry:
        fail("Reference model must define living room, foyer and entry-clearance bounds")
    if tv.get("room_id") != "living-room" or not rectangle_contains(living, tv):
        fail("TV console must be inside the first-floor living-room bounds")
    if rectangles_overlap(tv, foyer) or rectangles_overlap(tv, entry):
        fail("TV console overlaps the foyer or entrance-clearance bounds")

    second = layout.get("second_floor", {})
    karaoke_doors = [door for door in second.get("doorways", []) if door.get("room_id") == "karaoke-room"]
    if len(karaoke_doors) != 1:
        fail(f"Reference model must contain exactly one karaoke-room door, found {len(karaoke_doors)}")
    if int(second.get("constraints", {}).get("karaoke-room", {}).get("door_count", 0)) != 1:
        fail("Karaoke-room reference constraint must require door_count=1")

    floor_plan_ground = ROOT / "previews" / "phase5_A02_ground_floor.svg"
    floor_plan_second = ROOT / "previews" / "phase5_A03_second_floor.svg"
    for path in (floor_plan_ground, floor_plan_second):
        try:
            root = ET.parse(path).getroot()
        except (OSError, ET.ParseError) as exc:
            raise ValueError(f"Cannot validate architectural preview {path.name}: {exc}") from exc
        if path.name == "phase5_A02_ground_floor.svg":
            tv_markers = [el for el in root.iter() if el.attrib.get("id") == "tv-console"]
            if len(tv_markers) != 1 or tv_markers[0].attrib.get("data-room") != "living-room":
                fail("A-02 must mark exactly one TV console in the living room")
        else:
            door_markers = [el for el in root.iter() if el.attrib.get("data-room-door") == "karaoke-room"]
            if len(door_markers) != 1:
                fail(f"A-03 must mark exactly one karaoke-room door, found {len(door_markers)}")

    zoning_ground = ET.parse(SPACE_DIR / "ground_floor_zoning.svg").getroot()
    tv_zone_markers = [el for el in zoning_ground.iter() if el.attrib.get("id") == "tv-console"]
    if len(tv_zone_markers) != 1 or tv_zone_markers[0].attrib.get("data-room") != "living-room":
        fail("Ground-floor Phase 3 zoning must show one TV marker inside the living-room zone")
    zoning_second = ET.parse(SPACE_DIR / "second_floor_zoning.svg").getroot()
    karaoke_zone_doors = [el for el in zoning_second.iter() if el.attrib.get("data-room-door") == "karaoke-room"]
    if len(karaoke_zone_doors) != 1:
        fail(f"Second-floor Phase 3 zoning must show exactly one karaoke-room door marker, found {len(karaoke_zone_doors)}")


def main() -> int:
    names_by_floor, all_names, legacy_count = validate_schedule()
    adjacency_count = validate_adjacency(names_by_floor, all_names)
    validate_svg(SPACE_DIR / "adjacency_diagram.svg", all_names)
    validate_svg(SPACE_DIR / "ground_floor_zoning.svg", names_by_floor["Ground Floor"])
    validate_svg(SPACE_DIR / "second_floor_zoning.svg", names_by_floor["Second Floor"])
    try:
        model = json.loads(MODEL_PATH.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError(f"Cannot read shared building model {MODEL_PATH}: {exc}") from exc
    validate_layout_guardrails(model)
    print("PASS: assignment-required rooms and selected-reference spaces are in the revised schedule.")
    print(f"PASS: {legacy_count} inherited numerical targets are marked unverified; undimensioned reference spaces have blank dimensions.")
    print(f"PASS: {adjacency_count} adjacency relationships use valid space names, floors and relationship labels.")
    print("PASS: all three Phase 3 SVG diagrams parse and describe the required spaces.")
    print("PASS: A-02 and Phase 3 zoning place one TV in the living room, clear of the foyer/entry path.")
    print("PASS: A-03 and Phase 3 zoning each mark exactly one karaoke-room door.")
    print("NOTE: checks establish data/document consistency only, not final dimensions, code compliance, structural adequacy or construction readiness.")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, ValueError, KeyError, TypeError) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        raise SystemExit(1)
