import os
import discord
from keep_alive import keep_alive

client = discord.Client()

@client.event
async def on_ready():
  
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="The Forest Grand"))
  
    voice_channel = client.get_channel(Your id channel)
    await voice_channel.connect()
  
    print('Logged in as {0.user}'.format(client))
    print('Successful connect to voice channel.')
  
keep_alive()
client.run(os.getenv("TOKEN"), bot = False)


