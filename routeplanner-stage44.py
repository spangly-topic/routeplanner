# === Stage 44: Add backup creation for the data file ===
# Project: RoutePlanner
def create_backup(data_file):
    import shutil, os
    backup_path = data_file + ".bak"
    if os.path.exists(backup_path):
        os.remove(backup_path)
    shutil.copy2(data_file, backup_path)
    return backup_path
