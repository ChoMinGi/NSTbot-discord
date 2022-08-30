import discord
import asyncio
from discord.ext import commands
from function.wisesaying import wise
from function.statuscheck import state

bot = commands.Bot(command_prefix="!")


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')


@bot.event
async def on_message(message):
    if message.author == bot.user:

        return

    if message.content.startswith('!명언'):
        quote = wise()
        await message.channel.send(quote)

    if message.content.startswith('!hello'):
        await message.channel.send('hello')

    if message.content.startswith('!join'):
        a = state()
        print(a)


@bot.command()
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()


@bot.command()
async def leave(ctx):
    await ctx.voice_client.disconnect()

bot.run(
    'MTAwNDIxMjQ2MjU2MTc4ODA4NA.GIF_AA.mOhuc2GPNQlqMjbH7lWOtxtD3iubxlIdgTPuls')
