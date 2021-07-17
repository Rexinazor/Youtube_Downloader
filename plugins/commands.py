# Name     : Youtube_Downloader 'Inline' [ Telegram ]
# Repo     : https://github.com/Rexinazor/Youtube_Downloader
# Author   : Rexinazor


from presets import Presets
from pyrogram.types import Message
from pyrogram import Client, filters
from library.buttons import reply_markup_start

@Client.on_message(filters.private & filters.command(['start', 'help']))
async def start_bot(bot, m: Message):
    await m.reply_text(Presets.WELCOME_MSG.format(m.from_user.first_name),
                       reply_markup=reply_markup_start)
