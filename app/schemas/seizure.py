from pydantic import BaseModel, Field
from datetime import datetime
from enum import Enum
from typing import Optional


class SeizureType(str, Enum):
    GENERALIZED = "generalized"
    FOCAL = "focal"
    ABSENCE = "absence"
    UNKNOWN = "unknown"


class SeizureBase(BaseModel):
    occurrence_time: datetime = Field(..., description="The date and time when the seizure occurred.")
    duration_seconds: int = Field(..., gt=0, description="The duration of the seizure in seconds.")
    seizure_type: SeizureType = Field(..., description="The type of the seizure.")
    preictal_symptoms: Optional[str] = Field(None, description="Any symptoms observed before the seizure.")
    postictal_state: Optional[str] = Field(None, description="The child's state after the seizure.")
    video_url: Optional[str] = Field(None, description="URL of the video recording of the seizure.")


class SeizureCreate(SeizureBase):
    pass


class Seizure(SeizureBase):
    id: int
    user_id: str

    class Config:
        from_attributes = True
