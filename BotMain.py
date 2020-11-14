import discord as dc
import asyncio as asy

token = ""
dc.Emoji
client = dc.Client()
id=client.get_guild(768825635682254869)

@client.event
async def on_message(message):
    if message.content.find("!hello") !=-1:
        await message.channel.send("hi")
    
        
@client.event
async def on_message_delete(message):                       #for logging deleted messages
    if message.guild.id == 485358227249168396:
         ma=message.author
         mc=message.content
         id=777150786974515200
         channel=client.get_channel(id)
         await channel.send(f'{mc} | Author:{ma}')

client.run(token)
