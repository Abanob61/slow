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

client.run('NTIzMTcwMzQ4Nzg3Njk1NjE4.DvVrYg.lVYzS0VyPWLlBE57GeceMEM6IZo')
