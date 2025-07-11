from pydantic import BaseModel, Field, ValidationError
from typing import Optional, List, Literal, Dict

# --- Input Guardrails ---

class GoalInput(BaseModel):
    """
    Defines the expected structured format for user health goals.
    This model is used to validate the output of the GoalAnalyzerTool
    and ensure goals are in a consistent format.
    """
    type: Literal["weight_loss", "muscle_gain", "general_fitness", "endurance", "flexibility", "other"] = Field(
        ..., description="The type of health goal."
    )
    value: Optional[float] = Field(
        None, description="The numerical value associated with the goal (e.g., 5 for 5kg)."
    )
    unit: Optional[str] = Field(
        None, description="The unit of the value (e.g., 'kg', 'lbs')."
    )
    duration: Optional[str] = Field(
        None, description="The desired time frame for the goal (e.g., '2 months', '3 weeks')."
    )
    description: str = Field(
        ..., description="A natural language description of the goal."
    )

    class Config:
        json_schema_extra = {
            "examples": [
                {
                    "type": "weight_loss",
                    "value": 5.0,
                    "unit": "kg",
                    "duration": "2 months",
                    "description": "lose 5kg in 2 months"
                },
                {
                    "type": "muscle_gain",
                    "value": None,
                    "unit": None,
                    "duration": "3 months",
                    "description": "gain muscle mass over 3 months"
                },
                {
                    "type": "general_fitness",
                    "value": None,
                    "unit": None,
                    "duration": None,
                    "description": "improve overall fitness"
                }
            ]
        }


# --- Output Guardrails (Examples for Tools) ---

class MealPlanOutput(BaseModel):
    """
    Defines the structured format for the 7-day meal plan output from MealPlannerTool.
    """
    meal_plan: List[str] = Field(
        ..., min_length=7, max_length=7,
        description="A 7-day meal plan, where each item is a detailed daily meal description."
    )
    dietary_notes: Optional[str] = Field(
        None, description="Any specific notes or considerations regarding the dietary preferences."
    )

    class Config:
        json_schema_extra = {
            "examples": [
                {
                    "meal_plan": [
                        "Day 1: Breakfast - Oatmeal with berries; Lunch - Lentil soup; Dinner - Tofu stir-fry with brown rice.",
                        "Day 2: Breakfast - Smoothie with spinach and banana; Lunch - Chickpea salad sandwich; Dinner - Vegetable curry.",
                        # ... up to Day 7
                    ],
                    "dietary_notes": "All meals are vegetarian and designed to be balanced."
                }
            ]
        }

class WorkoutPlanOutput(BaseModel):
    """
    Defines the structured format for the workout plan output from WorkoutRecommenderTool.
    """
    workout_plan: Dict[str, List[str]] = Field(
        ...,
        description="A dictionary representing the weekly workout plan. Keys are days (e.g., 'Monday'), values are lists of exercises for that day."
    )
    workout_notes: Optional[str] = Field(
        None, description="Any specific notes or considerations regarding the workout plan."
    )

    class Config:
        json_schema_extra = {
            "examples": [
                {
                    "workout_plan": {
                        "Monday": ["Warm-up (10 min)", "Squats (3x10)", "Bench Press (3x10)", "Rows (3x10)", "Cool-down (5 min)"],
                        "Tuesday": ["Rest or Light Cardio"],
                        "Wednesday": ["Warm-up (10 min)", "Deadlifts (3x8)", "Overhead Press (3x10)", "Pull-ups (3xMax)", "Cool-down (5 min)"],
                        "Thursday": ["Rest or Active Recovery"],
                        "Friday": ["Warm-up (10 min)", "Lunges (3x10/leg)", "Push-ups (3xMax)", "Plank (3x60s)", "Cool-down (5 min)"],
                        "Saturday": ["Light Cardio or Stretching"],
                        "Sunday": ["Rest"]
                    },
                    "workout_notes": "This is a beginner-friendly strength training plan."
                }
            ]
        }

# You can add more guardrail models for other tools as needed