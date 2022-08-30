import discord
import wavelink


class state:
    # check user in voice channel
    async def UserInVC(self, ctx, bot):
        if ctx.author.voice:
            return True
        await ctx.channel.send(f'{ctx.author.mention} 음성채널 에 없습니다.')
        return False

    async def UserNotInVC(self, ctx, bot):
        if ctx.author.voice:
            return False
        await ctx.channel.send(f'{ctx.author.mention} 음성채널 내에 있습니다.')
        return True

    async def BotInVC(self, ctx, bot):
        if ctx.author.voice:
            return True
        await ctx.channel.send(f'{ctx.author.mention} 음성채널에 존재하지 않습니다.')
        return False

    async def UserInVC(self, ctx, bot):
        if ctx.author.voice:
            return True
        await ctx.channel.send(f'{ctx.author.mention} 음성채널에 존재하지 않습니다.')
        return False
