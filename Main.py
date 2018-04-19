# These are the dependecies. The bot depends on these to function, hence the name. Please do not change these unless your adding to them, because they can break the bot.
import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands
import platform
import random
# Here you can modify the bot's prefix and description and wether it sends help in direct messages or not.
client = Bot(description="HuggleBot", command_prefix="!", pm_help = False)

# This is what happens everytime the bot launches. In this case, it prints information like server count, user count the bot is connected to, and the bot id in the console.
# Do not mess with it because the bot can break, if you wish to do so, please consult me or someone trusted.

result = []



@client.event
async def on_ready():
	print('Logged in as '+client.user.name+' (ID:'+client.user.id+') | Connected to '+str(len(client.servers))+' servers | Connected to '+str(len(set(client.get_all_members())))+' users')
	print('--------')
	print('Current Discord.py Version: {} | Current Python Version: {}'.format(discord.__version__, platform.python_version()))
	print('--------')
	print('Use this link to invite {}:'.format(client.user.name))
	print('https://discordapp.com/oauth2/authorize?client_id={}&scope=bot&permissions=8'.format(client.user.id))
	print('--------')
	print('Support Discord Server: https://discord.gg/FNNNgqb')
	print('Github Link: https://github.com/Habchy/BasicBot')
	print('--------')
	print('You are running BasicBot v2.1') #Do not change this. This will really help us support you, if you need support.
	print('Created by Habchy#1665')
	return await client.change_presence(game=discord.Game(name='First BOT')) #This is buggy, let us know if it doesn't work.

# This is a basic example of a call and response command. You tell it do "this" and it does it.
@client.command()
async def hugglepls(*args):
	await client.say(":hugging: *hugggle*")
@client.command()	
async def nice(*args):
	await client.say("69 :wink:")
@client.command()
async def kissupls(*args):
	await client.say(":kissing_heart: *kissu*")
	
@client.command()
async def holdpls(*args):
	await client.say(":wave: *hold*")

@client.command()
async def kissu(message: str):

	await client.say(":kissing_heart: *kissu* " + message)	
	
@client.command()
async def yay(*args):

	await client.say(":tada: :tada: :tada:")	
	
	
@client.command()
async def children(*choices: str):
	await client.say("Now type !job followed by 5 jobs")
	result.append(random.choice(choices))
	
	
@client.command()
async def job(*choices: str):
	await client.say("Now type !car followed by 5 models of cars ")
	result.append(random.choice(choices))
		
@client.command()
async def car(*choices: str):
	await client.say("Now type !crush followed by the names of 5 people")
	result.append(random.choice(choices))
		
@client.command()
async def crush(*choices: str):
	await client.say("Now type !color followed by 5 colors")
	result.append(random.choice(choices))
		
@client.command()
async def color(*choices: str):
	await client.say("Now type !reveal to see your results")
	result.append(random.choice(choices))

@client.command()
async def reveal(*args):
	await client.say("Here are your results: ")
	await client.say('In the future, you will working as a/an {}. You drive a {} {} and have {} beautiful kids with your one and only {}'.format(result[1],result[4], result[2], result[0], result[3]))

client.run('NDM0NzU1OTE1MTE2MTgzNTUy.DbPBhQ.DQ_Zn2-osR3khe6x7rK9lbXROd8')

# Basic Bot was created by Habchy#1665
# Please join this Discord server if you need help: https://discord.gg/FNNNgqb
# Please modify the parts of the code where it asks you to. Example: The Prefix or The Bot Token
# This is by no means a full bot, it's more of a starter to show you what the python language can do in Discord.
# Thank you for using this and don't forget to star my repo on GitHub! [Repo Link: https://github.com/Habchy/BasicBot]

# The help command is currently set to be not be Direct Messaged.
# If you would like to change that, change "pm_help = False" to "pm_help = True" on line 9.
