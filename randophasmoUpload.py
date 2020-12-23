import discord, time, sys, random
from discord.ext import commands, tasks
from time import sleep
from itertools import cycle
from discord.utils import get

client = commands.Bot(command_prefix = ".")
status = cycle(["Status 1", "Status 2"])
global intervaltime
intervaltime = 120

god_list = ["EMF Reader","Ghost Writing Book","Spirit Box","Thermometer","Video Camera","UV Flashlight","Photo Camera","Flashlight","Strong Flashlight","Candle","Crucifix","Glow Stick","Head Mounted Camera","Infrared Light Sensor","Lighter","Motion Sensor","Parabolic Microphone","Salt Shaker","Sanity Pills","Smudge Sticks","Sound Sensor","Tripod"]

global master_list
global light_emitting
master_list = god_list.copy()
#master_list = ["EMF Reader","Ghost Writing Book","Spirit Box","Thermometer","Video Camera","UV Flashlight","Photo Camera","Flashlight","Strong Flashlight","Candle","Crucifix","Glow Stick","Head Mounted Camera","Infrared Light Sensor","Lighter","Motion Sensor","Parabolic Microphone","Salt Shaker","Sanity Pills","Smudge Sticks","Sound Sensor","Tripod"]
light_emitting = ["UV Flashlight","Flashlight","Strong Flashlight","Candle","Glow Stick","Infrared Light Sensor"]

@client.event
async def on_ready():
	print ("Bot ready")

@client.command()
async def putthatshitaway(ctx):
	master_list = god_list.copy()
	output = "```markdown"
	for i in light_emitting[:]:
		output += "\n* "
		output += i
		master_list.remove(i)
	output += "```"
	await ctx.send(f'PUT THAT SHIT AWAY\n{output}\n{master_list}')

@client.command()
async def bringthatshitback(ctx):
	master_list = god_list.copy()
	await ctx.send(f'Weenie hut Jr. mode activated')

@client.command()
async def userinput(ctx, *, input):
	global userlists
	userlists = {}
	global userallowed
	userallowed = {}
	global fancylist
	fancylist = input.split(',')
	await ctx.send(f'Users In: {fancylist}')
	for i in fancylist:
		userallowed[i] = [""]
		userlists[i] = master_list.copy()

		#print(userlists[i])
@client.command()
async def setinterval(ctx, *, input):
	intervaltime = int(input)
	await ctx.send(f'Interval set to: {intervaltime} seconds')

@client.command()
async def resetgame(ctx):
	for i in fancylist:
		userallowed[i] = [""]
		userlists[i] = master_list.copy()
	await ctx.send(f'Cleared Inventories')

@tasks.loop(seconds=intervaltime)
async def send_items(ctx):
	await ctx.send(f"Entered Loop, sending update every {intervaltime} seconds")
	await ctx.channel.purge(limit=99)	
	for i in fancylist:
		selected = random.choice(userlists[i])
		userallowed[i].append(selected)
		userlists[i].remove(selected)
		userallowed[i] = list(filter(None, userallowed[i]))
		outputstring = "``markdown\n"
		for y in userallowed[i]:
			outputstring += "* "
			outputstring += y
			outputstring += "\n"
		outputstring += "``" 
		await ctx.send(f"User: @{i}\n`{outputstring}`\n\n\n")

	#for i in fancylist:
	#	await ctx.send(f"User: {i}{userlists[i]}")

@client.command()
async def threeinone(ctx):
	await ctx.send(f"Activating 3 in one.")
	await ctx.channel.purge(limit=99)	
	for i in fancylist:
		x = 1
		while x <= 3:
			selected = random.choice(userlists[i])
			userallowed[i].append(selected)
			userlists[i].remove(selected)
			x += 1
		userallowed[i] = list(filter(None, userallowed[i]))
		outputstring = "``markdown\n"
		for y in userallowed[i]:
			outputstring += "* "
			outputstring += y
			outputstring += "\n"
		outputstring += "``" 
		await ctx.send(f"User: @{i}\n`{outputstring}`\n\n\n")
	for i in fancylist:
		userallowed[i] = [""]
		userlists[i] = master_list.copy()


	#for i in fancylist:
	#	await ctx.send(f"User: {i}{userlists[i]}")


@client.command()
async def start(ctx):

	send_items.start(ctx)

@client.command()
async def stop(ctx):
	send_items.stop()

@client.command()
async def clear(ctx, amount=5):
	await ctx.channel.purge(limit=amount)	


client.run("")
