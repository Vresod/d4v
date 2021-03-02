import discord
import random

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

with open("tokenfile", "r") as tokenfile:
	token=tokenfile.read()

@client.event
async def on_ready():
	print('Dojyan!')

prefix = "d4v!"

@client.event
async def on_message(message):

	theworld = discord.utils.get(message.guild.roles, id=816244945580982282)
	thehand = discord.utils.get(message.guild.roles, id=816244947761102850)
	starplatinum = discord.utils.get(message.guild.roles, id=816244946365186048)
	silverchariot = discord.utils.get(message.guild.roles, id=816244947224100864)

	stands = [thehand, theworld, starplatinum, silverchariot]

	argsraw = message.content.lower().replace(prefix, "")
	args = argsraw.split(" ")

	if message.content.lower().startswith(prefix):
		if args[0] == "reserve":
			try:
				standwanted = message.role_mentions[0]
			except IndexError:
				return
			if standwanted in stands:
				for x in stands:
					if x in message.author.roles:
						await message.channel.send(f"you already have {x.name}")
						return
				if standwanted.members == []:
					await message.author.add_roles(standwanted)
					await message.channel.send(f"you now have {standwanted.name}!")
				else:
					await message.channel.send(f"{standwanted.members[0].name} already has {standwanted.name}")

client.run(token)