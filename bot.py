import os

from discord.ext import commands


bot = commands.Bot(command_prefix=".")


@bot.event
async def on_ready():
    bot.load_extension("command.review")
    print("Bot started!")

bot.run(os.environ["BOT_TOKEN"])
