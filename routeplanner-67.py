# === Stage 67: Add a function that returns key project metrics ===
# Project: RoutePlanner
def project_metrics(stops, schedules, distances, completion_notes):
    total_stops = len(stops)
    total_distance = sum(distances.values())
    completed_stops = sum(1 for n in completion_notes.values() if n.get("status") == "completed")
    pending_stops = total_stops - completed_stops
    scheduled_days = len(schedules)
    active_stops = sum(1 for s in stops if s.get("active", True))
    return {
        "total_stops": total_stops,
        "completed_stops": completed_stops,
        "pending_stops": pending_stops,
        "total_distance_km": round(total_distance, 2),
        "scheduled_days": scheduled_days,
        "active_stops": active_stops,
    }
