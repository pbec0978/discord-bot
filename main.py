import os, time, asyncio, json, discord
from discord.ext import commands

#config
TOKEN = "INPUT_HERE" #Your Bot Token
WELCOME_CHANNEL = "INPUT_HERE" #Id of the channel for welcome message
LEAVE_CHANNEL = "INPUT_HERE" #Id of channel for leave messages

#prefix-settings
bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

#online-statement
@bot.event
async def on_ready():
    print("Bot is now Online")

#bot-command-test
@bot.command()
async def test(ctx):
  await ctx.send(":wave:")

#welcome-message
@bot.event
async def on_member_join(member):
    channel=bot.get_channel(WELCOME_CHANNEL)
    embed=discord.Embed(title=":wave: Welcome!", description=f"Hello {member.mention}, thanks for joining!", color=0xe83223)
    embed.add_field(name="We are so glad you made it!", value=f"We have approached {len(set(bot.users))} members now!!!")
    embed.set_image(url="https://cdn.discordapp.com/attachments/883805723807588423/901580387950686259/zerotwo_ist_scheie.gif")
    await channel.send(embed=embed)

#leave-message
@bot.event
async def on_member_remove(member):
    channel=bot.get_channel(LEAVE_CHANNEL)
    embed=discord.Embed(title=":wave: Bye!", description=f"{member.mention} just left :(", color=0xe83223)
    embed.add_field(name="Why would someone leave?", value=f"We are now {len(set(bot.users))} members...")
    embed.set_image(url="https://cdn.discordapp.com/attachments/883805723807588423/901580387950686259/zerotwo_ist_scheie.gif")
    await channel.send(embed=embed)

bot.run(TOKEN)
