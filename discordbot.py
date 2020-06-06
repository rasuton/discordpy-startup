import asyncio
import discord
import os
import datetime

token = os.environ['DISCORD_BOT_TOKEN']
client = discord.Client()
@client.event
async def on_ready():
    asyncio.ensure_future(greeting_gm())

async def greeting_gm():
    channel = client.get_channel('718811732243382345')
    while True:
        print(datetime.datetime.now().minute)
        if(datetime.datetime.now().minute==31):
            print("eeee")
            await client.send_message(channel, 'イキスギィ～' + str(datetime.datetime.now()))
            //待つ秒数
            await asyncio.sleep(55)
        elif(datetime.datetime.now().minute==32):
            await client.send_message(channel, 'ハメ～' + str(datetime.datetime.now()))
            await asyncio.sleep(55)
        else:
            await asyncio.sleep(55)

client.run(token)
