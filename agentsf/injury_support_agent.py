import asyncio
import google.generativeai as genai
from context import UserSessionContext
from hooks import LifecycleHooks
import os

async def injury_support_agent(user_input: str, context: UserSessionContext) -> dict:
    LifecycleHooks.on_agent_start(context, "InjurySupportAgent")
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
    model = genai.GenerativeModel("gemini-2.0-flash")
    prompt = f"Provide general guidelines for exercising with {user_input.lower()}. Include low-impact options, safety tips, and a disclaimer to consult a doctor. Return a structured response."
    response = await asyncio.to_thread(model.generate_content, prompt)
    message = f"Guidelines for exercising with {user_input.lower()}: {response.text}. Always consult a doctor before starting."
    result = {"status": "success", "message": message} if response.text else {"status": "error", "message": "No guidelines available"}
    LifecycleHooks.on_agent_end(context, "InjurySupportAgent")
    return result