import discord
from discord import commands
from discord.ext.commands import Bot
import asyncio



bot = commands.Bot(command_prefix="a.")



@bot.event()
async def on_ready():

bot.run(os.environ['BOT_TOKEN'])
