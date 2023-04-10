import discord
from discord.errors import *
from config import Config as confClass
from yt_dlp import YoutubeDL


class MuseCord(discord.Bot):
    def __init__(self):
        super().__init__()


musecord = MuseCord()
Config = confClass()


@musecord.slash_command(name="ping", description="Pings the bot", guild_ids=Config["guilds"])
async def hello(ctx):
    await ctx.respond("Pong")

