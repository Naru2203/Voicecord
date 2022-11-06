# Voicecord [![GitHub forks](https://img.shields.io/github/forks/Naru7/Voicecord)](https://github.com/Naru7/Voicecord/network)
Make your Discord Account Online 24/7 on Voice Channels!

----

A Code written by Python that helps you to keep your account 24/7 on Voice Channel.

# Installation

• Fork the repo

• Clone to [replit](https://replit.com)

---

The main.py is the main file. keep_alive.py prevents your repl from going to sleep. (If you have a replit hacker plan, then you can delete this file and paste this code inside the main.py file :
</br>

```py
import os
import time
from keep_alive import keep_alive
try:
	import discord
except:
	from setup import install
	install()
	import discord
    
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

```

Use [uptimerobot.com](https://uptimerobot.com) to make your repl online 24/7.

</br>

----

>Voicecord © 2022 by Naru#9262
