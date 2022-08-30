import requests
from bs4 import BeautifulSoup
import discord


client = discord.Client()

token_path = os.path.dirname(os.path.abspath(__file__))+'/token.txt'
get_token = open(token_path, "r", encoding="utf-8")
token = get_token.read()
client.run(token)


@client.command()
async def play(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()
