import discord
from discord.ext import commands
import random

client = discord.Client()
client = commands.Bot(command_prefix=';')

@client.command()
async def snap(ctx):
    guild = ctx.guild
    if ctx.author is not guild.owner:
        await ctx.send("**{}**, only the guild owner can harness this power.".format(ctx.author.name))
    else:
        those_exempt = [guild.owner, client.user]

        snap_setup = round(guild.member_count / 2)
        snap_list = guild.members

        for safe_user in those_exempt:
            snap_list.remove(safe_user)

        users = random.sample(snap_list, snap_setup)

        for user in users:
            channel = await user.create_dm()
            await channel.send("https://files.catbox.moe/rs5a55.gif")
            await ctx.send("{} has been banned.".format(user.mention))
            await guild.ban(user)
        await ctx.send("{} users banned".format(len(users)))

client.run(token)
