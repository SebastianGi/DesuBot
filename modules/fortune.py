import random
import discord
import datetime
import json
from discord.ext import commands


class fortune():
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True, aliases=['omikuji'])
    async def fortune(self, ctx):
        """Visit a shrine and recieve your fortune."""
        #Check if in DM
        if ctx.message.channel.is_private:
            await self.bot.say("Unfortunately i cannot execute this command in Private Messages")
        else:
            #Variables
            try:
                with open('userconfig.json') as json_data:
                    userconfig = json.load(json_data)
            except Exception:
                    fortunemessage = await self.bot.say("OOPSIE WOOPSIE!! uwu We made a fucky wucky!! A wittle fucko boingo! The code monkeys at our headquarters are working VEWY HAWD to fix this!")
            userboy = ctx.message.author
            shrines = ["Hakurei Shrine","Yatasai Shrine", "Tainaka Shrine"]
            shrinechoicelist = ['1⃣','2⃣','3⃣']
            drawerchoicexlist = ['1⃣','2⃣','3⃣','4⃣','5⃣']
            drawerchoiceylist = ['🇦','🇧','🇨']
            drawerchoiceylistraw = ['A','B','C']
            fortunetable = [["大吉","Great blessing",0,5],["中吉","Middle blessing",0,6],["小吉","Small blessing",0,7],["吉","Blessing",0,8],["半吉","Half-blessing",0,9],["末吉","future blessing",0,9],["末小吉","future small blessing",0,11],["凶","curse",1,11],["小凶","small curse",2,11],["半凶","half-curse",3,11],["末凶","future curse",4,11],["大凶","great curse",5,11]]
            themetable = [["願事","one's wish or desire"],["待人","a person being waited for"],["失せ物","lost article"],["旅立ち","travel"],["商い","business dealings"],["学問","studies or learning"],["相場","market speculation"],["争事","disputes"],["恋愛","romantic relationships"],["転居","moving or changing residence"],["出産","childbirth, delivery"],["病気","illness"],["縁談","marriage proposal or engagement"]]
            endchoice = ['🌳','📧']
            shrinelistformatgen = ""
            vip = userboy.id in userconfig['vips']
            shrinechoice = None
            drawerchoicex = None
            drawerchoicey = None
            generalfortune = None
            grid = "```+----+----+----+----+----+\n| A1 | A2 | A3 | A4 | A5 |\n+------------------------+\n| B1 | B2 | B3 | B4 | B5 |\n+------------------------+\n| C1 | C2 | C3 | C4 | C5 |\n+----+----+----+----+----+```"
            
            #Set embed for shrine choice
            embed = discord.Embed(colour=discord.Colour(0x663399))
            embed.set_author(name="Fortune for " + userboy.name, icon_url=userboy.avatar_url)
            if vip:
                embed.description = "Hey, which shrine shall we visit today? des~"
            else:
                embed.description = "Please choose a Shrine"
            for i in shrines:
                shrinelistformatgen = shrinelistformatgen + str(shrines.index(i) + 1) + ". " + i + "\n"
            embed.add_field(name="Shrines:", value=shrinelistformatgen)
            
            #Send shrine choice and handle reply
            fortunemessage = await self.bot.say(embed=embed)
            for i in shrinechoicelist:
                await self.bot.add_reaction(fortunemessage, i)
            tempchoice = await self.bot.wait_for_reaction(shrinechoicelist, message=fortunemessage, user=userboy, timeout=30)
            if tempchoice is None:
                raise Exception('No User input in 30 Seconds')
            for index, item in enumerate(shrinechoicelist):
                if tempchoice.reaction.emoji == item:
                    shrinechoice = index
            seedboy = userboy.id + str(shrinechoice)
            await self.bot.clear_reactions(fortunemessage)
            
            #Set new embed
            if vip:
                embed.description = "We arrived at " + shrines[shrinechoice] + ", " + userboy.name + "! des~"
            else:
                embed.description = "You arrive at your Destination, " + shrines[shrinechoice]
            embed.remove_field(0)
            embed.add_field(name="Please choose the drawer you'd like to take your fortune from.", value= grid)
            embed.set_footer(text="First pick a row, then pick a column")
            
            #Send drawer choice
            await self.bot.edit_message(fortunemessage, embed=embed)
            #Handle reply for axis Y
            for i in drawerchoiceylist:
                await self.bot.add_reaction(fortunemessage, i)
            tempchoice = await self.bot.wait_for_reaction(drawerchoiceylist, message=fortunemessage, user=userboy, timeout=30)
            if tempchoice is None:
                raise Exception('No User input in 30 Seconds')
            for index, item in enumerate(drawerchoiceylist):
                if tempchoice.reaction.emoji == item:
                    drawerchoicey = index
            seedboy = seedboy + str(drawerchoicey)
            await self.bot.clear_reactions(fortunemessage)
            
            #Handle reply for axis X
            for i in drawerchoicexlist:
                await self.bot.add_reaction(fortunemessage, i)
            tempchoice = await self.bot.wait_for_reaction(drawerchoicexlist, message=fortunemessage, user=userboy, timeout=30)
            if tempchoice is None:
                raise Exception('No User input in 30 Seconds')
            for index, item in enumerate(drawerchoicexlist):
                if tempchoice.reaction.emoji == item:
                    drawerchoicex = index
            seedboy = seedboy + str(drawerchoicex)
            await self.bot.clear_reactions(fortunemessage)
            
            #Generate fortune
            random.seed(seedboy + "general" + str(datetime.datetime))
            generalfortune = random.randint(0, 11)
            embed.description = "You have picked drawer " + drawerchoiceylistraw[drawerchoicey] + str(drawerchoicex + 1) + " from " + shrines[shrinechoice]
            embed.remove_field(0)
            embed.add_field(name="Your fortune:", value=fortunetable[generalfortune][0] + " *" + fortunetable[generalfortune][1] + "*\n ")
            chosenthemes = random.sample(themetable, random.randint(4,6))
            random.shuffle(chosenthemes)
            for i in chosenthemes:
                random.seed(seedboy + i[1] + str(datetime.datetime))
                tempfortune = random.randint(fortunetable[generalfortune][2],fortunetable[generalfortune][3])
                embed.add_field(name=i[0] + " *" + i[1] + "*", value=fortunetable[tempfortune][0] + " *" + fortunetable[tempfortune][1] + "*\n ", inline=False)
            embed.set_footer(text="React 🌳 to leave the fortune at the shrine or react 📧 to get it sent to your DMs for you to keep")
            
            #Post fortune and give choice to keep or leave
            await self.bot.edit_message(fortunemessage, embed=embed)
            for i in endchoice:
                await self.bot.add_reaction(fortunemessage, i)
            
            #DM or remove fortune
            tempchoice = await self.bot.wait_for_reaction(endchoice, message=fortunemessage, user=userboy, timeout=45)
            await self.bot.clear_reactions(fortunemessage)
            if tempchoice.reaction.emoji == "🌳":
                embed.clear_fields()
                embed.set_footer()
                embed.description = "You tied your fortune to a branch of the tree at the shrine, leaving it behind."
                await self.bot.edit_message(fortunemessage, embed=embed)
            if tempchoice.reaction.emoji == "📧":
                await self.bot.send_message(userboy, embed=embed)
                embed.clear_fields()
                embed.set_footer()
                embed.description = "Fortune has been sent as a direct meesage."
                await self.bot.edit_message(fortunemessage, embed=embed)


def setup(bot):
    bot.add_cog(fortune(bot))