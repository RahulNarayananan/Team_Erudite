
from distutils.command.clean import clean
import os
import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import discord
from discord import FFmpegPCMAudio
from apikeys import *

from dotenv import load_dotenv

# load_dotenv()
# TOKEN = os.getenv('DISCORD_TOKEN')
# GUILD = os.getenv('DISCORD_GUILD')
intents=discord.Intents.all()
client = commands.Bot(command_prefix = "!",intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    print("---------------------------")

# @client.event
# async def on_message(message):
#    await client.process_commands(message)
#    if message.author == client.user:
#         return

#    if 'cookie' in message.content.lower():
#         response = ":cookie:"
#         await message.channel.send(response)

@client.event
async def on_member_join(member):
    await member.send(f"Welcome")
#<---------------greet cmd--------------->

@client.command()
async def greet(ctx):
    await ctx.send("HI")
#<--------------join cmd------------------>

@client.command(pass_context=True)
async def join(ctx):
    if (ctx.author.voice):
        channel=ctx.author.voice.channel
        voice=await channel.connect()
        source=FFmpegPCMAudio()
    else:
        await ctx.send("You are not in a voice channel, please join a voice channel to run the command")
#----------------leave cmd---------------->
@client.command(pass_context=True)
async def leave(ctx):
    if (ctx.voice_client):
        await ctx.guild.voice_client.disconnect()
        await ctx.send("I left the voice channel")
    else:
        await ctx.send("I am not in a voice channel")

client.run(token)