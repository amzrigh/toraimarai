import discord
import asyncio
import .iclient

client = discord.Client()

token="blah"

channels=["blah"]

@client.event
async def on_ready():
	# check local logs for starting point
	
	# catch up

@client.event
async def on_message(message):
	# create object from relevant parameters
	
	# publish object
	
	# log object
	
	
@client.event
async def on_message_edit(before,after):
	# check timeliness of edit
	
		# publish edit
		
		# edit log
	
@client.event
async def on_message_delete(message):
	# check timeliness of delete
	
		# publish delete
		
		# edit log
