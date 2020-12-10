import discord as dc
from discord.ext import commands
import datetime
from bs4 import BeautifulSoup as BS
import requests
import random
import json
import time
import os

token='Nzc2ODkwMDg5NjgyMjM5NTMw.X67dRw.Ux3wp-wZmmZrdKGmv7FMB9EBSH8'

client=commands.Bot(command_prefix='.')

colors=[dc.Colour.blue(),dc.Colour.blurple(),dc.Colour.red(),dc.Colour.dark_blue(),dc.Colour.teal(),dc.Colour.gold(),dc.Colour.magenta()]

@client.command()
async def load(ctx,extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx,extension):
    client.unload_extension(f'cogs.{extension}')

@client.command()
async def reload(ctx,extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


'''
@client.event
async def on_ready():
    print('Bot ready')
'''


@client.command()
async def ping(ctx):
    await ctx.send(f'{round(client.latency*1000)} ms')
'''
@client.event
async def on_message(message):
    ma=message.author
    mc=message.content
    mc_l=mc.lower()
    if message.guild.id == 485358227249168396:
         if mc_l.find('jee')!=-1 or mc_l.find('neet')!=-1 or mc_l.find('law')!=-1:
             await message.channel.send(f'{ma.mention} STFU nerd, go fuck yourself')
         elif mc_l.find('no u')!=-1:
             await message.channel.send('https://cdn.discordapp.com/attachments/745681562502430721/777588149789392906/DUY04VxW4AEI43O-1.jpg')

@client.command(aliases=['del'])
async def _del(ctx,ammount='1'):
    try:
        n=int(ammount)
    except:
        await ctx.send('Give a number Retard !!!')
    else:
        await ctx.channel.purge(limit=n+1)


@client.command(aliases=['Kick','KICK'])
async def kick(ctx,member : dc.Member=None,*, reason=None):
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

    
@client.command(aliases=['Ban','BAN'])
async def ban(ctx,member : dc.Member=None,*, reason=None):
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
'''

'''    
@client.command()
async def unban(ctx,*,member):
    banned_users = await ctx.guild.bans()
    member_name,member_descriminator=member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name,user.discriminator)==(member_name,member_descriminator):
            await unban(user)
            embed=dc.Embed(title=f"Unbanned {user.name}#{user.discriminator}")
            await ctx.send(embed=embed,content=None)
'''
@client.command()
async def av(ctx,*,member : dc.Member=None):
    if member==None:
        member=ctx.author
    embed=dc.Embed(title=member.display_name)
    embed.add_field(name='Avatar',value='\u200b',inline=True)
    embed.set_image(url=member.avatar_url_as(format='jpg',size=256))
    await ctx.send(embed=embed,content=None)

@client.command()
async def emojis(ctx):
    s=''
    for i in (ctx.guild.emojis):
        if i.animated==False:
             s+=f'<:{i.name}:{i.id}>'
    await ctx.send(s)
'''
@client.command()
async def ui(ctx,*,member : dc.Member=None):
    if member==None:
        member=ctx.author
    embed=dc.Embed()
    embed.add_field(name=f'About {member.display_name}',value=f'Nickname : {member.nick} \n User ID : {member.id} \n Joined Server : {member.joined_at.strftime("%d-%b-%Y")} \n Joined Discord : {member.created_at.strftime("%d-%b-%Y")}')
    await ctx.send(embed=embed,content=None)
'''
'''
@client.command()
async def anime(ctx,command,*,name=None):
    if command.lower()=='search':
        url=f'https://myanimelist.net/search/all?q={name}&cat=all'
        link=requests.get(url).content
        html=BS(link,'lxml')
        #print(html.prettify)
        results=html.find('div',id='myanimelist').find('div',class_="information di-tc va-t pt4 pl8")
        try:
            result_1=results.a['href']
        except:
            embed=dc.Embed(title='Couldn\'t find anything related to the query',color=dc.Colour.red())
            await ctx.send(embed=embed,content=None)
        link_2=requests.get(result_1,'lxml').content
        html_2=BS(link_2,'lxml')
        content=html_2.find('div',id='myanimelist').find('div',id='content')
        sypnosis=content.find('p',itemprop="description").text
        if len(sypnosis)>900:
            sypnosis=sypnosis[:900]+'...\n \n[Written by MAL Rewrite] '
        score=content.find('div',class_="fl-l score").text
        rank=content.find('span',class_='numbers ranked').strong.text
        popularity=content.find('span',class_='numbers popularity').strong.text
        alt_titles=content.find('div',class_='spaceit_pad').text
        alt_titles=alt_titles.split(':')[1]
        name_1=html_2.find('div',id='myanimelist').find('div',class_="h1 edit-info").find('div',class_='h1-title').strong.text
        try:
            thumb=content.find('div',style="text-align: center;").find('img')['data-src']
        except:
            thumb='https://seeba.se/wp-content/themes/consultix/images/no-image-found-360x260.png'

        embed=dc.Embed(title=name_1,url=result_1,color=random.choice(colors))
        embed.add_field(name='Sypnosis',value=sypnosis,inline=False)
        l=['Type','Status','Aired','Episodes','Duration','Genres','Studios']
        for info in content.find('td',class_='borderClass').find_all('div'):
            info=info.text
            category=info.split(':')[0].strip()
            try:
                value=info.split(':')[1].strip()
            except:
                pass
            if category in l:
                if category=='Genres':
                    l2=value.split(',')
                    value=''
                    for i in l2:
                        i=i.strip()
                        i=i[:int((len(i))/2)]
                        value+=f'{i}, '
                    embed.add_field(name=f':performing_arts: {category}',value=value[:-2],inline=False)
                elif category=='Type':
                    embed.add_field(name=f':dividers: {category}',value=value)
                elif category=='Status':
                    embed.add_field(name=f':hourglass_flowing_sand: {category}',value=value)
                elif category=='Aired':
                    embed.add_field(name=f':calendar_spiral: {category}',value=value)
                elif category=='Episodes':
                    embed.add_field(name=f':minidisc: {category}',value=value)
                elif category=='Duration':
                    embed.add_field(name=f':watch: {category}',value=value)
                elif category=='Studios':
                    embed.add_field(name=f':movie_camera: {category}',value=value)
        embed.add_field(name=':globe_with_meridians: Alternate Titles',value=alt_titles)
        embed.add_field(name=':star: Score',value=f'**{score}/10**')
        embed.add_field(name=':military_medal: Rank',value=f'**#{rank[1:]}**')
        embed.add_field(name=':bar_chart: Popularity',value=f'**#{popularity[1:]}**')
        embed.set_thumbnail(url=thumb)
        await ctx.send(embed=embed,content=None)
        end_time=time.time()
        print(end_time-start_time)
    
    elif command.lower()=='top':
        url='https://myanimelist.net/topanime.php'
        link=requests.get(url).content
        html=BS(link,'lxml')
        content=html.find('div',id='myanimelist').find('div',id='content')
        table=content.find('div',class_="pb12")
        lst=table.find_all('tr',class_="ranking-list")
        embed=dc.Embed(title=f'Top {name} Anime Series',color=random.choice(colors))
        for i in range(int(name)):
            entry=lst[i]
            rank=entry.find('td',class_="rank ac").text.strip()
            title=entry.find('td',class_="title al va-t word-break").find('div',class_="di-ib clearfix").h3.text.strip()
            link=entry.find('td',class_="title al va-t word-break").find('div',class_="di-ib clearfix").h3.a['href']
            score=entry.find('td',class_="score ac fs14").text.strip()
            embed.add_field(name='\u200b',value=f'**{rank}.** [{title}]({link}) [Score : {score}/10]',inline=False)
        await ctx.send(embed=embed,content=None)
'''

@client.command()
async def sauce(ctx,no):
    await ctx.send(f'https://nhentai.net/g/{no}')
'''
@client.command()
async def cricket(ctx,status):
    url='https://www.espncricinfo.com/scores'
    link=requests.get(url).content
    html=BS(link,'lxml')
    page=html.find('section',id='pane-main').find('div',class_='row')
    wrap=page.find('div',class_="card content-block scores-live league-scores-container").find('div',class_="container-fluid p-0")
    l=wrap.find_all('div',class_="col-md-8 col-16")
    if status=='score':
        embed=dc.Embed(title=f':cricket_game: Live Cricket Score',url='https://www.espncricinfo.com/scores',color=dc.Colour.blue())
        for i in l:
            try:
                if i.find('span',class_="label match-status red").text in ['Live','Stumps']:
                    link=i.a['href']
                    link=f'https://www.espncricinfo.com{link}'
                    desc=i.find('p',class_="small mb-0 match-description").text
                    l2=i.find_all('div',class_="d-flex justify-content-between align-items-center competitor")
                    team1=l2[0]
                    try:
                        team2=l2[1]
                    except:
                        pass
                    name1=team1.find('p',class_='name').text
                    name2=team2.find('p',class_='name').text
                    score1=team1.find('span',class_='score').text
                    score2=team2.find('span',class_='score').text
                    try:
                        x_score1=team1.find('span',class_='extra-score').text.strip()          
                    except:
                        x_score1=''
                    try:
                        x_score2=team2.find('span',class_='extra-score').text.strip()
                    except:
                        x_score2=''
                    desc_2=i.find('p',class_="extra-small mb-0 match-description match-description-bottom").text
                    embed.add_field(name='\u200b',value='\u200b')
                    embed.add_field(name=f'\n{name1} Vs {name2} :',value=f"{desc}\n\n**{name1} : {score1} {x_score1} **\n**{name2} : {score2} {x_score2}**\n\n{desc_2}\n[Scorecard]({link})",inline=False)
            except:
                pass
    elif status=='results': 
        embed=dc.Embed(title=f':cricket_game: Recent Cricket Results',url='https://www.espncricinfo.com/scores',color=dc.Colour.blue())      
        for i in l:
            try:
                if i.find('span',class_="label match-status").text == 'Result':
                    link=i.a['href']
                    link=f'https://www.espncricinfo.com{link}'
                    desc=i.find('p',class_="small mb-0 match-description").text
                    team1=i.find('div',class_="d-flex justify-content-between align-items-center competitor gray")
                    team2=i.find('div',class_="d-flex justify-content-between align-items-center competitor")
                    name1=team1.find('p',class_='name').text
                    name2=team2.find('p',class_='name').text
                    score1=team1.find('span',class_='score').text
                    score2=team2.find('span',class_='score').text
                    desc_2=i.find('p',class_="extra-small mb-0 match-description match-description-bottom").text
                    embed.add_field(name='\u200b',value='\u200b')
                    embed.add_field(name=f'{name1} Vs {name2} :',value=f"{desc}\n\n**{name1} : {score1} **\n**{name2} : {score2} **\n\n{desc_2}\n[Scorecard]({link})",inline=False)
                    
            except:
                pass

    embed.set_thumbnail(url='https://i.imgur.com/OYdonUN.png')                  
    await ctx.send(embed=embed,content=None)
'''






            
            
    
    





    


client.run(token)