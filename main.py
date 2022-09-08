import os, time, asyncio, json, discord
from discord.ext import commands

#prefix-settings
bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

#online-statement
@bot.event
async def on ready():
    print("Bot is now Online")
