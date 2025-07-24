from context import UserSessionContext
from hooks import LifecycleHooks

async def escalation_agent(user_input: str, context: UserSessionContext) -> str:
    """
    Handles escalation to a human coach.

    Args:
        user_input: User input triggering escalation.
        context: User session context.

    Returns:
        Response message for escalation.
    """
    LifecycleHooks.on_agent_start(context, "EscalationAgent")
    response = "Escalating to a human coach. Please wait for further instructions."
    LifecycleHooks.on_handoff(context, "HealthWellnessAgent", "EscalationAgent")
    LifecycleHooks.on_agent_end(context, "EscalationAgent")
    return response