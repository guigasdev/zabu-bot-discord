import discord
from discord.ext import commands
from settings import token
from discord import app_commands
import os


intents = discord.Intents.default()
intents.message_content = True
intents.members = True
bot = commands.Bot(command_prefix='!', intents=intents)

async def carregar_cogs():
    for arquivo in os.listdir('cogs'):
        if arquivo.endswith('.py'):
            await bot.load_extension(f'cogs.{arquivo[:-3]}')

@bot.event
async def on_ready():
    await carregar_cogs()
    await bot.tree.sync()
    print('Bot online!')
    print(bot.user.name)

@bot.command()
async def sincronizar(ctx: commands.Context):
    if ctx.author.id == 709868042028449813:
        server = discord.Object(id=1220578591415210054)
        sincs = await bot.tree.sync(guild=server)
        await ctx.reply(f'{len(sincs)} comandos sincronizados')
    else:
        await ctx.reply('Apenas o meu criador pode executar esse comando!')

@bot.event
async def on_guild_channel_create(canal:discord.abc.GuildChannel):
    await canal.send(f'Novo canal criado: {canal.name}')

@bot.event
async def on_member_join(membro:discord.Member):
    canal = bot.get_channel(1220582686628909137)
    embed = discord.Embed(title=f'{membro.name} caiu de paraquedas aqui \nSeja Bem-vindo!',
        description= f'\nBem vindo ao {membro.guild.name} - \n veja as #📑・information para ficar por dentro de tudo!',
        color=0x0061ff,
    )
    role = discord.utils.get(membro.guild.roles, name='Members')
    imagem_arquivo = discord.File('media/happy-zabu.png', 'happy-zabu.png')
    embed.set_image(url='attachment://happy-zabu.png')
    embed.set_author(name='Zabu', url='https://github.com/guigasdev/zabu-bot-discord', icon_url='https://cdn.discordapp.com/attachments/720813300568293409/1220958458740736050/h4zzGYHpedro-nery-workbook.png?ex=6610d52c&is=65fe602c&hm=f752a4f3d8d5f6b06b4ead75ec53f6aec68f2a6a02e65805450cc6a51c37b333&')
    embed.set_thumbnail(url=membro.avatar)
    await membro.add_roles(role)
    await canal.send(embed=embed, file=imagem_arquivo)


@bot.event
async def on_member_remove(membro:discord.Member):
    canal = bot.get_channel(1220582686628909137)
    embed = discord.Embed(title=f'{membro.name} saiu do servidor 😥',
        description= f'\nAté uma próxima vez, te aguardamos aqui denovo! 😁',
        color=0x0061ff,
    )
    imagem_arquivo = discord.File('media/sadness-zabu.png', 'sadness-zabu.png')
    embed.set_image(url='attachment://sadness-zabu.png')
    embed.set_author(name='Zabu', url='https://github.com/guigasdev/zabu-bot-discord', icon_url='https://cdn.discordapp.com/attachments/720813300568293409/1220958458740736050/h4zzGYHpedro-nery-workbook.png?ex=6610d52c&is=65fe602c&hm=f752a4f3d8d5f6b06b4ead75ec53f6aec68f2a6a02e65805450cc6a51c37b333&')
    embed.set_thumbnail(url=membro.avatar)
    await canal.send(embed=embed, file=imagem_arquivo)

bot.run(token) ## ponha aqui o seu token entre aspas ''