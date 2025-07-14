from pydantic import BaseModel, Field
from datetime import datetime, time
from enum import Enum
from typing import Optional


class Condition(str, Enum):
    GOOD = "good"
    NORMAL = "normal"
    BAD = "bad"


class MedicationLog(BaseModel):
    medication_name: str
    dosage: str
    taken_at: datetime
    is_taken: bool = True


class SleepLog(BaseModel):
    bedtime: time
    wakeup_time: time


class LifestyleBase(BaseModel):
    log_date: datetime = Field(..., description="The date of the log entry.")
    medication_logs: list[MedicationLog] = []
    sleep_log: Optional[SleepLog] = None
    condition: Condition = Condition.NORMAL
    notes: Optional[str] = Field(None, description="Any special events or notes for the day.")


class LifestyleCreate(LifestyleBase):
    pass


class Lifestyle(LifestyleBase):
    id: int
    user_id: str

    class Config:
        from_attributes = True
