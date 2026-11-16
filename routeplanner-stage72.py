# === Stage 72: Add Markdown report export ===
# Project: RoutePlanner
def export_report(routes, output_path="route_report.txt"):
    with open(output_path, "w") as f:
        f.write("ROUTE PLANNER REPORT\n")
        f.write("=" * 40 + "\n\n")
        for route in routes:
            name = route.get("name", "Unnamed Route")
            total = 0.0
            f.write(f"Route: {name}\n")
            f.write(f"Stops: {len(route.get('stops', []))}\n")
            f.write(f"Total Distance: {total:.2f} km\n")
            f.write("-" * 40 + "\n")
            for stop in route.get("stops", []):
                status = stop.get("status", "pending")
                note = stop.get("note", "")
                if note:
                    f.write(f"  {stop.get('name')} - {status} ({note})\n")
                else:
                    f.write(f"  {stop.get('name')} - {status}\n")
            f.write("\n")
    return output_path
