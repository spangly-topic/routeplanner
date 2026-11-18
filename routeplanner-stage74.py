# === Stage 74: Add a snapshot comparison helper for before/after states ===
# Project: RoutePlanner
def compare_snapshots(before, after):
    """Compare two route snapshots and report added, removed, and changed stops."""
    before_stops = {stop["id"]: stop for stop in before.get("stops", [])}
    after_stops = {stop["id"]: stop for stop in after.get("stops", [])}

    removed = [stop_id for stop_id in before_stops if stop_id not in after_stops]
    added = [stop_id for stop_id in after_stops if stop_id not in before_stops]

    changes = []
    for stop_id in before_stops:
        if stop_id in after_stops:
            old_stop = before_stops[stop_id]
            new_stop = after_stops[stop_id]
            if old_stop.get("completed") != new_stop.get("completed"):
                changes.append({"id": stop_id, "field": "completed", "from": old_stop.get("completed"), "to": new_stop.get("completed")})
            if old_stop.get("schedule") != new_stop.get("schedule"):
                changes.append({"id": stop_id, "field": "schedule", "from": old_stop.get("schedule"), "to": new_stop.get("schedule")})
            if old_stop.get("distance") != new_stop.get("distance"):
                changes.append({"id": stop_id, "field": "distance", "from": old_stop.get("distance"), "to": new_stop.get("distance")})
            if old_stop.get("notes") != new_stop.get("notes"):
                changes.append({"id": stop_id, "field": "notes", "from": old_stop.get("notes"), "to": new_stop.get("notes")})

    return {"removed": removed, "added": added, "changes": changes}
