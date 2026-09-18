# === Stage 37: Add recommendations for the next useful action ===
# Project: RoutePlanner
def get_next_stop(self):
    """Return the stop with the shortest remaining distance, or None if all done."""
    remaining = [(s, self._distance(s)) for s in self._stops if not s.completed]
    if not remaining:
        return None
    remaining.sort(key=lambda x: x[1])
    return remaining[0][0]
