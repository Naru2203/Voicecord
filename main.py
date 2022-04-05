import os
import discord
import time
from keep_alive import keep_alive

print("""\
██╗░░░██╗░█████╗░██╗░█████╗░███████╗░█████╗░░█████╗░██████╗░██████╗░
██║░░░██║██╔══██╗██║██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗
╚██╗░██╔╝██║░░██║██║██║░░╚═╝█████╗░░██║░░╚═╝██║░░██║██████╔╝██║░░██║
░╚████╔╝░██║░░██║██║██║░░██╗██╔══╝░░██║░░██╗██║░░██║██╔══██╗██║░░██║
░░╚██╔╝░░╚█████╔╝██║╚█████╔╝███████╗╚█████╔╝╚█████╔╝██║░░██║██████╔╝
░░░╚═╝░░░░╚════╝░╚═╝░╚════╝░╚══════╝░╚════╝░░╚════╝░╚═╝░░╚═╝╚═════╝░
**Version: 1.0.0**""")
time.sleep(0.5)
client = discord.Client()

@client.event
async def on_ready():
  
    voice_channel = client.get_channel(add here) #<= add specific id voice channel to connect 
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Lofi"))
    await voice_channel.connect()
  
    print('Logged in as {0.user}'.format(client))
    print('Connected to voice channel {}'.format(voice_channel))
    
keep_alive()
client.run(os.getenv("TOKEN"), bot = False)


