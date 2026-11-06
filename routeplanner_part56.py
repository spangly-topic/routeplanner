# === Stage 56: Add compact error classes for domain failures ===
# Project: RoutePlanner
class RouteError(Exception):
    pass


class StopNotFoundError(RouteError):
    pass


class DistanceError(RouteError):
    pass


class ScheduleError(RouteError):
    pass


class CompletionError(RouteError):
    pass


class InvalidStopError(StopNotFoundError):
    pass


class UnknownDeliveryError(DistanceError):
    pass


class OverloadedScheduleError(ScheduleError):
    pass


class MissingNoteError(CompletionError):
    pass


class EmptyRouteError(RouteError):
    pass


class DuplicateStopError(RouteError):
    pass


class InvalidDistanceError(DistanceError):
    pass


class InvalidScheduleError(ScheduleError):
    pass


class InvalidCompletionError(CompletionError):
    pass


class InvalidNoteError(CompletionError):
    pass


class InvalidDeliveryError(RouteError):
    pass
