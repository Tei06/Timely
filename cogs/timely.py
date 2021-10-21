import discord
from discord.ext import commands
import time
import datetime
import asyncio
import secrets
import random
from utils.functions import text_to_owo

client = discord.Client()

class Timely(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(brief="shows server stats")
    async def server(self, ctx):
        server = ctx.message.guild

        roles = str(len(server.roles))
        emojis = str(len(server.emojis))
        channels = str(len(server.channels))

        embeded = discord.Embed(title=server.name, description='Server Info', color=ctx.author.color)
        embeded.set_thumbnail(url=server.icon_url)
        embeded.add_field(name="Created on:", value=server.created_at.strftime('%d %B %Y at %H:%M UTC+3'), inline=False)
        embeded.add_field(name="Server ID:", value=server.id, inline=False)
        embeded.add_field(name="Users on server:", value=server.member_count, inline=True)
        embeded.add_field(name="Server owner:", value=server.owner, inline=True)


        embeded.add_field(name="Server Region:", value=server.region, inline=True)
        embeded.add_field(name="Verification Level:", value=server.verification_level, inline=True)

        embeded.add_field(name="Role Count:", value=roles, inline=True)
        embeded.add_field(name="Emoji Count:", value=emojis, inline=True)
        embeded.add_field(name="Channel Count:", value=channels, inline=True)
        await ctx.send(embed=embeded)
    
    @commands.command(brief="hacks someone in the server")
    async def hack(self, ctx, member: discord.Member):
        await ctx.message.delete()
        message = await ctx.channel.send(f"[▝]Logging in to {member.mention} <a:EE_loading:855933211644788757>")
        await asyncio.sleep(1.3)
        await message.edit(content = f"Bypassing 2fa information  <a:EE_loading:855933211644788757>")
        await asyncio.sleep(1.5)
        await message.edit(content = "Successfully bypassed 2fa")
        await asyncio.sleep(0.9)
        await message.edit(content = f"**Username:**`{member.name}ishorny24/7@gmail.com`\n**Password:**`{member.name}likesdragonsandrainbowsbling\n**or**\n`{member.name}wantstoeatabigbalonisandwichwithyourmother`")
        await asyncio.sleep(2.4)
        await message.edit(content = f"[▗]Successfully logged in as {member.name}")
        await asyncio.sleep(0.5)
        await message.edit(content = f"[▖]Accessing search history <a:EE_loading:855933211644788757>")
        await asyncio.sleep(1.5)
        await message.edit(content = f"[▘]Sending sus search history to {member.name}'s school principle  <a:EE_loading:855933211644788757>")
        await asyncio.sleep(1.4)
        await message.edit(content = f"[▝]johnny is disaapointed", tts = True)
        await asyncio.sleep(0.8)
        await message.edit(content = f"[▗]Fetching sus dm's *if you have any friends at all*")
        await asyncio.sleep(1.6)
        await message.edit(content = f"[▖]Sending blackmail on all {member.name}'s social media <a:EE_loading:855933211644788757>")
        await asyncio.sleep(1.5)
        await message.edit(content = f"[▘]Injecting ligma and sussybaka virus into {member.name}'s 2001 block of plastic <a:EE_loading:855933211644788757>")
        await asyncio.sleep(1.6)
        await message.edit(content = f"virus files has been unleashed into {member.name}'s computer")
        await asyncio.sleep(1.6)
        await message.edit(content = "||totally legit hack, you should check your computer for virus||")
        await asyncio.sleep(0.5)
        await ctx.channel.send(content = f"the concerning and sus hack has been completed on {member.name}")

    @commands.command(brief="sned ur message but in owo")
    async def owo(self, ctx, *, message):
        await ctx.message.delete()
        await ctx.send(text_to_owo(message))
    @commands.command(aliases = ["sb"])
    async def starboard(self, ctx, id):
        message = await ctx.channel.fetch_message(id)
        await ctx.message.delete()
        channel = self.bot.get_channel(895875611162214420)
        embed = discord.Embed(description=f"__**Message:**__ {message.content} in <#{message.channel.id}>")
        embed.set_author(icon_url=message.author.avatar_url, name=message.author.display_name)
        embed.add_field(name="Source", value = f"[Jump to Message]({message.jump_url})")
        embed.set_footer(text=f"{datetime.datetime.now().date()}")
        await ctx.send("Successfully sent in <#895875611162214420>", delete_after = 3)
        await channel.send(embed=embed)
    
    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        message = await self.bot.get_channel(payload.channel_id).fetch_message(payload.message_id)
        reaction = discord.utils.get(message.reactions, emoji="⭐")
        user = payload.member
        if reaction and reaction.count >= 1:
            channel = self.bot.get_channel(895875611162214420)
            embed = discord.Embed(description=f"__**Message:**__ {message.content}")
            embed.set_author(icon_url=message.author.avatar_url, name=message.author.display_name)
            embed.add_field(name="Channel", value=f"in <#{message.channel.id}>", inline=False)
            embed.add_field(name="Source", value = f"[Jump to Message]({message.jump_url})", inline=False)
            embed.set_footer(text=f"{datetime.datetime.now().date()}")
            await channel.send(embed=embed)

    @commands.command(aliases = ['av'])
    async def avatar(self, ctx, *, member: discord.Member = None):
        if member == None:
            member = ctx.author
            embed = discord.Embed(title = f"{member.display_name}'s Avatar",
            color = ctx.author.color)
            embed.set_image(url = member.avatar_url)
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title = f"{member.display_name}'s Avatar",
            color = ctx.author.color)
            embed.set_image(url = member.avatar_url)
            await ctx.send(embed=embed)


    @commands.command(brief='The bot says what you want it to')
    async def echo(self, ctx, *, echo):
        await ctx.message.delete()
        await ctx.send(f"{echo}")
    
    @commands.command(aliases = ['p'], brief='shows bot response speed')
    async def ping(self, ctx):
        before = time.monotonic()
        message = await ctx.send("Pong!")
        ping = (time.monotonic() - before) * 1000
        await message.edit(content=f"Pong!  `{int(ping)}ms`")
    
    @commands.command()
    async def f(self, ctx, *, text: commands.clean_content = None):
        """ Press F to pay respect """
        hearts = ["❤", "💛", "💚", "💙", "💜"]
        reason = f"for **{text}** " if text else ""
        await ctx.message.delete()
        await ctx.send(f"**{ctx.author.name}** has paid their respect {reason}{random.choice(hearts)}")
    
    @commands.command(aliases=["howhot", "hot"])
    async def hotcalc(self, ctx, *, user: discord.Member = None):
        """ Returns a random percent for how hot is a discord user """
        user = user or ctx.author

        random.seed(user.id)
        r = random.randint(1, 100)
        hot = r / 1.17

        if hot > 25:
            emoji = "❤"
        elif hot > 50:
            emoji = "💖"
        elif hot > 75:
            emoji = "💞"
        else:
            emoji = "💔"

        await ctx.send(f"**{user.name}** is **{hot:.2f}%** hot {emoji}")
    
    @commands.command()
    async def reverse(self, ctx, *, text: str):
        """ !poow ,ffuts esreveR
        Everything you type after reverse will of course, be reversed
        """
        t_rev = text[::-1].replace("@", "@\u200B").replace("&", "&\u200B")
        await ctx.send(f"{t_rev}")


    @commands.command()
    async def password(self, ctx, nbytes: int = 18):
        """ Generates a random password string for you
        This returns a random URL-safe text string, containing nbytes random bytes.
        The text is Base64 encoded, so on average each byte results in approximately 1.3 characters.
        """
        if nbytes not in range(3, 1401):
            return await ctx.send("I only accept any numbers between 3-1400")
        if hasattr(ctx, "guild") and ctx.guild is not None:
            await ctx.send(f"Sending you a private message with your random generated password **{ctx.author.name}**")
        await ctx.author.send(f"🎁 **Here is your password:**\n{secrets.token_urlsafe(nbytes)}")

    @commands.command(brief='Creates instant invite')
    async def invite(self, ctx):
        channel = self.bot.get_channel(840651124633632819)
        link = await channel.create_invite()
        await ctx.send(f"Invite your friends to Timely!: {link}")
    @invite.error
    async def invite_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(f"{ctx.author.mention} Aw the bot doesn't have perms to create an invite :(")

    @commands.command()
    async def rate(self, ctx, *, thing: commands.clean_content):
        """ Rates what you desire """
        rate_amount = random.uniform(0.0, 100.0)
        await ctx.send(f"I'd rate `{thing}` a **{round(rate_amount, 4)} / 100**")

    @commands.command()
    async def beer(self, ctx, user: discord.Member = None, *, reason: commands.clean_content = ""):
        """ Give someone a beer🍻 """
        if not user or user.id == ctx.author.id:
            return await ctx.send(f"**{ctx.author.name}**: mmmm beer!🎉🍺")
        if user.id == self.bot.user.id:
            return await ctx.send("*drinks beer with you* 🍻")
        if user.bot:
            return await ctx.send(f"I would love to give beer to the bot **{ctx.author.name}**, but I don't think it will respond to you :/")

        beer_offer = f"**{user.name}**, you got a 🍺 offer from **{ctx.author.name}**"
        beer_offer = beer_offer + f"\n\n**Reason:** {reason}" if reason else beer_offer
        msg = await ctx.send(beer_offer)

        def reaction_check(m):
            if m.message_id == msg.id and m.user_id == user.id and str(m.emoji) == "🍻":
                return True
            return False

        try:
            await msg.add_reaction("🍻")
            await self.bot.wait_for("raw_reaction_add", timeout=30.0, check=reaction_check)
            await msg.edit(content=f"**{user.name}** and **{ctx.author.name}** are enjoying a lovely beer together 🍻")
        except asyncio.TimeoutError:
            await msg.delete()
            await ctx.send(f"well, doesn't seem like **{user.name}** wanted a beer with you **{ctx.author.name}** ;-;")
        except discord.Forbidden:
            # Yeah so, bot doesn't have reaction permission, drop the "offer" word
            beer_offer = f"**{user.name}**, you got a 🍺 from **{ctx.author.name}**"
            beer_offer = beer_offer + f"\n\n**Reason:** {reason}" if reason else beer_offer
            await msg.edit(content=beer_offer)
    @commands.command()
    async def booster(self, ctx):
        await ctx.message.delete()
        embed = discord.Embed(title = "Timely Booster Perks", color = ctx.author.color, description = "**Boost Timely to get the <@&851611308931547146> role**")
        embed.set_thumbnail(url = ctx.author.avatar_url)
        embed.add_field(name = "Custom Role", value = "Perks to create your own custom role. You can change the name and color of the role anytime", inline = False)
        embed.add_field(name = "Custom Text Channel", value = "The ability to create your own custom text channel!", inline = False)
        embed.add_field(name = "Permanent Voice Room", value = "You get to change the limit and name of your own custom voice channel", inline = False)
        embed.add_field(name = "Shoutouts on our socials!", value = "We will give you a huge shoutout on our instagram story as well as the announcements channel!", inline = False)
        embed.add_field(name = "Custom Emoji", value = "Add a regular or animated emoji to timely! (has to be sfw)", inline = False)
        embed.set_footer(text = "Timely Booster Perks")
        await ctx.send(embed=embed)
    @commands.command(aliases = ['playlist','spot'])
    async def spotify(self, ctx):
        await ctx.channel.send("Every person is allowed to add __**ONE song**__ to the following community playlist\n\n https://open.spotify.com/playlist/5dBX98CTFSYa7TaC0ZnuMQ?si=SwF8RVqBSIurqLInqDrBUw")

    @commands.command()
    async def insta(self, ctx):
        embed = discord.Embed(title = "**Timely instagram accounts:**", description = "Follow our instagram account:\n\n https://www.instagram.com/timely.1/", color = ctx.author.color)
        embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/840614260833124375/844040265220227092/logooo.png')
        await ctx.channel.send(embed=embed)

    @commands.command(aliases = ['anon', 'mysterious'])
    async def anonymous(self, ctx, *, message):
        anon_channel = self.bot.get_channel(900585191771357204)
        log_channel = self.bot.get_channel(843827757745045555)
        embed=discord.Embed(description = message, color = discord.Colour.random())
        embed.set_author(name="Message From an Anonymous Person")
        await anon_channel.send(embed=embed)
        embe = discord.Embed(title='Message Successfully Sent', description="Message sent successfully in <#900585191771357204>", color=discord.Colour.blurple())
        embe.add_field(name="Jump", value=f"[Jump to Message]({message.jump_url})")
        await ctx.author.send(embed=embe)
        emb = discord.Embed(title='Anonymous Message Log', description='message sent in <#900585191771357204>')
        username = self.bot.get_user(ctx.author.id)
        emb.add_field(name='Username', value=username.name, inline=False)
        emb.add_field(name='ID', value = ctx.author.id, inline=False)
        emb.add_field(name='Time Sent', value=f'{datetime.datetime.utcnow()}', inline=False)
        await log_channel.send(embed=emb)
    
    @anonymous.error
    async def anonymous_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.author.send(f"Please enter a message to send")
    


    @commands.command()
    async def remind(self, ctx, time, *, task):
        def convert(time):
            pos = ['s', 'm', 'h', 'd']

            time_dict = {"s": 1, "m": 60, "h": 3600, "d": 3600*24}

            unit = time[-1]

            if unit not in pos:
                return -1
            try:
                val = int(time[:-1])
            except:
                return -2
        
            return val * time_dict[unit]
        
        converted_time = convert(time)

        if converted_time == -1:
            await ctx.send("You didn't answer the time correctly")
            return

        if converted_time == -2:
            await ctx.send("The time must be a integer")
            return

        await ctx.send(f"Started reminder for **{task}** and will las for **{time}**.")
        await asyncio.sleep(converted_time)
        await ctx.send(f"{ctx.author.mention} your reminder for {task} has finished.")
def setup(bot):
    bot.add_cog(Timely(bot))