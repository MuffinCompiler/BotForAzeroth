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

    def printAffixesFromJSON(self, data):

    @commands.command()
    async def affixes(self):
        # Prints current affixes
        url = urllib.request.urlopen("https://eu.api.battle.net/data/wow/mythic-challenge-mode/?namespace=dynamic-eu&locale=en_GB&access_token=" + WOW_API_TOKEN)
        keystoneData = json.loads(url.read().decode())
        await self.bot.say("This weeks affixes:")
        for keystone in keystoneData["current_keystone_affixes"]:
            await self.bot.say("Level " + str(keystone['starting_level']) + ": " + keystone['keystone_affix']['name'])


    @commands.command()
    async def affixesDE(self):
        # Prints current affixes
        url = urllib.request.urlopen("https://eu.api.battle.net/data/wow/mythic-challenge-mode/?namespace=dynamic-eu&locale=de_DE&access_token=" + WOW_API_TOKEN)
        keystoneData = json.loads(url.read().decode())
        await self.bot.say("Affixe diese Woche:")
        for keystone in keystoneData["current_keystone_affixes"]:
            await self.bot.say("Level " + str(keystone['starting_level']) + ": " + keystone['keystone_affix']['name'])

        


def setup(bot):
    bot.add_cog(WoW(bot))