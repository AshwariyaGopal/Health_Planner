from agents import tool
from context import UserSessionContext
from typing import Dict, Any

# @tool
async def ProgressTrackerTool(progress_update: str, context:UserSessionContext) -> Dict[str, str]:
    """
    Accepts an update from the user regarding their progress and logs it in the session context.

    Args:
        progress_update: A natural language description of the user's progress (e.g., "I lost 1kg this week").
        context: The current user session context.

    Returns:
        A dictionary confirming the progress update.
    """
    print(f"ProgressTrackerTool called with update: '{progress_update}'")

    log_entry = {"timestamp": f"{context.current_date}", "update": progress_update} # current_date is implicitly available
    context.state.progress_logs.append(log_entry)

    message = f"Thanks for the update! I've logged your progress: '{progress_update}'."
    print(message)
    return {"status": "success", "message": message}