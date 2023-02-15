import discord
import asyncio

intents = discord.Intents.default()
intents.messages = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    while True:
        # find the target channel
        target_channel = discord.utils.get(client.get_all_channels(), name='general')
        # send message to the target channel
        await target_channel.send('test')
        await asyncio.sleep(60)  # wait for 2 hours

client.run('')
