from discord.ext import commands
import discord
import random
import health

intents = discord.Intents.all()
client = commands.Bot(command_prefix='d4v!', intents=intents)

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

	stands = [thehand, theworld, starplatinum, silverchariot]

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

# @commands.cooldown(1, getcooldown(), commands.BucketType.user)
@client.command(aliases=["p"],brief="ORAAAA!")
async def punch(ctx):

	theworld = discord.utils.get(ctx.guild.roles, id=816244945580982282)
	thehand = discord.utils.get(ctx.guild.roles, id=816244947761102850)
	starplatinum = discord.utils.get(ctx.guild.roles, id=816244946365186048)
	silverchariot = discord.utils.get(ctx.guild.roles, id=816244947224100864)

	stands = [thehand, theworld, starplatinum, silverchariot]

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

	await ctx.channel.send(f"{puncher.name} punched {punched}")    

client.run(token)
