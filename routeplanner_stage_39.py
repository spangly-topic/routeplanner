# === Stage 39: Add a repair function for simple data integrity issues ===
# Project: RoutePlanner
def repair_data(filepath, repair_type="auto"):
    """Repair common data integrity issues in the CSV file.

    Args:
        filepath: Path to the CSV file.
        repair_type: Type of repair ('auto', 'missing_stops', 'bad_dates', 'inconsistent_distances').
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
        return

    if repair_type == "auto":
        repair_type = detect_repair_needed(content)

    if repair_type == "missing_stops":
        content = repair_missing_stops(content)
    elif repair_type == "bad_dates":
        content = repair_bad_dates(content)
    elif repair_type == "inconsistent_distances":
        content = repair_inconsistent_distances(content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Data repaired for type: {repair_type}")

def detect_repair_needed(content):
    """Detect what type of repair is needed."""
    if 'delivery_stop' in content and 'delivery_stop' not in content:
        return "missing_stops"
    if 'delivery_date' in content:
        return "bad_dates"
    return "inconsistent_distances"

def repair_missing_stops(content):
    """Fix missing stop entries."""
    lines = content.split('\n')
    new_lines = []
    for line in lines:
        if 'delivery_stop' not in line and 'delivery_stop' not in line:
            new_lines.append(line)
    return '\n'.join(new_lines)

def repair_bad_dates(content):
    """Fix invalid date formats."""
    import re
    lines = content.split('\n')
    new_lines = []
    for line in lines:
        if 'delivery_date' in line:
            line = re.sub(r'(\d{4}-\d{2})', r'\1-01', line)
        new_lines.append(line)
    return '\n'.join(new_lines)

def repair_inconsistent_distances(content):
    """Fix inconsistent distance values."""
    lines = content.split('\n')
    new_lines = []
    for line in lines:
        if 'distance' in line:
            parts = line.split(',')
            for i, part in enumerate(parts):
                if 'distance' in part and not part.strip().isdigit():
                    parts[i] = '10'
            line = ','.join(parts)
        new_lines.append(line)
    return '\n'.join(new_lines)
