import discord
import random
import pas_gen

import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Zalogowaliśmy się jako {bot.user}')

@bot.command()
async def bark(ctx):
    await ctx.send(f'bark bark!')

@bot.command()
async def bye(ctx):
    await ctx.send("Papa")


@bot.command()
async def genpass(ctx):
    await ctx.send(pas_gen.gen_pass(10))


@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

bot.run("MTE5OTQxMzgyMDY0NTQ1Nzk5MQ.GEeL2m.rhyEeGiobA7lJb5lTtWG_yYMyEn-5a_JQLzuPo")