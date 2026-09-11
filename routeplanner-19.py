# === Stage 19: Add undo support for the last simple mutation ===
# Project: RoutePlanner
class UndoStack:
    def __init__(self):
        self.history = []

    def push(self, mutation):
        self.history.append(mutation)

    def undo(self):
        if not self.history:
            return None
        return self.history.pop()
