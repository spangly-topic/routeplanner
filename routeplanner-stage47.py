# === Stage 47: Add a demo scenario that exercises the main workflow ===
# Project: RoutePlanner
# Step 47: Demo – exercises the main workflow end-to-end
from routeplanner import RoutePlanner

planner = RoutePlanner()

# 1. Add stops with distances (meters) and scheduled times
planner.add_stop("Warehouse", 0, "2024-01-15 08:00")
planner.add_stop("School", 1500, "2024-01-15 08:30")
planner.add_stop("Hospital", 3200, "2024-01-15 09:15")
planner.add_stop("Market", 4800, "2024-01-15 10:00")
planner.add_stop("Home", 5500, "2024-01-15 10:30")

# 2. Plan the route
plan = planner.plan()
print(f"Total distance: {plan['total_distance']:.0f} m")
print(f"Estimated time: {plan['estimated_time']:.0f} min")

# 3. Mark stops as completed
planner.mark_complete("School")
planner.mark_complete("Hospital")
print(f"Completed: {[s for s in planner.completed]}\n")

# 4. Add completion notes
planner.add_note("School", "Early morning delivery; gate open at 08:15")
planner.add_note("Hospital", "Reception confirmed; drop-off at 09:20")
print("Notes:")
for stop, note in planner.notes.items():
    print(f"  {stop}: {note}")

# 5. Export to JSON
import json
with open("route_demo.json", "w") as f:
    json.dump(planner.export(), f, indent=2)
print("Saved to route_demo.json")
