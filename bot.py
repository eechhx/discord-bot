import os
import discord
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv('.env')


client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print("Bot is alive")

client.run(os.getenv('TOKEN'))