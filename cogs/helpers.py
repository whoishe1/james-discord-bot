import discord
from discord.ext import commands

class Helpers(commands.Cog):
    def __init__(self, client):
        self.client = client
 
    @commands.Cog.listener()
    async def on_ready(self):
        print('Helpers Cog is now online!')

    @commands.group(invoke_without_command = True)
    async def help(self,ctx):
        embed = discord.Embed(title = "Help", description = "Use !help <command> for more information", colour = discord.Colour.dark_orange())

        embed.add_field(name = "Commands", value = "hello, clear, dominion, gartic, apex")

        await ctx.send(embed = embed)
    
    @help.command()
    async def hello(self,ctx):
        embed = discord.Embed(title = "Hello", description = "JamLam likey :smile:", colour = ctx.author.color)

        embed.add_field(name = "Syntax", value = "!hello")

        await ctx.send(embed = embed)

    @help.command()
    async def clear(self,ctx):
        embed = discord.Embed(title = "Clear", description = "Deletes 'x' amount of lines, will delete up to 5 lines at once, defaults 1 line by default if nothing is specified (Includes current ", colour = ctx.author.color)

        embed.add_field(name = "Syntax", value = "!clear (integer), for example !clear 3 or !clear")

        await ctx.send(embed = embed)

    @help.command()
    async def dominion(self,ctx):
        embed = discord.Embed(title = "Dominion", description = "Asks Jordan, James, Nick, and Tony spefically to play dominion :sweat_smile:", colour = ctx.author.color)

        embed.add_field(name = "Syntax", value = "!dominion")

        await ctx.send(embed = embed)

    @help.command()
    async def gartic(self,ctx):
        embed = discord.Embed(title = "Clear", description = "Asks people who have the role 'board games' to play gartic", colour = ctx.author.color)

        embed.add_field(name = "Syntax", value = "!gartic")

        await ctx.send(embed = embed)

    @help.command()
    async def apex(self,ctx):
        embed = discord.Embed(title = "Apex", description = "Asks people who have the role 'apex' to play Apex", colour = ctx.author.color)

        embed.add_field(name = "Syntax", value = "!apex")

        await ctx.send(embed = embed)

def setup(client):
    client.add_cog(Helpers(client))