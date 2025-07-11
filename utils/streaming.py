# import asyncio

async def print_streaming_output(stream):
    """
    Asynchronously prints the output from the agent's stream.
    """
    async for step in stream:
        print(step.pretty_output)
        # You can also customize how each step is displayed
        # if step.type == "agent_response":
        #     print(f"AI: {step.content}")
        # elif step.type == "tool_code":
        #     print(f"Tool Call: {step.tool_name}({step.args})")
        # elif step.type == "tool_response":
        #     print(f"Tool Result: {step.content}")
        # else:
        #     print(step.pretty_output)