import discord
from discord.ext import commands

import os

import json #bNet API
import urllib.request

WOW_API_TOKEN = open(os.path.join(os.path.dirname(__file__), "../tokens/bNetAPI")).read()

class WoW:
    """Custom WoW Cog with basic commands"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def wow(self):
        #Your code will go here
        await self.bot.say("WOW!")

    @commands.command()
    async def affixes(self):
        await self.bot.say(WOW_API_TOKEN)
        # Prints current affixes
        url = urllib.request.urlopen("https://eu.api.battle.net/data/wow/mythic-challenge-mode/?namespace=dynamic-eu&locale=en_GB&access_token=" + WOW_API_TOKEN)
        keystoneData = json.loads(url.read().decode())
        await self.bot.say(keystoneData)


def setup(bot):
    bot.add_cog(WoW(bot))