import os
import discord
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv('.env')

client = commands.Bot(command_prefix = '-')

@client.command()
async def load(ctx, cog_extension):
    client.load_extension(f'cogs.{cog_extension}')
    await ctx.send(f'Cog {cog_extension} has been loaded')

@client.command()
async def unload(ctx, cog_extension):
    client.unload_extension(f'cogs.{cog_extension}')
    await ctx.send(f'Cog {cog_extension} has been unloaded')

@client.command()
async def reload(ctx, cog_extension):
    client.reload_extension(f'cogs.{cog_extension}')
    await ctx.send(f'Cogs {cog_extension} has been reloaded')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run(os.getenv('TOKEN'))