from discord.ext import commands
import discord
import random
import health
import json
import asyncio


intents = discord.Intents.all()
client = commands.Bot(command_prefix='d4v!', intents=intents)



@client.command()
async def ping(ctx):
	await ctx.send(f'Pong! {round(client.latency*1000)} ms')


@client.event
async def on_member_join(member,guild):
	cantstoptime = discord.utils.get(guild.roles, id=816382645964636180),
	await member.add_roles(cantstoptime)



@client.command(aliases=["sf","starfinger"],brief="finger goes brrr")
async def star_finger(ctx,member):
	target = ctx.message.mentions[0]
	user = ctx.author
	starplatinum = discord.utils.get(ctx.guild.roles, id=816244946365186048)
	if not starplatinum in ctx.author.roles:
		return
	await health.changehealth(user=target,add=0,subtract=10)
	await ctx.send(f'{user} used Star Finger on {target}!')


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
	cantstoptime = discord.utils.get(ctx.guild.roles, id=816382645964636180)
	
	stands = [thehand, theworld, starplatinum, silverchariot, crazydiamond]
	
	for x in stands:
		if x in ctx.author.roles:
			await ctx.author.remove_roles(x)
			await ctx.channel.send(f"you have lost {x.name}")
			return
	
	try:
		standwanted = ctx.message.role_mentions[0]
	except IndexError:
		return
	
	if standwanted in stands:
		if standwanted.members == []:
			await ctx.author.add_roles(standwanted)
			await ctx.channel.send(f"You now have {standwanted.name}!")
			if standwanted == theworld or standwanted == starplatinum:
				await ctx.author.remove_roles(cantstoptime)
		else:
			await ctx.channel.send(f"{standwanted.members[0].name} already has {standwanted.name}")

@client.command(aliases=["ts","st","timestop","stoptime","stop_time"],brief="za warudo toki wo tomare")
async def time_stop(ctx):
	channel = ctx.channel
	guild = ctx.guild
	starplatinum = discord.utils.get(ctx.guild.roles, id=816244946365186048)
	theworld = discord.utils.get(ctx.guild.roles, id=816244945580982282)
	cantstoptime = discord.utils.get(ctx.guild.roles, id=816382645964636180)
	if not theworld in ctx.author.roles:
		if not starplatinum in ctx.author.roles:
			return
	if theworld in ctx.author.roles:
		await ctx.channel.set_permissions(guild.get_role(816382645964636180), send_messages=False, read_messages=False)
		await asyncio.sleep(6)
		embed = discord.Embed(title="3 seconds...", colour=discord.Colour(0xdbf353))
		await ctx.channel.send(embed=embed)
		await asyncio.sleep(1)
		embed = discord.Embed(title="2 seconds...", colour=discord.Colour(0xf3ce53))
		await ctx.channel.send(embed=embed)
		await asyncio.sleep(1)
		embed = discord.Embed(title="1 second...", colour=discord.Colour(0xf3564e))
		await ctx.channel.send(embed=embed)
		await asyncio.sleep(1)
		embed = discord.Embed(title="Time resumes!", colour=discord.Colour(0x77140e))
		await ctx.channel.send(embed=embed)
		await ctx.channel.set_permissions(guild.get_role(816382645964636180), send_messages=True, read_messages=True)
	if starplatinum in ctx.author.roles:
		await ctx.channel.set_permissions(guild.get_role(816382645964636180), send_messages=False, read_messages=False)
		await asyncio.sleep(1)
		embed = discord.Embed(title="3 seconds...", colour=discord.Colour(0xdbf353))
		await ctx.channel.send(embed=embed)
		await asyncio.sleep(1)
		embed = discord.Embed(title="2 seconds...", colour=discord.Colour(0xf3ce53))
		await ctx.channel.send(embed=embed)
		await asyncio.sleep(1)
		embed = discord.Embed(title="1 second...", colour=discord.Colour(0xf3564e))
		await ctx.channel.send(embed=embed)
		await asyncio.sleep(1)
		embed = discord.Embed(title="Time resumes!", colour=discord.Colour(0x77140e))
		await ctx.channel.send(embed=embed)
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

	puncher = ctx.author

	if theworld in puncher.roles:
		async for message in ctx.channel.history():
			if(message == ctx.message) or (message.author == ctx.message.author) or (message.author == client.user):
				continue
			else:
				previous_message = message
				punched = previous_message.author
				await health.changehealth(user=punched, add=0, subtract=17)
				attack_embed = discord.Embed(title=f"{puncher.name} punched {punched.name}! MUDA!", colour=discord.Colour(0xffdc00))
				await ctx.channel.send(embed=attack_embed)
				break

	if thehand in puncher.roles:
		async for message in ctx.channel.history():
			if(message == ctx.message) or (message.author == ctx.message.author) or (message.author == client.user):
				continue
			else:
				previous_message = message
				punched = previous_message.author
				await health.changehealth(user=punched, add=0, subtract=15)
				attack_embed = discord.Embed(title=f"{puncher.name} punched {punched.name}! BBVV!", colour=discord.Colour(0x5957db))
				await ctx.channel.send(embed=attack_embed)
				break
	if starplatinum in puncher.roles:
		async for message in ctx.channel.history():
			if(message == ctx.message) or (message.author == ctx.message.author) or (message.author == client.user):
				continue
			else:
				previous_message = message
				punched = previous_message.author
				await health.changehealth(user=punched, add=0, subtract=20)
				attack_embed = discord.Embed(title=f"{puncher.name} punched {punched.name}! ORA!", colour=discord.Colour(0x9b20c2))
				await ctx.channel.send(embed=attack_embed)
				break
	if silverchariot in puncher.roles:
		async for message in ctx.channel.history():
			if(message == ctx.message) or (message.author == ctx.message.author) or (message.author == client.user):
				continue
			else:
				previous_message = message
				punched = previous_message.author
				await health.changehealth(user=punched, add=0, subtract=12)
				attack_embed = discord.Embed(title=f"{puncher.name} attacked {punched.name}!", colour=discord.Colour(0xf5f5f5))
				await ctx.channel.send(embed=attack_embed)
				break
	if crazydiamond in puncher.roles:
		async for message in ctx.channel.history():
			if(message == ctx.message) or (message.author == ctx.message.author) or (message.author == client.user):
				continue
			else:
				previous_message = message
				punched = previous_message.author
				await health.changehealth(user=punched, add=0, subtract=15)
				attack_embed = discord.Embed(title=f"{puncher.name} punched {punched.name}! DORA!", colour=discord.Colour(0xe277d5))
				await ctx.channel.send(embed=attack_embed)
				break




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
