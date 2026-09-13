# === Stage 24: Add grouped summaries by category or status ===
# Project: RoutePlanner
def summarize_routes(routes, category_fn=None, status_fn=None):
    """Group route summaries by category or status."""
    groups = {}
    for route in routes:
        key = category_fn(route) if category_fn else status_fn(route)
        if key not in groups:
            groups[key] = []
        groups[key].append(route)
    return {k: v for k, v in groups.items()}
