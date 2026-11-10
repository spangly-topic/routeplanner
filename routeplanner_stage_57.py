# === Stage 57: Add structured result objects for command handlers ===
# Project: RoutePlanner
class RouteResult:
    def __init__(self, route, total_distance):
        self.route = route
        self.total_distance = total_distance

    def to_dict(self):
        return {
            "route": self.route,
            "total_distance": self.total_distance,
        }

    def __repr__(self):
        return f"RouteResult(route={self.route}, total_distance={self.total_distance})"


class ScheduleResult:
    def __init__(self, assignments):
        self.assignments = assignments

    def to_dict(self):
        return {"assignments": self.assignments}

    def __repr__(self):
        return f"ScheduleResult(assignments={self.assignments})"


class DistanceResult:
    def __init__(self, matrix):
        self.matrix = matrix

    def to_dict(self):
        return {"matrix": self.matrix}

    def __repr__(self):
        return f"DistanceResult(matrix={self.matrix})"


class CompletionResult:
    def __init__(self, notes):
        self.notes = notes

    def to_dict(self):
        return {"notes": self.notes}

    def __repr__(self):
        return f"CompletionResult(notes={self.notes})"
