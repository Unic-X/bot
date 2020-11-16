import discord as dc
import asyncio
import time
from discord.ext import commands
import random


token = "NzY4ODI1NjM1NjgyMjU0ODY5.X5GGqw._ivQmwl03tujKUyMX5lg7Nwi34U"
dc.Emoji
client = commands.Bot(command_prefix="!",case_insensitive=False)
channels=[]
emoji=dc.Emoji
#@client.event

@client.event
async def on_ready():
    choices=["!for help","ROCKET LEAGUE","DOOM"]
    while not client.is_closed():
        await client.change_presence(activity=dc.Game(random.choice(choices)))
        await asyncio.sleep(10)

'''@client.event
async def on_message(message):
    if message.content=="!id":
        await message.channel.send(message.id)
    elif message.content=="!guilds":
        await message.channel.send(str(client.guilds))
    elif message.content=="!serverid":
        await message.channel.send(message.guild.id)
@client.event
async def on_message_delete(message):                       
    if message.guild.id == 485358227249168396 and message.author not in [client.user,'PokéRealm#1930','NQN#3454'] :
         ma=message.author
         mc=message.content
         id_c=777150786974515200
         
         embed_d=dc.Embed(color=dc.Colour.blurple(),title='Deleted Message')
         embed_d.add_field(name='Message  ',value=mc)
         embed_d.add_field(name='Author  ',value=ma)
         embed_d.add_field(name='Channel  ',value=str(message.channel))
         
         channel=client.get_channel(id_c)
         await channel.send(content=None,embed=embed_d)'''

@client.command(aliases=["ban","bun","BAN"])
async def Ban_func(ctx,member: dc.Member=None,*,reason=None):
    ctx_temp=ctx
    member_temp= dc.Member()
    reason_temp=None
    try:
        @commands.has_permissions(ban_members=True)
        async def _ban(ctx_temp,member_temp,*,reason_temp):
            if member==ctx_temp.author:
                embed_ban=dc.Embed(color=dc.Colour.red(),title="Usage of !ban")
                embed_ban.add_field(name="!ban usage",value='!ban[memmber](reason)')
                await ctx_temp.send("You Cannot Ban Yourself",embed=embed_ban)
            elif member==None:
                embed_ban=dc.Embed(title="Usage of !ban")
                embed_ban.add_field(name="!ban usage",value='!ban{}{}'.format("[Member]","(Reason <OPTIONAL> )"))
                await ctx_temp.send(content=None,embed=embed_ban)
            else:
                embed_ban=dc.Embed(color=dc.Colour.green(),title="Member Banned")
                embed_ban.add_field(name="Ban",value="banned {}".format(member_temp.display_name))
                await ctx_temp.send(content=None,embed=embed_ban)
    except:
        await ctx.send("oops error")
@client.command()
async def ping(ctx):
    await ctx.send("ping is {}".format(round(client.latency*1000)))

client.run(token)
