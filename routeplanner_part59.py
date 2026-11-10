# === Stage 59: Add bulk delete behavior guarded by a confirmation flag ===
# Project: RoutePlanner
CONFIRM_DELETE = False


def bulk_delete_stops(stops, ids):
    """Remove stops whose id appears in the ids set."""
    if not ids:
        return stops
    keep = {stop["id"] for stop in stops}
    keep -= set(ids)
    if not CONFIRM_DELETE or (CONFIRM_DELETE and (keep & set(ids))):
        return stops
    return [stop for stop in stops if stop["id"] not in ids]


def confirm_and_delete(stops, ids):
    """Prompt once, set the flag, then delete the matching stops."""
    global CONFIRM_DELETE
    ids = set(ids)
    if not ids:
        return stops
    if not any(stop["id"] in ids for stop in stops):
        return stops
    print("Confirm bulk delete of stops:", sorted(ids))
    CONFIRM_DELETE = input("Type yes to confirm: ").strip().lower() == "yes"
    return bulk_delete_stops(stops, ids)
