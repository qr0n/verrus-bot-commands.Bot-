import discord
from discord.ext import commands


class DevCommands(commands.Cog, name='Commands'):
	'''These areeloper commands'''

	@commands.command(name="ID")
  #'''gives a user they're own ID''' 
	async def ID(self, ctx):
	    await ctx.send(f"```md\n#{ctx.author.id}```\n is your ID")


def setup(bot):
	bot.add_cog(DevCommands(bot))