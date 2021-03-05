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
    await ctx.send(result)



bot.run(DISCORD_TOKEN)