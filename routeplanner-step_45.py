# === Stage 45: Add restore from backup with validation ===
# Project: RoutePlanner
def restore_from_backup(backup_path, target_path):
    """Restore backup file to target with format validation."""
    import json
    with open(backup_path, 'r') as f:
        data = json.load(f)
    if not isinstance(data, dict):
        raise ValueError("Backup must be a JSON object")
    for key in ['stops', 'schedules', 'distances', 'notes']:
        if key not in data:
            raise ValueError(f"Missing required field: {key}")
    with open(target_path, 'w') as f:
        json.dump(data, f, indent=2)
    print(f"Restored: {len(data['stops'])} stops, {len(data['schedules'])} schedules")
