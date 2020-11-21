import discord as dc
import asyncio
from discord.ext import commands
import random
import wikipedia as wik
from bs4 import BeautifulSoup
import requests
import datetime

intents=dc.Intents.default()
intents.members=True
intents.presences=True

banned_words=["bruh","BRUH"]

token = ""

client=commands.Bot(command_prefix="!",intents=intents)

@client.event
async def on_ready():
    await client.change_presence(activity=dc.Game("Supa Mario"))
    client.reaction_role=[]

@client.command()
@commands.has_permissions(manage_permissions=True)
async def addrole(ctx,*,role:dc.Role=None,member:dc.Member=None):
    if member==None:
        member=ctx.author
        e = dc.Embed(color=dc.Colour.dark_green(),title="addrole")
        e.add_field(name="Added Role",value="Added Role to {}".format(member.mention))
        await ctx.send(embed=e,content=None)
        await member.add_roles(role)
    elif role==None:
        e = dc.Embed(color=dc.Colour.dark_red(),title="Usage")
        e.add_field(name="!addrole",value="!addrole {} {}".format("[MemberName]","(RoleName)"))
        await ctx.send(embed=e,content=None)
    elif role==None and member==None:
        e = dc.Embed(color=dc.Colour.dark_red(),title="Usage")
        e.add_field(name="!addrole",value="!addrole {} {}".format("[MemberName]","(RoleName)"))
        await ctx.send(embed=e,content=None)

'''@client.event
async def on_message(msg):
    if msg.content=="emojiall":
        dc.Emoji(msg.guild.id,)'''

@client.event
async def on_message(msg):
    name=str(msg.content).lower()
    if name=="bruh":
        await msg.delete()
    await client.process_commands(msg)

@client.command()
async def warn(ctx,*,member:dc.Member=None,reason=None):
    if member==None or reason==None:
        await ctx.send("Please mention whom to warn")
    else:
        pass

@client.command()
async def invite(ctx):
    a = dc.utils.oauth_url(client_id="768825635682254869",permissions=dc.Permissions(8))
    await ctx.send(a)

@client.command(aliases=["id"])
async def _id(ctx):
    await ctx.send(ctx.guild.id)

@client.command()
async def emojis(ctx):
    s=''
    for i in (ctx.guild.emojis):
        if i.animated==False:
             s+="<:{}:{}>".format(i.name,i.id)
    await ctx.send(s)

@client.command()
async def addemojis(ctx,role:dc.Role,msg:dc.Message,emoji:dc.Emoji):
    if msg==None or emoji==None or role==None:
        ctx.send("Invalid Args")
    else:
        await msg.add_reaction(emoji)
        client.reaction_role.append((msg.id,role,emoji))

@client.event
async def on_raw_reaction_add(payload:dc.RawReactionActionEvent):
    channel=payload.channel_id

@client.command()
async def lock(ctx,channel:dc.TextChannel,role:dc.Role=None):
    if role==None:
        role=ctx.guild.roles[0]
    await channel.set_permissions(target=role,send_messages=False)
    await ctx.send(role.id)

@client.command()
async def search(ctx,*,inp):
    url="https://en.wikipedia.org/wiki/"+str(inp).replace(" ","_")

    response=requests.get(url).content

    soup=BeautifulSoup(response,"html.parser")

    e=dc.Embed(title=(soup.find(id="firstHeading")).text,url=url)

    await ctx.send(embed=e)

    #print(soup.find(id="firstHeading").text)


@client.command()
async def ui(ctx,*,member:dc.Member=None):
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

    is_bot="<:cross1:779006336854786058>"

    if member.bot == True:
        is_bot="<a:right:779006338671968256>"
    else:
        is_bot="<a:cross1:779006336854786058>"
    roles=""
    for i in member.roles:
        if i.id==ctx.guild.id:
            continue
        roles+=i.mention+"\n"
    e=dc.Embed()
    e.add_field(name=f"About {member}",value=f"<:arrow:778989582620426260> **Nick Name :** {member.display_name} \n <:arrow:778989582620426260> **User ID : ** {member.id} \n <:arrow:778989582620426260> **Joined Server ** {member.joined_at.strftime('%d-%b-%Y')} \n <:arrow:778989582620426260> **Joined Discord : ** {member.created_at.strftime('%d-%b-%Y')} \n <:arrow:778989582620426260> **Bot :** {is_bot} \n <:arrow:778989582620426260> **Avatar URL :** [Click here]({member.avatar_url})",inline=False)
    e.add_field(name="Status",value='{} | <:phone:778984480772980796> Mobile Status \n {} | <:web:778984466470797342> Web Status \n {} | <:pc:778984512372998204> Desktop Status'.format(mobile_sts,web_sts,desk_sts),inline=True)
    e.set_thumbnail(url=member.avatar_url)
    e.add_field(name=f"Roles({len(member.roles)-1})",value=roles)

    await ctx.send(content=f"<:info:779039384296882217> Information about **{member.name}**",embed=e)
                
 @client.command()
async def search(ctx,*,message=None):
    if message==None:

        message=wikipedia.random(pages=1)

        heading=message

    try:

        inp=wikipedia.search(message,results=1)[0].replace(" ","_")  # search(ctx,*,msg)

        url="https://en.wikipedia.org/wiki/"+inp

        response=requests.get(url).content

        soup=BeautifulSoup(response,"html.parser")

        related="\n".join(wikipedia.search(message,results=5))

        content=soup.find("div",class_="mw-parser-output")

        if message!=None:heading=soup.find(id="firstHeading").text

        #for image link scraping
        try:
            url1="https:"+content.find("table",class_="infobox").img["src"] #try to search on the table if any
        except:
            try:
                url1="https:"+content.find("div",class_="thumbinner").img["src"] #if not try to search on the thumbpanel if any
            except:
                url1="https://seeba.se/wp-content/themes/consultix/images/no-image-found-360x260.png" #if all fails then no image

        paragraphs = content.find_all("p",limit=10)  #returns list of all <p> inside <div> class_=mw-parser-output we only need 1st(and 2nd if the content is less and even 3rd can be added if needed)


        for par in paragraphs:
            for tags in par.find_all("sup"):    #deletes all the <sup> and returns a clean code without [] but has a time complexity of O(n^2)
                tags.decompose()

        counter=0
        while len(paragraphs[counter].text) == 1: #the loop will check until the paragraph is not empty
            counter+=1

        text_content=paragraphs[counter].text

        for paragraph in paragraphs[counter+1:]:  #O(3) is more better than searching the whole list
            if len(text_content)>1024 or len(text_content+paragraph.text)>1024:
                break                              #breaks the loop if more than 1024 char for Embed
            else:
                text_content+="\n"+paragraph.text 

        embed=dc.Embed(title="About",color=random.choice(colors),url=url)  #only embeds dw

        embed.add_field(name=heading,value=text_content,inline=False)

        embed.add_field(name="Related",value=related,inline=False)

        embed.set_thumbnail(url=url1)
        
        await ctx.send(embed=embed,content=f"<:info:779039384296882217> Information about **{message}**")

    except:                                                             #on exception the code will break and say nothing found daddy UwU

        embed=dc.Embed(color=dc.Colour.red())

        embed.add_field(name="Error",value="Nothing Found <:wetpussy:722737793545273416>")
    
        await ctx.send(content=f"<:info:779039384296882217> Information about **{message}**",embed=embed)


client.run(token)
