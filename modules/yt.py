import random
from discord.ext import commands


class YT():
    def __init__(self, bot):
        self.bot = bot

    @commands.command(description='ToDo.')
    async def yt(self):
        await self.bot.say("ToDo")


def setup(bot):
    bot.add_cog(YT(bot))