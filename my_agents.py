# from agents import Agent
# from typing import List, Dict, Any, Type
# from context import UserSessionContext

# # Import all tools
# from tools.goal_analyzer import GoalAnalyzerTool
# from tools.meal_planner import MealPlannerTool
# from tools.workout_recommender import WorkoutRecommenderTool
# from tools.scheduler import CheckinSchedulerTool
# from tools.tracker import ProgressTrackerTool

# # Import specialized agents
# from agentsf.escalation_agent import EscalationAgent
# from agentsf.nutrition_expert_agent import NutritionExpertAgent
# from agentsf.injury_support_agent import InjurySupportAgent

# # Import hooks (optional)
# # from hooks import CustomAgentHooks

# class HealthWellnessPlannerAgent(Agent):
#     def __init__(self, **kwargs):
#         super().__init__(
#             name="Health & Wellness Planner",
#             description="Your personal AI assistant for health, fitness, and wellness. I can help set goals, plan meals, recommend workouts, and track progress.",
#             tools=self._get_tools(),
#             handoffs=self._get_handoffs(),
#             # For agent-specific hooks, uncomment and pass an instance:
#             # hooks=CustomAgentHooks(),
#             **kwargs
#         )

#     def _get_tools(self) -> List[Type]:
#         """
#         Defines and returns the list of tools available to this agent.
#         """
#         return [
#             GoalAnalyzerTool,
#             MealPlannerTool,
#             WorkoutRecommenderTool,
#             CheckinSchedulerTool,
#             ProgressTrackerTool,
#         ]

#     def _get_handoffs(self) -> Dict[str, Dict[str, Any]]:
#         """
#         Defines the conditions under which the agent will hand off control
#         to specialized agents.
#         """
#         return {
#             "escalation_agent": {
#                 "agent": EscalationAgent(), # Instantiate the specialized agent
#                 "trigger_condition": "User wants to speak to a human coach or expresses frustration/dissatisfaction."
#             },
#             "nutrition_expert_agent": {
#                 "agent": NutritionExpertAgent(),
#                 "trigger_condition": "User mentions complex dietary needs such as diabetes, severe allergies, specific medical conditions affecting diet, or highly specialized dietary requirements (e.g., professional athlete diet)."
#             },
#             "injury_support_agent": {
#                 "agent": InjurySupportAgent(),
#                 "trigger_condition": "User mentions physical limitations, existing injuries (e.g., knee pain, back injury), or asks for injury-specific workout modifications."
#             }
#         }

#     async def on_start(self, context: UserSessionContext):
#         """
#         Optional: Custom logic when the main agent starts its turn.
#         """
#         # This hook is defined in AgentHooks for individual agents,
#         # but can also be overridden here directly if not using separate hooks class.
#         pass # print(f"Health & Wellness Planner Agent starting its turn.")

#     async def on_end(self, context: UserSessionContext):
#         """
#         Optional: Custom logic when the main agent ends its turn.
#         """
#         pass # print(f"Health & Wellness Planner Agent ending its turn.")

# from agents import Agent
# from typing import List, Type, Optional
# from context import UserSessionContext

# # Tools
# from tools.goal_analyzer import GoalAnalyzerTool
# from tools.meal_planner import MealPlannerTool
# from tools.workout_recommender import WorkoutRecommenderTool
# from tools.scheduler import CheckinSchedulerTool
# from tools.tracker import ProgressTrackerTool

# # Optional Specialized Agents
# try:
#     from agentsf.escalation_agent import EscalationAgent
#     from agentsf.nutrition_expert_agent import NutritionExpertAgent
#     from agentsf.injury_support_agent import InjurySupportAgent
#     HANDOFFS_ENABLED = True
# except ImportError:
#     HANDOFFS_ENABLED = False

# # Optional Hooks
# # from hooks import CustomAgentHooks

# class HealthWellnessPlannerAgent(Agent):
#     def __init__(self, **kwargs):
#         super().__init__(
#             name="HealthWellnessPlannerAgent",
#             tools=self._get_tools(),
#             handoffs=self._get_handoffs() if HANDOFFS_ENABLED else None,
#             # hooks=CustomAgentHooks(),  # Optional
#             **kwargs
#         )

#     def _get_tools(self) -> List[Type]:
#         return [
#             GoalAnalyzerTool,
#             MealPlannerTool,
#             WorkoutRecommenderTool,
#             CheckinSchedulerTool,
#             ProgressTrackerTool,
#         ]

#     def _get_handoffs(self) -> Optional[dict]:
#         if not HANDOFFS_ENABLED:
#             return None

#         return {
#             "escalation_agent": {
#                 "agent": EscalationAgent(),
#                 "trigger_condition": "User wants to speak to a human coach."
#             },
#             "nutrition_expert_agent": {
#                 "agent": NutritionExpertAgent(),
#                 "trigger_condition": "User has diabetes, allergies, or complex dietary needs."
#             },
#             "injury_support_agent": {
#                 "agent": InjurySupportAgent(),
#                 "trigger_condition": "User mentions injuries or limitations."
#             }
#         }

#     async def on_start(self, context: UserSessionContext):
#         pass  # Optional

#     async def on_end(self, context: UserSessionContext):
#         pass  # Optional

# from agents import Agent
# from typing import List, Optional
# from context import UserSessionContext

# # Tools
# from tools.goal_analyzer import GoalAnalyzerTool
# from tools.meal_planner import MealPlannerTool
# from tools.workout_recommender import WorkoutRecommenderTool
# from tools.scheduler import CheckinSchedulerTool
# from tools.tracker import ProgressTrackerTool

# # Optional Specialized Agents
# try:
#     from agentsf.escalation_agent import EscalationAgent
#     from agentsf.nutrition_expert_agent import NutritionExpertAgent
#     from agentsf.injury_support_agent import InjurySupportAgent
#     HANDOFFS_ENABLED = True
# except ImportError:
#     HANDOFFS_ENABLED = False

# class HealthWellnessPlannerAgent(Agent):
#     def __init__(self, user_session_context: Optional[UserSessionContext] = None):
#         # Store user session context
#         self.user_session_context = user_session_context

#         # Initialize base Agent class
#         super().__init__(
#             name="HealthWellnessPlannerAgent",
#             tools=self._get_tools(),
#             handoffs=self._get_handoffs() if HANDOFFS_ENABLED else None,
#             # context_type=UserSessionContext  # required by SDK
#         )

#     def _get_tools(self) -> List[type]:
#         return [
#             GoalAnalyzerTool,
#             MealPlannerTool,
#             WorkoutRecommenderTool,
#             CheckinSchedulerTool,
#             ProgressTrackerTool,
#         ]

#     def _get_handoffs(self) -> Optional[dict]:
#         return {
#             "escalation_agent": {
#                 "agent": EscalationAgent(),
#                 "trigger_condition": "User wants to speak to a human coach."
#             },
#             "nutrition_expert_agent": {
#                 "agent": NutritionExpertAgent(),
#                 "trigger_condition": "User has diabetes, allergies, or complex dietary needs."
#             },
#             "injury_support_agent": {
#                 "agent": InjurySupportAgent(),
#                 "trigger_condition": "User mentions injuries or limitations."
#             }
#         } if HANDOFFS_ENABLED else None

#     async def on_start(self, context: UserSessionContext):
#         # Optional: hook logic
#         pass

#     async def on_end(self, context: UserSessionContext):
#         # Optional: hook logic
#         pass


# from agents import Agent, Runner
# from typing import List, Type, Optional
# from context import UserSessionContext

# # Import tools
# from tools.goal_analyzer import GoalAnalyzerTool
# from tools.meal_planner import MealPlannerTool
# from tools.workout_recommender import WorkoutRecommenderTool
# from tools.scheduler import CheckinSchedulerTool
# from tools.tracker import ProgressTrackerTool

# # Optional Specialized Agents
# try:
#     from agentsf.escalation_agent import EscalationAgent
#     from agentsf.nutrition_expert_agent import NutritionExpertAgent
#     from agentsf.injury_support_agent import InjurySupportAgent
#     HANDOFFS_ENABLED = True
# except ImportError:
#     HANDOFFS_ENABLED = False

# class HealthWellnessPlannerAgent(Agent):
#     def __init__(self, user_session_context: UserSessionContext):
#         super().__init__(
#             name="HealthWellnessPlannerAgent",
#             tools=self._get_tools(),
#             handoffs=self._get_handoffs() if HANDOFFS_ENABLED else None
#         )
#         self.user_session_context = user_session_context

#     def _get_tools(self) -> List[Type]:
#         return [
#             GoalAnalyzerTool,
#             MealPlannerTool,
#             WorkoutRecommenderTool,
#             CheckinSchedulerTool,
#             ProgressTrackerTool,
#         ]

#     def _get_handoffs(self) -> Optional[dict]:
#         if not HANDOFFS_ENABLED:
#             return None
#         return {
#             "escalation_agent": {
#                 "agent": EscalationAgent(),
#                 "trigger_condition": "User wants to speak to a human coach."
#             },
#             "nutrition_expert_agent": {
#                 "agent": NutritionExpertAgent(),
#                 "trigger_condition": "User has diabetes, allergies, or complex dietary needs."
#             },
#             "injury_support_agent": {
#                 "agent": InjurySupportAgent(),
#                 "trigger_condition": "User mentions injuries or limitations."
#             }
#         }

#     def run(self, input_text: str):
#         return Runner.run_streamed(
#             starting_agent=self,
#             input=input_text,
#             context=self.user_session_context
#         )

# wait
# from agents import Agent,  Runner
# # from openai_agents.runner import run_streamed
# from typing import List, Type, Optional
# from context import UserSessionContext

# # Import tools
# from tools.goal_analyzer import GoalAnalyzerTool
# from tools.meal_planner import MealPlannerTool
# from tools.workout_recommender import WorkoutRecommenderTool
# from tools.scheduler import CheckinSchedulerTool
# from tools.tracker import ProgressTrackerTool

# # Optional Specialized Agents
# try:
#     from agentsf.escalation_agent import EscalationAgent
#     from agentsf.nutrition_expert_agent import NutritionExpertAgent
#     from agentsf.injury_support_agent import InjurySupportAgent
#     HANDOFFS_ENABLED = True
# except ImportError:
#     HANDOFFS_ENABLED = False

# class HealthWellnessPlannerAgent(Agent):
#     def __init__(self, user_session_context: UserSessionContext):
#         super().__init__(
#             name="HealthWellnessPlannerAgent",
#             tools=self._get_tools(),
#             handoffs=self._get_handoffs() if HANDOFFS_ENABLED else None,
#         )
#         self.user_session_context = user_session_context

#     def _get_tools(self) -> List[Type]:
#         return [
#             GoalAnalyzerTool,
#             MealPlannerTool,
#             WorkoutRecommenderTool,
#             CheckinSchedulerTool,
#             ProgressTrackerTool,
#         ]

#     def _get_handoffs(self) -> Optional[dict]:
#         if not HANDOFFS_ENABLED:
#             return None
#         return {
#             "escalation_agent": {
#                 "agent": EscalationAgent(),
#                 "trigger_condition": "User wants to speak to a human coach."
#             },
#             "nutrition_expert_agent": {
#                 "agent": NutritionExpertAgent(),
#                 "trigger_condition": "User has diabetes, allergies, or complex dietary needs."
#             },
#             "injury_support_agent": {
#                 "agent": InjurySupportAgent(),
#                 "trigger_condition": "User mentions injuries or limitations."
#             }
#         }

#     async def run(self, input_text: str):
#         return Runner.run_streamed(
#             starting_agent=self,
#             input=input_text,
#             context=self.user_session_context
#         )


#check
# from agents import Agent, Runner
# from typing import List, Type, Optional
# from context import UserSessionContext

# # Tools
# from tools.goal_analyzer import GoalAnalyzerTool
# from tools.meal_planner import MealPlannerTool
# from tools.workout_recommender import WorkoutRecommenderTool
# from tools.scheduler import CheckinSchedulerTool
# from tools.tracker import ProgressTrackerTool

# # Optional Specialized Agents
# try:
#     from agentsf.escalation_agent import EscalationAgent
#     from agentsf.nutrition_expert_agent import NutritionExpertAgent
#     from agentsf.injury_support_agent import InjurySupportAgent
#     HANDOFFS_ENABLED = True
# except ImportError:
#     HANDOFFS_ENABLED = False

# class HealthWellnessPlannerAgent(Agent):
#     def __init__(self, user_session_context: UserSessionContext):
#         super().__init__(
#             name="HealthWellnessPlannerAgent",
#             tools=self._get_tools(),
#             handoffs=self._get_handoffs() if HANDOFFS_ENABLED else None
#         )
#         self.user_session_context = user_session_context

#     def _get_tools(self) -> List[Type]:
#         return [
#             GoalAnalyzerTool,
#             MealPlannerTool,
#             WorkoutRecommenderTool,
#             CheckinSchedulerTool,
#             ProgressTrackerTool,
#         ]

#     def _get_handoffs(self) -> Optional[dict]:
#         if not HANDOFFS_ENABLED:
#             return None
#         return {
#             "escalation_agent": {
#                 "agent": EscalationAgent(),
#                 "trigger_condition": "User wants to speak to a human coach."
#             },
#             "nutrition_expert_agent": {
#                 "agent": NutritionExpertAgent(),
#                 "trigger_condition": "User has diabetes, allergies, or complex dietary needs."
#             },
#             "injury_support_agent": {
#                 "agent": InjurySupportAgent(),
#                 "trigger_condition": "User mentions injuries or limitations."
#             }
#         }

#     async def run(self, input_text: str):
#         return await Runner.run_streamed(
#             starting_agent=self,
#             input=input_text,
#             context=self.user_session_context
#         )
#check
# from agents import Agent, Runner
# from typing import List, Type, Optional
# from context import UserSessionContext

# # Tools
# from tools.goal_analyzer import GoalAnalyzerTool
# from tools.meal_planner import MealPlannerTool
# from tools.workout_recommender import WorkoutRecommenderTool
# from tools.scheduler import CheckinSchedulerTool
# from tools.tracker import ProgressTrackerTool

# # Optional Specialized Agents
# try:
#     from agentsf.escalation_agent import EscalationAgent
#     from agentsf.nutrition_expert_agent import NutritionExpertAgent
#     from agentsf.injury_support_agent import InjurySupportAgent
#     HANDOFFS_ENABLED = True
# except ImportError:
#     HANDOFFS_ENABLED = False

# class HealthWellnessPlannerAgent(Agent):
#     def __init__(self, user_session_context: UserSessionContext):
#         super().__init__(
#             name="HealthWellnessPlannerAgent",
#             tools=self._get_tools(),
#             handoffs=self._get_handoffs() if HANDOFFS_ENABLED else None
#         )
#         self.user_session_context = user_session_context

#     def _get_tools(self) -> List[Type]:
#         return [
#             GoalAnalyzerTool,
#             MealPlannerTool,
#             WorkoutRecommenderTool,
#             CheckinSchedulerTool,
#             ProgressTrackerTool,
#         ]

#     def _get_handoffs(self) -> Optional[dict]:
#         if not HANDOFFS_ENABLED:
#             return None
#         return {
#             "escalation_agent": {
#                 "agent": EscalationAgent(),
#                 "trigger_condition": "User wants to speak to a human coach."
#             },
#             "nutrition_expert_agent": {
#                 "agent": NutritionExpertAgent(),
#                 "trigger_condition": "User has diabetes, allergies, or complex dietary needs."
#             },
#             "injury_support_agent": {
#                 "agent": InjurySupportAgent(),
#                 "trigger_condition": "User mentions injuries or limitations."
#             }
#         }

#     def run(self, input_text: str):
#         return Runner.run_streamed(
#             starting_agent=self,
#             input=input_text,
#             context=self.user_session_context
#         )

#         # return result.steps  # ✅ iterable output

    
# check

# from agents import Agent, Runner
# from typing import List, Type, Optional
# from context import UserSessionContext

# # Import tools
# from tools.goal_analyzer import GoalAnalyzerTool
# from tools.meal_planner import MealPlannerTool
# from tools.workout_recommender import WorkoutRecommenderTool
# from tools.scheduler import CheckinSchedulerTool
# from tools.tracker import ProgressTrackerTool

# # Optional Specialized Agents
# try:
#     from agentsf.escalation_agent import EscalationAgent
#     from agentsf.nutrition_expert_agent import NutritionExpertAgent
#     from agentsf.injury_support_agent import InjurySupportAgent
#     HANDOFFS_ENABLED = True
# except ImportError:
#     HANDOFFS_ENABLED = False


# class HealthWellnessPlannerAgent(Agent):
#     def __init__(self, user_session_context: UserSessionContext):
#         super().__init__(
#             name="HealthWellnessPlannerAgent",
#             tools=self._get_tools(),
#             handoffs=self._get_handoffs() if HANDOFFS_ENABLED else None
#         )
#         self.user_session_context = user_session_context

#     def _get_tools(self) -> List[Type]:
#         return [
#             GoalAnalyzerTool,
#             MealPlannerTool,
#             WorkoutRecommenderTool,
#             CheckinSchedulerTool,
#             ProgressTrackerTool,
#         ]

#     def _get_handoffs(self) -> Optional[dict]:
#         if not HANDOFFS_ENABLED:
#             return None

#         return {
#             "escalation_agent": {
#                 "agent": EscalationAgent(),
#                 "trigger_condition": "User wants to speak to a human coach."
#             },
#             "nutrition_expert_agent": {
#                 "agent": NutritionExpertAgent(),
#                 "trigger_condition": "User has diabetes, allergies, or complex dietary needs."
#             },
#             "injury_support_agent": {
#                 "agent": InjurySupportAgent(),
#                 "trigger_condition": "User mentions injuries or limitations."
#             }
#         }

#     async def run(self, input_text: str) -> str:
#         """
#         Executes the agent with the given input text and returns the final output.
#         """
#         result = await Runner.run_streamed(
#             starting_agent=self,
#             input=input_text,
#             context=self.user_session_context
#         )
#         final_output = await result.get_final_output()
#         return final_output
    
# check
# import sys
# import os
# from agents import Agent, Runner
# from typing import List, Type, Optional
# from context import UserSessionContext

# # Import tools
# from tools.goal_analyzer import GoalAnalyzerTool
# from tools.meal_planner import MealPlannerTool
# from tools.workout_recommender import WorkoutRecommenderTool
# from tools.scheduler import CheckinSchedulerTool
# from tools.tracker import ProgressTrackerTool

# # Optional Specialized Agents
# try:
#     # Ensure these imports are correct based on your project structure
#     from agentsf.escalation_agent import EscalationAgent
#     from agentsf.nutrition_expert_agent import NutritionExpertAgent
#     from agentsf.injury_support_agent import InjurySupportAgent
#     HANDHOFFS_ENABLED = True
# except ImportError:
#     HANDHOFFS_ENABLED = False


# class HealthWellnessPlannerAgent(Agent):
#     def __init__(self, user_session_context: UserSessionContext):
#         super().__init__(
#             name="HealthWellnessPlannerAgent",
#             tools=self._get_tools(),
#             handoffs=self._get_handoffs() if HANDHOFFS_ENABLED else None
#         )
#         self.user_session_context = user_session_context

#     def _get_tools(self) -> List[Type]:
#         return [
#             GoalAnalyzerTool,
#             MealPlannerTool,
#             WorkoutRecommenderTool,
#             CheckinSchedulerTool,
#             ProgressTrackerTool,
#         ]

#     def _get_handoffs(self) -> Optional[dict]:
#         if not HANDHOFFS_ENABLED:
#             return None

#         return {
#             "escalation_agent": {
#                 "agent": EscalationAgent(),
#                 "trigger_condition": "User wants to speak to a human coach."
#             },
#             "nutrition_expert_agent": {
#                 "agent": NutritionExpertAgent(),
#                 "trigger_condition": "User has diabetes, allergies, or complex dietary needs."
#             },
#             "injury_support_agent": {
#                 "agent": InjurySupportAgent(),
#                 "trigger_condition": "User mentions injuries or limitations."
#             }
#         }

#     async def run(self, input_text: str):
#         """
#         Executes the agent with the given input text and yields chunks of the output.
#         """
#         # Runner.run_streamed is designed to be an async generator
#         async for chunk in Runner.run_streamed(
#             starting_agent=self,
#             input=input_text,
#             context=self.user_session_context
#         ):
#             yield chunk


import sys
import os
from agents import Agent, Runner # Assuming 'Agent' and 'Runner' are correctly imported
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