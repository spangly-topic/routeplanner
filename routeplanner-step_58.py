# === Stage 58: Add bulk update behavior for selected records ===
# Project: RoutePlanner
def bulk_update_records(records, updates):
    """Apply common field updates to all records in the list."""
    for record in records:
        for field, value in updates.items():
            record[field] = value
    return records


def bulk_toggle_completed(records, completed):
    """Set the completed flag on every record to a shared value."""
    for record in records:
        record["completed"] = completed
    return records


def bulk_set_distance(records, distance):
    """Assign a distance value to every record in the list."""
    for record in records:
        record["distance"] = distance
    return records


def bulk_add_note(records, note):
    """Append the same note to each record's notes list."""
    for record in records:
        record.setdefault("notes", []).append(note)
    return records


def bulk_filter_by_schedule(records, day):
    """Keep only records whose schedule matches the given day."""
    return [record for record in records if record.get("schedule") == day]


def bulk_export(records):
    """Return a shallow copy of the records list for safe sharing."""
    return [dict(record) for record in records]
