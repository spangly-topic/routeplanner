# === Stage 18: Add an activity log with timestamps and action names ===
# Project: RoutePlanner
class ActivityLog:
    def __init__(self):
        self.entries = []

    def log(self, action, timestamp=None):
        if timestamp is None:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.entries.append({"action": action, "timestamp": timestamp})
        return self

    def __repr__(self):
        return f"ActivityLog({len(self.entries)} entries)"
