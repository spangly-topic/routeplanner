# === Stage 61: Add performance timing for core list and search operations ===
# Project: RoutePlanner
import time


def _time_block(func, *args, **kwargs):
    start = time.perf_counter()
    result = func(*args, **kwargs)
    elapsed = time.perf_counter() - start
    return result, elapsed


def timed_insert(sorted_stops, stop):
    result, elapsed = _time_block(sorted_stops.insert, len(sorted_stops) // 2, stop)
    return result, elapsed


def timed_search(stops, target):
    start = time.perf_counter()
    result = target in stops
    elapsed = time.perf_counter() - start
    return result, elapsed


def timed_remove(stops, stop):
    start = time.perf_counter()
    result = stops.remove(stop)
    elapsed = time.perf_counter() - start
    return result, elapsed


def timed_index(stops, stop):
    start = time.perf_counter()
    result = stops.index(stop)
    elapsed = time.perf_counter() - start
    return result, elapsed


def timed_contains(stops, target):
    start = time.perf_counter()
    result = target in stops
    elapsed = time.perf_counter() - start
    return result, elapsed


def timed_scan(stops):
    start = time.perf_counter()
    result = sum(len(s) for s in stops if s.completed)
    elapsed = time.perf_counter() - start
    return result, elapsed
