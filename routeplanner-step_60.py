# === Stage 60: Add saved views for frequently used filters ===
# Project: RoutePlanner
SAVED_VIEWS = {}


def save_view(name, filters):
    SAVED_VIEWS[name] = filters


def get_view(name):
    return SAVED_VIEWS.get(name)


def list_views():
    return list(SAVED_VIEWS.keys())


def apply_view(name, stops, view_filters):
    saved = SAVED_VIEWS.get(name)
    if not saved:
        return []
    result = []
    for stop in stops:
        if not view_filters.get("city", True) or stop.city != view_filters["city"]:
            continue
        if not view_filters.get("active", True) or not stop.completed:
            continue
        if saved.get("min_distance") and stop.distance < saved["min_distance"]:
            continue
        if saved.get("max_distance") and stop.distance > saved["max_distance"]:
            continue
        if saved.get("service") and stop.service != saved["service"]:
            continue
        result.append(stop)
    return result
