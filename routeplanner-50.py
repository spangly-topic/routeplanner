# === Stage 50: Add unit tests for import and export behavior ===
# Project: RoutePlanner
import json
from routeplanner import RoutePlanner

def test_import_export():
    planner = RoutePlanner()
    planner.add_stop("Home", 0, 0)
    planner.add_stop("Shop", 5, 3)
    planner.add_stop("Office", 12, 7)
    planner.set_schedule("Mon 8-12", "Tue 9-13")
    planner.add_note("Delivered on time", "Home")

    data = planner.export()
    assert isinstance(data, dict)
    assert "stops" in data
    assert len(data["stops"]) == 3
    assert data["stops"][0]["name"] == "Home"
    assert data["stops"][1]["distance"] == 5
    assert "schedule" in data
    assert data["schedule"] == "Mon 8-12"
    assert "notes" in data
    assert data["notes"][0]["stop"] == "Home"
    assert data["notes"][0]["text"] == "Delivered on time"

    planner2 = RoutePlanner()
    planner2.import_data(data)
    assert len(planner2.get_stops()) == 3
    assert planner2.get_schedule() == "Mon 8-12"
    assert planner2.get_note_by_stop("Home") == "Delivered on time"

    planner3 = RoutePlanner()
    planner3.add_stop("Home", 0, 0)
    planner3.add_stop("Shop", 5, 3)
    planner3.add_stop("Office", 12, 7)
    planner3.set_schedule("Mon 8-12", "Tue 9-13")
    planner3.add_note("Delivered on time", "Home")
    planner3.add_note("Late arrival", "Office")

    json_str = planner3.export_json()
    assert isinstance(json_str, str)
    assert len(json_str) > 0

    planner4 = RoutePlanner()
    planner4.import_json(json_str)
    assert len(planner4.get_stops()) == 3
    assert planner4.get_schedule() == "Mon 8-12"
    assert planner4.get_note_by_stop("Home") == "Delivered on time"
    assert planner4.get_note_by_stop("Office") == "Late arrival"
