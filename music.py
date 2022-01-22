import discord
from discord.ext import commands
import youtube_dl
import random
from pytube import Playlist as pl
# from pytube import YouTube as yt

def ptol(url):
  p = pl(url)
  l = list(u for u in p.video_urls)
  return l 

class music(commands.Cog):
  def __intit__(self,client):
    self.client = client

  @commands.command()
  async def join(self,ctx):
    if ctx.author.voice is None:
      await ctx.send("Please Join a Voice Channel!")
    voice_channel = ctx.author.voice.channel
    if ctx.voice_client is None:
      await voice_channel.connect()
    else:
      await ctx.voice_client.move_to(voice_channel)

  @commands.command()
  async def disconnect(self,ctx):
    await ctx.voice_client.disconnect()

  @commands.command()
  async def play(self,ctx,url):
    try:
      ctx.voice_client.stop()
    except:
      pass
    FFMPEG_OPTIONS = {'before_options':'-reconnect_streamed 1 -reconnect_delay_max 5','options': '-vn'}
    YDL_OPTIONS = {'format':"bestaudio"}
    vc = ctx.voice_client

    with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
      info = ydl.extract_info(url,download = False)
      url2 = info['formats'][0]['url']
      source = await discord.FFmpegOpusAudio.from_probe(url2,**FFMPEG_OPTIONS)
      vc.play(source)

  @commands.command(aliases = ['meditate'])
  async def med(self,ctx):
    try:
      ctx.voice_client.stop()
    except:
      pass
    urls = ptol("https://www.youtube.com/playlist?list=PLw5NgVvYlQSWtIETvQeYTJrX3SYaDqCjt")
    url = random.choice(urls)
    FFMPEG_OPTIONS = {'before_options':'-reconnect_streamed 1 -reconnect_delay_max 5','options': '-vn'}
    YDL_OPTIONS = {'format':"bestaudio"}
    vc = ctx.voice_client

    with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
      info = ydl.extract_info(url,download = False)
      url2 = info['formats'][0]['url']
      source = await discord.FFmpegOpusAudio.from_probe(url2,**FFMPEG_OPTIONS)
      vc.play(source)

  @commands.command(aliases = ['smooth'])
  async def sooth(self,ctx):
    try:
      ctx.voice_client.stop()
    except:
      pass
    urls = ptol("https://www.youtube.com/playlist?list=PL6FB3Q57vUC-J2dJ77BOJiCBWtPlNH9F1")
    url = random.choice(urls)
    FFMPEG_OPTIONS = {'before_options':'-reconnect_streamed 1 -reconnect_delay_max 5','options': '-vn'}
    YDL_OPTIONS = {'format':"bestaudio"}
    vc = ctx.voice_client

    with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
      info = ydl.extract_info(url,download = False)
      url2 = info['formats'][0]['url']
      source = await discord.FFmpegOpusAudio.from_probe(url2,**FFMPEG_OPTIONS)
      vc.play(source)

  @commands.command(aliases = ['calming','anxiety','noanxiety'])
  async def calm(self,ctx):
    try:
      ctx.voice_client.stop()
    except:
      pass
    urls = ptol("https://www.youtube.com/playlist?list=PLt3RXjjdm-Rz-kyG4B009kHkZhUjBUfjG")
    url = random.choice(urls)
    FFMPEG_OPTIONS = {'before_options':'-reconnect_streamed 1 -reconnect_delay_max 5','options': '-vn'}
    YDL_OPTIONS = {'format':"bestaudio"}
    vc = ctx.voice_client

    with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
      info = ydl.extract_info(url,download = False)
      url2 = info['formats'][0]['url']
      source = await discord.FFmpegOpusAudio.from_probe(url2,**FFMPEG_OPTIONS)
      vc.play(source)

  @commands.command(aliases = ['happy','make_happy','happyme','happymood'])
  async def hpy(self,ctx):
    try:
      ctx.voice_client.stop()
    except:
      pass
    urls = ptol("https://www.youtube.com/playlist?list=PLucdVaCSKS8LVYxXgD1eIH6VZWh65mxYw")
    url = random.choice(urls)
    FFMPEG_OPTIONS = {'before_options':'-reconnect_streamed 1 -reconnect_delay_max 5','options': '-vn'}
    YDL_OPTIONS = {'format':"bestaudio"}
    vc = ctx.voice_client

    with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
      info = ydl.extract_info(url,download = False)
      url2 = info['formats'][0]['url']
      source = await discord.FFmpegOpusAudio.from_probe(url2,**FFMPEG_OPTIONS)
      vc.play(source)

  @commands.command(aliases = ['stop'])
  async def pause(self,ctx):
    ctx.voice_client.pause()
    await ctx.send("|PAUSED|")
  
  @commands.command()
  async def resume(self,ctx):
    ctx.voice_client.resume()
    await ctx.send("|RESUME|")    

def setup(client):
  client.add_cog(music(client))
