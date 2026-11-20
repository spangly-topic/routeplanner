# === Stage 81: Add final README text as a module string with usage examples ===
# Project: RoutePlanner
README = """
RoutePlanner — a delivery route planner with stops, schedules, distances, and completion notes.

Install
    No dependencies required. Python 3.8+ is all you need.

Usage
    from routeplanner import RoutePlanner
    planner = RoutePlanner("daily-deliveries")
    planner.add_stop("123 Main St", "2.5 km", "09:00")
    planner.add_stop("456 Oak Ave", "1.8 km", "09:30")
    planner.set_schedule("08:00", "12:00")
    planner.mark_complete("123 Main St")
    print(planner.summary())

Features
    - Stores multiple delivery stops with address, distance, and scheduled time
    - Tracks a working schedule window
    - Records completion notes per stop
    - Produces a compact summary of remaining and finished stops

License
    MIT — use freely, give credit where helpful.
"""
