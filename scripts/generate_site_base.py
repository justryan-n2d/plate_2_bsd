#!/usr/bin/env python3
"""Generate metre-unit DXF and matching SVG from the Phase 1 traverse CSV."""

from __future__ import annotations

import argparse
import html
import math
import sys
from pathlib import Path

import ezdxf

from validate_site_base import DEFAULT_CSV, get_plot_data, load_rows

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DXF = ROOT / "drawings" / "phase1_site_base.dxf"
DEFAULT_SVG = ROOT / "previews" / "phase1_site_base_preview.svg"


def add_text(msp, text: str, position: tuple[float, float], height: float, layer: str, rotation: float = 0.0) -> None:
    entity = msp.add_text(text, dxfattribs={"height": height, "layer": layer, "rotation": rotation})
    entity.dxf.insert = position


def make_dxf(csv_path: Path, output_path: Path) -> dict:
    plot = get_plot_data(load_rows(csv_path))
    vertices = plot["vertices"]
    courses = plot["ordered_courses"]
    doc = ezdxf.new("R2013")
    doc.units = ezdxf.units.M
    doc.header["$MEASUREMENT"] = 1
    for name, color, lineweight in [
        ("PROPERTY_BOUNDARY", 7, 35),
        ("VERTEX_MARKERS", 3, 25),
        ("VERTEX_LABELS", 3, 18),
        ("COURSE_LABELS", 5, 13),
        ("ANNOTATIONS", 7, 13),
        ("NORTH_ARROW", 7, 25),
        ("REFERENCE_NOTES", 1, 13),
    ]:
        doc.layers.new(name, dxfattribs={"color": color, "lineweight": lineweight})

    msp = doc.modelspace()
    coords = [(east, north) for east, north, _name in vertices]
    msp.add_lwpolyline(coords, close=True, dxfattribs={"layer": "PROPERTY_BOUNDARY"})
    for east, north, name in vertices:
        msp.add_circle((east, north), radius=0.10, dxfattribs={"layer": "VERTEX_MARKERS"})
        add_text(msp, name, (east + 0.16, north + 0.16), 0.24, "VERTEX_LABELS")

    for start, end, row in zip(vertices, vertices[1:] + vertices[:1], courses):
        x1, y1 = start[0], start[1]
        x2, y2 = end[0], end[1]
        dx, dy = x2 - x1, y2 - y1
        length = math.hypot(dx, dy)
        angle = math.degrees(math.atan2(dy, dx))
        if angle > 90.0:
            angle -= 180.0
        elif angle < -90.0:
            angle += 180.0
        normal_x, normal_y = (-dy / length, dx / length) if length else (0.0, 0.0)
        label_x = (x1 + x2) / 2.0 + normal_x * 0.35
        label_y = (y1 + y2) / 2.0 + normal_y * 0.35
        label = f"{row['course']} | {row['bearing']} | {float(row['distance_m']):.2f} m"
        add_text(msp, label, (label_x, label_y), 0.18, "COURSE_LABELS", angle)

    min_e = min(point[0] for point in vertices)
    max_e = max(point[0] for point in vertices)
    min_n = min(point[1] for point in vertices)
    max_n = max(point[1] for point in vertices)
    add_text(msp, "PLATE NO. 2 - PHASE 1 SITE BASE", (min_e, max_n + 2.0), 0.40, "ANNOTATIONS")
    add_text(msp, "Local coordinates in metres; P1 = (0,0).", (min_e, max_n + 1.35), 0.22, "ANNOTATIONS")
    notes = [
        "Original P5-1: N 08°10' W, 16.35 m (reference only).",
        "Adjusted P5-1: N 06°02'11'' E, 15.795414 m.",
        f"Closed perimeter: {plot['perimeter_m']:.4f} m.",
        f"Calculated closed-polygon area: {plot['area_m2']:.2f} m2.",
        "Assignment approximate area: 300.00 m2; not an equality target.",
        "Road cross-section per instructor: 8.00 m RROW = 5.00 m road + 1.50 m strip each side.",
    ]
    for i, note in enumerate(notes):
        add_text(msp, note, (max_e + 2.0, max_n + 1.0 - i * 0.45), 0.22, "REFERENCE_NOTES")
    add_text(msp, "PRELIMINARY ACADEMIC PLOT - not cadastral or construction certification.", (min_e, min_n - 1.0), 0.22, "REFERENCE_NOTES")

    arrow_x, arrow_base_y, arrow_top_y = min_e - 1.8, max_n - 1.6, max_n + 0.4
    msp.add_line((arrow_x, arrow_base_y), (arrow_x, arrow_top_y), dxfattribs={"layer": "NORTH_ARROW"})
    msp.add_line((arrow_x, arrow_top_y), (arrow_x - 0.22, arrow_top_y - 0.35), dxfattribs={"layer": "NORTH_ARROW"})
    msp.add_line((arrow_x, arrow_top_y), (arrow_x + 0.22, arrow_top_y - 0.35), dxfattribs={"layer": "NORTH_ARROW"})
    add_text(msp, "N", (arrow_x - 0.12, arrow_top_y + 0.15), 0.25, "NORTH_ARROW")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    doc.saveas(output_path)
    return plot


def make_svg(csv_path: Path, output_path: Path) -> dict:
    plot = get_plot_data(load_rows(csv_path))
    vertices, courses = plot["vertices"], plot["ordered_courses"]
    width, height = 1200, 760
    east_values = [point[0] for point in vertices]
    north_values = [point[1] for point in vertices]
    center_e = (min(east_values) + max(east_values)) / 2.0
    center_n = (min(north_values) + max(north_values)) / 2.0
    scale = min(440.0 / (max(east_values) - min(east_values)), 420.0 / (max(north_values) - min(north_values)))

    def xy(east: float, north: float) -> tuple[float, float]:
        return 300.0 + (east - center_e) * scale, 405.0 - (north - center_n) * scale

    points_xy = [xy(point[0], point[1]) for point in vertices]
    polygon_points = " ".join(f"{x:.2f},{y:.2f}" for x, y in points_xy)
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
        "<title>Generated Phase 1 site base, Lot 245-B</title>",
        "<desc>Generated from site/phase1_traverse_coordinates.csv. Geometry uses the adjusted closing course.</desc>",
        "<style>text{font-family:Arial,Helvetica,sans-serif;fill:#172033}.title{font-size:27px;font-weight:700}.sub{font-size:16px;fill:#475569}.head{font-size:18px;font-weight:700}.body{font-size:15px}.small{font-size:12px;fill:#475569}</style>",
        '<rect width="1200" height="760" fill="#fff"/>',
        '<text class="title" x="42" y="48">PLATE NO. 2 | GENERATED PHASE 1 SITE BASE</text>',
        '<text class="sub" x="42" y="77">Lot 245-B | Barangay San Isidro, Palo, Leyte</text>',
        f'<polygon points="{polygon_points}" fill="#eff6ff" stroke="#172033" stroke-width="3.2" stroke-linejoin="round"/>',
    ]
    for point, (x, y) in zip(vertices, points_xy):
        parts.append(f'<circle cx="{x:.2f}" cy="{y:.2f}" r="5" fill="#fff" stroke="#15803d" stroke-width="2"/>')
        parts.append(f'<text class="small" x="{x + 8:.2f}" y="{y - 8:.2f}">{html.escape(point[2])}</text>')

    bar_length = scale * 5.0
    parts.extend([
        '<line x1="555" y1="265" x2="555" y2="205" stroke="#172033" stroke-width="3"/>',
        '<path d="M555 194 L546 211 L555 207 L564 211 Z" fill="#172033"/>',
        '<text x="549" y="185" font-size="18" font-weight="700">N</text>',
        f'<line x1="42" y1="700" x2="{42 + bar_length:.2f}" y2="700" stroke="#172033" stroke-width="4"/>',
        '<line x1="42" y1="692" x2="42" y2="708" stroke="#172033" stroke-width="2"/>',
        f'<line x1="{42 + bar_length:.2f}" y1="692" x2="{42 + bar_length:.2f}" y2="708" stroke="#172033" stroke-width="2"/>',
        '<text class="small" x="42" y="722">0</text>',
        f'<text class="small" x="{max(42 + bar_length - 18, 70):.2f}" y="722">5 m</text>',
        '<text class="small" x="42" y="744">Graphic scale for preview only; inspect CAD model units for measurements.</text>',
        '<line x1="650" y1="110" x2="650" y2="710" stroke="#cbd5e1" stroke-width="1.5"/>',
        '<text class="head" x="690" y="135">TRAVERSE COURSES USED</text>',
    ])
    y = 170
    for row in courses:
        label = f"{row['course']}: {row['bearing']} | {float(row['distance_m']):.4f} m"
        parts.append(f'<text class="body" x="690" y="{y}">{html.escape(label)}</text>')
        y += 34
    notes = [
        f"Adjusted closed perimeter: {plot['perimeter_m']:.4f} m",
        f"Calculated closed area: {plot['area_m2']:.2f} m²",
        "Assignment approximate area: 300.00 m²",
        "The approximate area is not forced onto the plot.",
        "Original P5-1: N 08°10′ W, 16.35 m (reference only)",
        "Adjusted P5-1: N 06°02′11″ E, 15.795414 m",
        "RROW total: 8.00 m = road 5.00 m + side strips 1.50 m each.",
        "Instructor-provided allocation; side strips are not assigned a specific use.",
        "Local coordinates, with P1 at (0,0); not georeferenced.",
        "Preliminary academic plot; not survey certification.",
    ]
    y += 15
    parts.append(f'<text class="head" x="690" y="{y}">NOTES</text>')
    y += 28
    for note in notes:
        parts.append(f'<text class="body" x="690" y="{y}">{html.escape(note)}</text>')
        y += 28
    parts.append("</svg>")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("\n".join(parts) + "\n", encoding="utf-8")
    return plot


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--csv", type=Path, default=DEFAULT_CSV, help="Path to traverse-coordinate CSV.")
    parser.add_argument("--dxf", type=Path, default=DEFAULT_DXF, help="Output DXF path.")
    parser.add_argument("--svg", type=Path, default=DEFAULT_SVG, help="Output SVG preview path.")
    parser.add_argument("--dxf-only", action="store_true", help="Generate DXF but skip the SVG preview.")
    args = parser.parse_args()
    try:
        plot = get_plot_data(load_rows(args.csv))
        if not args.dxf_only:
            make_svg(args.csv, args.svg)
        make_dxf(args.csv, args.dxf)
    except (FileNotFoundError, ValueError, OSError, ezdxf.DXFError) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1

    print(f"PASS: generated DXF at {args.dxf}")
    if not args.dxf_only:
        print(f"PASS: generated SVG preview at {args.svg}")
    print(f"INFO: perimeter {plot['perimeter_m']:.4f} m; area {plot['area_m2']:.2f} m².")
    print("NEXT: open the DXF in compatible CAD software and inspect units, linework, labels, and plot scale.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
