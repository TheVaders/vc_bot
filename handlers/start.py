from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from helpers.filters import command, other_filters, other_filters2


@Client.on_message(command("start") & other_filters2)
async def start(_, message: Message):
    await message.reply_text(
        f"""🙃 Hi {message.from_user.first_name}!
✨ I am Hêllẞø† Music Player. 
🥳 I can play music in your Telegram Group's Voice Chat😉
⚜️ Use these buttons below to know more. 👇""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⚒ Source code", url="https://github.com/raghuvanshithakur/vc_bot/edit/master/handlers/start.py"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "💬 Group", url="https://t.me/mjsking786"
                    ),
                    InlineKeyboardButton(
                        "Channel 🔈", url="https://t.me/joinchat/UrRD-aX2KYx7pEvW"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "❌ Close ❌", callback_data="close"
                    )
                ]
            ]
        )
    )


@Client.on_message(command("start") & other_filters)
async def start2(_, message: Message):
    await message.reply_text(
        "**Hêllẞø†:** I'm Working!!!\nUse me in Inline to search for a YouTube Video/Music. \n**Happy Streaming**",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🎶 Search 🎶", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "❌ Close ❌", callback_data="close"
                    )
                ]
            ]
        )
    )
