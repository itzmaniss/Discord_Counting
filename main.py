import os, time
import discord
from discord.ext import commands
from discord.utils import get
import helper
import glob

with open("token.txt") as f:
    TOKEN = f.readline()


client = commands.Bot(command_prefix="%")
client.remove_command("help")

@client.event
async def on_ready():
    print("We are online")
    
@client.event
async def on_message(message):
    await client.process_commands(message)
    if message.author.bot == True:
        return
    else:
        if (os.getcwd() + "/" + str(message.guild.id) + ".db") not in glob.glob(os.getcwd()+"/*.db"):
            helper.init_db(str(message.guild.id), message.channel.id)
            await (message.channel).send("Initialised DB.")
        else:
            if message.channel.id != helper.count_channel(str(message.guild.id)):
                return
            res = helper.count(message.content, str(message.guild.id), int(message.author.id)) 
            if res[0] == 69:
                return
            elif res[0] == False:
                await message.add_reaction("\U0000274C")
                await (message.channel).send(f"<@{int(message.author.id)}> messed up! Count restarts at 1") 
                await message.author.add_roles(get(message.guild.roles, id=int(helper.fail_role(str(message.guild.id)))),"You can't even count",True)
            elif res[1] == False:
                await message.add_reaction("\U00002705")
            else:
                await message.add_reaction("\U00002611")
    
@client.command()
async def help(ctx):
    reply = discord.Embed(title="The Better Counting Bot")
    reply.add_field(name="__**Commands**__", value="Admins only! (other than help of course)", inline=False)
    reply.add_field(name="%help", value="Sends help message", inline=False)
    reply.add_field(name="%set_channel", value="Set counting channel, defaults to all", inline=False)
    reply.add_field(name="%set_fail_role", value="Set role given to person who counts wrongly", inline=False)
    reply.add_field(name="%user_stats [@user]", value="Gets user's stats, if no user is mentioned, it gets the sender's stats", inline=False)
    reply.add_field(name="%set_base", value="Set the base of the number system to be used. Default Base 10. (Work in progress)", inline=False)
    reply.add_field(name="%top", value="Top counters", inline=False)
    reply.add_field(name="%prime_top", value="Top prime number counters", inline=False)
    reply.add_field(name="%fail_top", value="Top failures", inline=False)
    reply.add_field(name="%next_prime", value="Returns the next prime number", inline=False)
    reply.add_field(name="__**Counting**__", value="Green tick - Correct \n Blue tick - Correct and prime number \n You cannot count consecutively, even after you mess up. ", inline=False)
    reply.add_field(name="__**Special Operators**__", value="Python math library functions and numpy library functions. For numpy, add 'numpy' before the function, e.g. numpycumsum", inline=False)
    await ctx.send(embed=reply)

@client.command()
async def next_prime(ctx):
    await ctx.send(f"The next prime number is {helper.next_prime(str(ctx.message.guild.id))}")
    
@client.command()
async def top(ctx):
    top_math = helper.top(str(ctx.message.guild.id))
    reply = discord.Embed(title="Top Counters!")
    for i in top_math:
        reply.add_field(name=f"{client.get_user(i[1])}", value=f"{i[0]} Counts", inline=False)
    await ctx.send(embed=reply)
    
@client.command()
async def prime_top(ctx):
    prime_math = helper.prime_top(str(ctx.message.guild.id))
    reply = discord.Embed(title="Top Prime Counters!")
    for i in prime_math:
        reply.add_field(name=f"<@!{i[1]}>", value=f"{i[0]} Prime Numbers", inline=False)
    await ctx.send(embed=reply)
    
@client.command()
async def fail_top(ctx):
    top_fail = helper.top_fail(str(ctx.message.guild.id))
    reply = discord.Embed(title="Top Failures!")
    for i in top_fail:
        reply.add_field(name=f"<@!{i[1]}>", value=f"{i[0]} Fails", inline=False)
    await ctx.send(embed=reply)
    

    
@client.command()
async def set_channel(ctx):
    prev = helper.count_channel(str(ctx.message.guild.id))
    if ctx.message.channel.id != prev:
        await ctx.send(f"Please run this command in the current counting channel, <#{prev}>.")
        return
    elif ctx.message.author.permissions_in(ctx.message.channel).administrator != True:
        await ctx.send("Your're not an Admin.")
        return
    try: 
        (ctx.message).raw_channel_mentions[0]
    except IndexError:
        await ctx.send("Mention a channel asshole.")
    else:
        if ctx.message.channel_mentions[0] not in ctx.guild.text_channels:
            await ctx.send("That's not a valid channel idiot.")
            return
        else:
            helper.change_count_channel(str(ctx.message.guild.id), (ctx.message).raw_channel_mentions[0])
            await ctx.send(f"Changed counting channel from <#{prev}> to <#{(ctx.message).raw_channel_mentions[0]}>")
        
@client.command()
async def set_fail_role(ctx):
    prev = helper.count_channel(str(ctx.message.guild.id))
    if ctx.message.channel.id != prev:
        await ctx.send(f"Please run this command in the current counting channel, <#{prev}>.")
        return
    elif ctx.message.author.permissions_in(ctx.message.channel).administrator != True:
        await ctx.send("Your're not an Admin.")
        return
    
    try:
        ctx.message.raw_role_mentions[0]
    except IndexError:
        await ctx.send("Mention a role asshole.")
    else:
        helper.change_fail_role(str(ctx.message.guild.id), ctx.message.raw_role_mentions[0])
        await ctx.send(f"Changed fail role to <@{ctx.message.raw_role_mentions[0]}>")

@client.command()
async def set_base(ctx):
    await ctx.send("Not implemented yet, Base 10 default applies.")
    
@client.command()
async def user_stats(ctx):
    try:
        user = (ctx.message.mentions)[0]
    except IndexError:
        user = ctx.message.author
    stats = helper.user_stats(str(ctx.message.guild.id), user.id)
    reply = discord.Embed(title=f"{user.name}#{ctx.message.author.discriminator} Stats")
    reply.add_field(name="Last Number Counted", value=f"{stats[0]}", inline=False)
    reply.add_field(name="Number of Counts", value=f"{stats[1]}", inline=False)
    reply.add_field(name="Number of Fails", value=f"{stats[2]}", inline=False)
    reply.add_field(name="Highest Count", value=f"{stats[3]}", inline=False)
    reply.add_field(name="Last Failed Number", value=f"{stats[4]}", inline=False)
    reply.add_field(name="Last Failure Date", value=f"{stats[5]}", inline=False)
    reply.add_field(name="Number of Primes Counted", value=f"{stats[6]}", inline=False)
    await ctx.send(embed=reply)
    
client.run(TOKEN)