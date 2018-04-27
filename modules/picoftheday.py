import discord
import random
import json
from discord.ext import commands
from desubot import userconfig


class picoftheday():
    def __init__(self, bot):
        self.bot = bot

    @commands.command(description='ToDo.')
    async def picoftheday(self):
        await self.bot.say('ToDo')


def setup(bot):
    bot.add_cog(picoftheday(bot))