# === Stage 48: Add small unit tests for creation and validation helpers ===
# Project: RoutePlanner
import unittest
from route_planner.stops import Stop
from route_planner.schedules import Schedule
from route_planner.distances import Distance
from route_planner.completion import Completion

class TestStops(unittest.TestCase):
    def test_create_stop(self):
        stop = Stop("Home", 10.0, 5.0, "Residential")
        self.assertEqual(stop.name, "Home")
        self.assertEqual(stop.lat, 10.0)
        self.assertEqual(stop.lon, 5.0)
        self.assertEqual(stop.type, "Residential")

    def test_validate_stop_invalid(self):
        with self.assertRaises(ValueError):
            Stop("", 0, 0, "")

class TestSchedules(unittest.TestCase):
    def test_create_schedule(self):
        schedule = Schedule("Mon", "2023-01-01", "2023-01-31")
        self.assertEqual(schedule.day, "Mon")
        self.assertEqual(schedule.start, "2023-01-01")
        self.assertEqual(schedule.end, "2023-01-31")

    def test_validate_schedule_invalid(self):
        with self.assertRaises(ValueError):
            Schedule("InvalidDay", "2023-01-01", "2023-01-31")

class TestDistances(unittest.TestCase):
    def test_create_distance(self):
        dist = Distance("StopA", "StopB", 5.5)
        self.assertEqual(dist.from_stop, "StopA")
        self.assertEqual(dist.to_stop, "StopB")
        self.assertEqual(dist.value, 5.5)

    def test_validate_distance_invalid(self):
        with self.assertRaises(ValueError):
            Distance("StopA", "StopB", -1.0)

class TestCompletion(unittest.TestCase):
    def test_create_completion(self):
        comp = Completion("Order123", "2023-01-15", "Delivered")
        self.assertEqual(comp.order_id, "Order123")
        self.assertEqual(comp.date, "2023-01-15")
        self.assertEqual(comp.status, "Delivered")

    def test_validate_completion_invalid(self):
        with self.assertRaises(ValueError):
            Completion("Order123", "2023-01-15", "InvalidStatus")

if __name__ == "__main__":
    unittest.main()
