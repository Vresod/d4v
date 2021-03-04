from discord.ext import commands
import discord
import random
from health import *
import json

intents = discord.Intents.all()
client = commands.Bot(command_prefix='d4v!', intents=intents)

with open("tokenfile", "r") as tokenfile:
	token=tokenfile.read()

@client.event
async def on_ready():
	print('Dojyan!')

@client.command(aliases=["r"],brief="reserve a stand")
async def reserve(ctx, mentionrole):

	theworld = discord.utils.get(ctx.guild.roles, id=816244945580982282)
	thehand = discord.utils.get(ctx.guild.roles, id=816244947761102850)
	starplatinum = discord.utils.get(ctx.guild.roles, id=816244946365186048)
	silverchariot = discord.utils.get(ctx.guild.roles, id=816244947224100864)
	crazydiamond = discord.utils.get(ctx.guild.roles, id=816602875014676480)
	NoTimeStop = discord.utils.get(ctx.guild.roles, id=816382645964636180)

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
			if standwanted == theworld or standwanted == starplatinum:
				await ctx.author.remove_roles(NoTimeStop)
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
#		elif crazydiamond in ctx.author.roles:
#			return 2

# @commands.cooldown(1, getcooldown(), commands.BucketType.user)
@client.command(aliases=["p"],brief="ORAAAA!")
async def punch(ctx, mentionuser):

	theworld = discord.utils.get(ctx.guild.roles, id=816244945580982282)
	thehand = discord.utils.get(ctx.guild.roles, id=816244947761102850)
	starplatinum = discord.utils.get(ctx.guild.roles, id=816244946365186048)
	silverchariot = discord.utils.get(ctx.guild.roles, id=816244947224100864)
	crazydiamond = discord.utils.get(ctx.guild.roles, id=816602875014676480)

	stands = [thehand, theworld, starplatinum, silverchariot, crazydiamond]

	punched = ctx.message.mentions[0]
	puncher = ctx.author

	if theworld in puncher.roles:
		await changehealth(user=punched, add=0, subtract=17)
	elif thehand in puncher.roles:
		await changehealth(user=punched, add=0, subtract=15)
	elif starplatinum in puncher.roles:
		await changehealth(user=punched, add=0, subtract=20)
	elif silverchariot in puncher.roles:
		await changehealth(user=punched, add=0, subtract=10)
	elif crazydiamond in puncher.roles:
		await changehealth(user=punched, add=0, subtract=14)

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

	stands = [thehand, theworld, starplatinum, silverchariot, crazydiamond]

	if ctx.message.mentions == []:
		InfoOn = ctx.author
	else:
		InfoOn = ctx.message.mentions[0]

	for x in stands:
		if x in InfoOn.roles:
			InfoOnStand = x
			break
		else:
			InfoOnStand = None
	
	try:
		embed = discord.Embed(title=f"{InfoOn}'s Info", colour=discord.Colour(0xabe05f), description=f"Stand: {InfoOnStand}\nHealth: {health[str(InfoOn.id)]}")
	except KeyError:
		await changehealth(user=InfoOn, add=0, subtract=0)
		with open("health.json", "rt") as healthraw: # reopens health.json
			health = json.loads(healthraw.read()) # sets the health varible to the contents of health.json
		embed = discord.Embed(title=f"{InfoOn}'s Info", colour=discord.Colour(0xabe05f), description=f"Stand: {InfoOnStand}\nHealth: {health[str(InfoOn.id)]}")

		
	await ctx.message.channel.send(embed=embed)



@client.event
async def on_command_error(ctx:commands.Context, exception):
    embed = discord.Embed(color=discord.Color.red())
    if type(exception) is commands.errors.MissingRequiredArgument:
        embed.title = "You forgot an argument"
        embed.description = f"The syntax to `{client.command_prefix}{ctx.command.name}` is `{client.command_prefix}{ctx.command.name} {ctx.command.signature}`."
        await ctx.send(embed=embed)
    elif type(exception) is commands.CommandNotFound:
        embed.title = "Invalid command"
        embed.description = f"The command you just tried to use is invalid. Use `{client.command_prefix}help` to see all commands."
        await ctx.send(embed=embed)
    else:
        print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
        traceback.print_exception(type(exception), exception, exception.__traceback__, file=sys.stderr)

@client.event
async def on_member_join(member):
	
	NoTimeStop = discord.utils.get(member.guild.roles, id=816382645964636180)

	await member.add_roles(NoTimeStop)

client.run(token)