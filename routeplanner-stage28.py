# === Stage 28: Add overdue item detection based on due dates ===
# Project: RoutePlanner
def detect_overdue_items(routes, current_date):
    overdue = []
    for route in routes:
        if route['schedule'] and route['schedule'].get('due_date'):
            due = route['schedule']['due_date']
            if due < current_date:
                overdue.append({
                    'route_id': route['id'],
                    'due_date': due,
                    'days_overdue': (current_date - due).days,
                    'status': 'completed' if route['status'] == 'completed' else 'overdue'
                })
    return overdue
