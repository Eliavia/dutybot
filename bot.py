#bot.py
print("Loading...\n")
import discord
from discord.ext import commands
TOKEN = ""
print("Connecting...\n")
intents = discord.Intents.default()
intents.members = True
client = commands.Bot(intents=intents,command_prefix=">")
print("Connected!")
@client.command()
async def onduty(ctx):
    role = discord.utils.get(ctx.message.guild.roles, id=943261286685347910)
    await ctx.message.author.add_roles(role)
    await ctx.send("Successfully marked you on duty!")
@client.command()
async def offduty(ctx):
    role = discord.utils.get(ctx.message.guild.roles, id=943261286685347910)
    await ctx.message.author.remove_roles(role)
    await ctx.send("Successfully marked you off duty!")
client.run(d4d4900b79d40c1d9290811c98f47923d2c562afba6e08caccbba5673dea351d)