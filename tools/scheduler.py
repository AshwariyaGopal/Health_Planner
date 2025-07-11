from agents import tool
from context import UserSessionContext
from typing import Dict, Any

# @tool
async def CheckinSchedulerTool(context: UserSessionContext) -> Dict[str, str]:
    """
    Schedules a recurring weekly progress check for the user.
    Updates the session context to indicate that check-ins are scheduled.

    Args:
        context: The current user session context.

    Returns:
        A dictionary confirming the scheduling.
    """
    print("CheckinSchedulerTool called.")
    # In a real application, you might integrate with a calendaring API or a notification service.
    # For this simulation, we'll just update the context and return a confirmation.

    message = "Weekly progress checks have been scheduled! I'll remind you every week to update your progress."
    context.state.progress_logs.append({"type": "scheduled_checkin", "message": message})

    print("Weekly check-ins scheduled.")
    return {"status": "success", "message": message}