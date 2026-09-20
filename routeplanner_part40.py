# === Stage 40: Add plain text report export ===
# Project: RoutePlanner
def export_report(stops):
    """Export a plain-text delivery route report."""
    lines = []
    lines.append("=" * 60)
    lines.append("DELIVERY ROUTE REPORT")
    lines.append("=" * 60)
    lines.append(f"Total stops: {len(stops)}")
    lines.append(f"Total distance: {sum(s['distance'] for s in stops):.1f} km")
    lines.append("")
    for i, stop in enumerate(stops, 1):
        status = "Completed" if stop.get("completed") else "Pending"
        lines.append(f"Stop {i}: {stop['location']}")
        lines.append(f"  Time: {stop.get('time', 'N/A')}")
        lines.append(f"  Distance: {stop.get('distance', 0):.1f} km")
        lines.append(f"  Status: {status}")
        lines.append(f"  Notes: {stop.get('notes', 'None')}")
        lines.append("")
    lines.append("=" * 60)
    return "\n".join(lines)
