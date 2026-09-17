# === Stage 34: Add support for multiple local user profiles ===
# Project: RoutePlanner
import json
from pathlib import Path

class UserProfiles:
    def __init__(self, profiles_dir="profiles"):
        self.profiles_dir = Path(profiles_dir)
        self.profiles_dir.mkdir(parents=True, exist_ok=True)

    def load_profile(self, name):
        path = self.profiles_dir / f"{name}.json"
        if not path.exists():
            return None
        with open(path) as f:
            return json.load(f)

    def save_profile(self, name, data):
        path = self.profiles_dir / f"{name}.json"
        with open(path, "w") as f:
            json.dump(data, f, indent=2)

    def list_profiles(self):
        return sorted(p.stem for p in self.profiles_dir.glob("*.json"))
