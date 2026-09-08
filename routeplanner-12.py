# === Stage 12: Add JSON import with friendly error handling for malformed data ===
# Project: RoutePlanner
import json

def load_route_data(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except json.JSONDecodeError as e:
        print(f"Error: Malformed JSON in '{file_path}': {e}")
        return None
    except PermissionError:
        print(f"Error: Permission denied reading '{file_path}'.")
        return None
    except Exception as e:
        print(f"Unexpected error reading '{file_path}': {e}")
        return None
