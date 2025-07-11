import streamlit as st
import asyncio
import uuid
import sys
import os
from dotenv import load_dotenv
import google.generativeai as genai

# --- Adjust path for imports ---
current_script_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, current_script_dir)

# --- Load environment ---
load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")
if not gemini_api_key:
    st.error("🔒 Gemini API Key not found. Please set `GEMINI_API_KEY` in your .env file.")
    st.stop()
genai.configure(api_key=gemini_api_key)

# --- Imports ---
# Make sure these imports are correct based on your file structure
from my_agents import HealthWellnessPlannerAgent
from context import UserSessionContext

# --- Streamlit setup ---
st.set_page_config(page_title="Health & Wellness Planner AI", page_icon="🏋️", layout="wide")

with st.sidebar:
    st.markdown("## 🧭 Instructions")
    st.info("💬 Type your health or fitness goal.\n📅 Get personalized plans.\n🤖 Real-time AI chat.")
    st.markdown("---")
    st.caption("Built with ❤️ using OpenAI Agents SDK + Gemini")

st.title("👨‍⚕️ Health & Wellness Planner")
st.markdown("Welcome! I'm your AI wellness assistant. Let’s plan a healthier you. 💪")

# --- Session states ---
if "agent_runner_instance" not in st.session_state:
    st.session_state["agent_runner_instance"] = None

if "user_session_context" not in st.session_state:
    st.session_state["user_session_context"] = UserSessionContext(
        name="User",
        uid=int(uuid.uuid4().int % 1e6),
        goal={"type": "general wellness"},
        diet_preferences=None,
        workout_plan={},
        meal_plan=None,
        injury_notes="",
        handoff_logs=[],
        progress_logs=[]
    )

if "messages" not in st.session_state:
    st.session_state.messages = []

# --- Display chat history ---
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        # Use markdown for content to allow proper rendering (e.g., bolding, lists)
        st.markdown(f"**{message['role'].capitalize()}:**\n\n{message['content']}")

# --- Async handler ---
async def handle_input():
    # Only process input if a prompt is submitted
    if prompt := st.chat_input("Type your health or fitness question..."):
        # Add user message to chat history and display
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(f"**You:** {prompt}")

        try:
            # Initialize agent instance if not already present in session state
            if st.session_state["agent_runner_instance"] is None:
                st.session_state["agent_runner_instance"] = HealthWellnessPlannerAgent(
                    user_session_context=st.session_state["user_session_context"]
                )

            full_response = ""
            with st.chat_message("assistant"):
                msg_placeholder = st.empty() # Create an empty placeholder to update the message dynamically

                # Iterate over the chunks yielded by the agent's run method
                # This `async for` loop is the crucial part for streaming
                async for chunk in st.session_state["agent_runner_instance"].run(prompt):
                    full_response += chunk
                    # Update the placeholder with the accumulating response and a typing indicator
                    msg_placeholder.markdown(f"**Assistant is typing...**\n\n{full_response}▌")

                # After the loop finishes, display the final complete response
                msg_placeholder.markdown(f"**Assistant:**\n\n{full_response}")

            # Append the full response to session messages
            st.session_state.messages.append({"role": "assistant", "content": full_response})

        except Exception as e:
            # Handle any exceptions during the agent's execution
            st.error(f"🚨 An error occurred: {e}")
            st.session_state.messages.append({"role": "assistant", "content": f"Error: {e}"})

# --- Run async logic ---
# This line ensures the async function `handle_input` is executed
asyncio.run(handle_input())