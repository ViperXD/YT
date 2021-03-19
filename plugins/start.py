from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("⭕️CHANNEL⭕️", url="https://t.me/VKPROJECTS")],
        [InlineKeyboardButton(
            "⭕️GROUP⭕️", url="https://t.me/VKP_BOTS")]
    ])
    welcomed = f"Hi, <b>{message.from_user.first_name}</b>.\nI'm A POWERFULL YOUTUBE Upload Bot💯.</b>\n\nPlease send me any YOUTUBE link, I can upload it to telegram as File/Video.</b>\n\nClick /help for more details...."
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
