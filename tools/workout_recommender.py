from agents import tool
from context import UserSessionContext
from guardrails import WorkoutPlanOutput # Import the output guardrail for workout plans
from typing import Dict, Any

# @tool
async def WorkoutRecommenderTool(context:UserSessionContext) -> Dict[str, Any]:
    """
    Suggests a weekly workout plan based on the user's parsed goals and (simulated) experience level.
    Stores the generated workout plan in the session context.

    Args:
        context: The current user session context, containing the parsed goal.

    Returns:
        A dictionary representing the structured workout plan, conforming to the WorkoutPlanOutput schema.
    """
    print("WorkoutRecommenderTool called.")
    user_goal = context.state.goal.get("type", "general_fitness") if context.state.goal else "general_fitness"
    # In a real scenario, you might also have an 'experience_level' in context.

    workout_plan_dict = {}
    workout_notes = ""

    if user_goal == "weight_loss":
        workout_plan_dict = {
            "Monday": ["Full Body Strength (Beginner)", "Cardio (20 min)"],
            "Tuesday": ["Rest"],
            "Wednesday": ["Full Body Strength (Beginner)", "Cardio (20 min)"],
            "Thursday": ["Rest"],
            "Friday": ["Full Body Strength (Beginner)", "Cardio (20 min)"],
            "Saturday": ["Active Recovery (Walk/Stretch)"],
            "Sunday": ["Rest"]
        }
        workout_notes = "This plan focuses on a mix of strength training and cardio for weight loss."
    elif user_goal == "muscle_gain":
        workout_plan_dict = {
            "Monday": ["Upper Body (Heavy)", "Abs"],
            "Tuesday": ["Lower Body (Heavy)"],
            "Wednesday": ["Rest"],
            "Thursday": ["Upper Body (Moderate)", "Abs"],
            "Friday": ["Lower Body (Moderate)"],
            "Saturday": ["Active Recovery / Light Cardio"],
            "Sunday": ["Rest"]
        }
        workout_notes = "This plan is a split routine focused on muscle hypertrophy."
    else: # general_fitness or other
        workout_plan_dict = {
            "Monday": ["Full Body Circuit (30 min)"],
            "Tuesday": ["Cardio (30 min)"],
            "Wednesday": ["Yoga / Flexibility (30 min)"],
            "Thursday": ["Full Body Circuit (30 min)"],
            "Friday": ["Cardio (30 min)"],
            "Saturday": ["Long Walk / Hike"],
            "Sunday": ["Rest"]
        }
        workout_notes = "This is a balanced plan for general fitness and well-being."

    # Validate the generated data against the WorkoutPlanOutput guardrail
    try:
        validated_plan = WorkoutPlanOutput(workout_plan=workout_plan_dict, workout_notes=workout_notes)
        context.state.workout_plan = validated_plan.model_dump() # Store in context
        print(f"Workout plan generated and stored.")
        return validated_plan.model_dump()
    except Exception as e:
        print(f"Failed to generate valid workout plan: {e}")
        return {"error": f"Could not generate a workout plan. Error: {e}"}