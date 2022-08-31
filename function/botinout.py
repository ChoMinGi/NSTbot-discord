import discord
from discord.ext import commands

import wavelink

from function.statuscheck import state


class FuncBotInOut(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.command(name="botin", usage="", description="Add bot in voice channel")
    async def botin(self, ctx):
        if not await state().UserInVC(ctx, self.bot):
            return
        if not await state().BotInVC(ctx, self.bot):
            return
