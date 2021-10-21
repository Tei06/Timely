import discord
from discord.ext import commands
from discord.flags import Intents
from dotenv import load_dotenv
import os
import random
load_dotenv()

prefixes = ["t!"]

bot = commands.Bot(command_prefix=prefixes, intents = discord.Intents.all())

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Streaming(name='t!help | be productive when', url='https://www.youtube.com/watch?v=g8jWi6ipSew'))
    print('Connected to bot: {}'.format(bot.user.name))
    print('Bot ID: {}'.format(bot.user.id))

@bot.event
async def on_member_join(member):
    guild = bot.get_guild(840614260833124372)
    channel = guild.get_channel(843642088629338122)
    embed = discord.Embed(title = f"Welcome to the Timely {member.name}!", colour=discord.Colour(0x3b12ef), description = f"{member.mention} We are pleased to have you here! Head over to <#840651124633632819> and <#840724842546593802> to get roles, and started with our community!")
    embed.set_thumbnail(url = member.avatar_url)
    embed.set_image(url = "https://media.tenor.com/images/ad46528ebd6a5bb3cd2b510e0e6f1b79/tenor.gif")
    embed.set_author(name = f"Our {member.guild.member_count}th member has joined")
    await channel.send(embed=embed)
    await channel.send(f"The Timely community greets {member.mention} with the warmest, most sincere welcome. Please enjoy your stay!")
    welcome1 = "**WELCOME TO TIMELY!!** :partying_face: :heartpulse:\n     ↳ Check out #╰»-self-roles  so you can get the best experience out of Timely possible\n     ↳ We're so excited to have you here!"
    welcome2 = "\n\nWant to build self-discipline and work towards the wildest of your dreams? Then you're at the right place!\n"
    welcome3 = "「In Timely, you can:」\n    `⤿`Explore over 50+ channels and 11 VC's (there's something for everyone!)\n    `⤿`:mega: Interact with like-minded students around the world\n"
    welcome4 = "    `⤿`:brain: Learn about faster ways to study\n"
    welcome5 = "    `⤿`Build self-discipline and ***fall in love with being the best version of yourself***"
    links1 = "\n\n**LINKS** :paperclips: : ────────────────────────\n• Instagram: @timely.1 (https://www.instagram.com/timely.1/)\n• Discord: discord.gg/VeddBXds7f\n• Link Tree: linktr.ee/timely1\n\n"
    sincere = "- *Sincerely, Brian & Evelyn* <3"
    msg = welcome1 + welcome2 + welcome3 + welcome4 + welcome5 + links1 + sincere
    await member.send(msg)

@bot.event
async def on_member_remove(member):
  guild = bot.get_guild(840614260833124372)
  channel = guild.get_channel(843827757745045555)
  embed = discord.Embed(title = f"{member.name} has left the server.", description = 'Thanks for being part of our community!', color = discord.Colour(0xf2463c))
  embed.set_thumbnail(url = member.avatar_url)
  await channel.send(embed=embed)


if __name__ == "__main__":
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py") and filename != "__init__.py":
            print(f"loaded: {filename}")
            bot.load_extension(f'cogs.{filename[:-3]}')


@bot.event
async def on_message(message):
        empty_array = []
        modmail_channel = bot.get_channel(896164593825632276)
        if message.author == bot.user:
            return
        if str(message.channel.type) == "private":
            if message.attachments != empty_array:
                files = message.attachments
                await modmail_channel.send("[" + message.author.display_name + f":{message.author.id}" + "]")

                for file in files:
                    await modmail_channel.send(file.url)
            else:
                if message.content.startswith("+modrequest"):
                    await message.author.send(f"please wait patiently, a moderator will be with you shortly")
                    await modmail_channel.send(f"<@&841118156385812521> Modmail Request from User: **[{message.author.display_name}]**\nID: {message.author.id}")
                elif message.content.startswith("t!anonymous"):
                    return
                else:
                    await modmail_channel.send(f"**User: [{message.author.display_name}]**\nID: {message.author.id}" + f"\nMessage: {message.content}")

        elif str(message.channel) == "mod-mail" and message.content.startswith("<"):
            member_object = message.mentions[0]
            if message.attachments != empty_array:
                files = message.attachments
                await member_object.send("[" + message.author.display_name + "]")

                for file in files:
                    await member_object.send(file.url)
            else:
                index = message.content.index(" ")
                string = message.content
                mod_message = string[index:]
                await member_object.send("[" + message.author.display_name + "]" + mod_message)

        await bot.process_commands(message)
@bot.command()
async def status(ctx, *, status):
        activity = discord.Activity(name=f"{status}", type=3)
        await bot.change_presence(status=discord.ActivityType.listening, activity=activity)
        await ctx.send("Bot status succesfully changed")

TOKEN = os.getenv("DISCORD_BOT_TOKEN")
bot.run(TOKEN)