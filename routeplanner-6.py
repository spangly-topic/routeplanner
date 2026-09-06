# === Stage 6: Implement delete operations with a confirmation flag argument ===
# Project: RoutePlanner
from typing import Optional

def remove_stop(stops: dict, stop_id: str) -> dict:
    if stop_id not in stops:
        return stops
    del stops[stop_id]
    return stops

def remove_route(route: dict, route_id: str) -> dict:
    if route_id not in route:
        return route
    del route[route_id]
    return route

def remove_schedule(schedule: dict, schedule_id: str) -> dict:
    if schedule_id not in schedule:
        return schedule
    del schedule[schedule_id]
    return schedule

def remove_stop_with_confirmation(stops: dict, stop_id: str, confirm: bool) -> dict:
    if not confirm:
        return stops
    return remove_stop(stops, stop_id)

def remove_route_with_confirmation(route: dict, route_id: str, confirm: bool) -> dict:
    if not confirm:
        return route
    return remove_route(route, route_id)

def remove_schedule_with_confirmation(schedule: dict, schedule_id: str, confirm: bool) -> dict:
    if not confirm:
        return schedule
    return remove_schedule(schedule, schedule_id)
