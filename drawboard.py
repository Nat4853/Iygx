from PIL import Image, ImageFont, ImageDraw

correlation = {'7': '[0,0]', '8': '[1,0]', '9': '[2,0]', '4': '[0,1]', '5': '[1,1]', '6': '[2,1]', '1': '[0,2]', '2': '[1,2]', '3': '[2,2]'}

x = 18 # Constant for text aligment.

def draw_board(board):
  image = Image.open('base.png').convert('RGBA')
  draw = ImageDraw.Draw(image)
  fnt = ImageFont.truetype('fonts/brushfont.ttf', 52)

  for pos in board: # Cycle through keys.:
    if board[pos] == "x" or board[pos] == "o":
      if board[pos] == "x":
        y = 16 # Different constants since different sized letters within font.
      elif board[pos] == "o":
        y = 13
      hor = eval(correlation[str(pos)])[0]
      ver = eval(correlation[str(pos)])[1]
      draw.text(((x+hor*99),(y+ver*99)), board[pos].upper(), font=fnt, fill=(255,255,255,255))
  image.save("temp.png")
