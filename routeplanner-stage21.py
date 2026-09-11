# === Stage 21: Add archive and restore behavior for completed or old records ===
# Project: RoutePlanner
import datetime, json

class RoutePlanner:
    def __init__(self):
        self.stops = []
        self.completed = []
        self.schedule = {}
        self.notes = {}

    def add_stop(self, name, distance, scheduled_time, completion_note=""):
        stop = {
            "name": name,
            "distance": distance,
            "scheduled_time": scheduled_time,
            "completion_note": completion_note,
            "completed": False
        }
        self.stops.append(stop)
        return stop

    def complete_stop(self, index, note=""):
        if 0 <= index < len(self.stops):
            self.stops[index]["completed"] = True
            self.stops[index]["completion_note"] = note
            self.completed.append(self.stops[index])
            return self.stops[index]
        return None

    def archive_old_records(self, cutoff_days=90):
        cutoff = datetime.datetime.now() - datetime.timedelta(days=cutoff_days)
        archived = []
        for stop in self.completed:
            if stop["scheduled_time"] < cutoff:
                archived.append(stop)
        return archived

    def restore_archive(self, archived):
        for stop in archived:
            self.stops.append(stop)

    def get_status(self):
        total = len(self.stops)
        done = len(self.completed)
        active = total - done
        return {"total": total, "active": active, "completed": done}
