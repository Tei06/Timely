from discord.ext import commands
import os
import aiohttp
import discord
import random
from utils.functions import get_quote

class Api(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    
    @commands.command(brief="gives you a inspirational quote")
    async def quote(self, ctx):
            file = open('C:/Discord Bots/Mr. Timely/utils/quotes.txt', encoding="utf-8")
            contents = file.read()
            x = contents.split("@")
            y = random.choice(x)
            await ctx.send(y)
            file.close()
    
    @commands.command(aliases=['motiv', 'm'])
    async def motivation(self, ctx):
        quote = get_quote()
        await ctx.channel.send(quote)

    @commands.command()
    async def cat(self, ctx):
        """gives you a cat pic"""
        async with aiohttp.ClientSession() as cs:
            async with cs.get("http://aws.random.cat/meow") as r:
                data = await r.json()
                embed = discord.Embed(title = "Catto")
                embed.set_image(url=data['file'])
                embed.set_footer(text = "Shizuku Cat pics :')")
                await ctx.send(embed=embed)
    
    @commands.command(brief="dog pics")
    async def dog(self, ctx):
        """gives you a dog pic"""
        async with aiohttp.ClientSession() as session:
            request = await session.get('https://some-random-api.ml/img/dog')
            dogjson = await request.json()
            request2 = await session.get('https://some-random-api.ml/facts/dog')
            factjson = await request2.json()

        embed = discord.Embed(title="doggo", color=discord.Color.purple())
        embed.set_image(url=dogjson['link'])
        embed.set_footer(text=factjson['fact'])
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Api(bot))