# === Stage 13: Add file save support using a configurable path ===
# Project: RoutePlanner
def save_route(plan, path="route_data.json"):
    with open(path, "w") as f:
        f.write(plan.get("json", ""))
