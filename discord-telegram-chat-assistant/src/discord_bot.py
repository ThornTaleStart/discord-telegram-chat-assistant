import discord
from discord.ext import commands
from config import Config
from ai_handler import AIHandler

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)
ai = AIHandler()

@bot.event
async def on_ready():
    print(f"Discord bot logged in as {bot.user}")

@bot.command(name="ask")
async def ask(ctx, *, question: str):
    async with ctx.typing():
        response = ai.get_response(question)
    await ctx.send(response)

@bot.command(name="clear")
async def clear_history(ctx):
    ai.history.clear()
    await ctx.send("Chat history cleared.")

def run_discord():
    Config.validate()
    bot.run(Config.DISCORD_TOKEN)