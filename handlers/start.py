import asyncio

from helpers.filters import command
from config import BOT_NAME as bn, BOT_USERNAME as bu, CHANNEL_UPDATES, SUPPORT_GROUP, OWNER_USERNAME as me, START_IMG
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_message(command("start") & filters.private & ~filters.group & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_sticker("CAACAgQAAxkBAAICnmNPw5ORQsh-E3CFX7KZIvK3cytcAALsCgACvyLZUYAtqvCiyckiKgQ")
    await message.reply_photo(
        photo=f"{START_IMG}",
        caption=f""" ** ʜᴇʏ {message.from_user.mention()} , 🥀\n\n
๏ ᴛʜɪs ɪs [{bn}](t.me/{bu}) ,  !
 ᴀ ᴩᴏᴡᴇʀғᴜʟ ᴍᴜsɪᴄ ᴩʟᴀʏᴇʀ ʙᴏᴛ ᴡɪᴛʜ sᴏᴍᴇ ᴀᴡᴇsᴏᴍᴇ ᴀɴᴅ ᴜsᴇғᴜʟ ғᴇᴀᴛᴜʀᴇs.

ᴀʟʟ ᴏғ ᴍʏ ᴄᴏᴍᴍᴀɴᴅs ᴀʀᴇ ʟɪsᴛᴇᴅ\n ɪɴ ᴛʜᴇ /help ʙᴜᴛᴛᴏɴ. ** """,
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✚ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ✚ ", url=f"https://t.me/{bu}?startgroup=true"
                       ),
                 ],[
                    InlineKeyboardButton(
                        "📨 ᴜᴘᴅᴀᴛᴇ ", url=f"https://t.me/{CHANNEL_UPDATES}"
                    ),
                    InlineKeyboardButton(
                        "📨 sᴜᴘᴘᴏʀᴛ ", url=f"https://t.me/{SUPPORT_GROUP}"
                    )
                  ],[
                    InlineKeyboardButton(
                        "👤 ʙᴏᴛ ᴏᴡɴᴇʀ ", url=f"https://t.me/{me}"
                    ),
                    InlineKeyboardButton(
                        "👨‍💻 ᴅᴇᴠᴇʟᴏᴘᴇʀ ", url=f"https://t.me/Prince_ariyan_143"
                    ),
                  ],[
                    InlineKeyboardButton(
                        "✅ ɪɴʟɪɴᴇ ", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "💡 ʙᴏᴛ ʀᴇᴘᴏ", url="https://github.com/Prince-ariyan-143/DarkxMusic"
                    )]
            ]
       ),
    )

