# === Stage 71: Add a seed-demo-data helper with deterministic sample data ===
# Project: RoutePlanner
def seed_demo_data(db, seed=42):
    import random
    random.seed(seed)
    sample_stops = [
        ("Central Depot", "0.0", "0.0"),
        ("Downtown Office", "1.2", "0.8"),
        ("Riverside Market", "2.5", "1.3"),
        ("North Park", "3.1", "2.9"),
        ("East Mall", "4.0", "2.2"),
        ("West Bakery", "2.8", "3.7"),
    ]
    for i, stop in enumerate(sample_stops):
        db.add_stop(stop[0], int(stop[1]), int(stop[2]))
    for i in range(1, len(sample_stops)):
        prev = sample_stops[i - 1]
        curr = sample_stops[i]
        db.add_distance(prev[0], curr[0], int(round(float(curr[1]) ** 2 + float(curr[2]) ** 2 ** 0.5)))
    db.add_route("Demo Route", "Central Depot", "Riverside Market", "East Mall", "West Bakery")
    db.add_schedule("Demo Route", ["2024-06-01", "2024-06-02", "2024-06-03"])
    db.add_note("Riverside Market", "Delivered before noon")
    db.add_note("West Bakery", "Customer requested evening drop")
    return sample_stops
