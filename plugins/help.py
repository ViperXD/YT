from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"Send me YouTube Video Link I will upload to Telegram! \n\n(No PlayList Supported!)"
    await message.reply_text(helptxt)
