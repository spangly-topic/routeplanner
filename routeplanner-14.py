# === Stage 14: Add file load support with fallback demo data ===
# Project: RoutePlanner
def load_routes(filename="routes.json", fallback=None):
    if fallback is None:
        fallback = [
            {"id": 1, "stops": ["Warehouse", "Downtown", "Airport"], "distance": 45, "notes": "Normal delivery"},
            {"id": 2, "stops": ["Warehouse", "Harbor", "University"], "distance": 30, "notes": "Evening shift"}
        ]
    try:
        with open(filename) as f:
            data = json.load(f)
            if isinstance(data, list):
                return data
            return data.get("routes", [])
    except (FileNotFoundError, json.JSONDecodeError):
        print(f"[RoutePlanner] Loaded fallback demo data ({len(fallback)} routes)")
        return fallback
