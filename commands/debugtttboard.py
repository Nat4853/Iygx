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
    open(f"ttt/{id}.info", "w").write("{"+f"'font': '{random.choice(['brushfont.ttf', 'typewriterfont.ttf'])}', '1': '0', '2': '0', '3': '0', '4': '0', '5': '0', '6': '0', '7': '0', '8': '0', '9': '0'"+"}")
    await ctx.send(f"Generated a blank board into `{id}.png`", file=discord.File(fp=f"{os.getcwd()}\\ttt\\{id}.png"))

  @commands.command(name="viewboard")
  @commands.is_owner()
  async def view(self, ctx, id: str = None):
    if not id:
      embed = discord.Embed(colour=0xf1524f).add_field(name="Wait a second..", value="You must enter an `ID` after the command to know where to store the board.")
      await ctx.send(embed=embed)
      return
    info = open(f"ttt/{id}.info", "r").readlines()[0]
    await ctx.send(f"Sending `{id}.png`..\n```{info}```", file=discord.File(fp=f"{os.getcwd()}\\ttt\\{id}.png"))

  @commands.command(name="listboards")
  @commands.is_owner()
  async def list(self, ctx):
    out = ""
    for item in glob.glob('ttt/*.png'):
      out += f"{item[4:-4]}\n"
    await ctx.send(f"These are all the currently accessable boards:\n```{out}```") 

  @commands.command(name="insert")
  @commands.is_owner()
  async def ins(self, ctx, id: str = None, pos: int = None, letter: str = None):
    if not id or not pos or not letter:
      embed = discord.Embed(colour=0xf1524f).add_field(name="Wait a second..", value="You have failed to insert one of the necessary fields. The available fields are as follows: `ID`, `POS`, `LETTER`.")
      await ctx.send(embed=embed)
    else:
      info = eval(open(f"ttt/{id}.info").readlines()[0])
      corr = eval(open("keypad-correlation", "r").readlines()[0])
      base = Image.open(f"ttt/{id}.png").convert('RGBA')
      d = ImageDraw.Draw(base)
      fnt = ImageFont.truetype("fonts/"+info['font'], 72)
      if not info[str(pos)] == '0':
        await ctx.send("Already a letter there.")
      open(f"ttt/{id}.info", "w").write(str(info).replace(f"'{str(pos)}': '0'", f"'{str(pos)}': '{letter}'"))
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
      os.remove(f"ttt/{id}.info")

def setup(bot):
  bot.add_cog(DebugBoard(bot))
