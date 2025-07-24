import streamlit as st
import asyncio
from my_agents import HealthWellnessAgent
from context import UserSessionContext
from pydantic import BaseModel
import uuid
from dotenv import load_dotenv
import os
import ast

# Load environment variables
load_dotenv()

# Streamlit page configuration
st.set_page_config(page_title="Health & Wellness Planner", layout="wide")

def main():
    """Main function to run the Streamlit app."""
    st.title("Health & Wellness Planner")
    st.markdown("Your AI-powered assistant for fitness and dietary goals!")

    # Initialize session state for user context
    if "user_context" not in st.session_state:
        st.session_state.user_context = UserSessionContext(
            name="User",
            uid=uuid.uuid4().int & (1<<31)-1,
            handoff_logs=[],
            progress_logs=[]
        )

    # Initialize the main agent with a fresh context per run
    agent = HealthWellnessAgent(st.session_state.user_context)

    # User input
    user_input = st.text_input("Tell me about your health goals or needs:", key="user_input")
    
    if st.button("Submit"):
        if user_input:
            with st.spinner("Processing your request..."):
                # Reset context goal before processing
                st.session_state.user_context.goal = None
                # Run the agent asynchronously and stream responses
                async def stream_response():
                    st.subheader("Response")
                    status_placeholder = st.empty()
                    message_placeholder = st.empty()
                    full_response = {}
                    async for response in agent.process_input(user_input):
                        print(f"Received response: {response}")  # Debug print
                        try:
                            # Safely evaluate the string to a dictionary
                            response_dict = ast.literal_eval(response)
                            full_response.update(response_dict)
                            status = full_response.get("status", "unknown")
                            message = full_response.get("message", "No message available")
                            status_placeholder.text(f"Status: {status}")
                            message_placeholder.text(f"Message: {message}")
                        except (ValueError, SyntaxError):
                            status_placeholder.text("Status: error")
                            message_placeholder.text(f"Message: Invalid response format: {response}")
                asyncio.run(stream_response())
        else:
            st.error("Please enter a valid input.")

if __name__ == "__main__":
    main()