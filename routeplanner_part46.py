# === Stage 46: Add a schema version field and migration helper ===
# Project: RoutePlanner
def migrate_schema(db, current_version=3):
    """Apply pending schema migrations to the RoutePlanner database."""
    db.execute("CREATE TABLE IF NOT EXISTS _schema_migrations (version INTEGER PRIMARY KEY)")
    db.execute("INSERT OR IGNORE INTO _schema_migrations (version) VALUES (?)", (current_version,))
    db.commit()
    return current_version
