from bs4 import BeautifulSoup

import wikipedia

import asyncio

import aiohttp

from discord.ext import commands

import random

import discord as dc

import time

import requests

async def funcname():
    pass

async def main(url):
    pass
    #async with aiohttp.ClientSession() as session:
     #   async with session.get(url) as response:

            #html = await response.text()
            #response.close()
            #return await html

colors=[dc.Colour.blue(),dc.Colour.blurple(),dc.Colour.red(),dc.Colour.dark_blue(),dc.Colour.teal(),dc.Colour.gold(),
dc.Colour.magenta()]

'''async def result_fetch(url):
    async with aiohttp.ClientSession() as session:
        response = await fetch(session,url)
        await session.close()
        return response'''

class wiki_search(commands.Cog):

    def __init__(self,bot):
        self.bot=bot

    @commands.command()
    async def search(self,ctx,*,message=None):

        start=time.time()

        if message==None:

            message=wikipedia.random(pages=1)

            heading=message

        try:

            inp=wikipedia.search(message,results=1)[0].replace(" ","_")  # search(ctx,*,msg)

            url="https://en.wikipedia.org/wiki/"+inp

            #response=requests.get(url).content
            loop=asyncio.get_running_loop()
            #loop=asyncio.get_event_loop()
            loop.create_task(main)
            response=await main(url)

            print("Request Time {}".format(time.time()-start))

            soup=BeautifulSoup(response,"html.parser")

            related="\n".join(wikipedia.search(message,results=5)[1:])

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

            if len(text_content)>1024:
                text_content=text_content[:1021]+'..'

            for paragraph in paragraphs[counter+1:]:  #O(3) is more better than searching the whole list
                if len(text_content)>1024 or len(text_content+paragraph.text)>1024:
                    break                            #breaks the loop if more than 1024 char for Embed
                else:
                    text_content+="\n"+paragraph.text 

            embed=dc.Embed(title="About",color=random.choice(colors),url=url)  #only embeds dw

            embed.add_field(name=heading,value=text_content,inline=False)

            embed.add_field(name="Related",value=related,inline=False)

            embed.set_thumbnail(url=url1)

            await ctx.send(embed=embed,content=f"<:info:779039384296882217> Information about **{message}**")

        except Exception as e:                                                             #on exception the code will break and say nothing found daddy UwU

            embed=dc.Embed(color=dc.Colour.red())

            embed.add_field(name="Error",value="Nothing Found <:wetpussy:722737793545273416>")

            await ctx.send(content=f" Information about **{message}**",embed=embed)
            
            print(e)

if __name__ == "__main__":
    funcname()


def setup(client):
    client.add_cog(wiki_search(client))