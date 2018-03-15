import discord
import json
from discord.ext import commands


# modules loaded on startup
startup_extensions = ["modules.rng", "modules.comfy", "modules.fortune", "modules.cgm"]

try:
    with open('config.json') as json_data:
        userconfig = json.load(json_data)
except Exception:
    print("OOPSIE WOOPSIE!! uwu We made a fucky wucky!! A wittle fucko boingo! The code monkeys at our headquarters are working VEWY HAWD to fix this!")
description = 'Well, what do we have here, desu~'
bot = commands.Bot(command_prefix=userconfig['prefix'], description=description)
client = discord.Client()
bot.remove_command('help')


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    await bot.change_presence(game=discord.Game(name='desu~'))


#@bot.command()
#async def load(extension_name : str):
#    """Loads an extension."""
#    try:
#        bot.load_extension(extension_name)
#    except (AttributeError, ImportError) as e:
#        await bot.say("```py\n{}: {}\n```".format(type(e).__name__, str(e)))
#        return
#    await bot.say("{} loaded.".format(extension_name))


#@bot.command()
#async def unload(extension_name : str):
#    """Unloads an extension."""
#    bot.unload_extension(extension_name)
#    await bot.say("{} unloaded.".format(extension_name))


@bot.command()
async def help():
    """Displays the help"""
    await bot.say("ToDo")


if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))
    bot.run(userconfig['token'])