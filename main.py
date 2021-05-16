from keys.keys import DISCORD_TOKEN
import discord
from discord.ext import commands
import os

#settings
intents = discord.Intents.all()
client = commands.Bot(command_prefix="!", intents=intents)
client.remove_command("help")

#find and load cogs
for filename in os.listdir("./cogs"):
    try:
        if filename.endswith(".py"):
            client.load_extension(f"cogs.{filename[:-3]}")
    except Exception as e:
        print(f"Could not load cog {filename}: {str(e)}")

#Load Cog
@client.command()
@client.is_owner()
async def load(ctx, cog = None):
    try:
        client.load_extension(cog)
    except Exception as e:
        print(f"Could not load cog {cog} due to: {str(e)}")
    else:
        print(f"{cog} loaded succesfully!")
        name = cog.split(".")[1]
        await ctx.send(f"{name} has been loaded")

#Unload Cog
@client.command()
@client.is_owner()
async def unload(ctx, cog = None):
    try:
        client.unload_extension(cog)
    except Exception as e:
        print(f"Could not unload cog {cog} due to: {str(e)}")
    else:
        print(f"{cog} unloaded succesfully!")
        name = cog.split(".")[1]
        await ctx.send(f"{name} has been unloaded")

#Catch errors
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, discord.ext.commands.errors.CommandNotFound):
        await ctx.send("Command wasn't found!:cry: Please use !help for the list of commands")

@client.event
async def on_ready():
    print("JamLam bot is ready!")

#Commands
@client.command
async def hello(ctx):
    await ctx.send("Hi :wave:, I'm JamLam I like HON and Chicken Shawarma plates :kissing_heart: :eggplant:")


@client.command()
async def userinfo(ctx, user: discord.User):
    await ctx.send(f"{user.display_name} {user.name} {user.id}")


@client.command()
@commands.has_role(304851155144540172)
async def clear(ctx, amount=1):
    if amount > 6:
        await ctx.send(f"You wanted to clear {amount} lines, that max is 5")
    elif amount <= 6:
        await ctx.channel.purge(limit=amount)
        await ctx.send(f"Cleared {amount} lines")


@client.command()
async def dominion(ctx):
    dominion = ctx.guild.get_role(843055201204174879)

    embed = discord.Embed(colour = discord.Colour.dark_teal())
    embed.set_image(url = "https://cdn.discordapp.com/attachments/842841855686737980/843011390054072320/a0urCDS.png")

    embed.add_field(name = ":wave:", value = f"{dominion.mention} lets play dominion! https://dominion.games/ :rice: :rice: :rice:")

    await ctx.send(embed = embed)


@client.command()
async def gartic(ctx):
    board_games = ctx.guild.get_role(751321414640074754)
    game_host = ctx.guild.get_member(190327326372790272)

    embed = discord.Embed(colour = discord.Colour.blue())
    embed.set_image(url = "https://cdn.discordapp.com/attachments/842841855686737980/843010353188700200/gartic-phone-kameto.png")

    embed.add_field(name = ":wave:", value = f"time to play gartic phone {board_games.mention} {game_host.mention} link it plz :paintbrush:")

    await ctx.send(embed = embed)


@client.command()
async def apex(ctx):
    apex = ctx.guild.get_role(842672891924447243)

    embed = discord.Embed(colour = discord.Colour.red())
    embed.set_image(url = "https://cdn.discordapp.com/attachments/842841855686737980/843006397401923594/Apex-Legends.png")
    embed.add_field(name = ":wave:", value = f"Assemble Apex Squad {apex.mention} :gun: :gun:")    

    await ctx.send(embed = embed)

client.run(DISCORD_TOKEN)