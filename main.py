import discord
import asyncio
from discord.ext import commands
import wavelink
from function.wisesaying import wise
from function.statuscheck import state


class Bot(commands.Bot):

    def __init__(self):
        super().__init__(command_prefix='>?')

    async def on_ready(self):
        print('Bot is ready!')


bot = Bot()

bot.run(
    'MTAwNDIxMjQ2MjU2MTc4ODA4NA.GPV5jE.Dcv0Eih7OkgZ5t709pc5WTzYKALInCYqIBaa6Y')
