# === Stage 51: Add unit tests for search and filter behavior ===
# Project: RoutePlanner
def test_search_by_name():
    stops = [
        Stop("North Hub", 10, 0.0),
        Stop("South Depot", 20, 5.0),
    ]
    found = find_stop_by_name(stops, "south")
    assert found is not None
    assert found.name == "South Depot"


def test_search_no_match():
    stops = [Stop("Alpha", 1, 0.0)]
    result = find_stop_by_name(stops, "omega")
    assert result is None


def test_filter_by_distance_max():
    stops = [
        Stop("A", 5, 0.0),
        Stop("B", 15, 1.0),
        Stop("C", 25, 2.0),
    ]
    within = filter_stops_within_distance(stops, 10)
    assert len(within) == 1
    assert within[0].name == "A"


def test_filter_by_status():
    stops = [
        Stop("Pending", 1, 0.0, "pending"),
        Stop("Done", 2, 1.0, "completed"),
    ]
    pending = filter_stops_by_status(stops, "pending")
    assert len(pending) == 1
    assert pending[0].name == "Pending"
