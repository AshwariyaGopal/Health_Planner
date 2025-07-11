from agents import Agent, Runner 
from typing import List, Type, Optional
from context import UserSessionContext

# Import tools
from tools.goal_analyzer import GoalAnalyzerTool
from tools.meal_planner import MealPlannerTool
from tools.workout_recommender import WorkoutRecommenderTool
from tools.scheduler import CheckinSchedulerTool
from tools.tracker import ProgressTrackerTool

# Import specific event types if needed for filtering, otherwise, check event.type string
# from openai.types.responses import ResponseTextDeltaEvent # Uncomment if you use type checking for event.data

# Optional Specialized Agents
try:
    from agentsf.escalation_agent import EscalationAgent
    from agentsf.nutrition_expert_agent import NutritionExpertAgent
    from agentsf.injury_support_agent import InjurySupportAgent
    HANDHOFFS_ENABLED = True
except ImportError:
    HANDHOFFS_ENABLED = False


class HealthWellnessPlannerAgent(Agent):
    def __init__(self, user_session_context: UserSessionContext):
        super().__init__(
            name="HealthWellnessPlannerAgent",
            tools=self._get_tools(),
            handoffs=self._get_handoffs() if HANDHOFFS_ENABLED else None
        )
        self.user_session_context = user_session_context

    def _get_tools(self) -> List[Type]:
        return [
            GoalAnalyzerTool,
            MealPlannerTool,
            WorkoutRecommenderTool,
            CheckinSchedulerTool,
            ProgressTrackerTool,
        ]

    def _get_handoffs(self) -> Optional[dict]:
        if not HANDHOFFS_ENABLED:
            return None

        return {
            "escalation_agent": {
                "agent": EscalationAgent(),
                "trigger_condition": "User wants to speak to a human coach."
            },
            "nutrition_expert_agent": {
                "agent": NutritionExpertAgent(),
                "trigger_condition": "User has diabetes, allergies, or complex dietary needs."
            },
            "injury_support_agent": {
                "agent": InjurySupportAgent(),
                "trigger_condition": "User mentions injuries or limitations."
            }
        }

    async def run(self, input_text: str):
        """
        Executes the agent with the given input text and yields chunks of the output.
        """
        # The crucial fix: DO NOT AWAIT Runner.run_streamed() itself.
        # It directly returns the RunResultStreaming object, which is an async iterable.
        stream_result_obj = Runner.run_streamed( # <-- NO 'await' here!
            starting_agent=self,
            input=input_text,
            context=self.user_session_context
        )
        
        # Now, iterate over the events stream from the RunResultStreaming object.
        async for event in stream_result_obj.stream_events():
            # Filter for raw_response_event types to get the actual text chunks.
            if event.type == "raw_response_event":
                # Check if the data is a ResponseTextDeltaEvent and has a 'delta' field
                if hasattr(event.data, 'delta') and event.data.delta:
                    yield event.data.delta # Yield the text chunk

# check