# === Stage 5: Implement update operations with clear handling for missing records ===
# Project: RoutePlanner
def update_stop(self, stop_id: str, **kwargs) -> dict:
    """Update a stop's fields; returns the stop dict or empty dict on missing record."""
    if stop_id not in self._stops:
        return {}
    for key, value in kwargs.items():
        if key not in self._stop_fields:
            raise ValueError(f"Unknown field: {key}")
        self._stops[stop_id][key] = value
    return self._stops[stop_id]

def update_schedule(self, schedule_id: str, **kwargs) -> dict:
    """Update a schedule's fields; returns the schedule dict or empty dict on missing record."""
    if schedule_id not in self._schedules:
        return {}
    for key, value in kwargs.items():
        if key not in self._schedule_fields:
            raise ValueError(f"Unknown field: {key}")
        self._schedules[schedule_id][key] = value
    return self._schedules[schedule_id]

def update_distance(self, distance_id: str, **kwargs) -> dict:
    """Update a distance record's fields; returns the distance dict or empty dict on missing record."""
    if distance_id not in self._distances:
        return {}
    for key, value in kwargs.items():
        if key not in self._distance_fields:
            raise ValueError(f"Unknown field: {key}")
        self._distances[distance_id][key] = value
    return self._distances[distance_id]

def update_note(self, note_id: str, **kwargs) -> dict:
    """Update a completion note's fields; returns the note dict or empty dict on missing record."""
    if note_id not in self._notes:
        return {}
    for key, value in kwargs.items():
        if key not in self._note_fields:
            raise ValueError(f"Unknown field: {key}")
        self._notes[note_id][key] = value
    return self._notes[note_id]
