import discord
from discord.ext import commands

luckynumbers = [
       (1, 2, 3),
       (4, 5, 6),
       (7, 8, 9),
       (1, 4, 7),
       (2, 5, 8),
       (3, 6, 9),
       (1, 5, 9),
       (3, 5, 7),
    ]

class TicTacToe:
  def __init__(self, bot):
    self.bot = bot

  @commands.command(name="")
  async def ttt(self, ctx):
    pass

def setup(bot):
  bot.add_cog(TicTacToe(bot))
