import discord
from discord import app_commands
from discord.ext import commands

class hexadecimalColor(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        super().__init__()
    
    @app_commands.command(description='Retorna em hexadecimal o valor das cores')
    @app_commands.choices(cor=[
    app_commands.Choice(name='Vermelho', value='BA2D0B'),
    app_commands.Choice(name='Azul', value='22577A'),
    app_commands.Choice(name='Verde', value='FFC145')
])
    async def cor(self, interact:discord.Interaction, cor:app_commands.Choice[str]):
        await interact.response.send_message(f'O código hexadecimal da cor {cor.name} é: {cor.value}')

async def setup(bot):
    await bot.add_cog(hexadecimalColor(bot))