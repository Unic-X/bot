from discord.ext import commands

import discord as dc

import json

def readjson(file:str=None):
    with open("bot/commands/blocked.json") as json_file:
        return json.load(json_file)
def writejson(file,text):
    with open(file,"a+") as f:
        json.dump(text,f)
for i in readjson():
    print(i["blocked_user"])
