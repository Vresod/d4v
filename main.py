import time
from discord.ext import commands
import discord
import random
import json
import asyncio
from extra import *

intents = discord.Intents.all()
client = commands.Bot(command_prefix='d4v!', intents=intents, help_command=MyHelpCommand())

with open("tokenfile", "r") as tokenfile:
	token=tokenfile.read()



@client.event
async def on_ready():
    print('Dojyan!')

@client.event
async def on_member_join(member):
    cantstoptime = discord.utils.get(member.guild.roles, id=816382645964636180)
    await member.add_roles(cantstoptime)



@client.command(aliases=["kc","kingcrimson","itjustworks"])
@commands.cooldown(rate=1,per=25,type=commands.BucketType.user)
async def king_crimson(ctx):
	kingcrimson = discord.utils.get(ctx.guild.roles, id=817441099173199923)
	if kingcrimson in ctx.author.roles:
		kc_list = []
		kc_ability = ""
		await ctx.message.delete()
		kc_embed = discord.Embed(title="King Crimson activated!", colour=discord.Colour(0xb90d0d))
		await ctx.author.send(embed=kc_embed)
		kc_ability = 1
		await asyncio.sleep(10)
		kc_ability = 0
		kc_embed = discord.Embed(title="Time has skipped!", colour=discord.Colour(0xb90d0d))
		await ctx.author.send(embed=kc_embed)
		await ctx.channel.purge(after=ctx.message)

@client.command(aliases=["mrp","mrpresident","mp"])
@commands.cooldown(rate=2,per=5,type=commands.BucketType.user)
async def mr_president(ctx):
	mrpresident = discord.utils.get(ctx.guild.roles, id=817885472734838795)
	mrpresident_inroom = discord.utils.get(ctx.guild.roles, id=817885610760208444)
	if mrpresident in ctx.author.roles:
		if mrpresident_inroom in ctx.author.roles:
			mrpresident_embed = discord.Embed(title=f"{ctx.author.display_name} left Mr. President!", colour=discord.Colour(0x2f964d))
			await ctx.channel.send(embed=mrpresident_embed)
			await ctx.author.remove_roles(mrpresident_inroom)
			return
		else mrpresident_inroom in ctx.author.roles:
			mrpresident_embed = discord.Embed(title=f"{ctx.author.display_name} entered Mr. President!", colour=discord.Colour(0x2f964d))
			await ctx.channel.send(embed=mrpresident_embed)
			await ctx.author.add_roles(mrpresident_inroom)
			return


@client.command(aliases=["pi"],brief="get bot latency")
async def ping(ctx):
	await ctx.send(f'Pong! {round(client.latency*1000)} ms')

@client.command(aliases=["sf","starfinger"],brief="finger goes brrr")
async def star_finger(ctx,member):
	if starplatinum in ctx.author.roles:
		target = ctx.message.mentions[0]
		user = ctx.author
		starplatinum = discord.utils.get(ctx.guild.roles, id=816244946365186048)
	
		await changehealth(user=target,add=0,subtract=10)
		finger_embed = discord.Embed(title=f"{user.display_name} used Star Finger on {target.display_name}!", colour=discord.Colour(0x9b20c2))
		await ctx.channel.send(embed=finger_embed)

@client.command(aliases=["r"],brief="reserve a stand")
async def reserve(ctx):
	if ctx.author.id == 600027585094877184:
		await ctx.send(f'Mi dispiace ma sei un po troppo stupido per usare questo Bot, torna quando sarai un po piu intelligente.')
		return
	theworld = discord.utils.get(ctx.guild.roles, id=816244945580982282)
	thehand = discord.utils.get(ctx.guild.roles, id=816244947761102850)
	starplatinum = discord.utils.get(ctx.guild.roles, id=816244946365186048)
	silverchariot = discord.utils.get(ctx.guild.roles, id=816244947224100864)
	crazydiamond = discord.utils.get(ctx.guild.roles, id=816602875014676480)
	kingcrimson = discord.utils.get(ctx.guild.roles, id=817441099173199923)
	mrpresident = discord.utils.get(ctx.guild.roles, id=817885472734838795)
	cantstoptime = discord.utils.get(ctx.guild.roles, id=816382645964636180)
	heavensdoor = discord.utils.get(ctx.guild.roles, id=818585440352469073)
	killerqueen = discord.utils.get(ctx.guild.roles, id=819249703291322450)
	

	stands = [thehand, theworld, starplatinum, silverchariot, crazydiamond, kingcrimson, mrpresident, heavensdoor, killerqueen]
	for x in stands:
		if x in ctx.author.roles:
			time_embed = 
			await ctx.channel.send(embed=time_embed)
			await ctx.author.add_roles(cantstoptime)
			await ctx.author.remove_roles(x)
			return
	try:
		standwanted = ctx.message.role_mentions[0]
	except IndexError:
		return

	if standwanted in stands:
		if standwanted.members == []:
			if standwanted == theworld or standwanted == starplatinum:
				await ctx.author.remove_roles(cantstoptime)
			await ctx.author.add_roles(standwanted)
			time_embed = discord.Embed(title=f"You now have {standwanted.name}", colour=discord.Colour(0xc5f164))
			await ctx.channel.send(embed=time_embed)
		else:
			stand_embed = discord.Embed(title=f"{standwanted.members[0].display_name} already has {standwanted.name}", colour=discord.Colour(0xf3564e))

@client.command(aliases=["ts","st","timestop","stoptime","stop_time"],brief="za warudo toki wo tomare")
@commands.cooldown(rate=1, per=20, type=commands.BucketType.user)
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
		time_embed = discord.Embed(title="Time stopped!", colour=discord.Colour(0x7bf164))
		await ctx.channel.send(embed=time_embed)
		await ctx.channel.set_permissions(guild.get_role(816382645964636180), send_messages=False, read_messages=False)
		await asyncio.sleep(6)
		time_embed = discord.Embed(title="3 seconds...", colour=discord.Colour(0xc5f164))
		await ctx.channel.send(embed=time_embed)
		await asyncio.sleep(1)
		time_embed = discord.Embed(title="2 seconds...", colour=discord.Colour(0xf3ce53))
		await ctx.channel.send(embed=time_embed)
		await asyncio.sleep(1)
		time_embed = discord.Embed(title="1 second...", colour=discord.Colour(0xf3564e))
		await ctx.channel.send(embed=time_embed)
		await asyncio.sleep(1)
		time_embed = discord.Embed(title="Time resumes!", colour=discord.Colour(0x77140e))
		await ctx.channel.send(embed=time_embed)
		await ctx.channel.set_permissions(guild.get_role(816382645964636180), send_messages=True, read_messages=True)
	if starplatinum in ctx.author.roles:
		time_embed = discord.Embed(title="Time stopped!", colour=discord.Colour(0x7bf164))
		await ctx.channel.send(embed=time_embed)
		await ctx.channel.set_permissions(guild.get_role(816382645964636180), send_messages=False, read_messages=False)
		await asyncio.sleep(1)
		time_embed = discord.Embed(title="3 seconds...", colour=discord.Colour(0xc5f164))
		await ctx.channel.send(embed=time_embed)
		await asyncio.sleep(1)
		time_embed = discord.Embed(title="2 seconds...", colour=discord.Colour(0xf3ce53))
		await ctx.channel.send(embed=time_embed)
		await asyncio.sleep(1)
		time_embed = discord.Embed(title="1 second...", colour=discord.Colour(0xf3564e))
		await ctx.channel.send(embed=time_embed)
		await asyncio.sleep(1)
		time_embed = discord.Embed(title="Time resumes!", colour=discord.Colour(0x77140e))
		await ctx.channel.send(embed=time_embed)
		await ctx.channel.set_permissions(guild.get_role(816382645964636180), send_messages=True, read_messages=True)

kq_list = []
@client.command(aliases=["p"],brief="ORAAAA!")
async def punch(ctx):

	theworld = discord.utils.get(ctx.guild.roles, id=816244945580982282)
	thehand = discord.utils.get(ctx.guild.roles, id=816244947761102850)
	starplatinum = discord.utils.get(ctx.guild.roles, id=816244946365186048)
	silverchariot = discord.utils.get(ctx.guild.roles, id=816244947224100864)
	crazydiamond = discord.utils.get(ctx.guild.roles, id=816602875014676480)
	kingcrimson = discord.utils.get(ctx.guild.roles, id=817441099173199923)
	mrpresident = discord.utils.get(ctx.guild.roles, id=817885472734838795)
	mrpresident_inroom = discord.utils.get(ctx.guild.roles, id=817885610760208444)
	heavensdoor = discord.utils.get(ctx.guild.roles, id=818585440352469073)
	hd_3 = discord.utils.get(ctx.guild.roles, id=818588024824659969)
	killerqueen = discord.utils.get(ctx.guild.roles, id=819249703291322450)

	stands = [thehand, theworld, starplatinum, silverchariot, crazydiamond, kingcrimson, mrpresident, heavensdoor, killerqueen]

	puncher = ctx.author

	if theworld in puncher.roles:
		async for message in ctx.channel.history():
			if(message == ctx.message) or (message.author == ctx.message.author) or (message.author == client.user):
				continue
			else:
				previous_message = message
				punched = previous_message.author
				await changehealth(user=punched, add=0, subtract=17)
				attack_embed = discord.Embed(title=f"{puncher.display_name} punched {punched.display_name}! MUDA!", colour=discord.Colour(0xffdc00))
				await ctx.channel.send(embed=attack_embed)
				break

	if thehand in puncher.roles:
		async for message in ctx.channel.history():
			if(message == ctx.message) or (message.author == ctx.message.author) or (message.author == client.user):
				continue
			else:
				previous_message = message
				punched = previous_message.author
				await changehealth(user=punched, add=0, subtract=15)
				attack_embed = discord.Embed(title=f"{puncher.display_name} punched {punched.display_name}! BBVV!", colour=discord.Colour(0x5957db))
				await ctx.channel.send(embed=attack_embed)
				break
	if starplatinum in puncher.roles:
		async for message in ctx.channel.history():
			if(message == ctx.message) or (message.author == ctx.message.author) or (message.author == client.user):
				continue
			else:
				previous_message = message
				punched = previous_message.author
				await changehealth(user=punched, add=0, subtract=20)
				attack_embed = discord.Embed(title=f"{puncher.display_name} punched {punched.display_name}! ORA!", colour=discord.Colour(0x9b20c2))
				await ctx.channel.send(embed=attack_embed)
				break
	if silverchariot in puncher.roles:
		async for message in ctx.channel.history():
			if(message == ctx.message) or (message.author == ctx.message.author) or (message.author == client.user):
				continue
			else:
				previous_message = message
				punched = previous_message.author
				await changehealth(user=punched, add=0, subtract=12)
				attack_embed = discord.Embed(title=f"{puncher.display_name} attacked {punched.display_name}!", colour=discord.Colour(0xf5f5f5))
				await ctx.channel.send(embed=attack_embed)
				break
	if crazydiamond in puncher.roles:
		async for message in ctx.channel.history():
			if(message == ctx.message) or (message.author == ctx.message.author) or (message.author == client.user):
				continue
			else:
				previous_message = message
				punched = previous_message.author
				await changehealth(user=punched, add=0, subtract=15)
				attack_embed = discord.Embed(title=f"{puncher.display_name} punched {punched.display_name}! DORA!", colour=discord.Colour(0xe277d5))
				await ctx.channel.send(embed=attack_embed)
				break
	if kingcrimson in puncher.roles:
		async for message in ctx.channel.history():
			if(message == ctx.message) or (message.author == ctx.message.author) or (message.author == client.user):
				continue
			else:
				previous_message = message
				punched = previous_message.author
				await changehealth(user=punched, add=0, subtract=14)
				attack_embed = discord.Embed(title=f"{puncher.display_name} neck chopped {punched.display_name}! WRYA!", colour=discord.Colour(0xb90d0d))
				await ctx.channel.send(embed=attack_embed)
				break
	if mrpresident in puncher.roles:
		async for message in ctx.channel.history():
			if(message == ctx.message) or (message.author == ctx.message.author) or (message.author == client.user):
				continue
			else:
				previous_message = message
				punched = previous_message.author
				await changehealth(user=punched, add=0, subtract=10)
				attack_embed = discord.Embed(title=f"{puncher.display_name} punched {punched.display_name}, now they are both inside Mr. President!", colour=discord.Colour(0x2f964d))
				await ctx.channel.send(embed=attack_embed)
				await punched.add_roles(mrpresident_inroom)
				await ctx.author.add_roles(mrpresident_inroom)
				await asyncio.sleep(15)
				attack_embed = discord.Embed(title=f"{puncher.display_name} and {punched.display_name} left Mr. President!", colour=discord.Colour(0x2f964d))
				await ctx.channel.send(embed=attack_embed)
				await punched.remove_roles(mrpresident_inroom)
				await ctx.author.remove_roles(mrpresident_inroom)
				break
	if heavensdoor in puncher.roles:
		async for message in ctx.channel.history():
			if(message == ctx.message) or (message.author == ctx.message.author) or (message.author == client.user):
				continue
			else:
				previous_message = message
				punched = previous_message.author
				await changehealth(user=punched, add=0, subtract=10)
				attack_embed = discord.Embed(title=f"{puncher.display_name} punched {punched.display_name}!", colour=discord.Colour(0xfff247))
				await ctx.channel.send(embed=attack_embed)
				break
	if killerqueen in puncher.roles:
		async for message in ctx.channel.history():
			if(message == ctx.message) or (message.author == ctx.message.author) or (message.author == client.user):
				continue
			else:
				if kq_list == []:
					previous_message = message
					punched = previous_message.author
					attack_embed = discord.Embed(title=f"{puncher.display_name} turned {punched.display_name}'s message into a bomb, use the punch again to detonate", colour=discord.Colour(0xdba4d3))
					await ctx.channel.send(embed=attack_embed)
					kq_list.append(previous_message)
					await previous_message.add_reaction("<a:KillerQueenClick:819250902925180989>")
					break
				if not kq_list == []:
					await message.delete()
					kq_list.pop(0)
					kq_embed = discord.Embed(title=f"Bomb Detonated!", colour=discord.Colour(0xdba4d3))
					await ctx.channel.send(embed=kq_embed)
					kq_embed2 = discord.Embed(title=f"You detonated {punched.display_name}'s message dealing 30 damage", colour=discord.Colour(0xdba4d3))
					await ctx.author.send(embed=kq_embed2)

@client.command(aliases=["b"],brief="ORA ORA ORA ORA ORA!")
async def barrage(ctx):

	theworld = discord.utils.get(ctx.guild.roles, id=816244945580982282)
	thehand = discord.utils.get(ctx.guild.roles, id=816244947761102850)
	starplatinum = discord.utils.get(ctx.guild.roles, id=816244946365186048)
	silverchariot = discord.utils.get(ctx.guild.roles, id=816244947224100864)
	crazydiamond = discord.utils.get(ctx.guild.roles, id=816602875014676480)
	kingcrimson = discord.utils.get(ctx.guild.roles, id=817441099173199923)
	mrpresident = discord.utils.get(ctx.guild.roles, id=817885472734838795)
	mrpresident_inroom = discord.utils.get(ctx.guild.roles, id=817885610760208444)
	heavensdoor = discord.utils.get(ctx.guild.roles, id=818585440352469073)
	killerqueen = discord.utils.get(ctx.guild.roles, id=819249703291322450)

	stands = [thehand, theworld, starplatinum, silverchariot, crazydiamond, kingcrimson, mrpresident, heavensdoor, killerqueen]

	puncher = ctx.author

	if theworld in puncher.roles:
		async for message in ctx.channel.history():
			if(message == ctx.message) or (message.author == ctx.message.author) or (message.author == client.user):
				continue
			else:
				previous_message = message
				punched = previous_message.author
				await changehealth(user=punched, add=0, subtract=4)
				await changehealth(user=punched, add=0, subtract=4)
				await changehealth(user=punched, add=0, subtract=4)
				await changehealth(user=punched, add=0, subtract=4)
				await changehealth(user=punched, add=0, subtract=4)
				await changehealth(user=punched, add=0, subtract=4)
				attack_embed = discord.Embed(title=f"{puncher.display_name} punched {punched.display_name}! MUDA MUDA MUDA MUDA!", colour=discord.Colour(0xffdc00))
				await ctx.channel.send(embed=attack_embed)
				break
	if starplatinum in puncher.roles:
		async for message in ctx.channel.history():
			if(message == ctx.message) or (message.author == ctx.message.author) or (message.author == client.user):
				continue
			else:
				previous_message = message
				punched = previous_message.author
				await changehealth(user=punched, add=0, subtract=4)
				await changehealth(user=punched, add=0, subtract=4)
				await changehealth(user=punched, add=0, subtract=4)
				await changehealth(user=punched, add=0, subtract=5)
				await changehealth(user=punched, add=0, subtract=5)
				await changehealth(user=punched, add=0, subtract=5)
				attack_embed = discord.Embed(title=f"{puncher.display_name} used a barrage on {punched.display_name}! ORA ORA ORA ORA ORA!", colour=discord.Colour(0x9b20c2))
				await ctx.channel.send(embed=attack_embed)
				break
	if thehand in puncher.roles:
		async for message in ctx.channel.history():
			if(message == ctx.message) or (message.author == ctx.message.author) or (message.author == client.user):
				continue
			else:
				previous_message = message
				punched = previous_message.author
				await changehealth(user=punched, add=0, subtract=30)
				await ctx.channel.purge(limit=4)
				attack_embed = discord.Embed(title=f"{puncher.display_name} erased {punched.display_name}! BBBBBBBVVVVV!", colour=discord.Colour(0x5957db))
				await ctx.channel.send(embed=attack_embed)
				break
	if silverchariot in puncher.roles:
		async for message in ctx.channel.history():
			if(message == ctx.message) or (message.author == ctx.message.author) or (message.author == client.user):
				continue
			else:
				previous_message = message
				punched = previous_message.author
				await changehealth(user=punched, add=0, subtract=2)
				await changehealth(user=punched, add=0, subtract=2)
				await changehealth(user=punched, add=0, subtract=3)
				await changehealth(user=punched, add=0, subtract=3)
				await changehealth(user=punched, add=0, subtract=3)
				attack_embed = discord.Embed(title=f"{puncher.display_name} attacked {punched.display_name}! HORA HORA HORA HORA!", colour=discord.Colour(0xf5f5f5))
				await ctx.channel.send(embed=attack_embed)
				break
	if crazydiamond in puncher.roles:
		async for message in ctx.channel.history():
			if(message == ctx.message) or (message.author == ctx.message.author) or (message.author == client.user):
				continue
			else:
				previous_message = message
				punched = previous_message.author
				await changehealth(user=punched, add=0, subtract=4)
				await changehealth(user=punched, add=0, subtract=4)
				await changehealth(user=punched, add=0, subtract=4)
				await changehealth(user=punched, add=0, subtract=4)
				await changehealth(user=punched, add=0, subtract=5)
				await changehealth(user=punched, add=0, subtract=5)
				await changehealth(user=puncher, add=15, subtract=0)
				attack_embed = discord.Embed(title=f"{puncher.display_name} used a barrage on {punched.display_name}! DORA-RA-RA-RA-RA-RA DORA!\nThe restoring effect also healed {puncher.display_name}", colour=discord.Colour(0xe277d5))
				await ctx.channel.send(embed=attack_embed)
				break
	if kingcrimson in puncher.roles:
		async for message in ctx.channel.history():
			if(message == ctx.message) or (message.author == ctx.message.author) or (message.author == client.user):
				continue
			else:
				previous_message = message
				punched = previous_message.author
				await changehealth(user=punched, add=0, subtract=40)
				attack_embed = discord.Embed(title=f"{puncher.display_name} donuted {punched.display_name}!", colour=discord.Colour(0xb90d0d))
				await ctx.channel.send(embed=attack_embed)
				break
	if mrpresident in puncher.roles:
		async for message in ctx.channel.history():
			if(message == ctx.message) or (message.author == ctx.message.author) or (message.author == client.user):
				continue
			else:
				previous_message = message
				punched = previous_message.author
				await changehealth(user=punched, add=0, subtract=20)
				attack_embed = discord.Embed(title=f"{puncher.display_name} barraged {punched.display_name}, now {puncher.display_name} is inside Mr. President!", colour=discord.Colour(0x2f964d))
				await ctx.channel.send(embed=attack_embed)
				await ctx.author.add_roles(mrpresident_inroom)
				await asyncio.sleep(10)
				attack_embed = discord.Embed(title=f"{puncher.display_name} left Mr. President!", colour=discord.Colour(0x2f964d))
				await ctx.channel.send(embed=attack_embed)
				await ctx.author.remove_roles(mrpresident_inroom)
				break
	if heavensdoor in puncher.roles:
		async for message in ctx.channel.history():
			if(message == ctx.message) or (message.author == ctx.message.author) or (message.author == client.user):
				continue
			else:
				previous_message = message
				punched = previous_message.author
				await changehealth(user=punched, add=0, subtract=6)
				await changehealth(user=punched, add=0, subtract=6)
				await changehealth(user=punched, add=0, subtract=6)
				attack_embed = discord.Embed(title=f"{puncher.display_name} barraged {punched.display_name}!", colour=discord.Colour(0xfff247))
				await ctx.channel.send(embed=attack_embed)
				break
	if killerqueen in puncher.roles:
		async for message in ctx.channel.history():
			if(message == ctx.message) or (message.author == ctx.message.author) or (message.author == client.user):
				continue
			else:
				previous_message = message
				punched = previous_message.author
				await changehealth(user=punched, add=0, subtract=5)
				await changehealth(user=punched, add=0, subtract=5)
				await changehealth(user=punched, add=0, subtract=5)
				await changehealth(user=punched, add=0, subtract=5)
				await changehealth(user=punched, add=0, subtract=5)
				attack_embed = discord.Embed(title=f"{puncher.display_name} barraged {punched.display_name}! SHIBOBOBOBOBO", colour=discord.Colour(0xdba4d3))
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
	kingcrimson = discord.utils.get(ctx.guild.roles, id=817441099173199923)
	heavensdoor = discord.utils.get(ctx.guild.roles, id=818585440352469073)
	killerqueen = discord.utils.get(ctx.guild.roles, id=819249703291322450)

	stands = [thehand, theworld, starplatinum, silverchariot, crazydiamond, kingcrimson, heavensdoor, killerqueen]

	if ctx.message.mentions == []:
		InfoOn = ctx.author
	else:
		InfoOn = ctx.message.mentions[0]

	for x in stands:
		if x in InfoOn.roles:
			try:
				hp_embed = discord.Embed(title=f"{InfoOn.display_name} has `{health[str(InfoOn.id)]}` health\n{InfoOn.display_name}'s stand is {x.name}")
				await ctx.channel.send(embed=hp_embed)
			except KeyError:
				hp_embed2 = discord.Embed(title=f"{InfoOn.display_name}'s stand is {x.name}")
				await ctx.channel.send(embed=hp_embed2)

client.run(token)