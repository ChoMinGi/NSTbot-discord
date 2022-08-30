import discord


class state:
    # check user in voice channel
    async def UserInVC(self, ctx, bot):
        if ctx.author.voice:
            return True
        await ctx.channel.send(f'{ctx.author.mention} 음성채널에 존재하지 않습니다.')
        return False
