from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("Bots Updates Channel", url="https://t.me/Discovery_Updates")],
        [InlineKeyboardButton(
            "Support Group", url="https://t.me/linux_repo")]
    ])
    welcomed = f"Hi, <b>{message.from_user.first_name}</b>.\nThis is <b>YouTube Uploader Bot.</b>\n\nBy @Discovery_Updates \nDeveloper: @AbirHasan2005"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
