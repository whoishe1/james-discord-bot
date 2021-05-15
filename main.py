from functools import total_ordering
from keys.keys import DISCORD_TOKEN
import discord
from discord.ext import commands

#Todo: move help commands to a Cog

intents = discord.Intents.all()
client = commands.Bot(command_prefix="!", intents=intents)
client.remove_command("help")

@client.event
async def on_ready():
    print("JamLam bot is ready!")

#Help
@client.group(invoke_without_command = True)
async def help(ctx):
    embed = discord.Embed(title = "Help", description = "Use !help <command> for more information", colour = discord.Colour.dark_orange())

    embed.add_field(name = "Commands", value = "hello, clear, dominion, gartic, apex")

    await ctx.send(embed = embed)
 
@help.command()
async def hello(ctx):
    embed = discord.Embed(title = "Hello", description = "JamLam likey :smile:", colour = ctx.author.color)

    embed.add_field(name = "Syntax", value = "!hello")

    await ctx.send(embed = embed)

@help.command()
async def clear(ctx):
    embed = discord.Embed(title = "Clear", description = "Deletes 'x' amount of lines, will delete up to 5 lines at once, defaults 1 line by default if nothing is specified", colour = ctx.author.color)

    embed.add_field(name = "Syntax", value = "!clear (integer), for example !clear 3 or !clear")

    await ctx.send(embed = embed)

@help.command()
async def dominion(ctx):
    embed = discord.Embed(title = "Dominion", description = "Asks Jordan, James, Nick, and Tony spefically to play dominion :sweat_smile:", colour = ctx.author.color)

    embed.add_field(name = "Syntax", value = "!dominion")

    await ctx.send(embed = embed)

@help.command()
async def gartic(ctx):
    embed = discord.Embed(title = "Clear", description = "Asks people who have the role 'board games' to play gartic", colour = ctx.author.color)

    embed.add_field(name = "Syntax", value = "!gartic")

    await ctx.send(embed = embed)

@help.command()
async def apex(ctx):
    embed = discord.Embed(title = "Apex", description = "Asks people who have the role 'apex' to play Apex", colour = ctx.author.color)

    embed.add_field(name = "Syntax", value = "!apex")

    await ctx.send(embed = embed)

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
    jordan = ctx.guild.get_member(249819836668968962)
    james = ctx.guild.get_member(190327326372790272)
    nick = ctx.guild.get_member(328824897914667009)
    tony = ctx.guild.get_member(520466645655748608)

    embed = discord.Embed(colour = discord.Colour.dark_teal())
    embed.set_image(url = "https://cdn.discordapp.com/attachments/842841855686737980/843011390054072320/a0urCDS.png")

    embed.add_field(name = ":wave:", value = f"{jordan.mention} {james.mention} {nick.mention} {tony.mention} lets play dominion! https://dominion.games/ :rice: :rice: :rice:")

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