# === Stage 20: Add duplicate detection for newly created records ===
# Project: RoutePlanner
def detect_duplicate(route_id, stop_id, schedule_id, delivery_id):
    """Check if the new record is a duplicate of an existing one."""
    if route_id and stop_id and schedule_id and delivery_id:
        if (route_id, stop_id, schedule_id, delivery_id) in _seen_routes:
            raise ValueError(
                f"Duplicate record: route={route_id}, stop={stop_id}, "
                f"schedule={schedule_id}, delivery={delivery_id}"
            )
    _seen_routes.add((route_id, stop_id, schedule_id, delivery_id))
