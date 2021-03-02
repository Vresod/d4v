import discord
import random
from discord.ext import commands,tasks
from discord.utils import get

intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix='d4v!',intents=intents)



@client.event
async def on_guild_join(guild):
	    await guild.create_role(name="The World",colour=discord.Colour(0xFFDC00))
	    await guild.create_role(name="Star Platinum",colour=discord.Colour(0x9B20C2))
	    await guild.create_role(name="Silver Chariot",colour=discord.Colour(0xDBDBDB))
	    await guild.create_role(name="The Hand",colour=discord.Colour(0x5957db))



@client.event
async def on_ready():
	print('Dojyan!')

#@client.command(aliases=['ts','timestop'])
#@commands.has_role(name="The World")
#async def time_stop(ctx):
#	await ctx.send(f'The World! Time has stopped!')


@client.command()
async def reserve(ctx, *, stand: discord.Role):
		if not stand.members:
			if stand.name == "The World":
				await ctx.author.add_roles(stand)
			if stand.name == "Star Platinum":
				await ctx.author.add_roles(stand)
			if stand.name == "Silver Chariot":
				await ctx.author.add_roles(stand)
			if stand.name == "The Hand":
				await ctx.author.add_roles(stand)
				
@client.command()
async def ping(ctx):
	await ctx.send(f'Pong! {round(client.latency*1000)}ms')


#@client.event()
#async def on_message(ctx):
#       the_world = discord.utils.get(ctx.guild.roles, the_world.id==815225512996634635),
#       guild = message.guild
#           for member in guild.members:
#               await ctx.author.add_roles(the_world)









##### RISPOSTA RANDOM
#@client.command(aliases=['8ball','8b'])
#async def _8ball(ctx,*,question):
#   responses = ['Yes','Of Course',
#                '100% Yes',
#                'Uh... I dont actually have an answer for that...',
#                'Like thats ever gonna happen',
#                'No U','No','False','Absolutely not!']
#   await ctx.send(f'**Question: {question}**\n*Answer:{random.choice(responses)}*')






#@client.command()
#@commands.has_permission(delete_messages=True)
#async def clear(ctx,amount=2):
#   await ctx.channel.purge(limit=amount)

#@client.command()
#@commands.has_permission(kick_members=True)
#async def kick(ctx,member:discord.Member,*,reason=None):
#   await member.kick(reason=reason)

#@client.command()
#@commands.has_permission(ban_members=True)
#async def ban(ctx,member:discord.Member,*,reason=None):
#   await member.ban(reason=reason)

#@client.command()
#@commands.has_permission(ban_members=True)
#async def unban(ctx,*,member):
#   banned_users = await ctx.guild.bans()
#   member_name,member_discriminator = member.split('#')

#   for ban_entry in banned_users:
#       user = ban_entry.user
#       if (user.name,user.discriminator) == (member_name,member_discriminator):
#           await ctx.guild.unban(user)
#           await ctx.send(f'{user.name}#{user.discriminator} has been unbanned')
#           return






client.run('ODE0ODM2NTQ4NzMzNzYzNjQ1.YDjprA.AormX6srsNBN4DN1igr1CXUkjvw')