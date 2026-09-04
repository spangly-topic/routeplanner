# === Stage 2: Add dataclasses or typed dictionaries for the main domain records ===
# Project: RoutePlanner
from dataclasses import dataclass, field
from datetime import date
from typing import Optional


@dataclass
class Stop:
    id: str
    name: str
    address: str
    latitude: float
    longitude: float
    scheduled: Optional[date] = None
    completed: bool = False
    notes: str = ""
