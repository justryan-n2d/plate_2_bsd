#!/usr/bin/env python3
"""Validate the Phase 1 traverse CSV without modifying source files."""

from __future__ import annotations

import argparse
import csv
import math
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CSV = ROOT / "site" / "phase1_traverse_coordinates.csv"
GIVEN_COURSES = ("1-2", "2-3", "3-4", "4-5")
EXPECTED_PERIMETER_M = 64.145414
EXPECTED_AREA_M2 = 265.2598
EXPECTED_ORIGINAL_MISCLOSURE_M = 4.011967


def parse_bearing(value: str) -> tuple[float, str, str]:
    normalized = value.strip().replace(" ", "").replace("′", "'").replace("″", '"')
    match = re.fullmatch(r"([NS])(\d+)°(\d+)'(?:(\d+(?:\.\d+)?)\")?([EW])", normalized)
    if not match:
        raise ValueError(f"Unsupported bearing format: {value!r}")
    ns, degrees, minutes, seconds, ew = match.groups()
    angle = int(degrees) + int(minutes) / 60.0 + float(seconds or 0.0) / 3600.0
    if not 0.0 <= angle <= 90.0:
        raise ValueError(f"Bearing angle must be between 0 and 90 degrees: {value!r}")
    return angle, ns, ew


def components(distance_m: float, bearing: str) -> tuple[float, float]:
    angle, ns, ew = parse_bearing(bearing)
    theta = math.radians(angle)
    latitude = distance_m * math.cos(theta) * (1.0 if ns == "N" else -1.0)
    departure = distance_m * math.sin(theta) * (1.0 if ew == "E" else -1.0)
    return latitude, departure


def load_rows(csv_path: Path) -> list[dict[str, str]]:
    if not csv_path.is_file():
        raise FileNotFoundError(f"Traverse CSV not found: {csv_path}")
    with csv_path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        required = {
            "course", "bearing", "distance_m", "start", "end",
            "start_easting_m", "start_northing_m", "latitude_m",
            "departure_m", "end_easting_m", "end_northing_m", "status",
        }
        missing = required.difference(reader.fieldnames or [])
        if missing:
            raise ValueError(f"CSV is missing required column(s): {', '.join(sorted(missing))}")
        rows = [dict(row) for row in reader]
    if not rows:
        raise ValueError("Traverse CSV has no data rows.")
    return rows


def number(row: dict[str, str], field: str) -> float:
    try:
        return float(row[field])
    except (TypeError, ValueError) as exc:
        raise ValueError(f"Invalid numeric field {field!r} for course {row.get('course')!r}") from exc


def close(a: float, b: float, tolerance: float = 1e-5) -> bool:
    return abs(a - b) <= tolerance


def get_plot_data(rows: list[dict[str, str]]) -> dict:
    by_course = {row["course"].strip(): row for row in rows}
    missing = [course for course in GIVEN_COURSES if course not in by_course]
    if missing:
        raise ValueError(f"Missing required course row(s): {', '.join(missing)}")
    adjusted_rows = [row for row in rows if row["course"].strip().lower().startswith("5-1 adjusted")]
    original_rows = [row for row in rows if row["course"].strip().lower().startswith("5-1 original")]
    diagnostic_rows = [row for row in rows if "closure gap" in row["course"].strip().lower()]
    if len(adjusted_rows) != 1 or len(original_rows) != 1 or len(diagnostic_rows) != 1:
        raise ValueError("Expected exactly one adjusted P5-1, original P5-1, and diagnostic-gap row.")
    adjusted, original, diagnostic = adjusted_rows[0], original_rows[0], diagnostic_rows[0]
    courses = [by_course[name] for name in GIVEN_COURSES] + [adjusted]

    for current, following in zip(courses, courses[1:]):
        if not close(number(current, "end_easting_m"), number(following, "start_easting_m")):
            raise ValueError(f"East-coordinate discontinuity between {current['course']} and {following['course']}.")
        if not close(number(current, "end_northing_m"), number(following, "start_northing_m")):
            raise ValueError(f"North-coordinate discontinuity between {current['course']} and {following['course']}.")

    sum_lat = 0.0
    sum_dep = 0.0
    for row in courses[:4]:
        lat, dep = components(number(row, "distance_m"), row["bearing"])
        if not close(lat, number(row, "latitude_m")) or not close(dep, number(row, "departure_m")):
            raise ValueError(f"Recalculated components disagree with CSV for course {row['course']}.")
        sum_lat += lat
        sum_dep += dep

    adjusted_lat = number(adjusted, "end_northing_m") - number(adjusted, "start_northing_m")
    adjusted_dep = number(adjusted, "end_easting_m") - number(adjusted, "start_easting_m")
    if not close(adjusted_lat, number(adjusted, "latitude_m")) or not close(adjusted_dep, number(adjusted, "departure_m")):
        raise ValueError("Adjusted course components disagree with its stored coordinates.")
    if not close(sum_lat + adjusted_lat, 0.0, 2e-5) or not close(sum_dep + adjusted_dep, 0.0, 2e-5):
        raise ValueError("Adjusted traverse does not close within tolerance.")
    if not close(math.hypot(adjusted_lat, adjusted_dep), number(adjusted, "distance_m"), 2e-5):
        raise ValueError("Adjusted closing-course distance disagrees with its endpoints.")
    calc_lat, calc_dep = components(number(adjusted, "distance_m"), adjusted["bearing"])
    if not close(calc_lat, adjusted_lat, 5e-5) or not close(calc_dep, adjusted_dep, 5e-5):
        raise ValueError("Adjusted closing-course bearing/distance disagrees with its endpoint vector.")

    original_lat, original_dep = components(number(original, "distance_m"), original["bearing"])
    original_misclosure = math.hypot(sum_lat + original_lat, sum_dep + original_dep)
    if not close(original_misclosure, EXPECTED_ORIGINAL_MISCLOSURE_M, 2e-5):
        raise ValueError("Original traverse diagnostic misclosure differs from the recorded value.")
    if not close(number(diagnostic, "distance_m"), original_misclosure, 2e-5):
        raise ValueError("Diagnostic closure-gap length disagrees with recomputed original misclosure.")

    vertices = [
        (number(row, "start_easting_m"), number(row, "start_northing_m"), row["start"].strip())
        for row in courses
    ]
    if vertices[0][2] != "P1" or vertices[-1][2] != "P5":
        raise ValueError("Unexpected vertex order in traverse source data.")
    if not close(number(adjusted, "end_easting_m"), vertices[0][0]) or not close(
        number(adjusted, "end_northing_m"), vertices[0][1]
    ):
        raise ValueError("Adjusted course endpoint does not return to P1.")

    perimeter = sum(number(row, "distance_m") for row in courses)
    double_area = sum(
        current[0] * following[1] - following[0] * current[1]
        for current, following in zip(vertices, vertices[1:] + vertices[:1])
    )
    area_m2 = abs(double_area) / 2.0
    if not close(perimeter, EXPECTED_PERIMETER_M, 2e-5):
        raise ValueError(f"Adjusted perimeter differs from the recorded value: {perimeter:.6f} m.")
    if not close(area_m2, EXPECTED_AREA_M2, 0.002):
        raise ValueError(f"Adjusted polygon area differs from the recorded value: {area_m2:.4f} m².")

    return {
        "ordered_courses": courses,
        "vertices": vertices,
        "adjusted": adjusted,
        "original": original,
        "diagnostic": diagnostic,
        "original_misclosure_m": original_misclosure,
        "perimeter_m": perimeter,
        "area_m2": area_m2,
        "latitude_sum_m": sum_lat + adjusted_lat,
        "departure_sum_m": sum_dep + adjusted_dep,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--csv", type=Path, default=DEFAULT_CSV, help="Path to traverse-coordinate CSV.")
    args = parser.parse_args()
    try:
        plot = get_plot_data(load_rows(args.csv))
    except (FileNotFoundError, ValueError) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1

    print("PASS: original, adjusted, and diagnostic rows are present.")
    print("PASS: first four course components match source bearings and distances.")
    print(
        f"PASS: adjusted closure = {plot['latitude_sum_m']:+.6f} m latitude, "
        f"{plot['departure_sum_m']:+.6f} m departure."
    )
    print(f"PASS: perimeter = {plot['perimeter_m']:.6f} m; area = {plot['area_m2']:.4f} m².")
    print(f"INFO: original unadjusted misclosure = {plot['original_misclosure_m']:.6f} m.")
    print("INFO: 300.00 m² is approximate; the calculated adjusted polygon area is checked independently.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
