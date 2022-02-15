import discord
import os
from discord import channel
from discord.ext import commands
from pinger import pings
auth_key=os.getenv("TOKEN")
import config

intents = discord.Intents.default()
intents.members=True
client = commands.Bot(command_prefix="-",intents=intents)

confess_id=config.confess_id
nicknames=config.nicknames
@client.event
async def on_ready():
 print("{0.user} is started".format(client))

@client.event
async def on_member_join(user):
  channel=client.get_channel(843437199206907954)
  await channel.send(f"Namaste <@{user.id}> ! Thanks for joining the server")

@client.event
async def on_member_remove(user):
  channel=client.get_channel(843437199206907954)
  await channel.send(f"{user} left the server")

@client.listen('on_message')
async def messenger(message):
  if (message.author==client.user):
    return 
  to_send = []
  #msg=[i for i in message.content.lower().split()]
  for username in nicknames:
    if username in message.content.lower():
      to_send.append(nicknames[username])

  if to_send:
    await message.channel.send('\n'.join(to_send))
  if (message.channel.id==confess_id):
    embed=discord.Embed(title="Confessions",description=f"```{message.content}```", color=discord.Color.green())

    await message.channel.send(embed=embed)
    await message.delete()    

@commands.has_permissions(administrator=True)
@client.command()
async def kick(k,user:discord.Member,*,because=None):
 await user.kick(reason=because)
 await k.send(f"{user.mention} is kicked from the server")

@commands.has_permissions(administrator=True)
@client.command(aliases=["bodhi_ban"])
async def ban(k,user:discord.Member,*,because=None):
 await user.ban(reason=because)
 await k.send(f"{user.mention} is banned from the server")

@commands.has_permissions(administrator=True)
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

@commands.has_permissions(manage_messages=True) 
@client.command(aliases=["kharani","clean"])
async def clear(k,clr=10):
 clr=clr+1 #including our message
 if (clr<=101):
  await k.channel.purge(limit=clr)
  await k.send(f"Removed {clr-1} messages")
    
 else:    
  await k.send("You can only clear upto 100 messages at a time")

@client.command()
async def invite(k):
  await k.send(f"https://discord.gg/rMNGzCVQhd")

@clear.error
@kick.error
@ban.error
@unban.error
async def clear_error(k, error):
 if isinstance(error, commands.MissingRequiredArgument):
  await k.send('Please specify the amount of messages you want to clear. Usage: //clear <number>')
 if isinstance(error, commands.MissingPermissions):
  await k.send('You do not have manage_messages permssion')

pings()
client.run(auth_key)
