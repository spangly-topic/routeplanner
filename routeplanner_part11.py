# === Stage 11: Add JSON export for the current application state ===
# Project: RoutePlanner
import json

def export_state(route_planner):
    """Export the current application state to a JSON string."""
    state = {
        "stops": route_planner["stops"],
        "current_stop": route_planner["current_stop"],
        "scheduled_time": route_planner["scheduled_time"],
        "distance": route_planner["distance"],
        "notes": route_planner["notes"],
        "is_complete": route_planner["is_complete"]
    }
    return json.dumps(state, indent=2)
