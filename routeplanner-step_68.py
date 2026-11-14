# === Stage 68: Add a compact changelog generated from the activity log ===
# Project: RoutePlanner
def build_changelog(activity_log):
    """Generate a compact changelog from the activity log."""
    if not activity_log:
        return "No activity recorded yet."
    entries = []
    for entry in activity_log:
        when = entry.get("timestamp", "unknown time")
        action = entry.get("action", "unknown action")
        detail = entry.get("detail", "")
        line = f"- {when}: {action}"
        if detail:
            line += f" — {detail}"
        entries.append(line)
    changelog = "\n".join(entries)
    return changelog
