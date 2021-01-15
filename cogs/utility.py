import discord
import random
from discord.ext import commands

class utility(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Events
    @commands.Cog.listener()
    async def on_ready(self):
        print("Bot is alive")
    
    # Commands
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'{round(client.latency * 1000)}ms')
    
    @commands.command()
    async def clear(self, ctx, amount = 10):
        await ctx.channel.purge(limit = amount)
    
    @commands.command(aliases = ['8ball', 'eightball'])
    async def _8ball(self, ctx, *, question):
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

def setup(client):
    client.add_cog(utility(client))
