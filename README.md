# Health & Wellness Planner Agent

A conversational AI-powered health and wellness assistant built with the OpenAI Agents SDK (simulated). It helps users set fitness and dietary goals, generates personalized meal and workout plans, tracks progress, and handles specialized needs via agent handoffs. The app includes a Streamlit UI for interactive user experience.

## Features
- **Goal Analysis**: Parses user goals (e.g., "lose 5kg in 2 months") into structured data.
- **Meal Planning**: Generates 7-day meal plans based on dietary preferences.
- **Workout Recommendations**: Suggests workout plans based on goals and experience.
- **Progress Tracking**: Logs user updates and schedules weekly check-ins.
- **Handoffs**: Delegates to specialized agents for complex needs (e.g., injuries, dietary restrictions).
- **Streaming**: Provides real-time responses for an interactive experience.
- **Guardrails**: Validates inputs and ensures structured outputs.
- **Lifecycle Hooks**: Logs tool usage and handoffs.
- **Streamlit UI**: Interactive frontend for user inputs and responses.

## Folder Structure
- `main.py`: Entry point for the Streamlit app.
- `agent.py`: Main agent logic.
- `context.py`: User session context definition.
- `guardrails.py`: Input/output validation.
- `hooks.py`: Lifecycle hooks for logging.
- `tools/`: Tool implementations.
- `agents/`: Specialized agent implementations.
- `utils/`: Streaming utilities.
- `requirements.txt`: Dependencies for `uv`.

## Setup
1. Ensure you have `uv` installed. Install it with:
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh