import discord
from discord.ext import commands
import music
import os
import random 
import json
import requests
import tensorflow as tf  
import tflearn
from tensorflow.python.framework import ops
import numpy as np
import nltk
from nltk.stem.lancaster import LancasterStemmer
import model as MODEL

TOKEN = os.environ['DISCORD_TOKEN']
GUILD = os.getenv('DISCORD_GUILD')
intents=discord.Intents.all()
intents.members=True
client = commands.Bot(command_prefix = "?",intents=intents)
cogs = [music]

for i in range(len(cogs)):
  cogs[i].setup(client)


stemmer= LancasterStemmer()  
ops.reset_default_graph()
words=[]
docx=[]
docy=[]
labels=[]
f=open('intents.json')
data=json.load(f)
for intent in data['intents']:
    for pattern in intent["patterns"]:
        wrds= nltk.word_tokenize(pattern)
        words.extend(wrds)
        docx.append(wrds)
        docy.append(intent['tag'])
    
    if intent["tag"] not in labels:
        labels.append(intent['tag'])
words = [stemmer.stem(w.lower()) for w in words if w not in "?" ]
words= sorted(list(set(words)))

labels=sorted(labels)
training=[]
output=[]

out_empty=[0 for _ in range(len(labels))]

for x, doc in enumerate(docx):
    bag=[]
    wrds=[stemmer.stem(w) for w in doc]
    for w in words:
        if w in wrds:
            bag.append(1)
        else:
            bag.append(0)
    output_row=out_empty[:]
    output_row[labels.index(docy[x])]=1

    training.append(bag)
    output.append(output_row)

training=np.array(training)
output= np.array(output)

net = tflearn.input_data(shape=[None, len(training[0])])
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, len(output[0]), activation='softmax')
net = tflearn.regression(net)
model = tflearn.DNN(net)
model.fit(training, output, n_epoch=1000, batch_size=8, show_metric=True)
model.save('model.tflearn')

################################################
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_member_join(member):

    quoteurl = "https://quotes-inspirational-quotes-motivational-quotes.p.rapidapi.com/quote"

    querystring = {"token":"ipworld.info"}

    headers = {
        'x-rapidapi-host': "quotes-inspirational-quotes-motivational-quotes.p.rapidapi.com",
        'x-rapidapi-key': xrapidkey
        }

    response = requests.request("GET", quoteurl, headers=headers, params=querystring)

    await member.send(f"Welcome")
    await member.send(json.loads(response.text)['text'])


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

    if message.channel.id == 934534628604260413:
      response = MODEL.chat(message.content.lower(),model,words,labels,data,stemmer)
      await message.channel.send(response)

    else:
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

client.run(TOKEN)
