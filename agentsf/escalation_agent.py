

from agents import Agent
from context import UserSessionContext

class EscalationAgent(Agent):
    """
    Handles user requests to speak to a human coach.
    """
    def __init__(self):
        super().__init__(name="Escalation Agent")

    async def on_handoff(self, input_message: str, context: UserSessionContext):
        handoff_message = f"Handoff to Escalation Agent triggered by: '{input_message}'."
        print(handoff_message)
        context.state.handoff_logs.append(handoff_message)
        await context.reply("Okay, I understand you'd like to speak with a human coach. Please hold while I connect you or provide contact information.")
        await context.reply("For immediate assistance, please visit our support page or call us at 1-800-WELLNESS.")
