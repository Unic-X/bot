import discord as dc
from discord.ext import commands
import mysql.connector

mydb=mysql.connector.connect(host='localhost',user='root',passwd='2003',database='discord')

class AFK(commands.Cog):

    def __init__(self, client):
        self.client=client
    
    if 'd' not in globals():
        global d
        d={}

    @commands.command()
    async def afk(self,ctx,*,reason=None):
        n=ctx.author.display_name
        ma=ctx.author
        if str(n).count('[AFK]')==0:
            await ma.edit(nick=f'[AFK]{n}')
            await ctx.channel.send(f'{ma.mention} AFK set : {reason} ')
            d[ma]=reason

    @commands.Cog.listener()
    async def on_message(self, message):
        ma=message.author
        n=ma.display_name

        if ma != self.client.user:

            if str(n).count('[AFK]')>0:
                await ma.edit(nick=n[5:])
                await message.channel.send(f'{ma.mention} Welcome Back !!!, Your AFK is removed')
                d.pop(ma)

            for i in d:
                if i.mentioned_in(message):
                    await message.channel.send(f'{i.mention} is AFK : {d[i]}')
'''
class pong(commands.Cog):
'''   

def setup(client):
    client.add_cog(AFK(client))
    

                 