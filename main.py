import discord
import asyncio
from discord.ext import commands
import requests
import os
from bs4 import BeautifulSoup

client = discord.Client()

token_path = os.path.dirname(os.path.abspath(__file__))+'/token.txt'
get_token = open(token_path, "r", encoding="utf-8")
token = get_token.read()
client.run(token)


def get_myeongan():
    response = requests.get("http://munit.co.kr/lucky/today_proverb.php")
    soup = BeautifulSoup(response.content.decode(
        'utf-8', 'replace'), 'html.parser')
    main = soup.find("p").text
    if len(main) <= 100:
        return(main)
    else:
        get_myeongan()


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!명언'):
        quote = get_myeongan()
        await message.channel.send(quote)
