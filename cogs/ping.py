from discord.ext import commands
import asyncio

class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1,300,commands.BucketType.user)
    async def request(self, ctx):
        await ctx.channel.send(f'{ctx.author.mention} has requested for assistance <@&841118156385812521>')

    @commands.command(aliases = ['st','stats'])
    @commands.has_role(841118156385812521)
    async def serverstats(self, member):
        await member.channel.send(f"Our server now has {member.guild.member_count} members")
        guild = self.bot.get_guild(840614260833124372)
        your_channel = guild.get_channel(840656406678994964)
        membri = guild.member_count
        await your_channel.edit(name='Current members: {}' .format(membri))
        await asyncio.sleep(1.5)
        await member.channel.send('*Successfully updated server stats*')

def setup(bot):
    bot.add_cog(Ping(bot))