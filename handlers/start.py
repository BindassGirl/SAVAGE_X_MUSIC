from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn




@Client.on_message(filters.command("start") & filters.private & ~filters.channel)
async def start(_, message: Message):
    await message.reply_text(
        f"""**Hey, I'm  {bn}, 𝙸 𝙰𝙼 𝙰𝙳𝚅𝙰𝙽𝙲𝙴𝙳 𝙱𝙾𝚃 🤖 𝙲𝚁𝙴𝙰𝚃𝙴𝙳 𝙱𝚈 [𝚂𝙰𝙼𝙴𝙴𝚁](t.me/sameer_795) & [𝚂𝙷𝚁𝚅𝙰𝙽](t.me/shrvan42) ❤️  𝙵𝙾𝚁 𝙿𝙻𝙰𝚈𝙸𝙽𝙶 𝙼𝚄𝚂𝙸𝙲 🎶 𝙸𝙽 𝚈𝙾𝚄𝚁 𝚅𝙾𝙸𝙲𝙴 𝙲𝙷𝙰𝚃𝚂 𝙾𝙵 𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼 𝙶𝚁𝙾𝚄𝙿𝚂 𝙰𝙽𝙳 𝙲𝙷𝙰𝙽𝙽𝙴𝙻𝚂.**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💖𝙲𝚁𝙴𝙰𝚃𝙾𝚁💖", url="https://t.me/SAMEER_795"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "💬𝚂𝚄𝙿𝙿𝙾𝚁𝚃💬", url="https://t.me/SAVAGE_USERBOT"
                    ),
                    InlineKeyboardButton(
                        "⚔️𝙰𝚂𝚂𝙸𝚂𝚃𝙰𝙽𝚃⚔️", url="https://t.me/SAVAGE_MUSIC_BOT_ASSISTANT"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "➕ 𝙰𝙳𝙳 𝙼𝙴 𝙸𝙽 𝚄𝚁 𝙶𝚁𝙿", url="https://t.me/SAVAGE_MUSIC_BOT?startgroup=true"
                    )
                ]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text(
        "💁🏻‍♂️ Do you want to search for a YouTube video?",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✅ Yes", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "No ❌", callback_data="close"
                    )
                ]
            ]
        )
    )
