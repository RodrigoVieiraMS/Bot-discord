import discord
from discord import app_commands


class PigBot(discord.Client):
    def __init__(self):  # inicializa uma instancia da classe (construtor)
        # self = referenciando a propria classe
        intents = discord.Intents.all()
        super().__init__(command_prefix='+', intents=intents)  # invoca dentro da classe filha a classe pai (discord.client)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        await self.tree.sync()

    async def on_ready(self):
        print(f"Bot {self.user} ligado com sucesso.")


bot = PigBot()  # pega a classe cria uma instancia dela e colocando na variavel bot

@bot.tree.command(name="olá-bot",description="Diga oi para o bot")
async def ola(interaction:discord.Interaction):
    await interaction.response.send_message(f"Olá{interaction.user.mention}!")


bot.run("seutoken13123213123")