# === Stage 1: Create the base application structure, in-memory state, and a small demo dataset ===
# Project: RoutePlanner
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum

class StopStatus(Enum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"

@dataclass
class Stop:
    name: str
    address: str
    scheduled_time: datetime
    distance_km: float
    status: StopStatus = StopStatus.PENDING
    note: str = ""

    def mark_complete(self, note: str = "") -> None:
        self.status = StopStatus.COMPLETED
        self.note = note

    def __repr__(self):
        return f"Stop({self.name}, {self.status.value}, {self.distance_km}km)"
