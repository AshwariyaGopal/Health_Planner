import asyncio
from typing import AsyncGenerator
from context import UserSessionContext
from tools.goal_analyzer import goal_analyzer_tool
from tools.meal_planner import meal_planner_tool
from tools.workout_recommender import workout_recommender_tool
from tools.scheduler import checkin_scheduler_tool
from tools.tracker import progress_tracker_tool
from agentsF.escalation_agent import escalation_agent
from agentsF.nutrition_expert_agent import nutrition_expert_agent
from agentsF.injury_support_agent import injury_support_agent
from hooks import LifecycleHooks
from utils.streaming import stream_response
import google.generativeai as genai
import os

class HealthWellnessAgent:
    def __init__(self, context: UserSessionContext):
        self.context = context
        genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
        self.model = genai.GenerativeModel("gemini-2.0-flash")

    async def process_input(self, user_input: str) -> AsyncGenerator[str, None]:
        LifecycleHooks.on_agent_start(self.context, "HealthWellnessAgent")
        if not any(word in user_input.lower() for word in ["lose", "gain", "weight", "muscle"]):
            self.context.goal = None
        prompt = f"Determine the primary intent of this input: '{user_input}'. Possible intents are: 'goal', 'diet', 'workout', 'injury', 'progress', 'escalation', 'nutrition'. Return only the intent."
        intent_response = await asyncio.to_thread(self.model.generate_content, prompt)
        intent = intent_response.text.lower().strip()
        print(f"Detected intent: {intent}")
        
        if "goal" in intent:
            result = await goal_analyzer_tool(user_input, self.context)
        elif "diet" in intent or "nutrition" in intent:
            self.context.goal = None
            result = await meal_planner_tool(user_input, self.context) if "diet" in intent else await nutrition_expert_agent(user_input, self.context)
        elif "workout" in intent:
            result = await workout_recommender_tool(None, self.context)
        elif "injury" in intent:
            result = await injury_support_agent(user_input, self.context)
        elif "progress" in intent:
            result = await progress_tracker_tool(user_input, self.context)
        elif "escalation" in intent:
            result = await escalation_agent(user_input, self.context)
        else:
            result = await checkin_scheduler_tool(self.context)
        print(f"Tool result: {result}")
        async for response in stream_response(result):
            yield response
        LifecycleHooks.on_agent_end(self.context, "HealthWellnessAgent")