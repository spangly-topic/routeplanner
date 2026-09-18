# === Stage 35: Add active user switching and user-specific records ===
# Project: RoutePlanner
class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id

    def __repr__(self):
        return f"<User {self.name}>"

class UserContext:
    def __init__(self):
        self.users = {}
        self._current_user = None

    def register(self, user):
        self.users[user.user_id] = user
        if self._current_user is None:
            self._current_user = user

    def switch(self, user_id):
        user = self.users.get(user_id)
        if user is None:
            return False
        self._current_user = user
        return True

    def get_current_user(self):
        return self._current_user

    def is_empty(self):
        return self._current_user is None

    def __repr__(self):
        return f"<UserContext current={self._current_user}>"

    def __iter__(self):
        for u in self.users.values():
            yield u
