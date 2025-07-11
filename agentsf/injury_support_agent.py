from agents import Agent
from context import UserSessionContext

class InjurySupportAgent(Agent):
    """
    Specialized agent for physical limitations or injury-specific workouts.
    """
    def __init__(self):
        super().__init__(name="Injury Support Agent")

    async def on_handoff(self, input_message: str, context: UserSessionContext):
        handoff_message = f"Handoff to Injury Support Agent triggered by: '{input_message}'."
        print(handoff_message)
        context.state.handoff_logs.append(handoff_message)
        await context.reply("Hi there! I'm the Injury Support Agent. I can help you find suitable exercises or modify workout plans if you have an injury or physical limitation.")
        await context.reply("Please describe your injury or limitation in detail, and I'll do my best to assist you.")
        await context.reply("Disclaimer: I am an AI and cannot provide medical advice. Always consult a medical professional for diagnosis and treatment of injuries.")
