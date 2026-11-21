# === Stage 82: Add an end-to-end demo function that prints a complete walkthrough ===
# Project: RoutePlanner
def demo_route_planner():
    stops = [
        {"id": "A", "name": "Warehouse", "address": "1 Main St", "schedule": "08:00", "distance": 0, "completed": False},
        {"id": "B", "name": "Downtown Shop", "address": "42 Oak Ave", "schedule": "09:30", "distance": 12.5, "completed": False},
        {"id": "C", "name": "Suburb Office", "address": "7 Pine Rd", "distance": 8.2, "completed": False},
        {"id": "D", "name": "Mall Pickup", "address": "100 Elm Blvd", "schedule": "11:00", "distance": 15.7, "completed": False},
    ]
    print("=== RoutePlanner Demo ===")
    print("Stops loaded:", len(stops))
    for stop in stops:
        status = "done" if stop["completed"] else "pending"
        print(stop["id"], stop["name"], stop["address"], stop["schedule"], stop["distance"], km, status)
    total = sum(s["distance"] for s in stops)
    print("Total distance:", round(total, 1), km)
    pending = [s["id"] for s in stops if not s["completed"]]
    print("Pending stops:", pending)
    stops[1]["completed"] = True
    stops[2]["completed"] = True
    print("After marking B and C complete, pending:", [s["id"] for s in stops if not s["completed"]])
    notes = {"A": "Loaded goods", "B": "Delivered package", "C": "Returned receipt"}
    for s in stops:
        if s["id"] in notes:
            print("Note for", s["id"], ":", notes[s["id"]])
    print("Demo finished.")
