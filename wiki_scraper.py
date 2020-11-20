from bs4 import BeautifulSoup

import requests


url="https://en.wikipedia.org/wiki/Albert_Einstein"

response=requests.get(url).content

soup=BeautifulSoup(response,"html.parser")

try:
    content=soup.find("div",class_="mw-parser-output")
    paragraphs=content.find_all("p")
    for paragraph in paragraphs:
        if len(paragraph.text)!=1:
            real_paragraph=paragraph.text
            if len(paragraph.find_next("p").text+real_paragraph)<2000:
                real_paragraph+=paragraph.find_next("p").text
            break
        else:
            continue
    try:
        url1="https:"+content.find("table").img["src"]
    except Exception:
        url1=None
        print("No Image Found")
    print(real_paragraph)
    print(url1)
except Exception:
    print("No exact page found")




