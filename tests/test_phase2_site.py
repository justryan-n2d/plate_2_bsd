import unittest

from scripts.calculate_phase2_site import (
    DEFAULT_SETBACKS,
    DEFAULT_TRAVERSE,
    build_phase2_report,
    build_preliminary_envelope_scenarios_report,
    calculate_preliminary_envelope_scenarios,
    calculate_maximum_occupancy,
    calculate_preliminary_parking_slots,
    inset_convex_polygon,
    load_boundary_inputs,
    load_code_requirements,
    load_traverse,
    polygon_area,
    parking_slot_geometry,
    resolve_buildable_envelope,
)


class Phase2SiteCalculationTests(unittest.TestCase):
    def test_corner_lot_occupancy_limit_uses_calculated_area(self):
        result = calculate_maximum_occupancy(265.2598, "corner")
        self.assertAlmostEqual(result["maximum_occupancy_m2"], 238.73382, places=5)
        self.assertAlmostEqual(result["minimum_open_space_m2"], 26.52598, places=5)
        self.assertEqual(result["factor"], 0.90)

    def test_inside_lot_occupancy_limit_is_eighty_percent(self):
        result = calculate_maximum_occupancy(265.2598, "inside")
        self.assertAlmostEqual(result["maximum_occupancy_m2"], 212.20784, places=5)
        self.assertAlmostEqual(result["minimum_open_space_m2"], 53.05196, places=5)

    def test_inset_polygon_respects_each_edge_offset(self):
        square = [(0.0, 0.0), (10.0, 0.0), (10.0, 10.0), (0.0, 10.0)]
        inset = inset_convex_polygon(square, [2.0, 2.0, 2.0, 2.0])
        self.assertEqual(len(inset), 4)
        self.assertAlmostEqual(polygon_area(inset), 36.0, places=6)
        self.assertTrue(all(2.0 - 1e-6 <= x <= 8.0 + 1e-6 for x, _ in inset))
        self.assertTrue(all(2.0 - 1e-6 <= y <= 8.0 + 1e-6 for _, y in inset))

    def test_missing_road_reference_offset_prevents_final_envelope(self):
        vertices = [(0.0, 0.0), (10.0, 0.0), (10.0, 10.0), (0.0, 10.0)]
        offsets = [2.0, 2.0, None, 2.0]
        envelope = resolve_buildable_envelope(vertices, offsets)
        self.assertIsNone(envelope["vertices"])
        self.assertIsNone(envelope["area_m2"])
        self.assertIn("missing", envelope["status"].lower())

    def test_preliminary_parking_for_this_lot_area_is_one_slot(self):
        self.assertEqual(calculate_preliminary_parking_slots(265.2598), 1)
        self.assertEqual(calculate_preliminary_parking_slots(120.01), 1)
        self.assertIsNone(calculate_preliminary_parking_slots(120.0))

    def test_parking_slot_dimensions_match_2004_irr_values(self):
        perpendicular = parking_slot_geometry("perpendicular")
        self.assertEqual(perpendicular["width_m"], 2.50)
        self.assertEqual(perpendicular["length_m"], 5.00)
        self.assertAlmostEqual(perpendicular["area_m2"], 12.50)

        parallel = parking_slot_geometry("parallel")
        self.assertEqual(parallel["width_m"], 2.15)
        self.assertEqual(parallel["length_m"], 6.00)
        self.assertAlmostEqual(parallel["area_m2"], 12.90)

        with self.assertRaises(ValueError):
            parking_slot_geometry("angled")

    def test_repository_inputs_select_working_academic_envelope(self):
        traverse = load_traverse(DEFAULT_TRAVERSE)
        boundaries = load_boundary_inputs(DEFAULT_SETBACKS)
        envelope = resolve_buildable_envelope(
            traverse["vertices"], [row["geometry_inset_m"] for row in boundaries]
        )
        self.assertAlmostEqual(traverse["area_m2"], 265.2598, places=3)
        self.assertAlmostEqual(traverse["perimeter_m"], 64.145414, places=4)
        self.assertAlmostEqual(envelope["area_m2"], 152.430851, places=5)
        self.assertEqual(envelope["missing_edge_indices"], [])
        self.assertTrue(all(row["geometry_inset_m"] == 2.0 for row in boundaries))
        self.assertTrue(all(row["status"] == "working academic baseline" for row in boundaries))

        road_rows = [row for row in boundaries if row["edge_type"] == "road frontage"]
        self.assertEqual(len(road_rows), 2)
        for row in road_rows:
            self.assertIn("8.00 m total RROW = 5.00 m carriageway + 1.50 m strip on each side", row["notes"])
            self.assertIn("formal lot-line/RROW alignment", row["notes"])
            self.assertNotIn("allocation is pending", row["notes"].lower())

    def test_preliminary_envelope_scenario_areas_are_reproducible(self):
        traverse = load_traverse(DEFAULT_TRAVERSE)
        scenarios = calculate_preliminary_envelope_scenarios(traverse["vertices"])
        areas = {item["scenario_id"]: item["area_m2"] for item in scenarios}
        self.assertAlmostEqual(areas["A"], 152.430851, places=5)
        self.assertAlmostEqual(areas["B"], 128.898939, places=5)
        self.assertAlmostEqual(areas["C"], 125.015904, places=5)
        self.assertAlmostEqual(areas["D"], 112.290926, places=5)
        self.assertEqual(scenarios[0]["offsets_m"], [2.0, 2.0, 2.0, 2.0, 2.0])
        self.assertEqual(scenarios[3]["offsets_m"], [2.0, 2.0, 4.5, 4.5, 2.0])

    def test_scenario_report_is_current_and_uses_selected_working_basis(self):
        traverse = load_traverse(DEFAULT_TRAVERSE)
        expected = build_preliminary_envelope_scenarios_report(traverse["vertices"])
        report_path = DEFAULT_TRAVERSE.parent.parent / "calculations" / "phase2_envelope_scenarios.md"
        self.assertEqual(report_path.read_text(encoding="utf-8"), expected)
        self.assertIn("Scenario A is selected as the working envelope for Phase 3", expected)
        self.assertIn("8.00 m total RROW = 5.00 m carriageway + 1.50 m strip on each side", expected)
        self.assertIn("152.43 m²", expected)

    def test_negative_offsets_are_rejected(self):
        square = [(0.0, 0.0), (10.0, 0.0), (10.0, 10.0), (0.0, 10.0)]
        with self.assertRaises(ValueError):
            inset_convex_polygon(square, [2.0, -1.0, 2.0, 2.0])

    def test_code_requirements_register_has_unique_traceable_rows(self):
        rows = load_code_requirements(DEFAULT_TRAVERSE.parent / "phase2_code_requirements.csv")
        ids = [row["requirement_id"] for row in rows]
        self.assertGreaterEqual(len(rows), 12)
        self.assertEqual(len(ids), len(set(ids)))
        self.assertIn("P2-05", ids)  # road centerline / right-of-way geometry
        self.assertIn("P2-07", ids)  # perpendicular / diagonal parking dimensions
        self.assertTrue(all(row["topic"].strip() for row in rows))
        self.assertTrue(all(row["status"].strip() for row in rows))

    def test_clockwise_and_counterclockwise_polygon_insets_have_same_area(self):
        ccw = [(0.0, 0.0), (10.0, 0.0), (10.0, 10.0), (0.0, 10.0)]
        cw = list(reversed(ccw))
        self.assertAlmostEqual(polygon_area(inset_convex_polygon(ccw, [2, 2, 2, 2])), 36.0)
        self.assertAlmostEqual(polygon_area(inset_convex_polygon(cw, [2, 2, 2, 2])), 36.0)

    def test_report_preserves_area_difference_and_does_not_fabricate_envelope(self):
        report = build_phase2_report(
            area_m2=265.2598,
            stated_approximate_area_m2=300.0,
            perimeter_m=64.145414,
            boundary_rows=[{
                "boundary_course": "3-4",
                "adjacency": "road",
                "geometry_inset_m": None,
                "code_clearance_m": 2.0,
                "status": "geometry pending",
                "notes": "road centerline not located",
            }],
            corner_occupancy=calculate_maximum_occupancy(265.2598, "corner"),
            inside_occupancy=calculate_maximum_occupancy(265.2598, "inside"),
            envelope={
                "vertices": None,
                "area_m2": None,
                "status": "Incomplete: missing road reference offsets",
            },
        )
        self.assertIn("265.26 m²", report)
        self.assertIn("300.00 m²", report)
        self.assertIn("34.74 m²", report)
        self.assertIn("NOT CALCULATED", report)


if __name__ == "__main__":
    unittest.main()
