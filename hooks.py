from agents import RunHooks, AgentHooks 
# from agents.tool_call import ToolCall, ToolResult  
from typing import Any
from context import UserSessionContext # Assuming context for logging

class CustomRunHooks(RunHooks):
    """
    Global run hooks to track activities across all agents and tools.
    """
    async def on_agent_start(self, agent_name: str, context: UserSessionContext):
        print(f"\n--- [RunHook] Agent '{agent_name}' started ---")
        context.state.handoff_logs.append(f"Agent '{agent_name}' started at {context.current_date}")

    async def on_agent_end(self, agent_name: str, context: UserSessionContext):
        print(f"--- [RunHook] Agent '{agent_name}' ended ---")
        context.state.handoff_logs.append(f"Agent '{agent_name}' ended at {context.current_date}")

    async def on_tool_start(self, tool_call: Any, context: UserSessionContext):
        print(f"--- [RunHook] Tool '{tool_call.tool_name}' started with args: {tool_call.args} ---")
        context.state.handoff_logs.append(f"Tool '{tool_call.tool_name}' started at {context.current_date}")

    async def on_tool_end(self, tool_call: Any, tool_result: Any, context: UserSessionContext):
        print(f"--- [RunHook] Tool '{tool_call.tool_name}' ended with result: {tool_result.content} ---")
        context.state.handoff_logs.append(f"Tool '{tool_call.tool_name}' ended at {context.current_date} with result: {tool_result.content[:50]}...") # Log first 50 chars of result


    async def on_handoff(self,
                         from_agent: str,
                         to_agent: str,
                         input_message: str,
                         context:UserSessionContext):
        log_message = f"\n--- [RunHook] Handoff from '{from_agent}' to '{to_agent}' with input: '{input_message}' ---"
        print(log_message)
        context.state.handoff_logs.append(log_message)


class CustomAgentHooks(AgentHooks):
    """
    Agent-specific hooks for more granular control, though RunHooks are often sufficient
    for global logging. This demonstrates their usage.
    """
    async def on_start(self, context: UserSessionContext):
        print(f"    [AgentHook] Agent '{context.current_agent_name}' is starting its turn.")

    async def on_end(self, context: UserSessionContext):
        print(f"    [AgentHook] Agent '{context.current_agent_name}' is ending its turn.")

    async def on_tool_start(self, tool_call: Any, context: UserSessionContext):
        print(f"        [AgentHook] Agent '{context.current_agent_name}' calling tool '{tool_call.tool_name}'.")

    async def on_tool_end(self, tool_call: Any, tool_result: Any, context: UserSessionContext):
        print(f"        [AgentHook] Agent '{context.current_agent_name}' tool '{tool_call.tool_name}' finished.")

    # Note: on_handoff is typically handled by RunHooks for global logging,
    # but could be implemented here for agent-specific handoff logic.
    # async def on_handoff(self, ...): pass