# === Stage 52: Add clearer docstrings for public helper functions ===
# Project: RoutePlanner
def get_stop_by_id(route, stop_id):
    """Return the stop whose id matches stop_id, or None if not found."""
    for stop in route.get("stops", []):
        if stop.get("id") == stop_id:
            return stop
    return None


def get_stops_by_status(route, status):
    """Return all stops in route that have the given status value."""
    return [stop for stop in route.get("stops", []) if stop.get("status") == status]


def get_stops_by_distance_range(route, min_distance, max_distance):
    """Return stops whose distance falls within the inclusive min and max range."""
    return [
        stop
        for stop in route.get("stops", [])
        if min_distance <= stop.get("distance", 0) <= max_distance
    ]


def get_stops_with_notes(route):
    """Return only the stops that have a non-empty completion note."""
    return [
        stop
        for stop in route.get("stops", [])
        if stop.get("note")
    ]


def get_stops_by_schedule(route, day, time_slot):
    """Return stops scheduled for the given day and time slot."""
    return [
        stop
        for stop in route.get("stops", [])
        if stop.get("schedule", {}).get("day") == day
        and stop.get("schedule", {}).get("time_slot") == time_slot
    ]
