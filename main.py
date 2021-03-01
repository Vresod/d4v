import discord
import random
from discord.ext import commands

client = commands.Bot(command_prefix='d4v!')


client = discord.Client()


client.run('ODE0ODM2NTQ4NzMzNzYzNjQ1.YDjprA.AormX6srsNBN4DN1igr1CXUkjvw')


@client.event
async def on_ready():
	print('Dojyan!')


@client.command
async def reserve(message, *, stand):
        channel = message.channel
        if stand == 'The World':
        	await channel.send('The World')
        if stand == 'Star Platinum':
        	await channel.send('Star Platinum')
        if stand == 'Silver Chariot':
        	await channel.send('Silver Chariot')

@client.command()
async def ping(ctx):
	await ctx.send(f'Pong! {round(client.latency*1000)}ms')


#@client.event()
#async def on_message(ctx):
#		the_world = discord.utils.get(ctx.guild.roles, the_world.id==815225512996634635),
#		guild = message.guild
#			for member in guild.members:
#				await ctx.author.add_roles(the_world)



#### CREARE UN RUOLO PER GLI STAND QUANDO IL BOT JOINA IL SERVER
#@client.event
#async def on_guild_join(guild):
#		await guild.create_role(name="The World",colour=discord.Colour(0xFFDC00))
#		await guild.create_role(name="Star Platinum",colour=discord.Colour(0x9B20C2))
#		await guild.create_role(name="Silver Chariot",colour=discord.Colour(0xDBDBDB))
#		await guild.create_role(name="The Hand",colour=discord.Colour(0x1727A9))




##### RISPOSTA RANDOM
#@client.command(aliases=['8ball','8b'])
#async def _8ball(ctx,*,question):
#	responses = ['Yes','Of Course',
#				 '100% Yes',
#				 'Uh... I dont actually have an answer for that...',
#				 'Like thats ever gonna happen',
#				 'No U','No','False','Absolutely not!']
#	await ctx.send(f'**Question: {question}**\n*Answer:{random.choice(responses)}*')






#@client.command()
#@commands.has_permission(delete_messages=True)
#async def clear(ctx,amount=2):
#	await ctx.channel.purge(limit=amount)

#@client.command()
#@commands.has_permission(kick_members=True)
#async def kick(ctx,member:discord.Member,*,reason=None):
#	await member.kick(reason=reason)

#@client.command()
#@commands.has_permission(ban_members=True)
#async def ban(ctx,member:discord.Member,*,reason=None):
#	await member.ban(reason=reason)

#@client.command()
#@commands.has_permission(ban_members=True)
#async def unban(ctx,*,member):
#	banned_users = await ctx.guild.bans()
#	member_name,member_discriminator = member.split('#')

#	for ban_entry in banned_users:
#		user = ban_entry.user
#		if (user.name,user.discriminator) == (member_name,member_discriminator):
#			await ctx.guild.unban(user)
#			await ctx.send(f'{user.name}#{user.discriminator} has been unbanned')
#			return





