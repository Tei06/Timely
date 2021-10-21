from discord.ext import commands
import discord
client = discord.Client()

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    
    @commands.Cog.listener()
    async def on_message_delete(self, message):
        self.bot.sniped_messages = {}
        self.bot.sniped_messages[message.guild.id] = (message.content, message.author, message.channel.name, message.created_at)
        await self.bot.process_commands(message)

    @commands.command()
    async def snipe(self, ctx):
        try:
            contents, author, channel_name, time = self.bot.sniped_messages[ctx.guild.id]
        except:
            await ctx.channel.send("Couldn't find a message to snipe lmao")
            return
        embed = discord.Embed(description=contents, color=discord.Color.purple(), timestamp=time)
        embed.set_author(name=f"{author.name}#{author.discriminator}", icon_url=author.avatar_url)
        embed.set_footer(text=f"Deleted in : #{channel_name}")
        await ctx.channel.send(embed=embed)

def setup(bot):
    bot.add_cog(Fun(bot))