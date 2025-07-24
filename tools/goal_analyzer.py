from guardrails import validate_goal_input
from context import UserSessionContext
from hooks import LifecycleHooks
from tools.workout_recommender import workout_recommender_tool
from tools.meal_planner import meal_planner_tool

async def goal_analyzer_tool(user_input: str, context: UserSessionContext) -> dict:
    LifecycleHooks.on_tool_start(context, "GoalAnalyzerTool")
    goal = validate_goal_input(user_input)
    if goal:
        context.goal = {"quantity": goal.quantity, "metric": goal.metric, "duration": goal.duration, "type": goal.type}
        workout_plan = await workout_recommender_tool(context.goal, context)
        meal_plan = await meal_planner_tool("balanced", context)
        workout_details = workout_plan.get("workout_plan", {}).get("days", ["Workout plan pending"])
        meal_details = meal_plan[0].get("meals", "Meal plan pending") if meal_plan else "Meal plan pending"
        action = "gain" if goal.type == "gain" else "lose"
        result = {
            "status": "success",
            "message": f"Your goal to {action} {goal.quantity} {goal.metric} in {goal.duration} has been set. Here’s a preliminary workout plan: {', '.join(workout_details[:2])}... (full plan in progress). Initial meal plan: {meal_details}... (specify dietary preferences!)."
        }
    else:
        result = {"status": "error", "message": "Invalid goal format. Example: 'lose 5kg in 2 months' or 'gain 2kg of muscle in 6 weeks'"}
    LifecycleHooks.on_tool_end(context, "GoalAnalyzerTool")
    return result