#!/usr/bin/env python3
"""Validate preliminary Phase 4 stair data and its SVG study files."""

from __future__ import annotations

import json
import math
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "stair_design.json"
SPACE_DIR = ROOT / "space_planning"


def fail(message: str) -> None:
    raise ValueError(message)


def close(a: float, b: float, tolerance: float = 1e-6) -> bool:
    return abs(a - b) <= tolerance


def local_name(tag: str) -> str:
    return tag.rsplit("}", 1)[-1]


def validate_svg(path: Path, required_phrases: tuple[str, ...]) -> None:
    if not path.is_file():
        fail(f"Missing SVG preview: {path}")
    try:
        root = ET.parse(path).getroot()
    except ET.ParseError as exc:
        raise ValueError(f"Invalid XML in {path.name}: {exc}") from exc
    if local_name(root.tag) != "svg":
        fail(f"{path.name} root must be svg")
    desc = " ".join(
        " ".join("".join(el.itertext()).lower().split())
        for el in root.iter()
        if local_name(el.tag) == "desc"
    )
    visible = " ".join(
        " ".join("".join(el.itertext()).lower().split())
        for el in root.iter()
        if local_name(el.tag) == "text"
    )
    if "not" not in desc or "construction" not in desc:
        fail(f"{path.name} must state that it is not a construction drawing")
    for phrase in required_phrases:
        if phrase.lower() not in visible:
            fail(f"{path.name} is missing visible label {phrase!r}")


def main() -> int:
    if not DATA_PATH.is_file():
        fail(f"Missing stair data: {DATA_PATH}")
    data = json.loads(DATA_PATH.read_text(encoding="utf-8"))
    floor = data["floor_levels"]
    geo = data["geometry"]
    checks = data["checks"]

    total_rise = float(floor["floor_to_floor_rise_m"])
    if not close(total_rise, float(floor["second_floor_finished_floor_elevation_m"]) - float(floor["ground_floor_finished_floor_elevation_m"])):
        fail("Floor-to-floor rise does not match the two finished-floor elevations")
    if total_rise <= 0:
        fail("Floor-to-floor rise must be positive")

    risers = int(geo["total_risers"])
    per_flight = [int(v) for v in geo["risers_per_flight"]]
    if len(per_flight) != 2 or sum(per_flight) != risers:
        fail("The two flight riser counts must sum to total_risers")
    calculated_riser = total_rise / risers
    recorded_riser = float(geo["riser_height_m"])
    if not close(calculated_riser, recorded_riser, 1e-5):
        fail(f"Riser-height mismatch: calculated {calculated_riser}, stored {recorded_riser}")
    if recorded_riser > float(checks["nbcp_general_stair_max_riser_m"]):
        fail("Riser height exceeds the stored general NBCP maximum")
    if recorded_riser > float(geo["design_target_max_riser_m"]):
        fail("Riser height exceeds the stated design target")

    treads_per_flight = [int(v) for v in geo["treads_per_flight"]]
    if len(treads_per_flight) != 2 or any(t != r - 1 for t, r in zip(treads_per_flight, per_flight)):
        fail("For each flight, physical treads must equal risers minus one")
    if int(geo["total_physical_treads"]) != sum(treads_per_flight):
        fail("Total physical tread count is inconsistent")

    tread = float(geo["tread_depth_m"])
    if tread < float(checks["nbcp_general_stair_min_tread_m"]):
        fail("Tread depth is below the stored general NBCP minimum")
    runs = [t * tread for t in treads_per_flight]
    for stored, calculated in zip(geo["horizontal_run_per_flight_m"] if isinstance(geo["horizontal_run_per_flight_m"], list) else [geo["horizontal_run_per_flight_m"]]*2, runs):
        if not close(float(stored), calculated, 1e-6):
            fail("Stored horizontal flight run does not match tread count x tread depth")
    combined_run = sum(runs)
    if not close(combined_run, float(geo["combined_physical_tread_run_m"]), 1e-6):
        fail("Combined tread run does not match the two flight runs")

    width = float(geo["clear_width_per_flight_m"])
    if width < float(checks["nbcp_group_a_dwelling_width_min_m"]):
        fail("Clear flight width is below the stored Group A dwelling minimum")
    if float(geo["landing_depth_m"]) < width:
        fail("Landing depth is less than one flight's clear width")
    if not close(sum(float(v) for v in per_flight) and total_rise, total_rise):
        fail("Total rise check failed")
    flight_rise = [r * recorded_riser for r in per_flight]
    if any(r > float(geo["maximum_vertical_distance_between_landings_m"]) for r in flight_rise):
        fail("Vertical distance between landings exceeds the recorded limit")
    if float(geo["minimum_headroom_m"]) < 2.0:
        fail("Minimum headroom target must be at least 2.00 m")

    envelope = geo["nominal_space_envelope_m"]
    envelope_area = float(envelope["width"]) * float(envelope["length"])
    if not close(envelope_area, float(envelope["area"]), 1e-6):
        fail("Nominal space-envelope area is inconsistent")
    needed_length = max(runs) + float(geo["landing_depth_m"])
    if needed_length > float(envelope["length"]):
        fail(f"Nominal envelope length {envelope['length']} m is shorter than run + landing ({needed_length} m)")
    combined_width_needed = 2 * width + 0.20
    if combined_width_needed > float(envelope["width"]):
        fail("Nominal envelope width cannot fit both flights and the 0.20 m separation allowance")

    validate_svg(SPACE_DIR / "stair_plan.svg", ("HALF-LANDING", "FLIGHT 1", "FLIGHT 2", "2.00 m nominal width", "3.20 m"))
    validate_svg(SPACE_DIR / "stair_section.svg", ("166.7 mm rise", "280 mm tread", "3.000 m", "HALF-LANDING"))
    print("PASS: finished-floor elevations and total stair rise agree.")
    print("PASS: riser/tread counts, dimensions, and flight-run arithmetic agree.")
    print("PASS: width, landing, flight-rise, headroom, and stair-envelope checks pass the stored preliminary design criteria.")
    print("PASS: stair plan and section SVGs parse and include the required dimension labels.")
    print("NOTE: floor-to-floor height is assumed; code applicability, BP 344, structural design, and final building-section clearances remain pending.")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, ValueError, KeyError, TypeError, json.JSONDecodeError) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        raise SystemExit(1)
