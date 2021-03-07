import os
from datetime import datetime
import aiohttp
import asyncio

from dotenv import load_dotenv

load_dotenv()

# URL for server info with server ID attached (9333822)
# will make configurable later
URL = "https://api.battlemetrics.com/servers/9333822"
TOKEN = os.getenv("BATTLE_METRICS_TOKEN")
HEADERS={"Authorization": "Bearer" + TOKEN}

async def get_info():
    data = {}
    async with aiohttp.ClientSession(headers=HEADERS) as session:
        async with session.get(URL) as resp:
            response = await resp.json()

            # Pull values from API resoponse
            data["server_name"] = response["data"]["attributes"]["name"]
            data["status"] = response["data"]["attributes"]["status"]
            data["players_online"] = response["data"]["attributes"]["players"]

            # Convert time string from 'HH:MM 24hr' to 'H AM', leading zero stripped
            data["server_time"] = (
                datetime.strptime(response["data"]["attributes"]["details"]["time"], "%H:%M")
                .strftime("%I %p")
                .lstrip('0'))

            return data