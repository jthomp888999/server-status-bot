import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

from api_handler import get_info


# Change to False before pushing to mains
TESTING = True

load_dotenv()
if TESTING:
    # Change in .env file
    DISCORD_TOKEN = os.getenv("DISCORD_TOKEN_TESTING")
    TRIGGER = "test"
else:
    DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
    TRIGGER = "status"


intents = discord.Intents.default()

# Command prefix i.e. '!status'
bot = commands.Bot(command_prefix='!', intents=intents)

# Message on startup
@bot.event
async def on_ready():
    bot_name = bot.user.name
    bot_id = bot.user.id
    print(f"logged in as {bot_name}, {bot_id}")

# Send status when trigger word seen
@bot.command(name=TRIGGER)
async def send_status(ctx):
    result = await get_info()

    # Pull values from API response
    server_name = result["server_name"]
    server_time = result["server_time"]
    status = result["status"]
    players_online = int(result["players_online"])

    # Decide which sentence to use based on player count, for grammer
    if players_online == 0:
        message = "There are no players online"
    elif players_online == 1:
        message = f"There is {players_online} player online."
    elif players_online > 1:
        message = f"There are {players_online} players online"

    # Discord's embed, for making the output look presentable
    embed=discord.Embed(title=f"{server_name} Info")
    embed.add_field(name="Current Time:", value=f"{server_time}", inline=True)
    embed.add_field(name="Status:", value=f"{status}", inline=True)
    embed.set_footer(text=f"{message}")

    # Finally send the formatted data
    await ctx.send(embed=embed)


if __name__ == "__main__":
    bot.run(DISCORD_TOKEN)