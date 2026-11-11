# === Stage 62: Add simple scoring or priority recommendation logic ===
# Project: RoutePlanner
def score_stop(route, stop):
    score = 0
    if stop.get('completed', False):
        score += 100
    else:
        score -= 100
    if stop.get('scheduled', ''):
        score += 50
    if stop.get('distance', 0) < 5:
        score += 20
    if stop.get('priority', 'normal') == 'high':
        score += 30
    if stop.get('urgent', False):
        score += 50
    return score

def recommend_order(route):
    stops = list(route['stops'].values())
    stops.sort(key=score_stop, reverse=True)
    return [s['id'] for s in stops]

def add_recommendation(route):
    route['recommendation'] = recommend_order(route)
    return route

def print_recommendation(route):
    print("Recommended order:", route['recommendation'])
    for stop_id in route['recommendation']:
        stop = next((s for s in route['stops'].values() if s['id'] == stop_id), None)
        if stop:
            status = "done" if stop.get('completed', False) else "pending"
            print(f"{stop_id} ({status})")
