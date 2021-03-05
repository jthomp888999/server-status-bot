import os
import aiohttp
import asyncio

from dotenv import load_dotenv

load_dotenv()
URL = "https://api.battlemetrics.com/servers/9333822"
TOKEN = os.getenv("BATTLE_METRICS_TOKEN")

headers={"Authorization": "Bearer" + TOKEN}
async def get_info():
    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get(URL) as resp:
            response = await resp.json()
            return response