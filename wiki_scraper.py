from bs4 import BeautifulSoup

import wikipedia

import time

import asyncio

import aiohttp

async def fetch(url):

    async with aiohttp.ClientSession() as session:
        response = await session.get(url)

        return await response.text()



def search():

    start=time.time()

    #inp=wikipedia.search("Ennio Morricone",results=1)[0].replace(" ","_")  # search(ctx,*,msg)

    url="https://en.wikipedia.org/wiki/"+"Ennio Morricone"
    loop=asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    response=loop.run_until_complete(fetch(url))
    parsing_time=time.time()
    soup=BeautifulSoup(response,"lxml")

    content=soup.find("div",class_="mw-parser-output")

    response_time=time.time()

    print("response time :",response_time-parsing_time)
    #for image link scraping
    try:
        url1="https:"+content.find("table",class_="infobox").img["src"] #try to search on the table if any
    except:
        try:
            url1="https:"+content.find("div",class_="thumbinner").img["src"] #if not try to search on the thumbpanel if any
        except:
            url1="https://seeba.se/wp-content/themes/consultix/images/no-image-found-360x260.png" #if all fails then no image

    #for content scraping

    paragraphs = content.find_all("p",limit=10)  #returns list of all <p> inside <div> class_=mw-parser-output we only need 1st(and 2nd if the content is less and even 3rd can be added if needed)


    for par in paragraphs:
        for tags in par.find_all("sup"):    #deletes all the <sup> and returns a clean code without [] but has a time complexity of O(n^2)
            tags.decompose()
    counter=0
    while len(paragraphs[counter].text) == 1: #the loop will check until the paragraph is not empty
        counter+=1

    text_content=paragraphs[counter].text

    for paragraph in paragraphs[counter+1:]:  #O(3) is more better than searching the whole list
        if len(text_content)>1024:
            break                              #breaks the loop if more than 1024 char for Embed
        else:
            text_content+="\n"+paragraph.text 
    end=time.time()
    print("logic :",end-response_time)
    print("total time :",end-start)
    print(text_content)
async def main():
    print('hello')
    await asyncio.sleep(1)
    print('world')

asyncio.run(main())
