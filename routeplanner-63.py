# === Stage 63: Add relationships between records where useful ===
# Project: RoutePlanner
def link_records(records):
    by_id = {r["id"]: r for r in records}
    for rec in records:
        related = []
        for other in records:
            if other["id"] != rec["id"]:
                continue
            if "stops" in rec and other["id"] in rec["stops"]:
                related.append(other)
            if "schedules" in rec and other["id"] in rec["schedules"]:
                related.append(other)
            if "distances" in rec and other["id"] in rec["distances"]:
                related.append(other)
            if "notes" in rec and other["id"] in rec["notes"]:
                related.append(other)
        rec["related"] = related

if __name__ == "__main__":
    data = [
        {"id": "route-1", "stops": ["stop-1", "stop-2"], "schedules": ["sched-1"]},
        {"id": "stop-1"},
        {"id": "stop-2"},
        {"id": "sched-1"},
    ]
    link_records(data)
    for rec in data:
        print(rec["id"], "<-", rec["related"])
