# Discord Inspirobot
# Sends inspirational images to discord on command

# Import required modules
import discord
from discord.ext import commands
import urllib.request
import io
import os
import random

# Declare some variables
userAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0"
prefix = "!"
token = "<token>"
apiUrl="http://inspirobot.me/api?generate=true"
fileUploadName = "inspirobot.jpg"

# Defines the bot which allows us to create commands
bot = commands.Bot(command_prefix=prefix, description="Inspirobot.me")

# Sets the bot's presence to indicate the command to use, and prints some text to indicate that it is ready.
@bot.listen()
async def on_ready():
	print("Bot ready")
	print(bot.user.name, "("+str(bot.user.id)+")")
	await bot.change_presence(activity=discord.Game(name='!inspire'))

# Defines the !inspire command which allows you to request inspirational images on demand.
@bot.command()
async def inspire(ctx):
	path_response = urllib.request.urlopen(urllib.request.Request(apiUrl,headers={"User-Agent":userAgent}))
	image = urllib.request.urlopen(urllib.request.Request(path_response.read().decode("utf-8"),headers={"User-Agent":UserAgent}))
	data = io.BytesIO(image.read())
	await ctx.send(file=discord.File(data, fileUploadName))

# Add a command which randomly picks one of the best images seen yet.
@bot.command()
async def bestof(ctx):
	file = open(random.choice(os.listdir("inspirobot-bestof/")), "rb")
	await ctx.send(file=discord.File((file, fileUploadName)))
	file.close()

# Removes the auto generated help command as it's not required
bot.remove_command('help')

# Starts running the bot
bot.run("<token>")
