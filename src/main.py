import logging
import sys
import traceback
from os import environ, getenv
import os

import discord
from discord.ext import commands, tasks

#from raygun4py import raygunprovider

from cogs.questions import pick_question, send_question

logging.basicConfig(level=logging.WARNING)

BOT_TOKEN = os.getenv("BOT_TOKEN")
#raygun_key = getenv("RAYGUN_KEY", None)


#def handle_exception(exc_type, exc_value, exc_traceback):
    #cl = raygunprovider.RaygunSender(raygun_key)
    #cl.send_exception(exc_info=(exc_type, exc_value, exc_traceback))

#sys.excepthook = handle_exception

intents = discord.Intents(messages=True, guilds=True, emojis=True, reactions=True)

bot = commands.Bot(command_prefix="c!", intents=intents)
logging.basicConfig(level=logging.INFO)

initial_cogs = ['cogs.challenge', 'cogs.answer']

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
    question_send_task.start()
    await bot.change_presence(status = discord.Status.online, activity = discord.Activity(type=discord.ActivityType.watching, name = ("c!answer")))
    print('We have logged in as {0.user}'.format(bot))


#task loop for sending question, need to set up date
@tasks.loop(hours = 168) #weekly, prob better way to do
async def question_send_task():
    channel = bot.get_channel(804784999676641311)
    #await channel.send('Question sent!')
    question = pick_question()
    await send_question(bot, channel, question)



bot.run(BOT_TOKEN, bot=True, reconnect=True)
