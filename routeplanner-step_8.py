# === Stage 8: Add filtering by status, category, owner, or tag ===
# Project: RoutePlanner
def filter_routes(routes, **criteria):
    """Filter routes by status, category, owner, tag, or any combination."""
    if not criteria:
        return routes
    filtered = routes
    for key, value in criteria.items():
        if key not in ('status', 'category', 'owner', 'tag'):
            raise ValueError(f"Unknown filter key: {key}")
        filtered = [r for r in filtered if r.get(key) == value]
    return filtered
