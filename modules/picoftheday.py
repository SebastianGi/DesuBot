import discord
import random
import datetime
import json
from discord.ext import commands
from desubot import userconfig


class picoftheday():
    def __init__(self, bot):
        self.bot = bot

    @commands.command(description='ToDo.', aliases=['potd'])
    async def picoftheday(self):
        """Shows a random picture of the day from a Database filled with very nice pictures"""
        random.seed("picoftheday" + str(datetime.date.today()) + "1")
        imageint = random.randrange(1,81)
        embed = discord.Embed(title="Image of the day " + str(datetime.date.today()), colour=discord.Colour(0x575b83))
        embed.set_image(url="http://sebg.moe/potd/" + str(imageint) + ".jpg")
        await self.bot.say(embed=embed)


def setup(bot):
    bot.add_cog(picoftheday(bot))