import discord
from discord.ext import commands
import json

class MyHelpCommand(commands.DefaultHelpCommand):
	def __init__(self, **options):
		self.paginator = commands.Paginator()
		super().__init__(**options)
		self.paginator.prefix = ""
		self.paginator.suffix = ""
		self.no_category = "Other"
	def add_indented_commands(self, commands, *, heading, max_size=None):
		if not commands:
			return
		self.paginator.add_line(f"**{heading}**")
		max_size = max_size or self.get_max_size(commands)
		get_width = discord.utils._string_width
		for command in commands:
			name = f"{command.name}"
			width = max_size - (get_width(name) - len(name))
			entry = "{0}{1:<{width}}: *{2}*".format(self.indent * " ", name, command.short_doc, width=width)
			self.paginator.add_line(self.shorten_text(entry))
	def get_ending_note(self):
		command_name = self.invoked_with
		return "Type `{0}{1} <command>` for more info on a command.\n".format(self.clean_prefix, command_name)
	def add_command_formatting(self, command):
		if command.description:
			self.paginator.add_line(command.description, empty=True)
		elif command.brief:
			self.paginator.add_line(command.brief,empty=True)
		signature = self.get_command_signature(command)
		self.paginator.add_line(f"`{signature}`""", empty=True)

		if command.help:
			try:
				self.paginator.add_line(command.help, empty=True)
			except RuntimeError:
				for line in command.help.splitlines():
					self.paginator.add_line(line)
				self.paginator.add_line()
	async def send_pages(self):
		destination = self.get_destination()
		e = discord.Embed(title="Help",color=discord.Color.blurple(), description="")
		for page in self.paginator.pages:
			e.description += page
		await destination.send(embed=e)

async def changehealth(user, add, subtract):

	with open("health.json", "rt") as healthraw: # opens health.json
		health = json.loads(healthraw.read()) # sets the health varible to the contents of health.json

	id = str(user.id)
	
	mrpresident_inroom = discord.utils.get(user.guild.roles, id=817885610760208444)
	if not mrpresident_inroom in user.roles:
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



	with open("health.json", "wt") as healthraw: # opens health.json
		healthraw.write(json.dumps(health)) # write the above changes to health.json


