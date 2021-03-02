import discord
import json

async def changehealth(user, add, subtract):

	with open("health.json", "rt") as healthraw: # opens health.json
		health = json.loads(rawhealth.read()) # sets the health varible to the contents of health.json

	id = str(user.id)
	
	try: # tries to run the below code
		health[id] -= subtract # subtracts what it was told to
		health[id] += add # adds what it was told to
	except KeyError: # if it couldnt find an object in the dictionary with the user's id, it runs this code instead
		health[id] = 200 # gives the user health
		health[id] -= subtract # subtracts what it was told to
		health[id] += add # adds what it was told to
		print(f"{user} didnt have health but now they do")

	with open("health.json", "rt") as healthraw: # opens health.json
		healthraw.write(json.dumps(health)) # write the above changes to health.json
