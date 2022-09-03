import discord
from discord.ext import commands

bot = commands.Bot(command_prefix ="?", description ="Bot de sabo",intents = discord.Intents.all())

@bot.event
async def on_ready():
    print("Le bot est démarré!")
    
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='One piece RED'))

@bot.command()
async def all(ctx):
    await ctx.send("Bonjour tout le monde!")
    await ctx.message.delete()
    
@bot.command()
async def ok(ctx):
    await ctx.send("mon frere sabo est plus fort que mihawk!")
    await ctx.message.delete()

@bot.command()
async def latence(ctx):
    await ctx.send(f"Ma latence est de: {round(bot.latency * 1000)} ms.")
   
bot.run("MTAxNTY0NjM3MTAxOTIzNTQzOA.GBj6ba.jGssMQ4FKTShntaRcUJQ5L62uT83A3pFbMcOu0")