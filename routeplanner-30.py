# === Stage 30: Add date parsing helpers with clear error messages ===
# Project: RoutePlanner
import re
from datetime import datetime

def parse_date(date_str):
    """Parse common date formats and return a datetime object.
    
    Supported formats:
    - YYYY-MM-DD
    - DD/MM/YYYY
    - DD-MM-YYYY
    - DD Month YYYY (e.g., 15 March 2023)
    
    Raises ValueError with a clear message if the format is unrecognized.
    """
    date_str = date_str.strip()
    
    # Try YYYY-MM-DD
    try:
        return datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        pass
    
    # Try DD/MM/YYYY or DD-MM-YYYY (ambiguous, assume MM/DD/YYYY if no separator found)
    try:
        return datetime.strptime(date_str, "%d/%m/%Y")
    except ValueError:
        pass
    
    # Try DD Month YYYY
    try:
        return datetime.strptime(date_str, "%d %B %Y")
    except ValueError:
        pass
    
    raise ValueError(f"Unrecognized date format: '{date_str}'. Supported formats: YYYY-MM-DD, DD/MM/YYYY, DD Month YYYY")
