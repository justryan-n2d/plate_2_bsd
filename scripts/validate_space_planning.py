#!/usr/bin/env python3
"""Validate Phase 3 space-planning schedules, relationships, and SVG diagrams."""

from __future__ import annotations

import csv
import math
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPACE_DIR = ROOT / "space_planning"
SCHEDULE_PATH = SPACE_DIR / "space_requirement_table.csv"
MATRIX_PATH = SPACE_DIR / "adjacency_matrix.csv"

REQUIRED_BY_FLOOR = {
    "Ground Floor": {
        "Entrance / foyer",
        "Living room",
        "Dining area",
        "Kitchen",
        "Toilet and bath (ground floor)",
        "Bedroom / guest room",
        "Stairway",
        "Storage / service area",
        "Garage / carport",
    },
    "Second Floor": {
        "Master bedroom",
        "Bedroom 2",
        "Bedroom 3",
        "Toilet and bath (second floor)",
        "Family area",
        "Stair landing / circulation",
        "Balcony",
    },
}
VALID_STATUSES = {"required", "optional", "allowance"}
VALID_TYPES = {"enclosed", "covered-open", "allowance", "optional-external"}
VALID_RELATIONSHIPS = {"direct", "near", "buffered", "conditional"}


def fail(message: str) -> None:
    raise ValueError(message)


def read_csv(path: Path, required_columns: set[str]) -> list[dict[str, str]]:
    if not path.is_file():
        fail(f"Required CSV not found: {path}")
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        fields = set(reader.fieldnames or [])
        missing = required_columns - fields
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


def validate_schedule() -> tuple[set[str], dict[str, set[str]], list[dict[str, str]]]:
    rows = read_csv(
        SCHEDULE_PATH,
        {
            "floor", "space", "requirement_status", "space_type",
            "target_length_m", "target_width_m", "target_area_m2",
            "area_basis", "zone", "preferred_relationships", "planning_notes",
        },
    )
    names_by_floor: dict[str, set[str]] = {}
    all_names: set[str] = set()
    seen: set[tuple[str, str]] = set()

    for row in rows:
        floor = row["floor"].strip()
        space = row["space"].strip()
        status = row["requirement_status"].strip()
        space_type = row["space_type"].strip()
        key = (floor, space)
        if not floor or not space:
            fail("Every schedule row must name a floor and space")
        if key in seen:
            fail(f"Duplicate space row: {floor} / {space}")
        seen.add(key)
        all_names.add(space)
        names_by_floor.setdefault(floor, set()).add(space)

        if status not in VALID_STATUSES:
            fail(f"Invalid requirement_status for {space!r}: {status!r}")
        if space_type not in VALID_TYPES:
            fail(f"Invalid space_type for {space!r}: {space_type!r}")

        area = numeric(row["target_area_m2"], "target_area_m2", space)
        if area <= 0:
            fail(f"target_area_m2 must be positive for {space!r}")
        length_text = row["target_length_m"].strip()
        width_text = row["target_width_m"].strip()

        if space_type == "allowance":
            if length_text or width_text:
                fail(f"Area allowance {space!r} must not pretend to have dimensions")
            if row["area_basis"].strip() != "planning allowance":
                fail(f"Area allowance {space!r} must use 'planning allowance' basis")
        else:
            if not length_text or not width_text:
                fail(f"Dimensioned space {space!r} needs length and width")
            length = numeric(length_text, "target_length_m", space)
            width = numeric(width_text, "target_width_m", space)
            if length <= 0 or width <= 0:
                fail(f"Dimensions must be positive for {space!r}")
            if not math.isclose(length * width, area, rel_tol=0.0, abs_tol=0.011):
                fail(
                    f"Area mismatch for {space!r}: {length} x {width} "
                    f"does not match {area} m²"
                )
            if row["area_basis"].strip() != "clear-dimension target":
                fail(f"Dimensioned space {space!r} must be marked as a clear-dimension target")

    for floor, required_names in REQUIRED_BY_FLOOR.items():
        missing = required_names - names_by_floor.get(floor, set())
        if missing:
            fail(f"{floor} is missing required spaces: {', '.join(sorted(missing))}")

    # Guard against accidental changes to the planning schedule's arithmetic.
    def area_sum(floor: str, types: set[str]) -> float:
        return sum(
            float(row["target_area_m2"])
            for row in rows
            if row["floor"].strip() == floor and row["space_type"].strip() in types
        )

    ground_enclosed = area_sum("Ground Floor", {"enclosed"})
    ground_allowance = area_sum("Ground Floor", {"allowance"})
    upper_enclosed = area_sum("Second Floor", {"enclosed"})
    carport = sum(
        float(row["target_area_m2"])
        for row in rows
        if row["floor"].strip() == "Ground Floor"
        and row["space_type"].strip() == "covered-open"
    )
    balcony = sum(
        float(row["target_area_m2"])
        for row in rows
        if row["space_type"].strip() == "optional-external"
    )
    expected = {
        "ground enclosed target": (ground_enclosed, 52.32),
        "ground circulation allowance": (ground_allowance, 4.50),
        "upper enclosed target": (upper_enclosed, 44.23),
        "carport placeholder": (carport, 15.40),
        "required balcony": (balcony, 4.50),
    }
    for label, (actual, target) in expected.items():
        if not math.isclose(actual, target, rel_tol=0.0, abs_tol=0.011):
            fail(f"Unexpected {label}: expected {target:.2f} m², found {actual:.2f} m²")

    return all_names, names_by_floor, rows


def validate_adjacency(all_names: set[str]) -> None:
    rows = read_csv(
        MATRIX_PATH,
        {"floor", "space_a", "space_b", "relationship", "reason"},
    )
    seen_pairs: set[tuple[str, str, str]] = set()
    for row in rows:
        floor = row["floor"].strip()
        a = row["space_a"].strip()
        b = row["space_b"].strip()
        relationship = row["relationship"].strip()
        if a not in all_names:
            fail(f"Adjacency matrix references unknown space: {a!r}")
        if b not in all_names:
            fail(f"Adjacency matrix references unknown space: {b!r}")
        if a == b:
            fail(f"Adjacency pair cannot reference the same space twice: {a!r}")
        if relationship not in VALID_RELATIONSHIPS:
            fail(f"Invalid relationship label: {relationship!r}")
        if not row["reason"].strip():
            fail(f"Adjacency pair has no reason: {a!r} / {b!r}")
        pair = (floor, *sorted((a, b)))
        if pair in seen_pairs:
            fail(f"Duplicate adjacency pair: {floor} / {a} / {b}")
        seen_pairs.add(pair)


def local_name(tag: str) -> str:
    return tag.rsplit("}", 1)[-1]


def validate_svg(path: Path, required_names: set[str]) -> None:
    if not path.is_file():
        fail(f"Required SVG not found: {path}")
    try:
        root = ET.parse(path).getroot()
    except ET.ParseError as exc:
        raise ValueError(f"Invalid SVG XML in {path.name}: {exc}") from exc
    if local_name(root.tag) != "svg":
        fail(f"{path.name} root element must be <svg>")
    desc = " ".join(
        "".join(element.itertext())
        for element in root.iter()
        if local_name(element.tag) == "desc"
    )
    normalized_desc = " ".join(desc.lower().split())
    if "not to scale" not in normalized_desc:
        fail(f"{path.name} must declare that the diagram is not to scale")
    for name in required_names:
        if name.lower() not in normalized_desc:
            fail(f"{path.name} description does not include required space {name!r}")
    visible_text = " ".join(
        " ".join("".join(element.itertext()).lower().split())
        for element in root.iter()
        if local_name(element.tag) == "text"
    )
    if not visible_text.strip():
        fail(f"{path.name} contains no visible text")


def main() -> int:
    all_names, names_by_floor, _rows = validate_schedule()
    validate_adjacency(all_names)
    validate_svg(SPACE_DIR / "adjacency_diagram.svg", all_names)
    validate_svg(
        SPACE_DIR / "ground_floor_zoning.svg",
        names_by_floor["Ground Floor"],
    )
    validate_svg(
        SPACE_DIR / "second_floor_zoning.svg",
        names_by_floor["Second Floor"],
    )
    print("PASS: required room schedule entries are present.")
    print("PASS: dimension/area arithmetic and planning area cross-checks are consistent.")
    print("PASS: adjacency references and relationship labels are valid.")
    print("PASS: all three SVG diagrams parse and describe their required spaces.")
    print("NOTE: checks validate data consistency only; they do not establish code compliance or a final building layout.")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, ValueError) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        raise SystemExit(1)
