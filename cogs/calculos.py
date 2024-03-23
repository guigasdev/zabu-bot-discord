import discord
from discord import app_commands
from discord.ext import commands

class Calculos(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        super().__init__()

    @app_commands.command(description='Soma dois números')
    @app_commands.commands.describe(num1='O primeiro número a ser somado', num2='O segundo número a ser somado')
    async def somar(self, interact:discord.Interaction, num1:float, num2:float):
        res = num1 + num2
        await interact.response.send_message(f'A soma dos números informados é: {res}')
    
    @app_commands.command(description='Subtrai dois númerosos')
    @app_commands.commands.describe(num1='O primeiro número a ser subtraído', num2='O segundo número a ser subtraído')
    async def subtrair(self, interact:discord.Interaction, num1:float, num2:float):
        res = num1 - num2
        await interact.response.send_message(f'A subtração dos números informados é: {res}')

    @app_commands.command(description='Multiplica dois númerosos')
    @app_commands.commands.describe(num1='O primeiro número a ser multiplicado', num2='O segundo número a ser multiplicado')
    async def multiplicar(self, interact:discord.Interaction, num1:float, num2:float):
        res = num1 * num2
        await interact.response.send_message(f'A multiplicação dos números informados é: {res}')

    @app_commands.command(description='Divide dois númerosos')
    @app_commands.commands.describe(num1='O primeiro número a ser dividido', num2='O segundo número a ser dividido')
    async def dividir(self, interact:discord.Interaction, num1:float, num2:float):
        res = num1 / num2
        await interact.response.send_message(f'A divisão dos números informados é: {res}')
    

async def setup(bot):
    await bot.add_cog(Calculos(bot))
