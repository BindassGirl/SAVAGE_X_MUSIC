from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn




@Client.on_message(filters.command("start") & filters.private & ~filters.channel)
async def start(_, message: Message):
    await message.reply_text(
        f"""**Hey, I'm  {bn}, 

        πΈ π°πΌ π°π³ππ°π½π²π΄π³ π±πΎπ π€ π²ππ΄π°ππ΄π³ π±π [bindass girl](t.me/Aarshy) β€οΈ  π΅πΎπ πΏπ»π°ππΈπ½πΆ πΌπππΈπ² πΆ πΈπ½ ππΎππ ππΎπΈπ²π΄ π²π·π°ππ πΎπ΅ ππ΄π»π΄πΆππ°πΌ πΆππΎππΏπ π°π½π³ π²π·π°π½π½π΄π»π.

        π°π³π³ πΌπ΄ πΈπ½ ππ πΆππΎππΏ π°π½π³ π΄π½πΉπΎπ πΌπππΈπ² β€οΈ..
         """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ππ²ππ΄π°ππΎππ", url="https://t.me/Aarshy"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "π¬πππΏπΏπΎπππ¬", url="https://t.me/SAVAGE_USERBOT"
                    ),
                    InlineKeyboardButton(
                        "βοΈπ°πππΈπππ°π½πβοΈ", url="https://t.me/Aarshy"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "β π°π³π³ πΌπ΄ πΈπ½ ππ πΆππΏ", url="https://t.me/Arshuu123_bot?startgroup=true"
                    )
                ]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text(
        "ππ»ββοΈ Do you want to search for a YouTube video?",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "β Yes", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "No β", callback_data="close"
                    )
                ]
            ]
        )
    )
