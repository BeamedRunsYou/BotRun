import discord
from discord.ext import commands

# Intents are required for the bot to have access to certain events
intents = discord.Intents.default()
intents.messages = True

# Create a bot instance with the specified prefix and intents
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send('Hello!')

@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

# Replace 'YOUR_BOT_TOKEN' with your bot's token
bot.run('MTMyMTAzNDM2MTM5ODYyNDI2Nw.GGSY2s.5hOinDrqPVd289Mu7DmZEAax2aMXhF7CRZFDmE')
