import discord as dc
from discord.ext import commands

class Log(commands.Cog):

    def __init__(self, client):
        self.client=client

    @commands.Cog.listener()
    async def on_message_delete(self, message):                       
        if message.guild.id == 485358227249168396 and message.author not in [self.client.user,'PokéRealm#1930','NQN#3454'] :
            ma=message.author
            mc=message.content
            id_c=777150786974515200
            
            embed_d=dc.Embed(title='Deleted Message',color=dc.Colour.blue())
            embed_d.add_field(name='Message : ',value=mc,inline=False)
            embed_d.add_field(name='Author : ',value=ma)
            embed_d.add_field(name='Channel : ',value=str(message.channel))
            
            
            channel=self.client.get_channel(id_c)
            await channel.send(content=None,embed=embed_d)

    @commands.Cog.listener()
    async def on_message_edit(self,before,after):
        if before:
            if before.guild.id == 485358227249168396 and before.author not in [self.client.user,'PokéRealm#1930','NQN#3454']:       
                ma=before.author
                bc=before.content
                ac=after.content
                id_c=777191174032195595
                if bc!=ac:
                    embed_e=dc.Embed(title='Edited Message',color=dc.Colour.blue())
                    embed_e.add_field(name='Before : ',value=bc,inline=False)
                    embed_e.add_field(name='After : ',value=ac,inline=False)
                    embed_e.add_field(name='Author : ',value=ma)
                    embed_e.add_field(name='Channel : ',value=str(before.channel))

                    channel=self.client.get_channel(id_c)
                    await channel.send(content=None,embed=embed_e)

class Moderation(commands.Cog):

    def __init__(self, client):
        self.client=client

    @commands.command(aliases=['del'])
    async def _del(self,ctx,ammount='1'):
        try:
            n=int(ammount)
        except:
            await ctx.send('Give a number Retard !!!')
        else:
            await ctx.channel.purge(limit=n+1)

    @commands.command()
    async def kick(self,ctx,member : dc.Member=None,*, reason=None):
        if ('kick_members', True) in list(ctx.author.guild_permissions):    
            if member==None:
                embed = dc.Embed(title='Command : .kick')
                embed.add_field(name='Description : ',value='Kick a member ',inline=False)
                embed.add_field(name='Usage : ',value='.kick [user] [reason] ',inline=False)
                embed.add_field(name='Example : ',value='.kick @Retard GTFO')
                await ctx.send(embed=embed,content=None)   
            elif ('kick_members', True) not in member.guild_permissions and ('ban_members', True) not in member.guild_permissions:
                await member.kick(reason= reason)
                embed = dc.Embed(title=f'{member} was kicked')
                embed.add_field(name='Reason : ',value=reason)
                await ctx.send(embed = embed, content=None)
            else:
                embed = dc.Embed(title=':x: That user is a mod/admin, I can\'t do that.')
                await ctx.send(embed=embed, content=None) 
        else:
            embed=dc.Embed(title=':x: You are not authorized to perform that action')
            await ctx.send(embed=embed, content=None)

    @commands.command()
    async def ban(self,ctx,member : dc.Member=None,*, reason=None):
        if ('ban_members', True) in list(ctx.author.guild_permissions):    
            if member==None:
                embed = dc.Embed(title='Command : .ban')
                embed.add_field(name='Description : ',value='Ban a member',inline=False)
                embed.add_field(name='Usage : ',value='.ban [user] [reason]',inline=False)
                embed.add_field(name='Example : ',value='.ban @Retard GTFO',inline=False)
                await ctx.send(embed=embed,content=None)
            elif ('kick_members', True) not in member.guild_permissions and ('ban_members', True) not in member.guild_permissions:
                await member.ban(reason= reason)
                embed = dc.Embed(title=f'{member} was banned')
                embed.add_field(name='Reason : ',value=reason)
                await ctx.send(embed = embed, content=None)
            else:
                embed = dc.Embed(title=':x: That user is a mod/admin, I can\'t do that.')
                await ctx.send(embed=embed, content=None)
    
        else:
            embed=dc.Embed(title=':x: You are not authorized to perform that action')
            await ctx.send(embed=embed, content=None)


def setup(client):
    client.add_cog(Log(client))
    client.add_cog(Moderation(client))