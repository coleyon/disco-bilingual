import os
from html import unescape
import discord
from discord.ext import commands
from oauth2client.client import GoogleCredentials
from google.cloud import translate_v2 as translate


bot = commands.Bot(command_prefix="/")
GoogleCredentials.get_application_default()
TRANSLATION_SOFT_LIMIT = 1000


@bot.event
async def on_ready():
    print("-----Logged in info-----")
    print(bot.user.name)
    print(bot.user.id)
    print(discord.__version__)
    print("------------------------")


@bot.command(name="man")
async def manual(ctx):
    """Get a languages that can be translated into the target language.

    Example:
        `/man`
    """
    await ctx.channel.send(
        "Syntax: \n`/tran <src> <dest> <message>`\nThe parameters `src` and `dest` can be `ISO_639-1 codes`.\n\nSee:\n<https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes>"
    )


@bot.command(name="tran")
async def translate_message(ctx, src, target):
    """Translate the text on content into dest language.

    Example:
        `/tran en ja Hello World, I'm Shingen Takeda.`
    """
    if ctx.author.bot:
        return

    # ctx.message.content
    text = " ".join(ctx.message.content.split(" ")[3:])
    if len(text) > TRANSLATION_SOFT_LIMIT:
        text = text[:TRANSLATION_SOFT_LIMIT] + "…"

    result = translate.Client().translate(
        text, source_language=src, target_language=target
    )
    msg = "`{author}` さんのメッセージを翻訳しました!!\n<{org_url}>\n```\n{translated}\n```".format(
        org_url=ctx.message.jump_url,
        author=ctx.author.display_name,
        translated=result["translatedText"],
    )
    await ctx.channel.send(unescape(msg))


bot.run(os.getenv("DISCORD_BOT_TOKEN"))
