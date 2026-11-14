# === Stage 69: Add a reset-demo-data command for manual testing ===
# Project: RoutePlanner
def reset_demo_data():
    stops = [
        {"id": 1, "name": "Depot", "address": "100 Main St", "scheduled": "08:00",
         "distance_km": 0, "completed": True, "note": "Start point"},
        {"id": 2, "name": "City Market", "address": "22 Oak Ave", "scheduled": "09:30",
         "distance_km": 12.5, "completed": False, "note": "Awaiting order 4091"},
        {"id": 3, "name": "Riverside Clinic", "address": "7 Harbor Rd", "scheduled": "11:00",
         "distance_km": 28.0, "completed": False, "note": "Delivery pending"},
        {"id": 4, "name": "North Park Cafe", "address": "15 Elm Blvd", "scheduled": "13:15",
         "distance_km": 41.3, "completed": False, "note": "Contact courier for access"},
        {"id": 5, "name": "West End Mall", "address": "99 Pine Cir", "scheduled": "15:00",
         "distance_km": 55.7, "completed": False, "note": "Loading dock open 14:00"},
    ]
    with open("stops.json", "w", encoding="utf-8") as f:
        json.dump(stops, f, indent=2)
    print("Demo data reset complete.")

if __name__ == "__main__":
    reset_demo_data()
