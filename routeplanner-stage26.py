# === Stage 26: Add weekly summary calculations ===
# Project: RoutePlanner
def weekly_summary(routes, days=None):
    """Return a dict with weekly stats: total stops, avg distance, busiest day."""
    if days is None:
        days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    total_stops = sum(len(r.get("stops", [])) for r in routes)
    total_dist = sum(r.get("distance", 0) for r in routes)
    avg_dist = total_dist / max(len(routes), 1)
    day_counts = {d: 0 for d in days}
    for r in routes:
        day = r.get("day", "Mon")
        if day in day_counts:
            day_counts[day] += 1
    busiest = max(day_counts, key=day_counts.get)
    return {
        "total_stops": total_stops,
        "avg_distance": round(avg_dist, 2),
        "busiest_day": busiest,
        "day_counts": day_counts,
    }
