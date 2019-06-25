import discord
from discord.ext import commands

class MagicalPowers:
    def __init__(self, bot):
        self.bot = bot

    # Commands for Loading / Unloading specific files.

    @commands.command(name="load")
    @commands.is_owner() # Prevents normal users from breaking the entire thing.
    async def load(self, ctx, *, toload: str = None):
        if not toload:
            embed = discord.Embed(colour=0xf1524f).add_field(name="Wait a second..", value="What do you wish to load? :thinking:")
            await ctx.send(embed=embed)
        else:
            try:
                self.bot.load_extension(toload)
            except Exception as exc:
                embed = discord.Embed(colour=0xf1524f).add_field(name="Wait a second..", value=f"Could not load file due to `{type(exc).__name__}`:\n`{exc}`")
                await ctx.send(embed=embed)
            else:
                embed = discord.Embed(colour=0x66b864).add_field(name="Done. :)", value="The specified file was loaded successfully.")
                await ctx.send(embed=embed)

    @commands.command(name="unload")
    @commands.is_owner() # Prevents normal users from breaking the entire thing.
    async def unload(self, ctx, *, toload: str = None):
        if not toload:
            embed = discord.Embed(colour=0xf1524f).add_field(name="Wait a second..", value="What do you wish to unload? :thinking:")
            await ctx.send(embed=embed)
        else:
            try:
                self.bot.unload_extension(toload)
            except Exception as exc:
                embed = discord.Embed(colour=0xf1524f).add_field(name="Wait a second..", value=f"Could not unload file due to `{type(exc).__name__}`:\n`{exc}`")
                await ctx.send(embed=embed)
            else:
                embed = discord.Embed(colour=0x66b864).add_field(name="Done. :)", value="The specified file was unloaded successfully.")
                await ctx.send(embed=embed)

    @commands.command(name="reload")
    @commands.is_owner() # Prevents normal users from breaking the entire thing.
    async def reload(self, ctx, *, toload: str = None):
        if not toload:
            embed = discord.Embed(colour=0xf1524f).add_field(name="Wait a second..", value="What do you wish to reload? :thinking:")
            await ctx.send(embed=embed)
        else:
            try:
                self.bot.unload_extension(toload)
                self.bot.load_extension(toload)
            except Exception as exc:
                embed = discord.Embed(colour=0xf1524f).add_field(name="Wait a second..", value=f"Could not reload file due to `{type(exc).__name__}`:\n`{exc}`")
                await ctx.send(embed=embed)
            else:
                embed = discord.Embed(colour=0x66b864).add_field(name="Done. :)", value="The specified file was reloaded successfully.")
                await ctx.send(embed=embed)


    # End of Loading / Unloading.

    # Command to pull from git repository
    @commands.command(name="gitpull")
    @commands.is_owner()
    async def pull(self, ctx):
        process = subprocess.Popen(["git", "pull"], stdout=subprocess.PIPE)
        output = process.communicate()[0]

def setup(bot):
    bot.add_cog(MagicalPowers(bot))