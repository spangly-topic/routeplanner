# === Stage 80: Polish user-facing messages, names, and examples for consistency ===
# Project: RoutePlanner
def describe_route(route):
    if not route:
        return "No stops have been added yet."
    stops = ", ".join(stop.label for stop in route)
    return f"Your route has {len(route)} stop(s): {stops}."


def format_completion_note(note):
    if not note:
        return "No completion note."
    return f"Completion note: {note}"


def format_schedule(schedule):
    if not schedule:
        return "No scheduled deliveries."
    lines = [f"Total scheduled deliveries: {len(schedule)}"]
    for delivery in schedule:
        lines.append(f"  - {delivery}")
    return "\n".join(lines)


def confirm_route_saved(route):
    total = sum(stop.distance_km for stop in route)
    return f"Route saved successfully with {len(route)} stops and {total:.1f} km total distance."
