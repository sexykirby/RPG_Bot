import discord
from discord.ext import commands
import sqlite3
import json

with open('setting.json', 'r', encoding = 'utF8') as jFile:
    jData = json.load(jFile)

intents = discord.Intents.default()
intents.message_content = True
intents.messages = True
bot = commands.Bot(command_prefix = '!', intents = intents)

#確認機器人成功啟動
@bot.event
async def on_ready():
    print(">> bot is online <<")

bot.run(jData['TOKEN'])