import logging
import sys
import traceback
from os import environ, getenv
import os

import discord
from discord.ext import commands
#from raygun4py import raygunprovider

logging.basicConfig(level=logging.WARNING)

BOT_TOKEN = os.getenv("BOT_TOKEN")
#raygun_key = getenv("RAYGUN_KEY", None)


#def handle_exception(exc_type, exc_value, exc_traceback):
    #cl = raygunprovider.RaygunSender(raygun_key)
    #cl.send_exception(exc_info=(exc_type, exc_value, exc_traceback))

#sys.excepthook = handle_exception

intents = discord.Intents(messages=True, guilds=True, emojis=True, reactions=True)

bot = commands.Bot(command_prefix="c~", intents=intents)
logging.basicConfig(level=logging.INFO)

initial_cogs = ['cogs.challenge', 'cogs.answer', 'cogs.question_reader']

for cog in initial_cogs:
    # noinspection PyBroadException
    try:
        bot.load_extension(cog)
        logging.info(f"Successfully loaded extension {cog}")
    except Exception as e:
        logging.exception(
            f"Failed to load extension {cog}.", exc_info=traceback.format_exc()
        )


@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))


bot.run(BOT_TOKEN, bot=True, reconnect=True)
