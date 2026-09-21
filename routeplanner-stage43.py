# === Stage 43: Add CSV import for the primary record type ===
# Project: RoutePlanner
import csv
from pathlib import Path

def import_stops(csv_path):
    """Read stops from a CSV file and return a list of Stop dicts."""
    stops = []
    with open(csv_path, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            stop = {
                'name': row['name'],
                'address': row['address'],
                'distance': float(row['distance']),
                'scheduled': row.get('scheduled', ''),
                'completed': row.get('completed', 'false') == 'true',
                'notes': row.get('notes', ''),
            }
            stops.append(stop)
    return stops
