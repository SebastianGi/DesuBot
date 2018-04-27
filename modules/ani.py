import discord
import random
import json
from discord.ext import commands
from desubot import userconfig


class ani():
    def __init__(self, bot):
        self.bot = bot

    @commands.command(description='Grab an Anime from MyAnimeList.net')
    async def mal(self):
        await self.bot.say('ToDo')


def setup(bot):
    bot.add_cog(ani(bot))