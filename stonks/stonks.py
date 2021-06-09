
from redbot.core import commands
from discord.ext import commands

class Stonks:
    """My custom cog"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def stonks(self, ctx):
        """This does stuff!"""
        # Your code will go here
        await ctx.send("I can do stuff!")
        await self.bot.say('BRO!')
