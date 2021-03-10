from discord.ext import commands
import discord
import json

async def changehealth(user, add, subtract):

	with open("health.json", "rt") as healthraw: # opens health.json
		health = json.loads(healthraw.read()) # sets the health varible to the contents of health.json

	id = str(user.id)
	
	mrpresident_inroom = discord.utils.get(user.guild.roles, id=817885610760208444)
	hd_3 = discord.utils.get(ctx.guild.roles, id=818588024824659969)
	if not mrpresident_inroom in user.roles:
		if not hd_3 in user.roles:
			try: # tries to run the below code
				health[id] -= subtract # subtracts what it was told to
				health[id] += add # adds what it was told to
			except KeyError: # if it couldnt find an object in the dictionary with the user's id, it runs this code instead
				health[id] = 200 # gives the user health
				health[id] -= subtract # subtracts what it was told to
				health[id] += add # adds what it was told to
				print(f"{user} didnt have health but now they do")
	if mrpresident_inroom in user.roles:
		room_embed = discord.Embed(title="The target is inside Mr. President", colour=discord.Colour(0x2f964d))
		await ctx.author.send(embed=room_embed)
	if hd_3 in user.roles:
		hd_embed2 = discord.Embed(title="The target is invulnerable", colour=discord.Colour(0xfff247))
		await ctx.author.send(embed=hd_embed2)


	with open("health.json", "wt") as healthraw: # opens health.json
		healthraw.write(json.dumps(health)) # write the above changes to health.json
