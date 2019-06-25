import discord
from discord.ext import commands

class Help:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="help", aliases=["commands"])
    async def help(self, ctx):
        if ctx.message.author.bot: return

def setup(bot):
    bot.add_cog(Help(bot))