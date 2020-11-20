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
            
@client.command()
async def anime(ctx,command,*,name=None):
    if command.lower()=='search':
        url=f'https://myanimelist.net/search/all?q={name}&cat=all'                                   #animu
        link=requests.get(url).content
        html=BS(link,'lxml')
        #print(html.prettify)
        results=html.find('div',id='myanimelist').find('div',class_="information di-tc va-t pt4 pl8")
        result_1=results.a['href']
        link_2=requests.get(result_1,'lxml').content
        html_2=BS(link_2,'lxml')
        content=html_2.find('div',id='myanimelist').find('div',id='content')
        sypnosis=content.find('p',itemprop="description").text
        score=content.find('div',class_="fl-l score").text
        rank=content.find('span',class_='numbers ranked').strong.text
        popularity=content.find('span',class_='numbers popularity').strong.text
        alt_titles=content.find('div',class_='spaceit_pad').text
        alt_titles=alt_titles.split(':')[1]
        name_1=html_2.find('div',id='myanimelist').find('div',class_="h1 edit-info").find('div',class_='h1-title').strong.text
        thumb=content.find('div',style="text-align: center;").find('img')['data-src']
        embed=dc.Embed(title=name_1,url=result_1)
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
                        value+=f'{i},'
                    embed.add_field(name=category,value=value,inline=False)
                else:
                    embed.add_field(name=category,value=value)
        embed.add_field(name='Alternate Titles',value=alt_titles)
        embed.add_field(name='Score',value=score)
        embed.add_field(name='Rank',value=rank)
        embed.add_field(name='Popularity',value=popularity)
        embed.set_thumbnail(url=thumb)
        await ctx.send(embed=embed,content=None)
            
client.run(token)
