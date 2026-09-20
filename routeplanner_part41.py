# === Stage 41: Add plain text import for a simple line-based format ===
# Project: RoutePlanner
def parse_stop_line(line):
    """Parse a single stop line in 'id;name;address;distance' format."""
    parts = line.strip().split(';')
    if len(parts) != 4:
        raise ValueError(f"Invalid stop line format: {line!r}")
    stop_id, name, address, distance = parts
    return {
        'id': stop_id,
        'name': name,
        'address': address,
        'distance': int(distance),
    }

def load_stops_from_file(filename):
    """Load multiple stops from a plain text file, one per line."""
    stops = []
    with open(filename, 'r') as f:
        for line in f:
            if line.strip():
                stops.append(parse_stop_line(line))
    return stops
