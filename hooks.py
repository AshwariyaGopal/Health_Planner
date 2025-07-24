from typing import Optional
from context import UserSessionContext

class LifecycleHooks:
    """Class to handle lifecycle hooks for logging."""
    
    @staticmethod
    def on_agent_start(context: UserSessionContext, agent_name: str):
        """
        Logs when an agent starts.

        Args:
            context: User session context.
            agent_name: Name of the agent.
        """
        context.handoff_logs.append(f"Agent {agent_name} started at {context.uid}")

    @staticmethod
    def on_agent_end(context: UserSessionContext, agent_name: str):
        """
        Logs when an agent ends.

        Args:
            context: User session context.
            agent_name: Name of the agent.
        """
        context.handoff_logs.append(f"Agent {agent_name} ended at {context.uid}")

    @staticmethod
    def on_tool_start(context: UserSessionContext, tool_name: str):
        """
        Logs when a tool starts.

        Args:
            context: User session context.
            tool_name: Name of the tool.
        """
        context.handoff_logs.append(f"Tool {tool_name} started at {context.uid}")

    @staticmethod
    def on_tool_end(context: UserSessionContext, tool_name: str):
        """
        Logs when a tool ends.

        Args:
            context: User session context.
            tool_name: Name of the tool.
        """
        context.handoff_logs.append(f"Tool {tool_name} ended at {context.uid}")

    @staticmethod
    def on_handoff(context: UserSessionContext, from_agent: str, to_agent: str):
        """
        Logs when a handoff occurs.

        Args:
            context: User session context.
            from_agent: Source agent name.
            to_agent: Target agent name.
        """
        context.handoff_logs.append(f"Handoff from {from_agent} to {to_agent} at {context.uid}")