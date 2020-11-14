import discord as dc
import asyncio as asy

token = "NzY4ODI1NjM1NjgyMjU0ODY5.X5GGqw.pO0vRZ_P4vBhzoj0qlq5fdFNsu4"
dc.Emoji
client = dc.Client()
id=client.get_guild(768825635682254869)

@client.event
async def on_message(message):
    if message.content.find("!hello") !=-1:
        await message.channel.send("hi")
    elif message.content.find("!mc") !=-1:
        await message.channel.send("tera baap mc ")
    

client.run(token)
