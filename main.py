import discord
from discord.ext import commands
from settings import token

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print('Bot online!')
    print(bot.user.name)

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
async def on_guild_channel_create(canal:discord.abc.GuildChannel):
    await canal.send(f'Novo canal criado: {canal.name}')

@bot.event
async def on_member_join(membro:discord.Member):
    canal = bot.get_channel(1220582686628909137)
    await canal.send(f'{membro.display_name} caiu de paraquedas aqui! \nBem-vindo!')

@bot.event
async def on_member_remove(membro:discord.Member):
    canal = bot.get_channel(1220582686628909137)
    await canal.send(f'{membro.display_name} saiu do servidor 😥')

bot.run(token) ## ponha aqui o seu token entre aspas ''