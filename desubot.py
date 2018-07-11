import discord
import json
from tinydb import TinyDB, Query
from discord.ext import commands


# Load config
try:
    with open('config.json') as json_data:
        userconfig = json.load(json_data)
except Exception:
    print("Exception while trying to read config.json!")

# Load database
try:
    userdb = TinyDB('userdb.json')
except Exception:
    print("Exception while trying to create or read database")

description = 'Well, what do we have here, desu~'
bot = commands.Bot(command_prefix=userconfig['prefix'], description=description)
client = discord.Client()
bot.remove_command('help')


@bot.event
async def on_ready():
    print('------')
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    await bot.change_presence(game=discord.Game(name='desu~'))

#Load and Unload commands, disabled until Admin feature has been added
@bot.command(pass_context=True)
async def load(ctx, extension_name : str):
    """Loads an extension."""
    try:
        if ctx.message.author.id in userconfig['admins']:
            bot.load_extension(extension_name)
            await bot.say("{} loaded.".format(extension_name))
        else:
            await bot.say("You don't have permissions to use this command, " + ctx.message.author.name)
    except (AttributeError, ImportError) as e:
        await bot.say("```py\n{}: {}\n```".format(type(e).__name__, str(e)))
        return

@bot.command(pass_context=True)
async def unload(ctx, extension_name : str):
    """Unloads an extension."""
    try:
        if ctx.message.author.id in userconfig['admins']:
            bot.unload_extension(extension_name)
            await bot.say("{} unloaded.".format(extension_name))
        else:
            await bot.say("You don't have permissions to use this command, " + ctx.message.author.name)
    except (AttributeError, ImportError) as e:
        await bot.say("```py\n{}: {}\n```".format(type(e).__name__, str(e)))
        return

@bot.command(pass_context=True)
async def db(ctx):
    """DMs all stored data about a specific User."""
    await bot.say("soon™")

@bot.command()
async def help():
    """Displays the help"""
    helpmessage = ("**-help** - Displays this help\n")
    if "modules.comfy" in userconfig['startup_extensions']:
        helpmessage += ("**-howcomf** - Display tomorrows comfiness for a User\n")
    if "modules.rng" in userconfig['startup_extensions']:
        helpmessage += ("**-roll** - Roll dice in NdN format\n")
        helpmessage += ("**-choose** - Chooses between multiple strings\n")
    if "modules.cgm" in userconfig['startup_extensions']:
        helpmessage += ("**-cgm** - Posts a random picture via the cuteGirls API\n")
    if "modules.fortune" in userconfig['startup_extensions']:
        helpmessage += ("**-fortune** - Will give you your fortune in the style of an omikuji\n")
    if "modules.picoftheday" in userconfig['startup_extensions']:
        helpmessage += ("**-picoftheday** - Shows a special image each day\n")
    if "modules.osu" in userconfig['startup_extensions']:
        helpmessage += ("**-osu set \*osu username\*** - Ties the given osu! username to your discord user\n")
        helpmessage += ("**-osu set \*osu username\*** - Removes the tie of any osu! username to your discord user\n")
        helpmessage += ("**-osu user \*osu username\*** - Shows stats for the specified user (user is optional if you tied your osu! username to your discord user)\n")
    helpmessage += ("Command List with examples and command aliases at <https://github.com/SebastianGi/DesuBot#commands>")
    await bot.say(helpmessage)


if __name__ == "__main__":
    for extension in userconfig['startup_extensions']:
        try:
            bot.load_extension(extension)
            print('Loaded extension: ' + extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))
    bot.run(userconfig['token'], reconnect=True)