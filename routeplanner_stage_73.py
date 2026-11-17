# === Stage 73: Add a lightweight HTML report export ===
# Project: RoutePlanner
def export_html_report(
    stops,
    schedules,
    distances,
    completion_notes,
    output_path="route_report.html",
):
    """Export route data to a compact, dependency-free HTML report."""
    try:
        from collections import OrderedDict
    except ImportError:
        OrderedDict = dict

    rows = []
    for stop in stops:
        schedule = schedules.get(stop, [])
        distance = distances.get(stop, 0)
        note = completion_notes.get(stop, "")
        if schedule:
            times = [str(t) for t in schedule]
            cells = "<td>" + "<td>".join(times) + "</td>"
        else:
            cells = "<td colspan='3'>No schedule</td>"
        rows.append(
            "<tr>" + cells + "<td>" + str(distance) + "</td>"
            + "<td>" + note + "</td></tr>"
        )
    table = "<tr><th>Stop</th><th>Schedule</th><th>Distance</th><th>Note</th></tr>"
    table += "".join(rows)
    body = (
        "<h1>Route Planner Report</h1>"
        "<table border='1' cellpadding='6' cellspacing='0'>" + table + "</table>"
    )
    html = "<!DOCTYPE html><html><head><meta charset='utf-8'><title>Route Report</title></head><body>" + body + "</body></html>"
    with open(output_path, "w", encoding="utf-8") as handle:
        handle.write(html)
    return output_path
