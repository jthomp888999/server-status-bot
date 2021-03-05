import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

from api_handler import get_info

load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    bot_name = bot.user.name
    bot_id = bot.user.id
    print(f"logged in as {bot_name}, {bot_id}")

@bot.command(name="status")
async def send_status(ctx):
    result = await get_info()

    server_name = result["server_name"]
    server_time = result["server_time"]
    status = result["status"]
    players_online = result["players_online"]

    embed=discord.Embed(title=f"{server_name} Info")
    embed.add_field(name="Current Time:", value=f"{server_time}", inline=True)
    embed.add_field(name="Satus:", value=f"{status}", inline=True)
    embed.set_footer(text=f"There are currently {players_online} players online.")
    await ctx.send(embed=embed)

bot.run(DISCORD_TOKEN)