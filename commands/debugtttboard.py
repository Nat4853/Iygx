import discord, os, glob
from discord.ext import commands

from PIL import Image, ImageFont, ImageDraw

onumber = 24 # These are constant pixel alignments to allow the Os and Xs to perfectly be aligned in their grid space.
xnumber = 27

class DebugBoard:
  def __init__(self, bot):
    self.bot = bot

  @commands.command(name="generate")
  @commands.is_owner()
  async def gen(self, ctx, id: str = None):
    if not id:
      embed = discord.Embed(colour=0xf1524f).add_field(name="Wait a second..", value="You must enter an `ID` after the command to know where to store the board.")
      await ctx.send(embed=embed)
      return
    im = Image.new('RGB', (298,298), (0,255,0))
    dr = ImageDraw.Draw(im)
    for i in range(0,3):
      for j in range(0,3):
        dr.rectangle([(0+j*99,0+i*99),(99+j*99,99+i*99)], fill="#36393F", outline="black")
    im.save(f"ttt/{id}.png")
    await ctx.send(f"Generated a blank board into `{id}.png`", file=discord.File(fp=f"{os.getcwd()}\\ttt\\{id}.png"))

  @commands.command(name="viewboard")
  @commands.is_owner()
  async def view(self, ctx, id: str = None):
    if not id:
      embed = discord.Embed(colour=0xf1524f).add_field(name="Wait a second..", value="You must enter an `ID` after the command to know where to store the board.")
      await ctx.send(embed=embed)
      return
    await ctx.send(f"Sending `{id}.png`..", file=discord.File(fp=f"{os.getcwd()}\\ttt\\{id}.png"))

  @commands.command(name="listboards")
  @commands.is_owner()
  async def list(self, ctx):
    out = ""
    for item in glob.glob('ttt/*.png'):
      out += f"{item[4:]}\n"
    await ctx.send(f"```{out}```") 

  @commands.command(name="insert")
  @commands.is_owner()
  async def ins(self, ctx, id: str = None, pos: int = None, letter: str = None):
    if not id or not pos or not letter:
      embed = discord.Embed(colour=0xf1524f).add_field(name="Wait a second..", value="You have failed to insert one of the necessary fields. The available fields are as follows: `ID`, `POS`, `LETTER`.")
      await ctx.send(embed=embed)
    else:
      base = Image.open(f"ttt/{id}.png").convert('RGBA')
      d = ImageDraw.Draw(base)
      fnt = ImageFont.truetype('font.ttf', 72)
      corr = eval(open("keypad-correlation", "r").readlines()[0])
      d.text(corr[f"{letter.lower()}{str(pos)}"], letter, font=fnt, fill=(255,255,255,255))
      base.save(f"ttt/{id}.png")
      
  @commands.command(name="deleteboard")
  @commands.is_owner()
  async def delb(self, ctx, id: str = None):
    if not id:
      embed = discord.Embed(colour=0xf1524f).add_field(name="Wait a second..", value="You must enter an `ID` after the command to know where to store the board.")
      await ctx.send(embed=embed)
    else:
      os.remove(f"ttt/{id}.png")

def setup(bot):
  bot.add_cog(DebugBoard(bot))
