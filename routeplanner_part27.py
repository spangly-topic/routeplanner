# === Stage 27: Add monthly summary calculations ===
# Project: RoutePlanner
def monthly_summary(routes, stop_data, notes):
    """Compute monthly summary statistics for delivery routes."""
    monthly_stats = {}
    for route in routes:
        month = route['date'][:7]  # YYYY-MM
        if month not in monthly_stats:
            monthly_stats[month] = {'stops': 0, 'distance': 0, 'notes': []}
        monthly_stats[month]['stops'] += len(route['stops'])
        monthly_stats[month]['distance'] += route['total_distance']
        if route.get('notes'):
            monthly_stats[month]['notes'].extend(route['notes'])
    return monthly_stats
