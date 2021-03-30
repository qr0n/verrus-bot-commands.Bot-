import discord
from discord.ext import commands
import os as o
from main import main

toen = o.environ.get("OEN")

bot = commands.Bot(command_prefix="V!ext")

@bot.command()
async def test(ctx):
  await ctx.send("yep this works")

main()
bot.run(toen)