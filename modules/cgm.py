import random
import discord
import requests
import json
import urllib.parse
from discord.ext import commands


class cgm():
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['cutegirl', 'cutegirls', 'moe'])
    async def cgm(self,* , source : str = None):
        """Get a random Picture from cutegirls.moe using the CuteGirls API."""
        try:
            if source == None:
                temp = requests.get('http://api.cutegirls.moe/json')
            else:
                temp = requests.get('http://api.cutegirls.moe/json?source=' + urllib.parse.quote_plus(source))
            imagedata = temp.json()
            embed = discord.Embed(colour=discord.Colour(0x663399), description="[Source]("+ imagedata['data']['link'] +")")
            embed.set_author(name=imagedata['data']['title'])
            embed.set_image(url=imagedata['data']['image'])
        except KeyError:
            await self.bot.say("It looks like i can't find anything when searching with the keyword " + source + "! \*dissapointed desu\*")
            return
        except Exception:
            await self.bot.say('Something went wrong!!! \*sad desu\*')
            return
        await self.bot.say(embed=embed)


def setup(bot):
    bot.add_cog(cgm(bot))