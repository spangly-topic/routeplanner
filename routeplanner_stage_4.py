# === Stage 4: Implement create operations for the primary records ===
# Project: RoutePlanner
def create_stop(name, address, coordinates):
    """Create a new Stop record and return it."""
    return Stop(name=name, address=address, coordinates=coordinates)

def create_schedule(date, time, duration_minutes):
    """Create a new Schedule record and return it."""
    return Schedule(date=date, time=time, duration_minutes=duration_minutes)

def create_distance(source, destination, distance_km):
    """Create a new Distance record and return it."""
    return Distance(source=source, destination=destination, distance_km=distance_km)

def create_completion_note(stop_id, note, status):
    """Create a new CompletionNote record and return it."""
    return CompletionNote(stop_id=stop_id, note=note, status=status)
