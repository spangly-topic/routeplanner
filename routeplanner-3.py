# === Stage 3: Add validation helpers for required fields, identifiers, and short text values ===
# Project: RoutePlanner
def is_valid_id(value, length=10):
    """Check if value is a non-empty alphanumeric string of given length."""
    if not isinstance(value, str):
        return False
    if len(value) != length or not value.isalnum():
        return False
    return True

def is_valid_short_text(value, max_len=50, min_len=1):
    """Check if value is a non-empty string within length limits."""
    if not isinstance(value, str) or len(value) < min_len or len(value) > max_len:
        return False
    return True

def is_valid_required_field(value, allow_empty=False):
    """Check if value is a non-empty string when required, or empty if allowed."""
    if allow_empty:
        return isinstance(value, str)
    return isinstance(value, str) and len(value) > 0
