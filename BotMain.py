import discord as dc
import asyncio
from discord.ext import commands
import random
from discord.ext import tasks

cogs_=("commands.wiki_search",
        "commands.error"
)

#checks if the guild has the jail role or not 
def jailcheck(guild:dc.Guild):
    for i in guild.roles[1:]:
        if i.name=="Jail":
            return (i,True)
            break
        else:
            continue

'''complete bot rewrite as there were many functions
 non readables and crashes that were to be handeled 
so instead of updating the bot there itself i made
 this as the rewrite'''

'''intents are present in order to find the 
status of the users and memebers around the bot'''

intents=dc.Intents.default()
intents.members=True
intents.presences=True

'''random colors just for fun'''

colors=[dc.Colour.blue(),dc.Colour.blurple(),dc.Colour.red(),dc.Colour.dark_blue(),dc.Colour.teal(),dc.Colour.gold(),
dc.Colour.magenta()]

'''token declaration'''

token = "NzY4ODI1NjM1NjgyMjU0ODY5.X5GGqw.MOnV8C7-uBahvdzJJjmrHBRsXZo"

'''prefix and help command decalration'''

client=commands.Bot(command_prefix="!",intents=intents,case_insensitive=False,owner_id=0)
commands.DefaultHelpCommand()

@commands.guild_only()
class Admin(commands.Cog,name="Admin"):

    @commands.is_owner()
    def __init__(self,*args):
        pass
    
    #user info about the user the method used here is complete non-async
    #but instead should be async
    @commands.command()
    @commands.is_owner()
    async def closebot(self,ctx,*,password):
        if password == "ZedawdawDW":
            await client.close()
        else:
            await ctx.send("Wrong Password")

    @closebot.error
    async def bot_error(self,ctx,error):
        if isinstance(error,commands.CheckFailure):
            await ctx.send("Y ARE HA")

    @commands.guild_only()
    @commands.command()
    async def ui(self,ctx,*,member:dc.Member=None):
        await ctx.trigger_typing()
        '''sends sex'''
        if member==None:
            member=ctx.author
        if member.mobile_status == dc.Status.online:
            mobile_sts="Mobile status <:online1:778941955740663828>"
        elif member.mobile_status == dc.Status.idle: 
            mobile_sts="Mobile status <:idle1:778942115136143370>"
        elif member.mobile_status == dc.Status.dnd:
            mobile_sts="Mobile status <:dnd:778942294233186374>"
        elif member.mobile_status == dc.Status.offline or member.mobile_status == dc.Status.invisible:
            mobile_sts="Mobile status <:ded1:778942365527703562>"

        if member.web_status == dc.Status.online:
           web_sts="Web status <:online1:778941955740663828>"
        elif member.web_status == dc.Status.idle:
            web_sts="Web status <:idle1:778942115136143370>"
        elif member.web_status == dc.Status.dnd:
            web_sts="Web status <:dnd:778942294233186374>"
        elif member.web_status == dc.Status.offline or member.web_status == dc.Status.invisible:
            web_sts="Web status <:ded1:778942365527703562>"

        if member.desktop_status == dc.Status.online:
            desk_sts="Desktop status <:online1:778941955740663828>"
        elif member.desktop_status == dc.Status.idle:
            desk_sts="Desktop status <:idle1:778942115136143370>"
        elif member.desktop_status == dc.Status.dnd:
            desk_sts="Desktop status <:dnd:778942294233186374>"
        elif member.desktop_status == dc.Status.offline or member.desktop_status == dc.Status.invisible:
            desk_sts="Desktop status <:ded1:778942365527703562>"

        is_bot="<a:cross1:779006336854786058>"

        if member.bot == True:
            is_bot="<a:right:779006338671968256>"
        else:
            is_bot="<a:cross1:779006336854786058>"
        roles=[]
        for i in member.roles:
            roles.append(i.mention)
        e=dc.Embed(colour=random.choice(colors))
        e.add_field(name=f"About {member}",value=f"<:arrow:778989582620426260> **Nick Name :** {member.display_name} \n <:arrow:778989582620426260> **User ID : ** {member.id} \n <:arrow:778989582620426260> **Joined Server ** {member.joined_at.strftime('%d-%b-%Y')} \n <:arrow:778989582620426260> **Joined Discord : ** {member.created_at.strftime('%d-%b-%Y')} \n <:arrow:778989582620426260> **Bot :** {is_bot} \n <:arrow:778989582620426260> **Avatar URL :** [Click here]({member.avatar_url})",inline=False)
        e.add_field(name="Status",value='{} | <:phone:778984480772980796> Mobile Status \n {} | <:web:778984466470797342> Web Status \n {} | <:pc:778984512372998204> Desktop Status'.format(mobile_sts,web_sts,desk_sts),inline=True)
        e.set_thumbnail(url=member.avatar_url)
        if len(member.roles)==1:
            e.add_field(name=f"Roles({len(member.roles)-1})",value="None")
        else:
            e.add_field(name=f"Roles({len(member.roles)-1})",value="\n".join(roles[1:]))

        await ctx.send(content=f"<:info:779039384296882217> Information about **{member.name}**",embed=e)
    @commands.guild_only()
    @commands.command(aliases=["j"])
    async def jail(self,ctx,*,member:dc.Member=None):
        await ctx.trigger_typing()
        #if "jail" in [i.name for i in ctx.guild.channels] and jailcheck(ctx.guild)[1]==True:
            #memeber.add_roles()
        if member!=None:  
            try:
                jail,bool_ = jailcheck(ctx.guild)
                message = await ctx.send("Wait while bot checks some stuff... <a:load:788355404794429460>")
                await member.add_roles(jail)
                if bool_==True:
                   for channel in ctx.guild.channels:                    
                        if "jail" in (i.name for i in ctx.guild.channels):
                            if channel.name!="jail":
                                await channel.set_permissions(target=jail,read_messages=False,send_messages=False)
                                print(f"sat perms for {channel.name}")
                            else:
                                await channel.set_permissions(target=jail,read_messages=True,send_messages=True)
                                print("set perms for jail")
                        elif "jail" not in (i.name for i in ctx.guild.channels):
                            await ctx.guild.create_text_channel(name="jail",overwrites={ctx.guild.default_role:dc.PermissionOverwrite(read_messages=False)
                                                                                        ,jail:dc.PermissionOverwrite(read_messages=True,send_messages=True)})
                            print("made channel and sat perms")
                await dc.Message.edit(message,content="Done everything finally!! <a:right:779006338671968256>",delete_after=20)         

            except Exception as e:
                await ctx.guild.create_role(name="Jail")
                print("created role")
                await asyncio.sleep(1)              #sleeping so as to make the role 1st and then excecute the program 
                await self.jail(ctx,member=member)
                await ctx.send(f'Following caused the problem to slow ```Role was either removed or not created```')
        else:
            emb=dc.Embed(title="Jail",colour=dc.Color.teal())
            emb.add_field(name="How to use the command",value="U must mention whom to jail")
            await ctx.send(embed=emb)
    
    @jail.error
    async def jail_error(self,ctx,error):
        if isinstance(error,commands.CheckFailure):
            await ctx.send("PORN")

    @commands.command()
    async def send(self,ctx):
        await ctx.send("https://media.discordapp.net/attachments/781804302812839966/788619896169955358/error.gif")

    @commands.guild_only()
    @commands.command()
    async def lock(self,ctx,channel:dc.TextChannel=None,role:dc.Role=None):
        if channel==None:
            channel=ctx.channel
        if role==None:
            role=ctx.guild.roles[0]
        await channel.set_permissions(target=role,send_messages=False)
        await ctx.send(f"locked {channel} <a:right:779006338671968256>")

    @commands.guild_only()
    @commands.command(help="Sex pORn Hub DEcx")
    async def cinf(self,ctx,channel:dc.TextChannel=None):
        if channel==None:
            channel=ctx.channel
        e=dc.Embed(title=channel.name,colour=dc.Color.dark_teal())
        e.add_field(name="Info",value=f'''{channel.position}
                                        {channel.created_at}
                                        {channel.category}
                                        {"".join((f.url for f in await channel.invites()))}''')
        await ctx.send(embed=e)


client.add_cog(Admin(client))

for cog in cogs_:
    client.load_extension(cog)

client.run(token)

