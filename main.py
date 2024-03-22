import discord
from discord.ext import commands
from settings import token

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command()
async def ola(ctx:commands.Context):
    usuario = ctx.author
    await ctx.reply(f'Olá {usuario.display_name}, em que posso ajudar?')

@bot.command()
async def somar(ctx:commands.Context, num1:float, num2:float):
    usuario = ctx.author
    res = num1 + num2
    await ctx.reply(f'Opa, {usuario.display_name}, a soma dos números informados é: {res}')

@bot.command()
async def falar(ctx:commands.Context, *,frase):
    await ctx.send(frase)

@bot.event
async def on_ready():
    print('Bot online!')
    print(bot.user.name)


bot.run(token) ## ponha aqui o seu token entre aspas ''