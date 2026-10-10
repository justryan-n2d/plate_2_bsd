#!/usr/bin/env python3
"""Validate a generated DXF and SVG against the Phase 1 source CSV."""

from __future__ import annotations

import argparse
import math
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

import ezdxf

from validate_site_base import DEFAULT_CSV, close, get_plot_data, load_rows

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DXF = ROOT / "drawings" / "phase1_site_base.dxf"
DEFAULT_SVG = ROOT / "previews" / "phase1_site_base_preview.svg"

REQUIRED_LAYERS = {
    "PROPERTY_BOUNDARY",
    "VERTEX_MARKERS",
    "VERTEX_LABELS",
    "COURSE_LABELS",
    "ANNOTATIONS",
    "NORTH_ARROW",
    "REFERENCE_NOTES",
}
REQUIRED_DXF_NOTES = (
    "Original P5-1:",
    "Adjusted P5-1:",
    "Closed perimeter:",
    "Calculated closed-polygon area:",
    "Assignment approximate area:",
    "Road width 5.0 m; total ROW 8.00 m;",
    "PRELIMINARY ACADEMIC PLOT",
)
REQUIRED_SVG_NOTES = (
    "Original P5-1:",
    "Adjusted P5-1:",
    "Assignment approximate area: 300.00 m²",
    "Road width: 5.0 m | total ROW: 8.00 m",
    "Preliminary academic plot; not survey certification.",
)


def polygon_area(points: list[tuple[float, float]]) -> float:
    if len(points) < 3:
        raise ValueError("A parcel outline needs at least three vertices.")
    twice_area = sum(
        x1 * y2 - x2 * y1
        for (x1, y1), (x2, y2) in zip(points, points[1:] + points[:1])
    )
    return abs(twice_area) / 2.0


def polyline_perimeter(points: list[tuple[float, float]]) -> float:
    return sum(
        math.hypot(x2 - x1, y2 - y1)
        for (x1, y1), (x2, y2) in zip(points, points[1:] + points[:1])
    )


def validate_dxf(dxf_path: Path, source_plot: dict) -> list[str]:
    if not dxf_path.is_file():
        raise FileNotFoundError(f"Generated DXF not found: {dxf_path}")

    try:
        doc = ezdxf.readfile(dxf_path)
    except (OSError, ezdxf.DXFError) as exc:
        raise ValueError(f"Cannot read generated DXF: {exc}") from exc

    auditor = doc.audit()
    if auditor.has_errors:
        sample_errors = "; ".join(str(error) for error in auditor.errors[:5])
        raise ValueError(f"DXF structural audit reported errors: {sample_errors}")

    if doc.header.get("$INSUNITS", 0) != ezdxf.units.M:
        raise ValueError(
            f"DXF model units must be metres ($INSUNITS={ezdxf.units.M}); "
            f"found {doc.header.get('$INSUNITS', 0)!r}."
        )

    missing_layers = REQUIRED_LAYERS.difference(set(doc.layers.entries.keys()))
    # Some ezdxf releases expose layer entries differently; use the public
    # layer collection as a fallback if necessary.
    if missing_layers:
        available_layers = {layer.dxf.name for layer in doc.layers}
        missing_layers = REQUIRED_LAYERS.difference(available_layers)
    if missing_layers:
        raise ValueError(f"DXF missing required layers: {', '.join(sorted(missing_layers))}")

    msp = doc.modelspace()
    boundary_entities = [
        entity
        for entity in msp
        if entity.dxftype() == "LWPOLYLINE"
        and entity.dxf.get("layer", "0") == "PROPERTY_BOUNDARY"
    ]
    if len(boundary_entities) != 1:
        raise ValueError(
            "Expected exactly one LWPOLYLINE on PROPERTY_BOUNDARY; "
            f"found {len(boundary_entities)}."
        )
    boundary = boundary_entities[0]
    if not (int(boundary.dxf.get("flags", 0)) & 1):
        raise ValueError("The DXF property boundary polyline is not closed.")

    actual_points = [(float(x), float(y)) for x, y in boundary.get_points("xy")]
    expected_points = [(float(east), float(north)) for east, north, _name in source_plot["vertices"]]
    if len(actual_points) != len(expected_points):
        raise ValueError(
            f"Boundary vertex count mismatch: DXF has {len(actual_points)}, "
            f"CSV expects {len(expected_points)}."
        )
    for index, (actual, expected) in enumerate(zip(actual_points, expected_points), start=1):
        if not close(actual[0], expected[0], 1e-6) or not close(actual[1], expected[1], 1e-6):
            raise ValueError(
                f"DXF vertex {index} differs from source CSV: "
                f"DXF={actual}, CSV={expected}."
            )

    expected_count = 5
    if len(actual_points) != expected_count:
        raise ValueError(f"Expected {expected_count} parcel vertices; found {len(actual_points)}.")

    closed_perimeter = polyline_perimeter(actual_points)
    closed_area = polygon_area(actual_points)
    if not close(closed_perimeter, source_plot["perimeter_m"], 2e-5):
        raise ValueError(
            f"DXF perimeter {closed_perimeter:.6f} m does not match "
            f"source value {source_plot['perimeter_m']:.6f} m."
        )
    if not close(closed_area, source_plot["area_m2"], 0.002):
        raise ValueError(
            f"DXF area {closed_area:.4f} m² does not match "
            f"source value {source_plot['area_m2']:.4f} m²."
        )

    circles = [
        entity for entity in msp
        if entity.dxftype() == "CIRCLE"
        and entity.dxf.get("layer", "0") == "VERTEX_MARKERS"
    ]
    if len(circles) != expected_count:
        raise ValueError(f"Expected {expected_count} vertex markers; found {len(circles)}.")

    course_labels = [
        entity for entity in msp
        if entity.dxftype() == "TEXT"
        and entity.dxf.get("layer", "0") == "COURSE_LABELS"
    ]
    if len(course_labels) != expected_count:
        raise ValueError(f"Expected {expected_count} course labels; found {len(course_labels)}.")

    vertex_labels = [
        entity for entity in msp
        if entity.dxftype() == "TEXT"
        and entity.dxf.get("layer", "0") == "VERTEX_LABELS"
    ]
    if len(vertex_labels) != expected_count:
        raise ValueError(f"Expected {expected_count} vertex labels; found {len(vertex_labels)}.")

    all_text = "\n".join(
        entity.dxf.get("text", "")
        for entity in msp
        if entity.dxftype() in {"TEXT", "MTEXT"}
    )
    missing_notes = [note for note in REQUIRED_DXF_NOTES if note not in all_text]
    if missing_notes:
        raise ValueError(f"DXF is missing required note(s): {', '.join(missing_notes)}")

    return [
        f"PASS: DXF opens and audit reports no structural errors.",
        f"PASS: DXF model-space units are metres and required layers are present.",
        f"PASS: one closed parcel polyline has {len(actual_points)} vertices matching the source CSV.",
        f"PASS: DXF perimeter = {closed_perimeter:.6f} m; area = {closed_area:.4f} m².",
        f"PASS: {expected_count} vertex markers, {expected_count} vertex labels, and {expected_count} course labels found.",
        "PASS: DXF retains original/adjusted course, area, road/ROW, and preliminary-status notes.",
    ]


def validate_svg(svg_path: Path) -> list[str]:
    if not svg_path.is_file():
        raise FileNotFoundError(f"Generated SVG preview not found: {svg_path}")
    try:
        root = ET.parse(svg_path).getroot()
    except (ET.ParseError, OSError) as exc:
        raise ValueError(f"Cannot parse generated SVG: {exc}") from exc
    if not root.tag.endswith("svg"):
        raise ValueError(f"Preview root element is not SVG: {root.tag!r}")

    namespace = {"svg": "http://www.w3.org/2000/svg"}
    polygons = root.findall(".//svg:polygon", namespace)
    if len(polygons) != 1:
        raise ValueError(f"Expected exactly one generated parcel polygon in SVG; found {len(polygons)}.")
    points = polygons[0].attrib.get("points", "").strip().split()
    if len(points) != 5:
        raise ValueError(f"Expected five parcel vertices in generated SVG; found {len(points)}.")

    text_content = " ".join(part.strip() for part in root.itertext() if part.strip())
    missing_notes = [note for note in REQUIRED_SVG_NOTES if note not in text_content]
    if missing_notes:
        raise ValueError(f"SVG preview is missing required note(s): {', '.join(missing_notes)}")
    return [
        "PASS: generated SVG is well-formed XML and has one parcel polygon with five vertices.",
        "PASS: SVG preview includes original/adjusted course, approximate area, road/ROW, and status notes.",
    ]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--csv", type=Path, default=DEFAULT_CSV, help="Source traverse CSV.")
    parser.add_argument("--dxf", type=Path, default=DEFAULT_DXF, help="Generated DXF to validate.")
    parser.add_argument("--svg", type=Path, default=DEFAULT_SVG, help="Generated SVG preview to validate.")
    parser.add_argument("--dxf-only", action="store_true", help="Skip SVG validation.")
    args = parser.parse_args()

    try:
        plot = get_plot_data(load_rows(args.csv))
        messages = validate_dxf(args.dxf, plot)
        if not args.dxf_only:
            messages.extend(validate_svg(args.svg))
    except (FileNotFoundError, ValueError, OSError, ezdxf.DXFError) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1

    for message in messages:
        print(message)
    print("PASS: generated drawing validation completed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
