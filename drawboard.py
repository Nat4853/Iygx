from PIL import Image, ImageFont, ImageDraw

correlation = {'7': '[0,0]', '8': '[1,0]', '9': '[2,0]', '4': '[0,1]', '5': '[1,1]', '6': '[2,1]', '1': '[0,2]', '2': '[1,2]', '3': '[2,2]'}

x = 18 # Constant for text aligment.

def draw_board(board):
  image = Image.open('base.png').convert('RGBA')
  draw = ImageDraw.Draw(image)
  fnt = ImageFont.truetype('fonts/brushfont.ttf', 52)

  for pos in board: # Cycle through keys.
    if not board[pos] == "0":
      if board[pos] == "x":
        y = 16 # Different constants since different sized letters within font.
      else:
        y = 13
      hor = eval(correlation[str(pos)])[0]
      ver = eval(correlation[str(pos)])[1]
      print(f"({x+hor*99}),({y+ver*99})")
      draw.text(((x+hor*99),(y+ver*99)), str(board[pos]), font=fnt, fill=(255,255,255,255))
  image.save("temp.png")

if __name__ == "__main__":
  board = {'7': 'X', '8': 'X', '9': 'X', '4': 'X', '5': 'X', '6': 'X', '1': 'X', '2': 'X', '3': 'O'}
  draw_board(board)
