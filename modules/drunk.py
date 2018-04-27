import discord
import random
import json
from tinydb import TinyDB, Query
from discord.ext import commands
from desubot import userconfig


class drunk():
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True, description='Calculate how drunk you are', aliases=['sipp'])
    async def drunk(self, ctx , drinkboye: str = None, amountboye: str = None ):
        await self.bot.say('ToDo')


def setup(bot):
    bot.add_cog(drunk(bot))