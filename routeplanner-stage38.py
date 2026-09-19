# === Stage 38: Add data integrity checks for broken references ===
# Project: RoutePlanner
def check_references(route):
    if not isinstance(route, dict):
        raise ValueError("Route must be a dictionary")
    required_keys = ["stops", "schedule", "distances", "completion_notes"]
    missing = [k for k in required_keys if k not in route]
    if missing:
        raise ValueError(f"Missing required fields: {', '.join(missing)}")
    if not isinstance(route["stops"], list) or len(route["stops"]) == 0:
        raise ValueError("Stops must be a non-empty list")
    for stop in route["stops"]:
        if not isinstance(stop, dict) or "name" not in stop:
            raise ValueError("Each stop must be a dict with a 'name' key")
    if not isinstance(route["schedule"], list) or len(route["schedule"]) != len(route["stops"]):
        raise ValueError("Schedule length must match stops count")
    for day, stops in zip(route["schedule"], route["stops"]):
        if not isinstance(day, dict) or "time" not in day:
            raise ValueError("Each schedule entry must be a dict with a 'time' key")
    if not isinstance(route["distances"], dict):
        raise ValueError("'distances' must be a dictionary")
    for stop_name, dist in route["distances"].items():
        if dist is not None and (not isinstance(dist, (int, float)) or dist < 0):
            raise ValueError("Distances must be non-negative numbers")
    if not isinstance(route["completion_notes"], dict):
        raise ValueError("'completion_notes' must be a dictionary")
    return True
