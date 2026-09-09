# === Stage 15: Add a simple command dispatcher for text commands ===
# Project: RoutePlanner
class Dispatcher:
    def __init__(self):
        self._handlers = {}

    def register(self, name, handler):
        self._handlers[name.lower()] = handler

    def dispatch(self, text):
        key = text.strip().lower()
        if key in self._handlers:
            return self._handlers[key](text)
        return "Unknown command: " + text
