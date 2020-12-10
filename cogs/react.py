import discord as dc
from discord.ext import commands

class React(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    
    @commands.Cog.listener()
    async def on_message(self, message):
        ma=message.author
        mc=message.content
        mc_l=mc.lower()
        l=mc_l.split(' ')
        if message.guild.id == 485358227249168396:
            if l.count('jee')>0 :
                await message.channel.send(f'{ma.mention} STFU nerd, go fuck yourself')
            elif l.count('neet')>0 :
                await message.channel.send(f'{ma.mention} STFU nerd, go fuck yourself')
            elif l.count('iit')>0 :
                await message.channel.send(f'{ma.mention} STFU nerd, go fuck yourself')
            elif l.count('aiims')>0 :
                await message.channel.send(f'{ma.mention} STFU nerd, go fuck yourself')
            elif mc_l.find('no u')!=-1:
                await message.channel.send('https://cdn.discordapp.com/attachments/745681562502430721/777588149789392906/DUY04VxW4AEI43O-1.jpg')
            elif mc_l.find('hello there')!=-1:
                await message.channel.send('https://i.imgur.com/LQpucTS.jpg')

def setup(client):
    client.add_cog(React(client))