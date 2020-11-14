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
            
@client.event
async def on_message(message):                             #for deleting messages
    mc_l=(message.content).lower()
    if mc_l[0:5]=='.del ':
        try:
            n=int(mc_l[5:])
        except:
            await message.channel.send('Give a number Retard')
        else:
            await message.channel.purge(limit=n+1)
            
@client.event
async def on_message_edit(before,after):
    if before.guild.id == 485358227249168396 and before.author != client.user:         #for logging edited message
         ma=before.author
         bc=before.content
         ac=after.content
         id=777191174032195595
         embed_e=dc.Embed(title='Edited Message')
         embed_e.add_field(name='Before : ',value=bc)
         embed_e.add_field(name='After : ',value=ac)
         embed_e.add_field(name='Author : ',value=ma)
         
         channel=client.get_channel(id)
         await channel.send(content=None,embed=embed_e)            
            
client.run(token)
