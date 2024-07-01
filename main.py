import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

bot.run('MTIzODMwOTc4MDE3OTc4MzcxMQ.GyEyNm.exa7ylq12StPXv57HUHVtqn5qpPufc4JOkNmqs')  # Reemplaza 'TOKEN_DEL_BOT' con tu token real del bot
