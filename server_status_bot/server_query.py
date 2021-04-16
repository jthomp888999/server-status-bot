import os
import asyncio
import a2s

async def get_info(address):
    data = await a2s.ainfo(address)
    return dict(data)

        



