# === Stage 78: Refactor one large function into smaller helpers while preserving behavior ===
# Project: RoutePlanner
def split_stop(entry):
    parts = entry.split('|')
    stop_id = parts[0].strip()
    address = parts[1].strip() if len(parts) > 1 else ''
    distance = float(parts[2]) if len(parts) > 2 else 0.0
    return {'id': stop_id, 'address': address, 'distance': distance}


def parse_schedule(line):
    fields = line.split(',')
    stop_id = fields[0].strip()
    time = fields[1].strip() if len(fields) > 1 else ''
    return {'id': stop_id, 'time': time}


def compute_total_distance(stops):
    total = 0.0
    for stop in stops:
        total += stop['distance']
    return total


def mark_completed(stops, stop_id):
    for stop in stops:
        if stop['id'] == stop_id:
            stop['completed'] = True
    return stops


def load_notes(path):
    notes = {}
    with open(path, 'r') as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            if '=' in line:
                key, value = line.split('=', 1)
                notes[key.strip()] = value.strip()
    return notes
