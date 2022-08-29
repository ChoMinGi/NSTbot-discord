import discord
import asyncio
from discord.ext import commands
from func import wisesaying

bot = commands.Bot(command_prefix="!")


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')


@bot.event
async def on_message(message):
    if message.author == bot.user:

        return

    if message.content.startswith('!명언'):
        quote = wisesaying.wise()
        await message.channel.send(quote)

    if message.content.startswith('!hello'):
        await message.channel.send('hello')


bot.run(
    'MTAwNDIxMjQ2MjU2MTc4ODA4NA.GIF_AA.mOhuc2GPNQlqMjbH7lWOtxtD3iubxlIdgTPuls')
