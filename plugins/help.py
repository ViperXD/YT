from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"<b>Hai, Follow these steps..</b>\n\n1. Send Custom Thumbnail if required (It will be saved permenantly!)\n\n2. Send your youtube link and select desired option."
    await message.reply_text(helptxt)
