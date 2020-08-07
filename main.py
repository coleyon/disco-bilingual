import os
from html import unescape
import discord
from discord.ext import commands
from oauth2client.client import GoogleCredentials
from google.cloud import translate_v2 as translate


bot = commands.Bot(command_prefix="/")
GoogleCredentials.get_application_default()


@bot.event
async def on_ready():
    print("-----Logged in info-----")
    print(bot.user.name)
    print(bot.user.id)
    print(discord.__version__)
    print("------------------------")


@bot.event
async def on_message(message):
    """/tls jp en"""
    if message.author.bot:
        return

    if message.content.startswith("/j2e"):
        srclang = "ja"
        tgtlang = "en"
        posted_contents = message.content.replace(u"\u3000", " ")[5:]
        result = translate.Client().translate(
            posted_contents,
            source_language=srclang,
            target_language=tgtlang,
            model="nmt",
        )
        msg = "{auther} さんのメッセージを翻訳しました:\n```\n{org}\n```\n\n{translated}".format(
            auther=message.author.name,
            org=result["input"],
            translated=result["translatedText"],
        )
        # print(msg)
        await message.channel.send(unescape(msg))

    if message.content.startswith("/e2j"):
        srclang = "en"
        tgtlang = "ja"
        posted_contents = message.content.replace(u"\u3000", " ")[5:]
        result = translate.Client().translate(
            posted_contents,
            source_language=srclang,
            target_language=tgtlang,
            model="nmt",
        )
        msg = "{auther}'s post has translated:\n```\n{org}\n```\n\n{translated}".format(
            auther=message.author.name,
            org=result["input"],
            translated=result["translatedText"],
        )
        # print(msg)
        await message.channel.send(unescape(msg))


bot.run(os.getenv("DISCORD_BOT_TOKEN"))
