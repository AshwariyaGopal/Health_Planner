# from agents import Agent
# from context import UserSessionContext

# class NutritionExpertAgent(Agent):
#     """
#     Specialized agent for complex dietary needs like diabetes or allergies.
#     """
#     def __init__(self, **kwargs):
#         super().__init__(name="Nutrition Expert Agent", description="Provides expert advice on complex dietary needs.", **kwargs)

#     async def on_handoff(self, input_message: str, context: UserSessionContext):
#         """
#         Executed when control is handed off to this agent.
#         """
#         handoff_message = f"Handoff to Nutrition Expert Agent triggered by: '{input_message}'."
#         print(handoff_message)
#         context.state.handoff_logs.append(handoff_message)
#         await context.reply("Hello! I'm your Nutrition Expert Agent. I can help with complex dietary needs like allergies or managing conditions like diabetes. Please tell me more about your specific requirements.")
#         # In a real system, this agent would have specific tools or LLM prompts
#         # to process and respond to complex nutrition queries.
#         await context.reply("Please note: For medical conditions, always consult with a healthcare professional.")

from agents import Agent
from context import UserSessionContext

class NutritionExpertAgent(Agent):
    """
    Specialized agent for complex dietary needs like diabetes or allergies.
    """
    def __init__(self):
        super().__init__(name="Nutrition Expert Agent")

    async def on_handoff(self, input_message: str, context: UserSessionContext):
        handoff_message = f"Handoff to Nutrition Expert Agent triggered by: '{input_message}'."
        print(handoff_message)
        context.state.handoff_logs.append(handoff_message)
        await context.reply("Hello! I'm your Nutrition Expert Agent. I can help with complex dietary needs like allergies or managing conditions like diabetes. Please tell me more about your specific requirements.")
        await context.reply("Please note: For medical conditions, always consult with a healthcare professional.")
