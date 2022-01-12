import random
import nextcord
from typing import List

def readFromFile(file:str):
    with open(file, "r") as f:
        data = f.read().split(',')
        return [string for string in data if string != ""]

        

def appendFile(file:str, data):
    if data not in readFromFile(file):
        with open(file, 'a') as f:
            f.write(f',{data}')


def removeFromFile(file:str,item_to_remove: str):
    data = readFromFile(file)
    data.remove(item_to_remove)
    data = [string for string in data if string != ""]

    output = ""
    for i in data:
        output += "," + i
    with open(file,"w") as f:
        f.write(output)

def add_fields(embed: nextcord.Embed, fields: List[tuple]):
    for name, value, inline in fields:
        embed.add_field(name=name, value=value, inline=inline)
    return embed

def getAffirmation():
    affermations = readFromFile(r"data/Affirmations.csv")
    return random.choice(affermations)
