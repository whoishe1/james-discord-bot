# from keys.keys import token
import discord
from discord.ext import commands
import os

# Settings
intents = discord.Intents.all()
client = commands.Bot(command_prefix="!", intents=intents)
client.remove_command("help")

# Find and load cogs
for filename in os.listdir("./cogs"):
    try:
        if filename.endswith(".py"):
            client.load_extension(f"cogs.{filename[:-3]}")
    except Exception as e:
        print(f"Could not load cog {filename}: {str(e)}")

# Load Cog
@client.command()
@commands.has_role(304851155144540172)
async def load(ctx, cog=None):
    try:
        client.load_extension(cog)
    except Exception as e:
        print(f"Could not load cog {cog} due to: {str(e)}")
    else:
        print(f"{cog} loaded succesfully!")
        name = cog.split(".")[1]
        await ctx.send(f"{name} has been loaded")


# Unload Cog
@client.command()
@commands.has_role(304851155144540172)
async def unload(ctx, cog=None):
    try:
        client.unload_extension(cog)
    except Exception as e:
        print(f"Could not unload cog {cog} due to: {str(e)}")
    else:
        print(f"{cog} unloaded succesfully!")
        name = cog.split(".")[1]
        await ctx.send(f"{name} has been unloaded")


# Catch errors
@client.event
async def on_command_error(ctx, error):
    spec_user = ctx.guild.get_member(191410964019675137)
    spec_user2 = ctx.guild.get_member(803540330750017576)

    if (
        isinstance(error, discord.ext.commands.errors.CommandNotFound)
        and ctx.message.author.id == 191410964019675137
    ):
        await ctx.send(
            f"{spec_user.mention} (Wiley) that command wasn't found you noob :laughing:  Use !help for the list of commands."
        )
    elif (
        isinstance(error, discord.ext.commands.errors.CommandNotFound)
        and ctx.message.author.id == 803540330750017576
    ):
        await ctx.send(
            f"{spec_user2.mention} (Wiley) that command wasn't found you noob :laughing:  Use !help for the list of commands."
        )
    elif isinstance(error, discord.ext.commands.errors.CommandNotFound):
        await ctx.send(
            f"Command wasn't found! :cry: Please use !help for the list of commands."
        )


@client.event
async def on_ready():
    print("JamLam bot is ready!")


# Commands
@client.command()
async def hello(ctx):
    await ctx.send(
        "Hi :wave:, I'm JamLam I like HON and Chicken Shawarma plates :kissing_heart: :eggplant:"
    )


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

    embed = discord.Embed(colour=discord.Colour.dark_teal())
    embed.set_image(
        url="https://cdn.discordapp.com/attachments/842841855686737980/843011390054072320/a0urCDS.png"
    )

    embed.add_field(
        name=":wave:",
        value=f"lets play dominion! https://dominion.games/ :rice: :rice: :rice:",
    )

    await ctx.send(f"{dominion.mention}", embed=embed)


@client.command()
async def gartic(ctx):
    board_games = ctx.guild.get_role(751321414640074754)
    game_host = ctx.guild.get_member(190327326372790272)

    embed = discord.Embed(colour=discord.Colour.blue())
    embed.set_image(
        url="https://cdn.discordapp.com/attachments/842841855686737980/843010353188700200/gartic-phone-kameto.png"
    )

    embed.add_field(
        name=":wave:",
        value=f"time to play gartic phone {game_host.mention} link it plz :paintbrush:",
    )

    await ctx.send(f"{board_games.mention}", embed=embed)


@client.command()
async def apex(ctx):
    apex = ctx.guild.get_role(842672891924447243)

    embed = discord.Embed(colour=discord.Colour.red())
    embed.set_image(
        url="https://cdn.discordapp.com/attachments/842841855686737980/843006397401923594/Apex-Legends.png"
    )
    embed.add_field(name=":wave:", value=f"Assemble Apex Squad :gun: :gun:")

    await ctx.send(f"{apex.mention}", embed=embed)


@client.command()
async def unite(ctx):
    unite = ctx.guild.get_role(871333695787773982)

    embed = discord.Embed(colour=discord.Colour.gold())
    embed.set_image(
        url="https://cdn.discordapp.com/attachments/853158897170513951/871316895087882240/unite.png"
    )
    embed.add_field(
        name=":wave:", value=f"Pokemon battle time! :dog::cat::pig::panda_face::frog:"
    )

    await ctx.send(f"{unite.mention}", embed=embed)


@client.command()
async def hon(ctx):
    unite = ctx.guild.get_role(894322801383714886)

    embed = discord.Embed(colour=discord.Colour.purple())
    embed.set_image(
        url="https://cdn.discordapp.com/attachments/842841855686737980/894320880216342579/220px-Hon_logo_box_art.png"
    )
    embed.add_field(
        name=":wave:",
        value=f"guys James wants to play HoN :elephant::octopus::ox::cow::lion_face::fish:",
    )

    await ctx.send(f"{unite.mention}", embed=embed)


client.run(os.environ["DISCORD_TOKEN"])
