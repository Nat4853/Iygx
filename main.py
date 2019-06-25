import discord, traceback
from discord.ext import commands

bot = commands.Bot(command_prefix=",", case_insensitive=True)
bot.remove_command("help")

initial = ['c.help']

if __name__ == '__main__':
    for extension in initial:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print(f'Failed to load extension {extension}.', file=sys.stderr)
            traceback.print_exc()

@bot.event
async def on_ready():
    print(f'Authentication Success.\nReady for interaction.')

token = open("token", "r").readlines()[0]
bot.run(token, bot=True, reconnect=True)