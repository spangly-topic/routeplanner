# === Stage 49: Add unit tests for update and delete edge cases ===
# Project: RoutePlanner
import unittest
from route_planner import RoutePlanner

class TestUpdateDelete(unittest.TestCase):
    def setUp(self):
        self.planner = RoutePlanner()
        self.planner.add_stop("A", "2024-01-01", 10, "First delivery")
        self.planner.add_stop("B", "2024-01-02", 15, "Second delivery")
        self.planner.add_stop("C", "2024-01-03", 5, "Third delivery")

    def test_update_valid_stop(self):
        self.planner.update_stop("A", "2024-02-01", 20, "Updated first delivery")
        stops = self.planner.get_stops()
        self.assertEqual(stops["A"]["distance"], 20)
        self.assertEqual(stops["A"]["completion_note"], "Updated first delivery")
        self.assertEqual(stops["A"]["scheduled_date"], "2024-02-01")

    def test_update_nonexistent_stop(self):
        self.planner.update_stop("Z", "2024-02-01", 20, "Should fail")
        stops = self.planner.get_stops()
        self.assertNotIn("Z", stops)

    def test_delete_valid_stop(self):
        self.planner.delete_stop("B")
        stops = self.planner.get_stops()
        self.assertNotIn("B", stops)
        self.assertIn("A", stops)
        self.assertIn("C", stops)

    def test_delete_nonexistent_stop(self):
        self.planner.delete_stop("Z")
        stops = self.planner.get_stops()
        self.assertIn("A", stops)
        self.assertIn("B", stops)
        self.assertIn("C", stops)

    def test_update_then_delete(self):
        self.planner.update_stop("A", "2024-02-01", 20, "Updated")
        self.planner.delete_stop("A")
        stops = self.planner.get_stops()
        self.assertNotIn("A", stops)
        self.assertIn("B", stops)
        self.assertIn("C", stops)

    def test_delete_then_update(self):
        self.planner.delete_stop("B")
        self.planner.update_stop("Z", "2024-02-01", 20, "Should fail")
        stops = self.planner.get_stops()
        self.assertNotIn("Z", stops)
        self.assertIn("A", stops)
        self.assertIn("C", stops)

if __name__ == "__main__":
    unittest.main()
