import discord as dc
from discord.ext import commands
from bs4 import BeautifulSoup as BS
import requests
import random

colors=[dc.Colour.blue(),dc.Colour.blurple(),dc.Colour.red(),dc.Colour.dark_blue(),dc.Colour.teal(),dc.Colour.gold(),dc.Colour.magenta()]

class scrapes(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def anime(self,ctx,command,*,name=None):
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

def setup(client):
    client.add_cog(scrapes(client))
