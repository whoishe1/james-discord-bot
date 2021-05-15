from keys.keys import DISCORD_TOKEN
import discord
from discord.ext import commands

intents = discord.Intents.all()
client = commands.Bot(command_prefix="!", intents=intents)


@client.event
async def on_ready():
    print("JamLam bot is ready!")


@client.command
async def hello(ctx):
    await ctx.send("Hi, I'm JamLam I like HON and Chicken Shawarma plates")


@client.command()
async def userinfo(ctx, user: discord.User):
    await ctx.send(f"{user.display_name} {user.name} {user.id}")


@client.command()
async def clear(ctx, amount=1):
    if amount > 5:
        await ctx.send(f"You wanted to clear {amount} lines, that max is 5")
    elif amount <= 5:
        await ctx.channel.purge(limit=amount)


@client.command()
async def dominion_test(ctx):
    jordan = ctx.guild.get_member(249819836668968962)
    james = ctx.guild.get_member(190327326372790272)
    nick = ctx.guild.get_member(328824897914667009)
    tony = ctx.guild.get_member(520466645655748608)
    await ctx.send(
        f"{jordan.mention} {james.mention} {nick.mention} {tony.mention} lets play dominion! https://dominion.games/ :rice: :rice: :rice:"
    )


@client.command()
async def gartic_test(ctx):
    board_games = ctx.guild.get_role(751321414640074754)
    game_host = ctx.guild.get_member(190327326372790272)
    await ctx.send(
        f"time to play gartic phone {board_games.mention}, {game_host.mention} link it :paintbrush:"
    )


@client.command()
async def apex_test(ctx):
    apex = ctx.guild.get_role(842672891924447243)
    await ctx.send(f"Assemble Apex Squad {apex.mention} :gun: :gun:")


client.run(DISCORD_TOKEN)