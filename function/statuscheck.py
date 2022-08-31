import discord
import wavelink
from discord.ext import commands


class state:
    # check user in voice channel
    async def UserInVC(self, ctx, bot):
        if ctx.author.voice:
            return True
        await ctx.channel.send(f'{ctx.author.mention} 음성채널에 없습니다.')
        return False

    # check user not in voice channel
    async def UserNotInVC(self, ctx, bot):
        if ctx.author.voice:
            return False
        await ctx.channel.send(f'{ctx.author.mention} 음성채널 내에 있습니다.')
        return True

    # check bot in voice channel
    async def BotInVC(self, ctx, bot):
        playuser = bot.wavelink.get_player(ctx.guild.id)

        if playuser.is_connected:
            return True
        await ctx.channel.send(f'{ctx.author.mention} 봇이 음성채널 내에 없습니다.')
        return False

    # check bot not in voice channel
    async def BotNotInVC(self, ctx, bot):
        playuser = bot.wavelink.get_player(ctx.guild.id)

        if not playuser.is_connected:
            return True
        await ctx.channel.send(f'{ctx.author.mention} 봇이 음성채널 내에 있습니다.')
        return False
