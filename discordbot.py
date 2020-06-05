#coding:UTF-8
import discord
from discord.ext import tasks
from discord.ext import commands
from datetime import datetime 
from tasks import loop
from asyncio import sleep
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


target_channel_id = "471251063715004420"

"""
async def my_task():
    while True:
        # do something
        message_channel = bot.get_channel(target_channel_id)
        print(f"Got channel {message_channel}")
        await message_channel.send("Your message")
        await asyncio.sleep(10)"""

@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')
    
"""@tasks.loop(seconds=60)
async def loop():
    message_channel = bot.get_channel(target_channel_id)
    print(f"Got channel {message_channel}")
    await message_channel.send("Your message")
    await asyncio.sleep(60)
    """
"""@client.command()
async def info():
    client.loop.create_task(my_task())"""

@loop(seconds=10)
async def name_change():
    message_channel = bot.get_channel(target_channel_id)
    print(f"Got channel {message_channel}")
    await message_channel.send("Your message")
    await sleep(10)
    await message_channel.send("Your message")

name_change.before_loop(bot.wait_until_ready())    
name_change.start()
bot.run(token)
