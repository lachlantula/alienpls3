import os
import discord

TOKEN = 'TOKEN'

client = discord.Client()

@client.event
async def on_ready():
  print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  messageContent = message.content.lower()
  
  if ('alienpls3' in messageContent):
    response = 'https://media.discordapp.net/attachments/758617780387315755/838040094010769418/alienpls3.gif'
    await message.channel.send(response)
  elif ('get in there' in messageContent or 'lewis' in messageContent):
    response = 'https://media.discordapp.net/attachments/758617780387315755/848889035229364224/get-in-there-lewis.gif'
    await message.channel.send(response)

client.run(TOKEN)
