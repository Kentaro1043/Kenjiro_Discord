import os

import discord
from discord.ext import commands

import requests

from dotenv import load_dotenv

# 開発用.env読み込み、本番環境ではエラーを出さずに無視される
load_dotenv(".env")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.command()
async def blog(ctx):
	res = requests.get('https://blog.kentaro1043.com/wp-json/wp/v2/posts?per_page=1')
	data = res.json()

	await ctx.send(data[0]['link'])


bot.run(os.environ.get("DISCORD_TOKEN"))
