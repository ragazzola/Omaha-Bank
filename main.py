import discord
from discord.ext import commands
import os
import requests
import json
import random
from replit import db

#1a função do bot -- dar dinheiro pra pessoa de acordo com a role delx

TOKEN = os.environ['TOKEN']

key = os.getenv("REPLIT_DB_URL")
GUILD = os.getenv('DISCORD_GUILD')

intents = discord.Intents.all() 
client = discord.Client(intents = intents)

@client.event
async def on_ready():
  print('Bot is ready.')
  for guild in client.guilds:
      if guild.name == TOKEN:
          break

  print(
      f'{client.user} is connected to the following guild:\n'
      f'{guild.name}(id: {guild.id})\n'
  )
  
  roles = '\n - '.join([role.name for role in guild.roles])
  members = '\n - '.join([member.display_name for member in guild.members
])
  for member in guild.members:
    print(f'Member: {member.display_name} - Roles: {member.roles[-1]}\n')
  #print(f'Guild Roles:\n - {roles}')
  #print(f'Members:\n - {members}')

@client.event
async def on_member_join(member):
  role = discord.utils.get(member.server.roles, name="Agiota")
  await client.add_roles(member, role)

@client.event
async def on_message(message):
  if  message.content.startswith('$teste'):
    await message.channel.send(client.user)

  if message.content.startswith('$set'):
    #db['Batata'] += 123
    await message.channel.send(db['Batata'])

@client.event
@commands.cooldown(1, 10, commands.BucketType.user)
async def daily(message):
  if message.content.startswith('$daily'):
    db['Batata'] += 1
    print("teste")

#Chave privada do discord criptografada
client.run(TOKEN)

