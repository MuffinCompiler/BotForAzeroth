import discord
from discord.ext import commands

import os

import json #bNet API
import urllib.request

WOW_API_TOKEN = open(os.path.join(os.path.dirname(__file__), "../tokens/bNetAPI")).read()
affix_descs = json.load(open(os.path.join(os.path.dirname(__file__), "wowData/affixDescriptions.json")))

class WoW:
    """Custom WoW Cog with basic commands"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def github(self):
        """Link zum Github Repo"""
        await self.bot.say("Hier gehts zum Repo: https://github.com/MuffinCompiler/BotForAzeroth")

    @commands.command()
    async def logs(self):
        """Link zu den Bot Logs"""
        await self.bot.say("Debug-Logs: http://muffincompiler.de/bfalog.php\nDebug-Logs-Dev: http://muffincompiler.de/bfalog_dev.php")

    async def affix_en(self):
        url = urllib.request.urlopen("https://eu.api.battle.net/data/wow/mythic-challenge-mode/?namespace=dynamic-eu&locale=en_GB&access_token=" + WOW_API_TOKEN)
        keystoneData = json.loads(url.read().decode())
        await self.bot.say("This weeks affixes:")
        for keystone in keystoneData["current_keystone_affixes"]:
            await self.bot.say("Level " + str(keystone['starting_level']) + ": " + keystone['keystone_affix']['name'] + "\n" + affix_descs['affix_descriptions'][keystone['keystone_affix']['id'] - 1]['d_EN'])

    @commands.command()
    async def affixes(self):
        """Prints current M+ affixes"""
        self.affix_en()
    
    @commands.command()
    async def affix(self):
        self.affix_en()

    @commands.command()
    async def affixesDE(self):
        """Gibt aktuelle M+ Affixes aus"""
        url = urllib.request.urlopen("https://eu.api.battle.net/data/wow/mythic-challenge-mode/?namespace=dynamic-eu&locale=de_DE&access_token=" + WOW_API_TOKEN)
        keystoneData = json.loads(url.read().decode())
        await self.bot.say("Affixe diese Woche:")
        for keystone in keystoneData["current_keystone_affixes"]:
            await self.bot.say("Level " + str(keystone['starting_level']) + ": " + keystone['keystone_affix']['name'] + "\n" + affix_descs['affix_descriptions'][keystone['keystone_affix']['id'] - 1]['d_DE'])

    @commands.command()
    async def token(self):
        """Aktueller Token-Preis"""
        url = urllib.request.urlopen("https://eu.api.battle.net/data/wow/token/?namespace=dynamic-eu&locale=en_GB&access_token=" + WOW_API_TOKEN)
        tokenData = json.loads(url.read().decode())
        goldTokenPrice = int(tokenData['price'] / 10000)
        strTokenPrice = "{:,}".format(goldTokenPrice).replace(",",".")
        await self.bot.say("Aktueller Token-Preis: " + strTokenPrice + "g")

    @commands.command()
    async def reset(self):
        """Wann ist wöchentlicher Reset?"""
        resetHr = 7 # reset at 7am UTC
        import time
        if time.localtime().tm_isdst:
            resetDiff = 2
        else:
            resetDiff = 1
        await self.bot.say("Wöchentlicher Reset: Mittwoch " + str(resetHr + resetDiff) + " Uhr (GMT+" + str(resetDiff) + ")");

    @commands.command()
    async def lw(self):
        """Mir is langweilig..."""
        await self.bot.say("Laaangweilig... http://muffincompiler.de/media/dalaran.gif")

def setup(bot):
    bot.add_cog(WoW(bot))