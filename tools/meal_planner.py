from agents import tool

from context import UserSessionContext
from guardrails import MealPlanOutput # Import the output guardrail for meal plans
from typing import List, Dict, Any
try:
    from agents import tool
    if not callable(tool):
        raise ImportError
except Exception:
    def tool(func):
        return func
@tool
async def MealPlannerTool(context: UserSessionContext) -> Dict[str, Any]:
    """
    Generates a 7-day meal plan based on the user's dietary preferences and goals.
    Stores the generated meal plan in the session context.

    Args:
        context: The current user session context, containing diet preferences and goal.

    Returns:
        A dictionary representing the structured meal plan, conforming to the MealPlanOutput schema.
    """
    print("MealPlannerTool called.")
    diet_pref = context.state.diet_preferences if context.state.diet_preferences else "standard"
    user_goal = context.state.goal.get("description", "general health") if context.state.goal else "general health"

    # In a real scenario, you'd use an LLM call here to generate the meal plan.
    # Example prompt for LLM:
    # "Generate a 7-day meal plan for a user with '{diet_pref}' dietary preferences,
    # aiming for '{user_goal}'. Ensure each day has breakfast, lunch, and dinner.
    # Format the output as a list of strings, one string per day. Each string should start with 'Day X:'"

    # Simulating LLM response for demonstration
    meal_plan_list = [
        f"Day 1: Breakfast - Oatmeal with berries; Lunch - {diet_pref} lentil soup; Dinner - {diet_pref} stir-fry.",
        f"Day 2: Breakfast - {diet_pref} smoothie; Lunch - Chickpea salad sandwich; Dinner - {diet_pref} curry.",
        f"Day 3: Breakfast - Scrambled eggs (or tofu scramble for vegan); Lunch - Quinoa salad; Dinner - {diet_pref} pasta.",
        f"Day 4: Breakfast - Yogurt with granola; Lunch - Veggie wrap; Dinner - Baked {diet_pref} dish.",
        f"Day 5: Breakfast - Whole wheat toast with avocado; Lunch - {diet_pref} and vegetable skewers; Dinner - {diet_pref} pizza.",
        f"Day 6: Breakfast - Pancakes with fruit; Lunch - {diet_pref} burrito bowl; Dinner - {diet_pref} casserole.",
        f"Day 7: Breakfast - Fruit salad; Lunch - Leftovers; Dinner - {diet_pref} soup and bread."
    ]

    dietary_notes = f"This 7-day meal plan is designed for a {diet_pref} diet, focusing on your goal of {user_goal}."

    # Validate the generated data against the MealPlanOutput guardrail
    try:
        validated_plan = MealPlanOutput(meal_plan=meal_plan_list, dietary_notes=dietary_notes)
        context.state.meal_plan = validated_plan.meal_plan # Store in context
        print(f"Meal plan generated and stored.")
        return validated_plan.model_dump()
    except Exception as e:
        print(f"Failed to generate valid meal plan: {e}")
        return {"error": f"Could not generate a meal plan. Error: {e}"}