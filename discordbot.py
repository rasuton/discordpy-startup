#coding:UTF-8
import discord
from discord.ext import tasks
import os

#bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']

client = discord.Client()
channel_sent = None

target_channel_id = "471251063715004420"

"""
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
    """
    
@tasks.loop(seconds=10)
async def send_message_every_10sec():
    await channel_sent.send("10秒経ったよ")
    
@client.event
async def on_ready():
    global channel_sent 
    channel_sent = client.get_channel(target_channel_id)
    send_message_every_10sec.start()



client.run(token)
