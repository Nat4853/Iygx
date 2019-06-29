import discord
from discord.ext import commands
from PIL import Image, ImageFont, ImageDraw
from drawboard import draw_board

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

  @commands.command(name="testdraw")
  async def td(self, ctx):
    board = {'7': '0', '8': 'x', '9': '0', '4': 'x', '5': '0', '6': '0', '1': 'o', '2': '0', '3': 'o'}
    draw_board(board)
    await ctx.send(file=discord.File(fp="temp.png"))

  @commands.command(name="tictactoe", aliases=["ttt"])
  async def ttt(self, ctx):
    embed = discord.Embed(colour=0x0fe295).add_field(name="Tic Tac Toe.", value="Welcome to Tic Tac Toe! To play, mention a member that you wish to challenge within the next minute.")
    await ctx.send(embed=embed)
    def check(msg):
      if msg.author.id == ctx.message.author.id and len(msg.mentions) > 0 and len(msg.mentions) < 2 and not msg.author.bot:
        return True
    try:
      msg = await self.bot.wait_for('message', check=check, timeout=60.0)
    except Exception as e:
      embed = discord.Embed(colour=0xf1524f).add_field(name="Timeout.", value="Your prompt has timed out. If you want to retry, run the original command again.")
      await ctx.send(embed=embed)
      return
    embed = discord.Embed(colour=0x0fe295).add_field(name="Hey!", value=f"{ctx.message.author.mention} has challenged you to a game of Tic Tac Toe! Do you accept? Reply with \"Yes\" to accept or anything other than that to cancel their request.")
    await ctx.send(msg.mentions[0].mention, embed=embed)
    def check2(msg2):
      return msg2.author.id == msg.mentions[0].id
    try:
      consent = await self.bot.wait_for('message', check=check2, timeout=60.0)
    except Exception as e:
      embed = discord.Embed(colour=0xf1524f).add_field(name="Timeout.", value="Your prompt has timed out. If you want to retry, run the original command again.")
      await ctx.send(embed=embed)
    if consent.content.lower().startswith("yes"):
      embed = discord.Embed(colour=0x0fe295).add_field(name="Get Ready.", value="The game is now starting.")
      await ctx.send(embed=embed, file=discord.File(fp=f"{os.getcwd()}\\ttt\\{id}.png"))

    players = [ctx.message.author.id, msg.mentions[0].id]
    options = ["X", "O"]
    turn = 0
    while True:
      current = players[(turn % 2) + 1]
      letter = options[(turn % 2) + 1]
      embed = discord.Embed(colour=0x0fe295).add_field(name="Turn.", value=f"It is <@{current}>'s turn. Choose a number on a keypad that corresponds to a grid space to play an `{letter}`.")
      await ctx.send(embed=embed)
      def gamecheck(msg):
        if msg.author.id == current:
          if msg.content in ['1','2','3','4','5','6','7','8','9']:
            return True
        return False
      try:
        msg = await self.bot.wait_for('message', check=gamecheck, timeout=300.0)
      except Exception as e:
        embed = discord.Embed(colour=0xf1524f).add_field(name="Timeout.", value="Your prompt has timed out. If you want to retry, run the original command again.")
        await ctx.send(embed=embed)
        return
        # Resume from here.

      turn += 1

    else:
      embed = discord.Embed(colour=0xf1524f).add_field(name="Sure.", value=f"Denied the Tic Tac Toe request from {ctx.message.author.mention}.")
      await ctx.send(embed=embed)
      return

def setup(bot):
  bot.add_cog(TicTacToe(bot))
