# === Stage 7: Add list and detail formatting helpers for console output ===
# Project: RoutePlanner
def format_route(route):
    lines = []
    for stop in route:
        lines.append(f"  {stop[0]}: {stop[1]} km")
    return "\n".join(lines)

def format_completion_notes(completed):
    if not completed:
        return "No stops completed."
    lines = []
    for stop, note in completed:
        lines.append(f"  {stop}: {note}")
    return "\n".join(lines)

def print_route_summary(route, completed, distances, completion_notes):
    print("=== Delivery Route Planner ===")
    print(f"Total stops: {len(route)}")
    print(f"Completed: {len(completed)}")
    print("Route:")
    print(format_route(route))
    print("Completion Notes:")
    print(format_completion_notes(completed))
    if distances:
        print("Distances:")
        for stop, dist in distances:
            print(f"  {stop}: {dist} km")
