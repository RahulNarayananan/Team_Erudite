
import os
import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import discord

from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
intents=discord.Intents.all()
client = commands.Bot(command_prefix = "!",intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
   await client.process_commands(message)
   if message.author == client.user:
        return

   if 'cookie' in message.content.lower():
        response = ":cookie:"
        await message.channel.send(response)

@client.event
async def on_member_join(member):
    await member.send(f"Welcome to Erudite")


client.run(TOKEN)