import discord
import asyncio
import socket
import requests

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    await client.change_presence(game=discord.Game(name='SlowBall'), status=discord.Status("online"))

@client.event
async def on_message(message):
    if message.content.startswith('!test'):
        counter = 0
        tmp = await client.send_message(message.channel, 'Calculating messages...')
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1

        await client.edit_message(tmp, 'You have {} messages.'.format(counter))
    elif message.content.startswith('!sleep'):
        await asyncio.sleep(5)
        await client.send_message(message.channel, 'Done sleeping')
    elif message.content.startswith('+help') or message.content.startswith('!verify-help') or message.content.startswith('!getverified'):
        await client.send_message(message.channel, "First: You need to open https://www.haxball.com/headlesstoken and solve the recaptcha to get the token code from there.")  
        await client.send_message(message.channel, "Second: Type here: **+restartroomUS TOKEN_CODE** for restart the US room or **+restartroomEU TOKEN_CODE** for restart the EU room")       
    elif message.content.startswith('+restartroomUS'):
           msg = message.content.strip()
           profilename = msg[15:].strip()
           print (profilename)
           url = requests.get("http://35.211.89.225/exc.php?token=%s" % profilename)
           await client.send_message(message.author, "Starting room")

client.run('NTIzMTcwMzQ4Nzg3Njk1NjE4.DvVrYg.lVYzS0VyPWLlBE57GeceMEM6IZo')
