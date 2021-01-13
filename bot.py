import os
import discord
import random
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv('.env')
client = commands.Bot(command_prefix = '-')

@client.event
async def on_ready():
    print("Bot is alive")

@client.event
async def on_member_join(member):
    print(f'{member} has joined the server!')

@client.event
async def on_member_remove(member):
    print(f'{member} has abandoned ship!')

@client.command()
async def clear(ctx, amount = 10):
    await ctx.channel.purge(limit = amount)

@client.command()
async def ping(ctx):
    await ctx.send(f'{round(client.latency * 1000)}ms')

@client.command(aliases = ['8ball', 'eightball'])
async def _8ball(ctx, *, question):
    responses = [
        'It is certain',
        'It is decidedly so',
        'Without a doubt',
        'Yes definitely',
        'You may rely on it',
        'As I see it, yes',
        'Most likely',
        'Outlook good',
        'Mos def',
        'Reply hazy try again',
        'Ask again later',
        'Better not tell you now',
        'Cannot predict now',
        'Concentrate',
        'Don\'t count on it',
        'My reply is no',
        'My sources say no',
        'Outlook not so good',
        'Very doubtful']
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

client.run(os.getenv('TOKEN'))