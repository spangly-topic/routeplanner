# === Stage 9: Add sorting by title, date, priority, and last update time ===
# Project: RoutePlanner
def sort_routes_by(self, key):
    """Sort routes by title, date, priority, or last_update_time."""
    reverse = False
    if key == 'priority':
        reverse = True
    elif key == 'last_update_time':
        reverse = True
    elif key == 'title':
        reverse = True
    return sorted(self.routes, key=lambda r: r.get(key, ''), reverse=reverse)
