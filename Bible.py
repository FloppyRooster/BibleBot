from nextcord.ext import commands  # This is the part of discord.py that helps us build bots
from dotenv import load_dotenv
import os
import nextcord
import sys
#from discord_slash import SlashCommand # Importing the newly installed library.

bot = commands.Bot(command_prefix="~",case_insensitive=True)

bot.owner_id = 432420942535327756
bot.load_extension("cogs.christian")
bot.load_extension("cogs.errors")
bot.load_extension("cogs.reload")

load_dotenv('data/bibleToken.env')
bot.run(os.getenv("TOKEN"))
