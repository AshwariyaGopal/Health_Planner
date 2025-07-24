from pydantic import BaseModel
from typing import Optional, List, Dict

class UserSessionContext(BaseModel):
    """Context model to store user session data."""
    name: str
    uid: int
    goal: Optional[dict] = None
    diet_preferences: Optional[str] = None
    workout_plan: Optional[dict] = None
    meal_plan: Optional[List[str]] = None
    injury_notes: Optional[str] = None
    handoff_logs: List[str] = []
    progress_logs: List[Dict[str, str]] = []

    class Config:
        """Pydantic configuration."""
        arbitrary_types_allowed = True