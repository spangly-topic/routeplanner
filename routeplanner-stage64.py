# === Stage 64: Add validation for relationship references ===
# Project: RoutePlanner
def validate_references(data):
    if not isinstance(data, dict):
        raise ValueError("data must be a dict")

    stops = data.get("stops", [])
    if not isinstance(stops, list):
        raise ValueError("stops must be a list")

    valid_stops = {stop["id"] for stop in stops}

    routes = data.get("routes", [])
    if not isinstance(routes, list):
        raise ValueError("routes must be a list")

    for route in routes:
        if not isinstance(route, dict):
            raise ValueError("each route must be a dict")

        route_stops = route.get("stops", [])
        if not isinstance(route_stops, list):
            raise ValueError("route stops must be a list")

        for stop_id in route_stops:
            if stop_id not in valid_stops:
                raise ValueError(f"route references unknown stop: {stop_id}")

        delivery = route.get("delivery")
        if delivery is not None and "delivery_id" in delivery:
            delivery_id = delivery["delivery_id"]
            if delivery_id not in valid_deliveries(data, delivery_id):
                raise ValueError(f"route references unknown delivery: {delivery_id}")

        schedule = route.get("schedule")
        if schedule is not None and "schedule_id" in schedule:
            schedule_id = schedule["schedule_id"]
            if schedule_id not in valid_schedules(data, schedule_id):
                raise ValueError(f"route references unknown schedule: {schedule_id}")

        notes = route.get("notes", [])
        if not isinstance(notes, list):
            raise ValueError("route notes must be a list")

        return True


def valid_deliveries(data, delivery_id):
    deliveries = data.get("deliveries", [])
    return any(d["id"] == delivery_id for d in deliveries)


def valid_schedules(data, schedule_id):
    schedules = data.get("schedules", [])
    return any(s["id"] == schedule_id for s in schedules)
