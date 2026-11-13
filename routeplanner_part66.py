# === Stage 66: Add export of a short status dashboard ===
# Project: RoutePlanner
def print_status_dashboard(stops):
    if not stops:
        print("No stops scheduled today.")
        return
    total = len(stops)
    done = sum(1 for s in stops if s.get("done"))
    print("=== RoutePlanner Status ===")
    print("Stops total: %d" % total)
    print("Stops done:  %d" % done)
    print("Stops left:  %d" % (total - done))
    pct = round(done * 100 / total, 1) if total else 0.0
    print("Progress:    %s%%" % pct)
    for s in stops:
        mark = "x" if s.get("done") else "-"
        print("  [%s] %s -> %s" % (mark, s.get("from", "?"), s.get("to", "?")))
