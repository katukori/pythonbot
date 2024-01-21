import discord 
from discord.ext import commands 

client = commands.Bot(command_prefix = '/')

@client.event
async def on_ready():
  await client.change_presence(status=discord.Status.online, activity=discord.Game('made in china'))
  print('Bot Ready')

#@client.command()
#async def say(ctx):
#  await ctx.send('made in china')

@client.command()
async def ping(ctx):
  await ctx.send(f'Pong! {round(client.latency * 1000)}ms*)


client.run('NjY0MDQ4NjIwODk0NjgzMTQ3.XhRZsw.xGTwQWttyn5tRaElbXqQp8-mBgo')
