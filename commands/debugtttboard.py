import discord, os, glob, random
from discord.ext import commands

from PIL import Image, ImageFont, ImageDraw

onumber = 24 # These are constant pixel alignments to allow the Os and Xs to perfectly be aligned in their grid space.
xnumber = 27

class DebugBoard:
  def __init__(self, bot):
    self.bot = bot

  @commands.command(name="tttcommands")
  @commands.is_owner()
  async def comms(self, ctx):
    s = "          "
    embed = discord.Embed(colour=0xf3ebfb, description=
        f"__**TTT Admin Command Menu.**__\n\n\
         **,generate [ID]**{s}The generate command allows creation of a new board. It will be as if a game was started but the board will remain blank and no game will be running.\n\
         **,viewboard [ID]**{s}This allows you to view any board just be having its ID. This doesn't affect the board at all, and only sends the board itself.\n\
         **,listboards**{s}This will return the list of current board files that exist.\n\
         **,insert [ID] [POSITION] [LETTER]**{s}This inserts the chosen letter into the chosen position on the chosen board.\n\
         **,deleteboard [ID]**{s}This deletes the board using its ID. It deletes the PNG and all files affiliated with the board.")
    await ctx.send(embed=embed)

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
      out += f"\n{item[4:-4]}"
    await ctx.send(f"These are all the currently accessable boards:\n```{out}```") 

  @commands.command(name="insert")
  @commands.is_owner()
  async def ins(self, ctx, id: str = None, pos: int = None, letter: str = None):
    if not id or not pos or not letter:
      embed = discord.Embed(colour=0xf1524f).add_field(name="Wait a second..", value="You have failed to insert one of the necessary fields. The available fields are as follows: `ID`, `POS`, `LETTER`.")
      await ctx.send(embed=embed)
    else:
      correlation = {'7': '[0,0]', '8': '[1,0]', '9': '[2,0]', '4': '[0,1]', '5': '[1,1]', '6': '[2,1]', '1': '[0,2]', '2': '[1,2]', '3': '[2,2]'}
      im = Image.open(f'ttt/{id}.png').convert('RGBA')
      fnt = ImageFont.truetype('fonts/brushfont.ttf', 52)
      d = ImageDraw.Draw(im)
      x = 18
      if letter.lower() == "x":
        y = 16
      else:
        y = 13
      hor = eval(correlation[str(pos)])[0]
      ver = eval(correlation[str(pos)])[1]
      d.text((x+hor*99,y+ver*99), letter, font=fnt, fill=(255,255,255,255))
      im.save(f"ttt/{id}.png")
      await ctx.send(f"Sending `{id}.png`..", file=discord.File(fp=f"{os.getcwd()}\\ttt\\{id}.png"))
      
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
