from discord.ext import commands
import discord
import random
import health

intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix='d4v!', help_command=None, intents=intents)

with open("tokenfile", "r") as tokenfile:
	token=tokenfile.read()

@client.event
async def on_ready():
	print('Dojyan!')

@client.command()
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

client.run(token)