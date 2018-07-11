import random
import discord
from datetime import date
from discord.ext import commands
from time import sleep


class comfy():
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True, aliases=['comf', 'comfy'])
    async def howcomf(self, ctx, userboy: discord.User=None):
        """Shows your comfyness for the following day."""
        if userboy is None:
            userboy = ctx.message.author
        tomdate = date.today()
        userseed = userboy.id + str(tomdate)
        random.seed(userseed)
        comfyness = (random.randrange(0, 1000, 1)) / 10
        output_bar = '['
        for _i in range (round(comfyness * 0.2)):
            output_bar = output_bar + '█'
        for _i in range (20 - round(comfyness * 0.2)):
            output_bar = output_bar + '░'
        output_bar = output_bar + ']'
        outputboy = output_bar + ' ' + str(comfyness) + '%'

        embed = discord.Embed(colour=discord.Colour(0x663399))
        embed.set_author(name="Comfiness Prediction for " + userboy.name, icon_url=userboy.avatar_url)
        embed.add_field(name="Your predicted comfiness for tomorrow is:", value=outputboy)
        await self.bot.say(embed=embed)


def setup(bot):
    bot.add_cog(comfy(bot))
