import re
import string
import argparse

import discord
from discord.ext import commands

parser = argparse.ArgumentParser()

# Filepath for the .ink file (relative)
inkfilepath = "ShopTest.ink"

# Variables used to interface with this like an "api"
inktextline = ""
inkstoryended = False
# globals()["optionprevtext"+str(optionnumber)]
# globals()["optionfulltext"+str(optionnumber)]

# Discord stuff
intents = discord.Intents.default()
intents.members = True
intents.reactions = True
intents.messages = True

bot = commands.Bot(command_prefix=',', intents=intents)

# Gets bot token from cli arguments
parser.add_argument("bottoken")
args = parser.parse_args()

reactnumbers = ["1️⃣","2️⃣","3️⃣", "4️⃣","5️⃣","6️⃣","7️⃣","8️⃣","9️⃣"]

@bot.event
async def on_ready():
    print("Bot ready...")

bot.run(args.bottoken)