import asyncio
from guardrails import validate_dietary_input, validate_output
from context import UserSessionContext
from hooks import LifecycleHooks
import google.generativeai as genai
import os

async def meal_planner_tool(diet_preferences: str, context: UserSessionContext) -> list:
    """
    Generates a 7-day meal plan based on dietary preferences.

    Args:
        diet_preferences: User's dietary preferences.
        context: User session context.

    Returns:
        List of daily meal plans.
    """
    LifecycleHooks.on_tool_start(context, "MealPlannerTool")
    
    if not validate_dietary_input(diet_preferences):
        LifecycleHooks.on_tool_end(context, "MealPlannerTool")
        return [{"status": "error", "message": "Invalid dietary preference"}]

    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
    model = genai.GenerativeModel("gemini-2.0-flash")
    
    prompt = f"Generate a 7-day {diet_preferences} meal plan with breakfast, lunch, dinner, and snacks."
    response = await asyncio.to_thread(model.generate_content, prompt)
    
    meal_plan = response.text.split("\n")[:7]  # Simplified parsing for demo
    if validate_output(meal_plan):
        context.meal_plan = meal_plan
        result = [{"day": i+1, "meals": meal_plan[i]} for i in range(len(meal_plan))]
    else:
        result = [{"status": "error", "message": "Invalid meal plan format"}]
    
    LifecycleHooks.on_tool_end(context, "MealPlannerTool")
    return result