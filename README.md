# DesuBot

A small bot for [Discord](https://discordapp.com/), themed after the Character Karen Kujō from the anime Kiniro Mosaic

## Getting Started

### Prerequisites

To run the bot you need to create a new app on the [Discord developer page](https://discordapp.com/developers/applications/me). Create the app, give it a name and an avatar, on the next page "Create a Bot User" and copy the token. You will need to add this token in the `config.json` file later.

To run the -osu command you also need an [an osu!-API key](https://github.com/ppy/osu-api/wiki) which needs to be added in the `config.json` file.

Packages that need to be installed in Python 3.6:

* [discord.py](https://github.com/Rapptz/discord.py) - *I'm using version v0.16.12*
* urllib3
* TinyDB
* (**optional**) ujson - *will speed up TinyDB if installed*


### Installation

Rename `config.default.json` to `config.json` and add your Data before the first use.

Values in `config.json`:

* **admins** - UserIDs of Users which are allowed to use Admin commands
* **vips** - UserIDs of Users which should recieve special replies (this feature is mostly WIP)
* **token** - Your Discord bot token (**important**)
* **prefix** - The command prefix, default is "-", e.g. "-help"
* **osuapi** - Your API key form the [osu! API](https://github.com/ppy/osu-api/wiki) to look up users and beatmaps

To start the bot, just run desubot.py.


## Commands

* **-help** - Displays a list of commands
* **-howcomf** - Displays tomorrows comfiness for you or (if you append a @mention) for another user
    - *aliases: -comf, -comfy*
* **-roll** - Rolls dice in NdN format
    - *e.g. "-roll 3d6" will roll 3 six sided dice* 
* **-choose** - Chooses between multiple given choices
    - *e.g. "-choose pizza pasta" will randomly choose between "pizza" or "pasta"* 
* **-cgm** - Gets a random picture from the [CuteGirls API](http://api.cutegirls.moe/). If you append an anime name, it will try to get a picture from that anime
    - *e.g. "-cgm Kiniro Mosaic" will return a cute picture from the anime Kiniro Mosaic together with the source*
    - *aliases: -cutegirl, -cutegirls, -moe*
* **-fortune** - Will give you your fortune in the style of an [omikuji](https://en.wikipedia.org/wiki/O-mikuji)
    - *alias: -omikuji*
* **-picoftheday** - Shows a special image every day
    - *alias: -potd*
* **-osu** - Get data from the [osu! API](https://github.com/ppy/osu-api/wiki)
    - **-osu set** *"-osu set Cookiezi" will tie the osu! user Cookiezi to your discord user*
    - **-osu unset** *Will untie the osu! user tied to your discord user*
    - **-osu user** *"-osu user Cookiezi" displays information about osu! user Cookiezi. If you don't add a username the osu! username tied to your discord user will be used*

## Authors

* **Sebastian G.** - [GitHub profile](https://github.com/SebastianGi)

## License

This project is licensed under the GPL-3.0 License - see the [LICENSE](LICENSE) file for details

## Resources 

* [osu! API](https://github.com/ppy/osu-api/wiki)
* [CuteGirls API](http://api.cutegirls.moe/)
