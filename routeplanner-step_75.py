# === Stage 75: Add a validation report that lists warnings and errors ===
# Project: RoutePlanner
def generate_validation_report(routes):
    warnings = []
    errors = []

    for i, route in enumerate(routes):
        name = route.get("name", f"Route {i + 1}")
        stops = route.get("stops", [])

        if not name:
            errors.append(f"Route at index {i} is missing a name")
            continue

        if not stops:
            warnings.append(f"Route '{name}' has no stops")

        total_distance = 0.0
        total_time = 0.0

        for j, stop in enumerate(stops):
            stop_id = stop.get("id", f"stop_{i + 1}_{j + 1}")

            if not stop_id:
                errors.append(f"Route '{name}' stop at position {j} is missing an id")
                continue

            if stop_id in [s.get("id") for s in stops if s.get("id")]:
                errors.append(f"Duplicate stop id '{stop_id}' in route '{name}'")

            distance = stop.get("distance")
            if distance is not None:
                if not isinstance(distance, (int, float)) or distance < 0:
                    errors.append(f"Stop '{stop_id}' has invalid distance {distance}")
                else:
                    total_distance += distance

            duration = stop.get("duration")
            if duration is not None:
                if not isinstance(duration, (int, float)) or duration < 0:
                    errors.append(f"Stop '{stop_id}' has invalid duration {duration}")
                else:
                    total_time += duration

            if not stop.get("scheduled"):
                warnings.append(f"Stop '{stop_id}' in route '{name}' is not scheduled")

            if not stop.get("completed"):
                warnings.append(f"Stop '{stop_id}' in route '{name}' is not completed")

        if total_distance == 0.0 and len(stops) > 0:
            warnings.append(f"Route '{name}' has zero total distance")

    report = {
        "warnings": warnings,
        "errors": errors,
        "total_warnings": len(warnings),
        "total_errors": len(errors),
    }

    return report
