import discord as dc
import asyncio as asy
import time

token = ""
dc.Emoji
client = dc.Client()
id=client.get_guild(768825635682254869)
channels=[]


@client.event
async def on_message(message):
    if message.content.find("!hello") !=-1:
        await message.channel.send("hi")
    elif message.mention_everyone == True:
        await message.channel.send("kisne ping kiya madarchod")
    elif message.content=="!id":
        await message.channel.send(message.id)
    elif message.content=="!channels":
        pass
    elif message.content == "!serverid":
        await message.channel.send(message.guild.id)
        

client.run(token)
