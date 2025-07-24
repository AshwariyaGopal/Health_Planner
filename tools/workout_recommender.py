import asyncio
from guardrails import validate_output
from context import UserSessionContext
from hooks import LifecycleHooks
import google.generativeai as genai
import os

async def workout_recommender_tool(goal: dict = None, context: UserSessionContext = None) -> dict:
    LifecycleHooks.on_tool_start(context, "WorkoutRecommenderTool")
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
    model = genai.GenerativeModel("gemini-2.0-flash")
    prompt = f"Generate a 7-day workout plan for {'a goal to ' + goal['type'] + ' ' + str(goal['quantity']) + ' ' + goal['metric'] + ' in ' + goal['duration'] if goal else 'general fitness, focusing on strength and cardio'}."
    response = await asyncio.to_thread(model.generate_content, prompt)
    workout_plan = {"days": response.text.split("\n")[:7] if response.text else ["Plan not available"]}
    message = "Here’s a 7-day workout plan: " + " ".join(workout_plan["days"]) + " (full plan in progress). Consult a doctor before starting."
    result = {"status": "success", "message": message} if validate_output(workout_plan) else {"status": "error", "message": "Failed to generate workout plan"}
    context.workout_plan = workout_plan if context else None
    LifecycleHooks.on_tool_end(context, "WorkoutRecommenderTool")
    return result