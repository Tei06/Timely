from discord.ext import commands
import discord
import pymongo
import datetime


bot = discord.Client()

class Study(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    @commands.cooldown(1,3600,commands.BucketType.user)
    async def study(self, ctx):
        await ctx.channel.send(f"{ctx.author.name} has requested for a <@&844044834460925972>")

    @commands.command()
    @commands.has_role(841118156385812521)
    async def water(self, ctx):
        embed = discord.Embed(title = "Take a break!", description = "Go for a stroll around the house and get some water!", color = discord.Colour.blue())
        embed.set_image(url = "https://i.pinimg.com/originals/30/ac/29/30ac29596106faebb84133046de41355.gif")
        await ctx.channel.send(embed=embed)

    
    


        

    

def setup(bot):
    bot.add_cog(Study(bot))