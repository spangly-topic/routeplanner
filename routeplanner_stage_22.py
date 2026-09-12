# === Stage 22: Add favorite records and quick favorite listing ===
# Project: RoutePlanner
class Favorite:
    def __init__(self, stop_id, note=''):
        self.stop_id = stop_id
        self.note = note

    def __repr__(self):
        return f'Favorite(stop_id={self.stop_id}, note={self.note!r})'

    def to_dict(self):
        return {'stop_id': self.stop_id, 'note': self.note}

    @classmethod
    def from_dict(cls, d):
        return cls(stop_id=d['stop_id'], note=d.get('note', ''))


class FavoriteManager:
    def __init__(self):
        self._favorites = []

    def add(self, stop_id, note=''):
        self._favorites.append(Favorite(stop_id, note))

    def remove(self, stop_id):
        self._favorites = [f for f in self._favorites if f.stop_id != stop_id]

    def is_favorited(self, stop_id):
        return any(f.stop_id == stop_id for f in self._favorites)

    def list_favorites(self):
        return [f for f in self._favorites if f.note]

    def clear(self):
        self._favorites = []

    def __len__(self):
        return len(self._favorites)
