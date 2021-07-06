import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()
auth_key=os.environ["TOKEN"]
client = commands.Bot(command_prefix="-")

@client.event
async def on_ready():
 print("{0.user} is started".format(client))

@client.command()
async def kick(k,user:discord.Member,*,because=None):
 await user.kick(reason=because)
 await k.send(f"{user.mention} is kicked from the server")

@client.command(aliases=["bodhi_ban"])
async def ban(k,user:discord.Member,*,because=None):
 await user.ban(reason=because)
 await k.send(f"{user.mention} is banned from the server")

@client.command()
async def unban(k, *, member):
  banned_users = await k.guild.bans()
  member_name, member_discriminator = member.split('#')

  for ban_entry in banned_users:
    user = ban_entry.user
  
  if (user.name, user.discriminator) == (member_name, member_discriminator):
    await k.guild.unban(user)
    await k.send(f"{user} have been unbanned sucessfully")
    
  return
        
client.run(auth_key)
