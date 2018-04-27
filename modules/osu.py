import discord
import random
import requests
import json
import urllib.parse
from tinydb import TinyDB, Query
from discord.ext import commands
from desubot import userconfig
from desubot import userdb

osutable = userdb.table('osu')

class osu():
    def __init__(self, bot):
        self.bot = bot

    # first argument after -osu (-osu xyz) decides which subcommand will be run
    # no argument (-osu): display this help
    # -osu set [osu username]: ties an osu! username to your discord user
    # -osu user [osu username(optional)]: displays data for a specific osu user
    # -osu maps [osu beatmap/beatmapset url/id]: displays data for a specific beatmap
    # -osu alert: enables alerts for the username tied to your discord user

    @commands.command(pass_context=True)
    async def osu(self, ctx, switchboye: str = None, argboyone: str = None, argboyetwo: str = None):
        userboy = ctx.message.author
        if switchboye == None:
            await self.bot.say('soon™')
        # SET
        elif switchboye == "set":
            if argboyone is None:
                await self.bot.say('You forgot to add your osu! User')
            else:
                userquery = Query()
                if osutable.count(userquery.discord_uid == userboy.id) == 0:
                    try:
                        temp = osuapirequest('get_user?k=' + userconfig['keys']['osuapi'] + '&u=' + argboyone)
                        osutable.insert({'discord_uid': userboy.id, 'osu_uid': argboyone})
                        await self.bot.say('osu! user **' + temp['username'] + '** has been tied to your Discord user')
                    except IndexError:
                        await self.bot.say(argboyone + " doesn't seem to be a valid osu! user")
                else:
                    temp = osutable.get(userquery.discord_uid == userboy.id)
                    await self.bot.say("osu! user **" + temp.get('osu_uid') + '** is currently tied to your account, use "-osu unset" to remove')
        # UNSET
        elif switchboye == "unset":
            userquery = Query()
            if osutable.count(userquery.discord_uid == userboy.id) == 1:
                osutable.remove(userquery.discord_uid == userboy.id)
                await self.bot.say('osu! user tied to your discord user has been removed')
            else:
                await self.bot.say("No osu! user currently tied to your account")
# _TODO_       # USER
        elif switchboye == "user":
            if argboyone is None:
                await self.bot.say('You forgot to add your osu! User')
            else:
                try:
                    temp = osuapirequest('get_user?k=' + userconfig['keys']['osuapi'] + '&u=' + argboyone)
                    embed = discord.Embed(colour=discord.Colour(0xff66aa))
                    embed.set_author(name="osu! user " + temp['username'])
                    embed.set_thumbnail(url='https://a.ppy.sh/' + temp['user_id'])
                    embed.add_field(name="rank", value=temp['pp_rank'], inline=True)
                    embed.add_field(name="pp", value=temp['pp_raw'], inline=True)
                    await self.bot.say(embed=embed)
                except IndexError:
                    await self.bot.say(argboyone + " doesn't seem to be a valid osu! user")
            
        # MAPS
        elif switchboye == "maps":
            await self.bot.say('maps: soon™')
        # ALERT
        elif switchboye == "alert":
            await self.bot.say('alert: soon™')
        # EXCEPTION
        else:
            await self.bot.say('Unknown argument ' + switchboye)

    @commands.command(description='ToDo.')
    async def temp(self):
        await self.bot.say('ToDo')

def osuapirequest(requeststring):
    temp = requests.get('https://osu.ppy.sh/api/' + requeststring)
    temp = temp.json()
    temp = temp[0]
    return temp

def setup(bot):
    bot.add_cog(osu(bot))