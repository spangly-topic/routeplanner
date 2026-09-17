# === Stage 33: Add a settings dictionary and functions to update settings ===
# Project: RoutePlanner
def get_settings():
    """Return the current settings dictionary."""
    if not _settings:
        _settings = {
            "max_stops": 50,
            "max_distance": 100.0,
            "default_speed": 30.0,
            "notes_enabled": True,
            "auto_complete": False,
        }
    return _settings


def update_settings(key, value):
    """Update a single setting and return the full settings dict."""
    current = get_settings()
    if key not in current:
        raise ValueError(f"Unknown setting: {key}")
    current[key] = value
    return current


def reset_settings():
    """Reset all settings to defaults."""
    return {
        "max_stops": 50,
        "max_distance": 100.0,
        "default_speed": 30.0,
        "notes_enabled": True,
        "auto_complete": False,
    }
