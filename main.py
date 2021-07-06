import discord
import os
from dotenv import load_dotenv

load_dotenv()

auth_key=os.environ["TOKEN"]
client = discord.Client()

@client.event
async def on_ready():
    print('Running the app {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('-mr'):
        await message.channel.send("Morning Nirey's server members")

    if message.content.startswith('-help'):
        await message.channel.send("this bot is just on testing phase")
@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )

client.run(auth_key)
