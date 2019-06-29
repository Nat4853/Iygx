import discord
from discord.ext import commands
from PIL import Image, ImageFont, ImageDraw
from drawboard import draw_board

luckynumbers = [
       ("1", "2", "3"),
       ("4", "5", "6"),
       ("7", "8", "9"),
       ("1", "4", "7"),
       ("2", "5", "8"),
       ("3", "6", "9"),
       ("1", "5", "9"),
       ("3", "5", "7"),
    ]

class TicTacToe:
  def __init__(self, bot):
    self.bot = bot

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
      await ctx.send(embed=embed, file=discord.File(fp="base.png"))
      global players
      players = [ctx.message.author.id, msg.mentions[0].id]
    async def game(self, ctx):
      options = ["x", "o"]
      board = {'7': '7', '8': '8', '9': '9', '4': '4', '5': '5', '6': '6', '1': '1', '2': '2', '3': '3'}
      turn = 0
      while True:
        current = players[turn % 2]
        letter = options[turn % 2]
        embed = discord.Embed(colour=0x0fe295).add_field(name="Turn.", value=f"It is <@{current}>'s turn. Choose a number on a keypad that corresponds to a grid space to play an `{letter}`.")
        await ctx.send(embed=embed)
        def gamecheck(msg):
          if msg.author.id == current:
            if msg.content in ['1','2','3','4','5','6','7','8','9'] and len(msg.content) == 1:
              if board[msg.content] == msg.content:
                return True
          return False
        try:
          msg = await self.bot.wait_for('message', check=gamecheck, timeout=300.0)
        except Exception as e:
          embed = discord.Embed(colour=0xf1524f).add_field(name="Timeout.", value="Your prompt has timed out. If you want to retry, run the original command again.")
          await ctx.send(embed=embed)
          return
        embed = discord.Embed(colour=0x0fe295).add_field(name="Nice Move.", value="Your move has been recorded.")
        board[msg.content] = letter
        draw_board(board)
        await ctx.send(embed=embed, file=discord.File(fp="temp.png"))

        for a, b, c in luckynumbers:
          if board[a] == board[b] == board[c]:
            embed = discord.Embed(colour=0x0fe295).add_field(name="Winner!", value=f"<@{current}> has won the game! :tada:")
            await ctx.send(embed=embed)
            return

        turn += 1
      else:
        embed = discord.Embed(colour=0xf1524f).add_field(name="Sure.", value=f"Denied the Tic Tac Toe request from {ctx.message.author.mention}.")
        await ctx.send(embed=embed)
        return
    self.bot.loop.create_task(game(self, ctx))

def setup(bot):
  bot.add_cog(TicTacToe(bot))
