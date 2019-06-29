import discord
from discord.ext import commands

class Help:
  def __init__(self, bot):
    self.bot = bot

  @commands.command(name="help", aliases=["commands"])
  async def help(self, ctx):
    if ctx.message.author.bot: return
    s = "          "
    embed = discord.Embed(colour=0xf3ebfb, description=
        f"__**Iygx Help and Commands Menu.**__\n\n\
         **,help** / **,commands**{s}Both aliases of this command open this menu.\n\
         **,ttt**{s}This command begins a classic game of Tic Tac Toe. You will need another server member to be able to play.\n\n\
         __Sorry about the lack of games. I put all my time into Tic Tac Toe to ensure it worked well, and I ran out of time faster than I'd expected.__ <3")
    await ctx.send(embed=embed)

def setup(bot):
  bot.add_cog(Help(bot))
