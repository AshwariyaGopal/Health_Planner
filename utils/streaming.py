import asyncio
from typing import AsyncGenerator

async def stream_response(responses: dict | str) -> AsyncGenerator[str, None]:
    if isinstance(responses, dict):
        yield str(responses)
    elif isinstance(responses, str):
        yield f"{{'status': 'success', 'message': '{responses}'}}"
    await asyncio.sleep(0.1)