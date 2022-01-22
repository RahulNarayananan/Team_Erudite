import discord
from discord.ext import commands
import music
import os
import random
import time

GUILD = os.getenv('DISCORD_GUILD')
client =   commands.Bot(command_prefix = '?',intents = discord.Intents.all())

cogs = [music]

for i in range(len(cogs)):
  cogs[i].setup(client)

################################################
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_member_join(member):
    await member.send(f"Welcome to Erudite")

###############################

@client.command()
async def encourage(ctx):
    responses = ['You can reach your goals!',
                 'You\'re wonderful!',
                 'You\'re amazing!',
                 'You\'re the best!',
                 'Keep going, you\'re almost there!',
                 'You are worth it!'
                 ]
    await ctx.send(random.choice(responses))#sends encouragement



@client.command()
async def hotline(ctx):
    await ctx.send('Suicide Hotline: 800-273-8255')#suicide hotline

@client.command()
async def dating(ctx):
    await ctx.send('Dating Abuse and Domestic Violence Hotline:  866-331-9474')#dating abuse hotline

@client.command()
async def lgbtq(ctx):
    await ctx.send('The Trevor Project(LGBTQ Support Hotline):  866-488-7386')#LGBTQ Support

@client.command()
async def eating(ctx):
    await ctx.send('National Eating Disorder Association - Eating Disorder Hotline:  800-931-2237')#Eating Disorder

@client.command()
async def general(ctx):
    await ctx.send('General Crisis Hotline: text "SUPPORT" to 741-741 ')#General Crisis
    
@client.command()
async def mental(ctx):
    await ctx.send('National Alliance on Mental Illness - Mental Illness Hotline: 800-950-6264')#mental illness
     
@client.command()
async def sex(ctx):
    await ctx.send('Rape, Abuse and Incest National Network - Sexual Assault Hotline: 800-656-4673')#Sexual assault
 
@client.command(aliases=['veteran'])
async def vet(ctx):
    await ctx.send('Veterans Association - Veterans Crisis Hotline: 800-273-8255')#veteran crisis line
 
@client.command(aliases=['abort'])
async def abortion(ctx):
    await ctx.send('National Domestic Violence Hotline - Abortion Hotline: 800-799-SAFE')#abortion hotline

@client.command()
async def coronavirus(ctx):
    await ctx.send('Protect yourself from the virus! \n While 25 feet is recommended, be sure to try to stay at least')
    await ctx.send('6 feet from people you don\'t normally come in contact with!')
    await ctx.send( 'f you would like more information, feel free to call the CDC')
    await ctx.send('coronavirus hotline! : 1-800-CDC-INFO (1-800-232-4636)')

@client.event
async def on_message(message):
    await client.process_commands(message)
    if message.author == client.user:
      return

    if 'kys' in message.content.lower():
        response = "That is not appropriate to say to anyone. Please watch your language."
        await message.channel.send(response)

    if 'faggot' in message.content.lower():
        response = "That is not appropriate to say to anyone. Please watch your language."
        await message.channel.send(response)

    if 'fag' in message.content.lower():
        response = "That is not appropriate to say to anyone. Please watch your language."
        await message.channel.send(response)

    if 'fuck' in message.content.lower():
        response ="That is not appropriate to say to anyone. Please watch your language."
        await message.channel.send(response)

    if 'nigger' in message.content.lower():
        response = "That is not appropriate to say to anyone. Please watch your language."
        await message.channel.send(response)

    if 'nigga' in message.content.lower():
        response = "That is not appropriate to say to anyone. Please watch your language."
        await message.channel.send(response)

    if 'kill urself' in message.content.lower():
        response = "That is not appropriate to say to anyone. Please watch your language."
        await message.channel.send(response)

    if 'kill yourself' in message.content.lower():
        response = "That is not appropriate to say to anyone. Please watch your language."
        await message.channel.send(response)

    if 'kms' in message.content.lower():
        response = "Help is available, speak with a counselor today by calling the National Suicide Prevention Lifeline at 800-273-8255"
        await message.channel.send(response)

    if 'kill my self' in message.content.lower():
        response = "Help is available, speak with a counselor today by calling the National Suicide Prevention Lifeline at 800-273-8255"
        await message.channel.send(response)

    if 'suicide' in message.content.lower():
        response = "Help is available, Speak with a counselor today by calling the National Suicide Prevention Lifeline at 800-273-8255"
        await message.channel.send(response)


client.run("OTM0Mzc3Njg4NzA0MTA2NTM2.YevNCA.VZ2qPyYk2fpFV0Ps39L9yU1pOoE")