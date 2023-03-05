import os
import time
from keep_alive import keep_alive
try:
    import discord
except:
    from setup import install
    install()
    import discord

print("""\
██╗░░░██╗░█████╗░██╗░█████╗░███████╗░█████╗░░█████╗░██████╗░██████╗░
██║░░░██║██╔══██╗██║██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗
╚██╗░██╔╝██║░░██║██║██║░░╚═╝█████╗░░██║░░╚═╝██║░░██║██████╔╝██║░░██║
░╚████╔╝░██║░░██║██║██║░░██╗██╔══╝░░██║░░██╗██║░░██║██╔══██╗██║░░██║
░░╚██╔╝░░╚█████╔╝██║╚█████╔╝███████╗╚█████╔╝╚█████╔╝██║░░██║██████╔╝
░░░╚═╝░░░░╚════╝░╚═╝░╚════╝░╚══════╝░╚════╝░░╚════╝░╚═╝░░╚═╝╚═════╝░
**Version: 1.0.0**""")
time.sleep(0.5)
client = discord.Client(intents=discord.Intents.default())
Token = input("Please Enter Your Token: ")
Id = int(input("Please Enter Your Channel ID: "))


@client.event
async def on_ready():
    voice_channel = client.get_channel(Id) 
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Lofi"))
    await voice_channel.connect()
  
    print('Logged in as {0.user}'.format(client))
    print('Connected to voice channel: {}'.format(voice_channel))
    
keep_alive()
client.run(Token, bot = False)
