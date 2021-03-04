from discord.ext import commands
import discord
import random
import health
import json
import asyncio






intents = discord.Intents.all()
client = commands.Bot(command_prefix='d4v!', intents=intents)

@client.event
async def on_member_join(member):
	cantstoptime = discord.utils.get(guild.roles, id=816382645964636180),
	await member.add_roles(cantstoptime)



with open("tokenfile", "r") as tokenfile:
	token=tokenfile.read()

@client.event
async def on_ready():
	print('Dojyan!')

@client.command(aliases=["r"],brief="reserve a stand")
async def reserve(ctx):
	theworld = discord.utils.get(ctx.guild.roles, id=816244945580982282)
	thehand = discord.utils.get(ctx.guild.roles, id=816244947761102850)
	starplatinum = discord.utils.get(ctx.guild.roles, id=816244946365186048)
	silverchariot = discord.utils.get(ctx.guild.roles, id=816244947224100864)
	crazydiamond = discord.utils.get(ctx.guild.roles, id=816602875014676480)
	stands = [thehand, theworld, starplatinum, silverchariot, crazydiamond]
	try:
		standwanted = ctx.message.role_mentions[0]
	except IndexError:
		return
	if standwanted in stands:
		for x in stands:
			if x in ctx.author.roles:
				await ctx.channel.send(f"you already have {x.name}")
				return
		if standwanted.members == []:
			await ctx.author.add_roles(standwanted)
			await ctx.channel.send(f"you now have {standwanted.name}!")
		else:
			await ctx.channel.send(f"{standwanted.members[0].name} already has {standwanted.name}")

@client.command(aliases=["ts","st","timestop","stoptime","stop_time"],brief="za warudo toki wo tomare")
async def time_stop(ctx):
	channel = ctx.channel
	guild = ctx.guild
	theworld = discord.utils.get(ctx.guild.roles, id=816244945580982282)
	cantstoptime = discord.utils.get(ctx.guild.roles, id=816382645964636180)
	if not theworld in ctx.author.roles:
		return
	await ctx.channel.set_permissions(guild.get_role(816382645964636180), send_messages=False, read_messages=False)
	await asyncio.sleep(9)
	await ctx.channel.set_permissions(guild.get_role(816382645964636180), send_messages=True, read_messages=True)






#def getcooldown(): 
#	
#	joe = discord.utils.get(client.guilds, id=814836159821250661)
#	
#	for x in joe.channels:
#		ctx = x.history[0]
#
#		if not ctx.content.startswith("d4v!"):
#			continue
#
#		if theworld in ctx.author.roles:
#			return 3
#		elif thehand in ctx.author.roles:
#			return 4
#		elif starplatinum in ctx.author.roles:
#			return 3
#		elif silverchariot in ctx.author.roles:
#			return 1
#		elif crazydiamond in ctx.author.roles:
#			return 2

# @commands.cooldown(1, getcooldown(), commands.BucketType.user)
@client.command(aliases=["p"],brief="ORAAAA!")
async def punch(ctx):

	theworld = discord.utils.get(ctx.guild.roles, id=816244945580982282)
	thehand = discord.utils.get(ctx.guild.roles, id=816244947761102850)
	starplatinum = discord.utils.get(ctx.guild.roles, id=816244946365186048)
	silverchariot = discord.utils.get(ctx.guild.roles, id=816244947224100864)
	crazydiamond = discord.utils.get(ctx.guild.roles, id=816602875014676480)

	stands = [thehand, theworld, starplatinum, silverchariot, crazydiamond]

	punched = ctx.message.mentions[0]
	puncher = ctx.author

	if theworld in puncher.roles:
		await health.changehealth(user=punched, add=0, subtract=17)
	elif thehand in puncher.roles:
		await health.changehealth(user=punched, add=0, subtract=15)
	elif starplatinum in puncher.roles:
		await health.changehealth(user=punched, add=0, subtract=20)
	elif silverchariot in puncher.roles:
		await health.changehealth(user=punched, add=0, subtract=10)
	elif crazydiamond in puncher.roles:
		await health.changehealth(user=punched, add=0, subtract=14)

	await ctx.channel.send(f"{puncher.name} punched {punched.name}")    

@client.command(aliases=["i"],brief="get info on a user's health and stand")
async def info(ctx):

	with open("health.json", "rt") as healthraw: # opens health.json
		health = json.loads(healthraw.read()) # sets the health varible to the contents of health.json

	theworld = discord.utils.get(ctx.guild.roles, id=816244945580982282)
	thehand = discord.utils.get(ctx.guild.roles, id=816244947761102850)
	starplatinum = discord.utils.get(ctx.guild.roles, id=816244946365186048)
	silverchariot = discord.utils.get(ctx.guild.roles, id=816244947224100864)
	crazydiamond = discord.utils.get(ctx.guild.roles, id=816602875014676480)

	stands = [thehand, theworld, starplatinum, silverchariot, silverchariot]

	if ctx.message.mentions == []:
		InfoOn = ctx.author
	else:
		InfoOn = ctx.message.mentions[0]

	for x in stands:
		if x in InfoOn.roles:
			try:
				await ctx.message.channel.send(f"{InfoOn} has `{health[str(InfoOn.id)]}` health\n{InfoOn}'s stand is {x.name}")
			except KeyError:
				await ctx.message.channel.send(f"{InfoOn}'s stand is {x.name}")
			return

client.run(token)
