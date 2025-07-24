from pydantic import BaseModel, ValidationError
import re
from typing import Optional, Dict, List

class GoalInput(BaseModel):
    """Model for validating goal input."""
    quantity: float
    metric: str
    duration: str
    type: str  # 'lose' or 'gain'

class OutputGuardrail(BaseModel):
    """Model for validating tool outputs."""
    result: Dict | List

def validate_goal_input(user_input: str) -> Optional[GoalInput]:
    """
    Validates user goal input (e.g., 'I want to gain 2kg of muscle in 6 weeks' or 'lose 4kg in 2 months').
    """
    pattern = r"(?:i\s+want\s+to\s+)?(?:can\s+you\s+help\s+me\s+)?(?:lose|gain)\s+(\d+\.?\d*)\s*(kg|lbs|pounds)?(?:\s+of\s+(weight|muscle))?\s*in\s+(\d+)\s+(months|weeks)"
    match = re.match(pattern, user_input.lower().strip())
    if not match:
        return None
    try:
        return GoalInput(
            quantity=float(match.group(1)),
            metric=match.group(2) if match.group(2) else "kg",
            duration=f"{match.group(4)} {match.group(5)}",
            type=match.group(0).split()[0] if match.group(0) else "lose"  # Extract 'lose' or 'gain'
        )
    except ValidationError:
        return None

def validate_dietary_input(diet_input: str) -> bool:
    valid_diets = ["vegetarian", "vegan", "keto", "paleo", "gluten-free"]
    return any(diet in diet_input.lower() for diet in valid_diets)

def validate_injury_input(injury_input: str) -> bool:
    return bool(injury_input.strip())

def validate_output(output: Dict | List) -> bool:
    try:
        OutputGuardrail(result=output)
        return True
    except ValidationError:
        return False