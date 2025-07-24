import asyncio
from context import UserSessionContext
from hooks import LifecycleHooks
import google.generativeai as genai
import os

async def nutrition_expert_agent(user_input: str, context: UserSessionContext) -> str:
    """
    Handles complex dietary needs (e.g., diabetes, allergies).

    Args:
        user_input: User input for dietary needs.
        context: User session context.

    Returns:
        Response with dietary advice.
    """
    LifecycleHooks.on_agent_start(context, "NutritionExpertAgent")
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
    model = genai.GenerativeModel("gemini-2.0-flash")
    
    prompt = f"Provide dietary advice for someone with {user_input}."
    response = await asyncio.to_thread(model.generate_content, prompt)
    
    LifecycleHooks.on_handoff(context, "HealthWellnessAgent", "NutritionExpertAgent")
    LifecycleHooks.on_agent_end(context, "NutritionExpertAgent")
    return response.text