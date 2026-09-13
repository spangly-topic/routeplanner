# === Stage 25: Add daily summary calculations ===
# Project: RoutePlanner
def daily_summary(stops):
    """Generate a daily summary from a list of stop dicts."""
    today = {}
    for stop in stops:
        date = stop.get("date", stop.get("scheduled_date", ""))
        if not date:
            continue
        today[date] = today.get(date, 0) + 1
    total = sum(today.values())
    return {
        "total_stops": total,
        "unique_days": len(today),
        "days": today,
    }
