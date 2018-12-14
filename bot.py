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
    await client.change_presence(game=discord.Game(name='SlowBot'), status=discord.Status("online"))

@client.event
async def on_message(message):
    if message.content.startswith('!test'):
        counter = 0
        tmp = await client.send_message(message.channel, 'Calculating messages...')
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1

        await client.edit_message(tmp, 'You have {} messages.'.format(counter))
            elif message.content.startswith('!clear823'):
        tmp = await client.send_message(message.channel, 'Clearing messages...')
        async for msg in client.logs_from(message.channel):
            await client.delete_message(msg)
    elif message.content.startswith('!sleep'):
        await asyncio.sleep(5)
        await client.send_message(message.channel, 'Done sleeping')
    elif message.content.startswith('!verifyhelp') or message.content.startswith('!verify-help') or message.content.startswith('!getverified'):
        await client.send_message(message.channel, "```First: You need to open the PES6 game and type at the chat at any place at game @verifyme```")  
        await client.send_message(message.channel, "```Second: Go to #verificaton channel and type !verify [profile name], The profile name which you are logged with it and type with it @verifyme command!```")       
    elif message.content.startswith('+restartroomUS'):
           msg = message.content.strip()
           profilename = msg[15:].strip()
           print (profilename)
           url = requests.get("http://35.211.89.225/exc.php?token=%s" % profilename)
           await client.send_message(message.author, "Starting room")

client.run('NTIzMTcwMzQ4Nzg3Njk1NjE4.DvVrYg.lVYzS0VyPWLlBE57GeceMEM6IZo')
