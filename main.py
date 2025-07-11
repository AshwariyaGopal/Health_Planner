# import streamlit as st # NEW: Added for Streamlit UI
# import asyncio         # NEW: Added for Streamlit UI (if using async operations)
# import uuid            # NEW: Added for Streamlit UI (for user_id)
# import sys
# import os
# from dotenv import load_dotenv # NEW: For loading .env file
# import google.generativeai as genai # NEW: For Gemini configuration

# # --- Essential: Add the project root directory to sys.path ---
# # This allows Python to find sibling modules (like my_agents, context, hooks, utils)
# current_script_dir = os.path.dirname(os.path.abspath(__file__))
# sys.path.insert(0, current_script_dir)
# # --- End of essential path modification ---

# # --- NEW: Load environment variables and configure Gemini ---
# load_dotenv() # Load variables from .env file
# # Get the Gemini API key from the environment variable
# gemini_api_key = os.getenv("GOOGLE_API_KEY")

# if not gemini_api_key:
#     st.error("Google API Key not found. Please set GOOGLE_API_KEY in your .env file.")
#     st.stop() # Stop the Streamlit app if no key is found

# genai.configure(api_key=gemini_api_key)
# # --- END NEW Gemini config ---

# # --- Your Local Project Imports (corrected based on my_agents.py) ---
# from my_agents import HealthWellnessPlannerAgent # Correct import for your agent
# from context import UserSessionContext
# from hooks import CustomRunHooks
# from utils.streaming import print_streaming_output # Assuming utils is a folder/package

# # --- Removed: from openai_agents import Runner and openai_agents.types ---
# # Based on previous code, you were directly instantiating HealthWellnessPlannerAgent
# # and calling its .run() method, not using a generic 'Runner' class from openai_agents.
# # If HealthWellnessPlannerAgent itself uses openai-agents' Runner internally,
# # it will handle those imports within its own module.

# # --- Streamlit UI Setup (Moved from old app.py) ---
# st.set_page_config(page_title="Health & Wellness Planner AI", page_icon="🏋️", layout="wide")
# st.title("👨‍⚕️ Health & Wellness Planner AI")

# # Initialize Session state
# if "agent_runner_instance" not in st.session_state: # Renamed from "agent_runner" to avoid confusion
#     st.session_state["agent_runner_instance"] = None
# if "user_session_context" not in st.session_state:
#     st.session_state["user_session_context"] = UserSessionContext(
#         user_id=str(uuid.uuid4()),
#         name="User",
#         gender="Not specified",
#         age=0,
#         weight=0,
#         height=0,
#         goals=[],
#         workout_plan=[],
#         meal_plan=[],
#         injury_notes=[],
#         handoff_logs=[],
#         progress_logs=[],
#         current_focus="general wellness"
#     )
# if "messages" not in st.session_state:
#     st.session_state.messages = []

# # Display chat messages from history
# for message in st.session_state.messages:
#     with st.chat_message(message["role"]):
#         st.markdown(message["content"])

# # Chat input
# if prompt := st.chat_input("Ask your health question..."):
#     st.session_state.messages.append({"role": "user", "content": prompt})
#     with st.chat_message("user"):
#         st.markdown(prompt)

#     try:
#         # Create or get the agent instance
#         if st.session_state["agent_runner_instance"] is None:
#             st.session_state["agent_runner_instance"] = HealthWellnessPlannerAgent(
#                 user_session_context=st.session_state["user_session_context"],
#                 # IMPORTANT: If your HealthWellnessPlannerAgent needs a model parameter,
#                 # you will pass it here. For Gemini, it's typically "gemini-pro" or "gemini-1.5-pro".
#                 # Example (if your agent class accepts 'model_name'):
#                 # model_name="gemini-pro",
#             )

#         # Get response from the agent
#         # Assuming HealthWellnessPlannerAgent's .run method is blocking or returns an iterable
#         # If it's truly async, you'd need asyncio.run() or a Streamlit async handler
#         response_generator = st.session_state["agent_runner_instance"].run(prompt)

#         full_response = ""
#         with st.chat_message("assistant"):
#             message_placeholder = st.empty()
#             for chunk in response_generator:
#                 full_response += chunk
#                 message_placeholder.markdown(full_response + "▌") # Typing effect
#             message_placeholder.markdown(full_response)

#         st.session_state.messages.append({"role": "assistant", "content": full_response})

#     except Exception as e:
#         st.error(f"An error occurred: {e}")
#         st.session_state.messages.append({"role": "assistant", "content": f"Error: {e}"})

# # --- End of Streamlit UI code in main.py ---

# # Note: The original 'def main_cli()' and 'if __name__ == "__main__":'
# # are removed as this file is now purely for Streamlit UI.


# ✅ FINAL COMPLETE Streamlit UI (main.py) matching your assignment specs

# import streamlit as st
# import asyncio
# import uuid
# import sys
# import os
# from dotenv import load_dotenv
# import google.generativeai as genai

# # --- Adjust path to enable local imports ---
# current_script_dir = os.path.dirname(os.path.abspath(__file__))
# sys.path.insert(0, current_script_dir)

# # --- Load .env and configure Gemini ---
# load_dotenv()
# gemini_api_key = os.getenv("GOOGLE_API_KEY")
# if not gemini_api_key:
#     st.error("Google API Key not found. Please set GOOGLE_API_KEY in your .env file.")
#     st.stop()
# genai.configure(api_key=gemini_api_key)

# # --- Local project imports ---
# from my_agents import HealthWellnessPlannerAgent
# from context import UserSessionContext
# from hooks import CustomRunHooks
# from utils.streaming import print_streaming_output

# # --- Streamlit page config ---
# st.set_page_config(page_title="Health & Wellness Planner AI", page_icon="🏋️", layout="wide")
# st.title("👨‍⚕️ Health & Wellness Planner AI")

# # --- Session state initialization ---
# if "agent_runner_instance" not in st.session_state:
#     st.session_state["agent_runner_instance"] = None

# if "user_session_context" not in st.session_state:
#     st.session_state["user_session_context"] = UserSessionContext(
#         name="User",
#         uid=int(uuid.uuid4().int % 1e6),  # UID as int
#         goal={"type": "general wellness"},
#         diet_preferences=None,
#         workout_plan={},
#         meal_plan=None,
#         injury_notes="",
#         handoff_logs=[],
#         progress_logs=[]
#     )

# if "messages" not in st.session_state:
#     st.session_state.messages = []

# # --- Chat UI rendering (History) ---
# for message in st.session_state.messages:
#     with st.chat_message(message["role"]):
#         st.markdown(message["content"])

# # --- Input: User message ---
# if prompt := st.chat_input("Ask your health question..."):
#     st.session_state.messages.append({"role": "user", "content": prompt})
#     with st.chat_message("user"):
#         st.markdown(prompt)

#     try:
#         if st.session_state["agent_runner_instance"] is None:
#             st.session_state["agent_runner_instance"] = HealthWellnessPlannerAgent(
#                 user_session_context=st.session_state["user_session_context"]
#             )

#         # Streamed response
#         response_generator = st.session_state["agent_runner_instance"].run(prompt)

#         full_response = ""
#         with st.chat_message("assistant"):
#             message_placeholder = st.empty()
#             for chunk in response_generator:
#                 full_response += chunk
#                 message_placeholder.markdown(full_response + "▌")
#             message_placeholder.markdown(full_response)

#         st.session_state.messages.append({"role": "assistant", "content": full_response})

#     except Exception as e:
#         st.error(f"An error occurred: {e}")
#         st.session_state.messages.append({"role": "assistant", "content": f"Error: {e}"})

#mre
# import streamlit as st
# import asyncio
# import uuid
# import sys
# import os
# from dotenv import load_dotenv
# import google.generativeai as genai

# # --- Adjust path to enable local imports ---
# current_script_dir = os.path.dirname(os.path.abspath(__file__))
# sys.path.insert(0, current_script_dir)

# # --- Load .env and configure Gemini ---
# load_dotenv()
# gemini_api_key = os.getenv("GOOGLE_API_KEY")
# if not gemini_api_key:
#     st.error("🔒 Google API Key not found. Please set `GOOGLE_API_KEY` in your .env file.")
#     st.stop()
# genai.configure(api_key=gemini_api_key)

# # --- Local project imports ---
# from my_agents import HealthWellnessPlannerAgent
# from context import UserSessionContext
# from hooks import CustomRunHooks
# from utils.streaming import print_streaming_output

# # --- Page config ---
# st.set_page_config(page_title="Health & Wellness Planner AI", page_icon="🏋️", layout="wide")

# # --- Sidebar ---
# with st.sidebar:
#     st.markdown("## 🧭 Instructions")
#     st.info("💬 Type your health or fitness goal.\n\n📅 Get custom meal/workout plans.\n\n🤖 AI replies in real-time!")
#     st.markdown("---")
#     st.caption("Built with ❤️ using OpenAI Agents SDK + Gemini")

# # --- Title ---
# st.title("👨‍⚕️ Health & Wellness Planner")
# st.markdown("Welcome! I'm your virtual wellness assistant. Let’s plan a healthier you. 💪")

# # --- Session state ---
# if "agent_runner_instance" not in st.session_state:
#     st.session_state["agent_runner_instance"] = None

# if "user_session_context" not in st.session_state:
#     st.session_state["user_session_context"] = UserSessionContext(
#         name="User",
#         uid=int(uuid.uuid4().int % 1e6),
#         goal={"type": "general wellness"},
#         diet_preferences=None,
#         workout_plan={},
#         meal_plan=None,
#         injury_notes="",
#         handoff_logs=[],
#         progress_logs=[]
#     )

# if "messages" not in st.session_state:
#     st.session_state.messages = []

# # --- Display chat history ---
# for message in st.session_state.messages:
#     with st.chat_message(message["role"]):
#         st.markdown(f"**{message['role'].capitalize()}:**\n\n{message['content']}")

# # --- Input box ---
# if prompt := st.chat_input("Type your health or fitness question..."):
#     st.session_state.messages.append({"role": "user", "content": prompt})
#     with st.chat_message("user"):
#         st.markdown(f"**You:** {prompt}")

#     try:
#         if st.session_state["agent_runner_instance"] is None:
#             st.session_state["agent_runner_instance"] = HealthWellnessPlannerAgent(
#                 user_session_context=st.session_state["user_session_context"]
#             )

#         response_generator = st.session_state["agent_runner_instance"].run(prompt)

#         full_response = ""
#         with st.chat_message("assistant"):
#             message_placeholder = st.empty()
#             for chunk in response_generator:
#                 full_response += chunk
#                 message_placeholder.markdown(f"**Assistant is typing...**\n\n{full_response}▌")
#             message_placeholder.markdown(f"**Assistant:**\n\n{full_response}")

#         st.session_state.messages.append({"role": "assistant", "content": full_response})

#     except Exception as e:
#         st.error(f"🚨 An error occurred: {e}")
#         st.session_state.messages.append({"role": "assistant", "content": f"Error: {e}"})

# check
# import streamlit as st
# import asyncio
# import uuid
# import sys
# import os
# from dotenv import load_dotenv
# import google.generativeai as genai

# # --- Adjust path to enable local imports ---
# current_script_dir = os.path.dirname(os.path.abspath(__file__))
# sys.path.insert(0, current_script_dir)

# # --- Load .env and configure Gemini ---
# load_dotenv()
# gemini_api_key = os.getenv("GOOGLE_API_KEY")
# if not gemini_api_key:
#     st.error("🔒 Google API Key not found. Please set `GOOGLE_API_KEY` in your .env file.")
#     st.stop()
# genai.configure(api_key=gemini_api_key)

# # --- Local project imports ---
# from my_agents import HealthWellnessPlannerAgent
# from context import UserSessionContext
# from hooks import CustomRunHooks
# from utils.streaming import print_streaming_output

# # --- Page config ---
# st.set_page_config(page_title="Health & Wellness Planner AI", page_icon="🏋️", layout="wide")

# # --- Sidebar ---
# with st.sidebar:
#     st.markdown("## 🧭 Instructions")
#     st.info("💬 Type your health or fitness goal.\n\n📅 Get custom meal/workout plans.\n\n🤖 AI replies in real-time!")
#     st.markdown("---")
#     st.caption("Built with ❤️ using OpenAI Agents SDK + Gemini")

# # --- Title ---
# st.title("👨‍⚕️ Health & Wellness Planner")
# st.markdown("Welcome! I'm your virtual wellness assistant. Let’s plan a healthier you. 💪")

# # --- Session state ---
# if "agent_runner_instance" not in st.session_state:
#     st.session_state["agent_runner_instance"] = None

# if "user_session_context" not in st.session_state:
#     st.session_state["user_session_context"] = UserSessionContext(
#         name="User",
#         uid=int(uuid.uuid4().int % 1e6),
#         goal={"type": "general wellness"},
#         diet_preferences=None,
#         workout_plan={},
#         meal_plan=None,
#         injury_notes="",
#         handoff_logs=[],
#         progress_logs=[]
#     )

# if "messages" not in st.session_state:
#     st.session_state.messages = []

# # --- Display chat history ---
# for message in st.session_state.messages:
#     with st.chat_message(message["role"]):
#         st.markdown(f"**{message['role'].capitalize()}:**\n\n{message['content']}")

# # --- Input box ---
# if prompt := st.chat_input("Type your health or fitness question..."):
#     st.session_state.messages.append({"role": "user", "content": prompt})
#     with st.chat_message("user"):
#         st.markdown(f"**You:** {prompt}")

#     try:
#         async def process_response():
#             if st.session_state["agent_runner_instance"] is None:
#                 st.session_state["agent_runner_instance"] = HealthWellnessPlannerAgent(
#                     user_session_context=st.session_state["user_session_context"]
#                 )

#             full_response = ""
#             with st.chat_message("assistant"):
#                 message_placeholder = st.empty()
#                 response_generator = await st.session_state["agent_runner_instance"].run(prompt)
#                 async for step in response_generator:
#                     chunk = step.pretty_output
#                     full_response += chunk
#                     message_placeholder.markdown(f"**Assistant is typing...**\n\n{full_response}▌")
#                 message_placeholder.markdown(f"**Assistant:**\n\n{full_response}")

#             st.session_state.messages.append({"role": "assistant", "content": full_response})

#         asyncio.run(process_response())

#     except Exception as e:
#         st.error(f"🚨 An error occurred: {e}")
#         st.session_state.messages.append({"role": "assistant", "content": f"Error: {e}"})


# check2
# import streamlit as st
# import asyncio
# import uuid
# import sys
# import os
# from dotenv import load_dotenv
# import google.generativeai as genai

# # --- Adjust path for imports ---
# current_script_dir = os.path.dirname(os.path.abspath(__file__))
# sys.path.insert(0, current_script_dir)

# # --- Load environment ---
# load_dotenv()
# gemini_api_key = os.getenv("GOOGLE_API_KEY")
# if not gemini_api_key:
#     st.error("🔒 Google API Key not found. Please set `GOOGLE_API_KEY` in your .env file.")
#     st.stop()
# genai.configure(api_key=gemini_api_key)

# # --- Imports ---
# from my_agents import HealthWellnessPlannerAgent
# from context import UserSessionContext

# # --- Streamlit setup ---
# st.set_page_config(page_title="Health & Wellness Planner AI", page_icon="🏋️", layout="wide")

# with st.sidebar:
#     st.markdown("## 🧭 Instructions")
#     st.info("💬 Type your health or fitness goal.\n📅 Get personalized plans.\n🤖 Real-time AI chat.")
#     st.markdown("---")
#     st.caption("Built with ❤️ using OpenAI Agents SDK + Gemini")

# st.title("👨‍⚕️ Health & Wellness Planner")
# st.markdown("Welcome! I'm your AI wellness assistant. Let’s plan a healthier you. 💪")

# # --- Session states ---
# if "agent_runner_instance" not in st.session_state:
#     st.session_state["agent_runner_instance"] = None

# if "user_session_context" not in st.session_state:
#     st.session_state["user_session_context"] = UserSessionContext(
#         name="User",
#         uid=int(uuid.uuid4().int % 1e6),
#         goal={"type": "general wellness"},
#         diet_preferences=None,
#         workout_plan={},
#         meal_plan=None,
#         injury_notes="",
#         handoff_logs=[],
#         progress_logs=[]
#     )

# if "messages" not in st.session_state:
#     st.session_state.messages = []

# # --- Display chat history ---
# for message in st.session_state.messages:
#     with st.chat_message(message["role"]):
#         st.markdown(f"**{message['role'].capitalize()}:**\n\n{message['content']}")

# # --- Async handler ---
# async def handle_input():
#     if prompt := st.chat_input("Type your health or fitness question..."):
#         st.session_state.messages.append({"role": "user", "content": prompt})
#         with st.chat_message("user"):
#             st.markdown(f"**You:** {prompt}")

#         try:
#             if st.session_state["agent_runner_instance"] is None:
#                 st.session_state["agent_runner_instance"] = HealthWellnessPlannerAgent(
#                     user_session_context=st.session_state["user_session_context"]
#                 )

#             full_response = ""
#             with st.chat_message("assistant"):
#                 msg_placeholder = st.empty()

#                 # ✅ Properly stream output
#                 async for chunk in st.session_state["agent_runner_instance"].run(prompt):
#                     full_response += chunk
#                     msg_placeholder.markdown(f"**Assistant is typing...**\n\n{full_response}▌")

#                 msg_placeholder.markdown(f"**Assistant:**\n\n{full_response}")

#             st.session_state.messages.append({"role": "assistant", "content": full_response})

#         except Exception as e:
#             st.error(f"🚨 An error occurred: {e}")
#             st.session_state.messages.append({"role": "assistant", "content": f"Error: {e}"})

# # --- Run async logic ---
# asyncio.run(handle_input())


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