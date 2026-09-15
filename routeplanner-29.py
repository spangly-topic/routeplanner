# === Stage 29: Add reminder helpers that return upcoming items ===
# Project: RoutePlanner
def upcoming_reminders(
    schedule: dict,
    now: str = "2024-01-01",
    order: str = "earliest",
) -> list[dict]:
    """Return reminder items that have not yet been completed,
    ordered by their scheduled date (or notes if no date)."""
    reminders = [
        {"name": k, "scheduled": v["scheduled"], "notes": v["notes"]}
        for k, v in schedule.items()
        if v.get("completed", False) is False
    ]
    if order == "earliest":
        reminders.sort(key=lambda r: r["scheduled"])
    elif order == "notes":
        reminders.sort(key=lambda r: r["notes"])
    return reminders
