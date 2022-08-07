import discord
from discord.ext import commands
import datetime

from urllib import parse, request
import re

bot = commands.Bot(command_prefix='>', description="This is a Helper Bot")


@bot.command()
async def ping(ctx):
    await ctx.send('pong')


@bot.command()
async def sum(ctx, numOne: int, numTwo: int):
    await ctx.send(numOne + numTwo)


@bot.command()
async def info(ctx):
    embed = discord.Embed(title=f"{ctx.guild.name}",
                          description="Server Information",
                          timestamp=datetime.datetime.utcnow(),
                          color=discord.Color.blue())
    embed.add_field(name="Server created at", value=f"{ctx.guild.created_at}")
    embed.add_field(name="Server Owner", value=f"{ctx.guild.owner}")
    embed.add_field(name="Server Region", value=f"{ctx.guild.region}")
    embed.add_field(name="Server ID", value=f"{ctx.guild.id}")
    # embed.set_thumbnail(url=f"{ramon.guild.icon}")
    embed.set_thumbnail(
        url="https://pluralsight.imgix.net/paths/python-7be70baaac.png")

    await ctx.send(embed=embed)
  

  
  #Events
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Streaming(
        name="python bot", url="http://www.twitch.tv/hidayatmramon"))
    print('python discord bot')


@bot.listen()
async def on_message(message):
    if "python bot" in message.content.lower():

        await bot.process_commands(message)


bot.run(
    'MTAwMjc4NTM4OTk2ODM2NzcxNw.GVPhhc.DyNqQzWv0QUGD0kayq8C2ZKzq434TKuZJEdOc0')
