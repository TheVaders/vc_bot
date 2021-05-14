from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_text(
        f"""Selam Ben `{bn}`

Sesli sohbetlerde müzik dinlemenize olanak sağlarım.

Kullanma kılavuzu:
💠 /play - __Parçayı oynatmaya yarayan komut.__
💠 /pause - __Botu durdurmaya yarayan komut.__
💠 /resume - __Botu devam ettirmeye yarayan komut.__
💠 /skip - __Diğer şarkıya geçmeye yarayan komut.__
💠 /stop - __Botu kapatmaya yarayan komut.__

🤖 **Developer by @Zep_Unb**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Sohbet Grubumuz💬", url="https://t.me/DepressionalistChat"
                    ),
                    InlineKeyboardButton(
                        "Kanalımız 📣", url="https://t.me/Depressionalist"
                    )
                ]
            ]
        )
    )
