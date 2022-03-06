# Voicecord
Make your Discord Account Online 24/7 on Voice Channels!

----

A Code written by Python that helps you to keep your account 24/7 on Voice Channel.

# Installation

• Fork the repo

• Install PyNaCl using the Package Manager

• Add TOKEN to env file

• Add id channel to the script

---

The main.py is the main file. keep_alive.py prevents your repl from going to sleep. (If you have a replit hacker plan, then you can delete this file and paste this code inside the main.py file :
</br>

```py
import os
import discord
from keep_alive import keep_alive

client = discord.Client()

@client.event
async def on_ready():
    voice_channel = client.get_channel(add here) #<= add id voice channel
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="The Forest Grand"))
    await voice_channel.connect()
    print('Logged in as {0.user}'.format(client))
    print('Successful connect to voice channel.')
  
keep_alive()
client.run(os.getenv("TOKEN"), bot = False)
```

Use [uptimerobot.com](https://uptimerobot.com) to make your repl online 24/7.

Lastest version: See in version.txt
</br>

----

>Voicecord © 2022 by Naru#3078
