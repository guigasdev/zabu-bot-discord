import discord
from discord import app_commands
from discord.ext import commands

class falar(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        super().__init__()
        
    @app_commands.command(description='Faça o Zabu falar o que você escreveu')
    async def falar(self, interact: discord.Interaction, frase:str):
        await interact.response.send_message(frase)

async def setup(bot):
    await bot.add_cog(falar(bot))