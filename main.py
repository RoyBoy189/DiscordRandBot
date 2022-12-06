 # This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import random
import secrets

import discord
from discord.ext import commands
from discord.ext.commands import has_permissions,MissingPermissions


idealist = ["Greeks", "fanasty", "cyberpunk", "monsters", "Love", "sea", "space", "Colonial", "pirates",
            "superheros",
            "animals", "robots", "memes", "mythical creatures or persons", "islands", "store", "plants",
            " musical instrument", "something you can't live without"]
intents = discord.Intents.all()  # or .all() if you ticked all, that is easier

bot = commands.Bot(command_prefix="!", intents=intents)
# client = discord.Client()
n = 19
token = 'put token here'


@bot.event
async def on_ready():
    print("The bot is ready!")


@bot.command(pass_context=True)
async def randomidea(ctx):
    embed = discord.Embed(title="RandomIdea", description=(random.choice(idealist)), color=(0xF85252))
    await ctx.send(embed=embed)


@bot.command(pass_context=True)
@has_permissions(ban_members=True, )
async def addtolist(ctx, item):
    idealist.append(item)
    ctx.send(f'item added to list successfully\nList is now: {idealist}')
    embed = discord.Embed(title="add", description=(item + " has been removed"), color=(0xF85252))
    await ctx.send(embed=embed)

@bot.command(pass_context=True)
@has_permissions(ban_members=True)
async def remove(ctx,  item):
    for x in idealist:
        if x == item:
            idealist.remove(item)
            embed = discord.Embed(title="Remove", description=(x + " has been added"), color=(0xF85252))
            await ctx.send(embed=embed)
    else:
        embed = discord.Embed(title="error", description="Can't find the idea you are looking for", color=(0xF85252))
        ctx.send(embed)


@bot.command(help='Shows bot list')
async def showlist(ctx):
    embed = discord.Embed(title="ListofIdeas", description=', '.join(idealist), color=(0xF85252))
    await ctx.send(embed=embed)

@bot.command(help='Shows bot list')
async def shutdown(ctx):
    exit()


bot.run(token)


