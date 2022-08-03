import discord
import requests
from bs4 import BeautifulSoup

client = discord.Client()


def get_myeongan():
    response = requests.get("http://munit.co.kr/lucky/today_proverb.php")
    soup = BeautifulSoup(response.content.decode(
        'utf-8', 'replace'), 'html.parser')
    main = soup.find("p").text
    return (main)


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

client.run(
    'MTAwNDIxMjQ2MjU2MTc4ODA4NA.GIF_AA.mOhuc2GPNQlqMjbH7lWOtxtD3iubxlIdgTPuls')
