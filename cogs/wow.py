import discord
from discord.ext import commands

class WoW:
    """Custom WoW Cog with basic commands"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def wow(self):
        #Your code will go here
        await self.bot.say("I can do stuff!")

def setup(bot):
    bot.add_cog(WoW(bot))