import discord
from discord import app_commands
from discord.ext import commands

class ola(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        super().__init__()

    @app_commands.command(description='Fale com o Zabu')
    async def ola(self, interact: discord.Interaction):
        await interact.response.send_message(f'Olá {interact.user.display_name}, em que posso ajudar?', ephemeral=True)
        
async def setup(bot):
    await bot.add_cog(ola(bot))