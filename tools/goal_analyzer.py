
from agents import tool

from context import UserSessionContext
from guardrails import GoalInput
from typing import Dict, Any

# We'll use the default LLM, but you could explicitly pass one if needed.
# For simplicity, this example assumes the agent's LLM will handle the parsing.
try:
    from agents import tool
    if not callable(tool):
        raise ImportError
except Exception:
    def tool(func):
        return func
@tool
async def GoalAnalyzerTool(input_goal: str, context:UserSessionContext) -> Dict[str, Any]:
    """
    Analyzes a user's natural language health goal and converts it into a structured format.
    Uses the GoalInput Pydantic model for output validation.

    Args:
        input_goal: The user's natural language description of their health goal (e.g., "I want to lose 5kg in 2 months").
        context: The current user session context, allowing the tool to access and update session data.

    Returns:
        A dictionary representing the structured goal, conforming to the GoalInput schema.
    """
    # The agent's underlying LLM will be prompted to produce output matching GoalInput schema.
    # The SDK automatically handles the Pydantic parsing and validation if the tool's
    # return annotation is a Pydantic model or if the tool is registered with an output schema.
    # For this demonstration, we'll simulate the LLM's parsing.
    # In a real scenario, you'd likely use the LLM to generate the dict output.

    print(f"GoalAnalyzerTool called with input: '{input_goal}'")

    # Example of how an LLM might parse this.
    # In a real application, you'd feed 'input_goal' to the LLM and
    # instruct it to return a JSON conforming to GoalInput.
    parsed_goal_data = {}
    input_goal_lower = input_goal.lower()

    if "lose" in input_goal_lower and "kg" in input_goal_lower:
        try:
            value = float(''.join(filter(str.isdigit, input_goal_lower.split("lose")[1].split("kg")[0])))
            parsed_goal_data = {
                "type": "weight_loss",
                "value": value,
                "unit": "kg",
                "description": input_goal
            }
            if "month" in input_goal_lower:
                parsed_goal_data["duration"] = "2 months" # Simplified for example
        except ValueError:
            pass # Handle cases where parsing fails

    elif "gain muscle" in input_goal_lower:
        parsed_goal_data = {
            "type": "muscle_gain",
            "description": input_goal
        }
        if "month" in input_goal_lower:
            parsed_goal_data["duration"] = "3 months"


    elif "fitness" in input_goal_lower or "overall health" in input_goal_lower:
        parsed_goal_data = {
            "type": "general_fitness",
            "description": input_goal
        }
    else:
        # Fallback for unparsed goals or 'other' type
        parsed_goal_data = {
            "type": "other",
            "description": input_goal
        }

    # Attempt to validate against the GoalInput Pydantic model
    # This step is often handled implicitly by the Agent SDK if the tool signature
    # specifies the Pydantic model as its return type.
    try:
        validated_goal = GoalInput(**parsed_goal_data)
        context.state.goal = validated_goal.model_dump() # Store the parsed goal in context
        print(f"Goal parsed and stored: {context.state.goal}")
        return validated_goal.model_dump() # Return as a dictionary
    except Exception as e:
        print(f"Failed to parse goal with guardrail: {e}")
        # In a real scenario, you might return an error message or
        # signal the agent to ask for clarification.
        return {"error": f"Could not parse your goal. Please try rephrasing. Error: {e}"}