# === Stage 23: Add tag add/remove helpers and tag-based summaries ===
# Project: RoutePlanner
def add_tag(stops, tag):
    for stop in stops:
        stop.setdefault("tags", []).append(tag)
    return stops

def remove_tag(stops, tag):
    for stop in stops:
        stop["tags"] = [t for t in stop.get("tags", []) if t != tag]
    return stops

def tag_summary(stops, tag):
    matching = [s for s in stops if tag in s.get("tags", [])]
    total = sum(s.get("distance", 0) for s in matching)
    done = sum(1 for s in matching if s.get("done"))
    return {"tag": tag, "count": len(matching), "total_distance": total, "done": done}
