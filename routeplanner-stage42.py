# === Stage 42: Add CSV export without external dependencies ===
# Project: RoutePlanner
import csv

def export_routes_to_csv(routes, filename="routes_export.csv"):
    with open(filename, "w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=["stop_id", "address", "scheduled_time", "distance_km", "status", "completion_note"])
        writer.writeheader()
        for route in routes:
            writer.writerow(route)
    print(f"Exported {len(routes)} routes to {filename}")
