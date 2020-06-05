#coding:UTF-8
import discord
from discord.ext import tasks
from discord.ext import commands
from datetime import datetime 
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']

target_channel_id = "471251063715004420"

async def my_task():
    while True:
        # do something
        message_channel = bot.get_channel(target_channel_id)
        print(f"Got channel {message_channel}")
        await message_channel.send("Your message")
        await asyncio.sleep(10)

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
@bot.command()
async def info():
    client.loop.create_task(my_task())

loop.start()
bot.run(token)
