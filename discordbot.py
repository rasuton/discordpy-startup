# Python 3 interval discord bot
# Interval discord bot that sends custom messages to select discord server's channel at a defined time interval.
# Version 1.0
#
# DEPENDENCIES
# sudo apt-get install python3
# sudo apt-get -y install python3-pip
# python3 -m pip install discord.py==0.16.12 
#
#
# HOW TO USE
#  Go to https://discordapp.com/developers/applications/
#  Create an application
#  Go to 'Bot' section of discordapp.com/developers portal from the menu and add new bot
#  Get a bot token and add it to TOKEN value inside intervalbot.py file
#  Go to 'Auth' section of discordapp.com/developers portal and mark the checkbox 'bot' to generate an invite link for your new bot. 
#  Visit that generated link to invite your bot to your Discord server.
#  INSIDE DISCORD APP: right click on your Discord server's channel where you want the messages to display and then add it as a value for CHANNEL in the intervalbot.py file.
# 
#
# RUN THE BOT (run from command line)
#
# python3 intervalbot.py
"""
import discord
import asyncio

import os

# secret bot token
# never give your secret bot token to anyone
# get it at discordapp.com/developers/applications/me
TOKEN = os.environ['DISCORD_BOT_TOKEN']

# time interval
# how often the message is sent to specified channel in seconds (default: 60)
INTERVAL = 30

# channel to send the message to
# the message is sent to a channel specified with an ID below
# right click on the Discord channel and click 'copy id' to get one
CHANNEL = '471251063715004420'

# message to be sent
# custom message to be sent to specified channel
MESSAGE = '''
```はぁあ～～～```
URL **example**
<https://somelink.to.somewhere>
Plain text **example**
This is your _plain text_ for example.
'''

# send the message function
client = discord.Client()
async def send_interval_message():
    await client.wait_until_ready()
    channel = CHANNEL
    interval = INTERVAL
    message = MESSAGE
    channel = discord.Object(id=channel)
    while not client.is_closed:
        await client.send_message(channel, message)
        await asyncio.sleep(interval)


# print list of servers where this bot is active to console
async def list_servers():
    await client.wait_until_ready()
    while not client.is_closed:
        # you can customize the output message(s) below
        print("--- INTERVAL BOT ONLINE ---")
        for server in client.servers:
            # you can customize the output message(s) below
            print('Active servers: ' + str(server.name))
        await asyncio.sleep(600)


client.loop.create_task(list_servers())

# print the active bot details to console 
@client.event
async def on_ready():
    messageinterval = INTERVAL
    messagechannel = CHANNEL
    messagecontent = MESSAGE
    # you can customize the output message(s) below
    print('Message sent every: ' + str(messageinterval) + ' sec.')
    print('Destination channel id: ' + str(messagechannel))
    print('Message content: ' + str(messagecontent))

    client.loop.create_task(send_interval_message())



client.run(TOKEN)


from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)

@bot.command()
async def taso(ctx):
    await ctx.send('  ( ☞三☞´3｀ )☞三☞それそれたそー')

@bot.command()
async def pping(ctx):
    await ctx.send('pong')



bot.run(token)
"""


from discord.ext import tasks
import discord
import os

token = os.environ['DISCORD_BOT_TOKEN']
client = discord.Client()

channel_sent = None
"""
10秒ごとに発言するメソッドを定義している部分。
async def の1行上が定期実行を示すもので、()内で間隔を指定します。
例えば5分ごとなら(minutes=5)です。
"""
@tasks.loop(seconds=10)
async def send_message_every_10sec():
    await channel_sent.send("10秒経ったよ")

"""
今回はbotの起動直後に定期実行を開始したいので、
botの準備ができた段階で定期実行をstart()します
"""
@client.event
async def on_ready():
    global channel_sent 
    channel_sent = client.get_channel(any_channel_id)
    send_message_every_10sec.start() #定期実行するメソッドの後ろに.start()をつける


client.run(token)
