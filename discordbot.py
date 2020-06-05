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
