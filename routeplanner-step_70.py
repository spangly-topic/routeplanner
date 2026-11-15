# === Stage 70: Add a clear-state command protected by a confirmation flag ===
# Project: RoutePlanner
CONFIRM = {}


def clear_state() -> None:
    if input("Clear all data? Type 'yes' to confirm: ").strip().lower() != "yes":
        print("Aborted.")
        return
    for key in ("stops", "schedules", "distances", "notes"):
        globals()[key] = {}
    CONFIRM.clear()
    print("State cleared.")
