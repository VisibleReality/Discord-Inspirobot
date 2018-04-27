# Discord Inspirobot
# Sends inspirational images to discord on command

# Import required modules
import discord
from discord.ext import commands
import urllib.request
import io

# Declare some variables
userAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0"
prefix = "!"
token = "<token>"

# Defines the bot which allows us to create commands
bot = commands.Bot(command_prefix=prefix, description="Inspirobot.me")

@bot.listen()
async def on_ready():
	print("Bot ready")
	print(bot.user.name, "("+str(bot.user.id)+")")
	await bot.change_presence(activity=discord.Game(name='!inspire'))

@bot.command()
async def inspire(ctx):
	path_response = urllib.request.urlopen(urllib.request.Request("http://inspirobot.me/api?generate=true",headers={"User-Agent":userAgent}))
	image = urllib.request.urlopen(urllib.request.Request(path_response.read().decode("utf-8"),headers={"User-Agent":UserAgent}))
	data = io.BytesIO(image.read())
	await ctx.send(file=discord.File(data, "inspirobot.jpg"))

bot.remove_command('help')

bot.run("<token>")
