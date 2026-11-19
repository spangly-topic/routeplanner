# === Stage 77: Add type hints to older helper functions that are missing them ===
# Project: RoutePlanner
def load_stops(path: str) -> list:
    stops = []
    with open(path, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split(",")
            stops.append(
                {
                    "id": int(parts[0]),
                    "name": parts[1],
                    "address": parts[2],
                    "lat": float(parts[3]),
                    "lng": float(parts[4]),
                }
            )
    return stops


def load_schedule(path: str) -> dict:
    schedule = {}
    with open(path, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            day, time, stop_id = line.split(",")
            schedule[day.strip()] = {
                "departure": time.strip(),
                "stop_id": int(stop_id.strip()),
            }
    return schedule


def load_distances(path: str) -> dict:
    distances = {}
    with open(path, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            a, b, dist = line.split(",")
            distances[(a.strip(), b.strip())] = float(dist.strip())
            distances[(b.strip(), a.strip())] = float(dist.strip())
    return distances


def load_notes(path: str) -> dict:
    notes = {}
    with open(path, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            stop_id, note = line.split("|", 1)
            notes[int(stop_id.strip())] = note.strip()
    return notes
