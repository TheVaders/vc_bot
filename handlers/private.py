from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_text(
        f"""Selam Ben {bn}

Sesli sohbetlerde müzik dinlemenize olanak sağlarım.

          📜Kullanma Kılavuzu📜

💠 /play - Şarkıyı oynatır.
💠 /pause - Şarkıyı durdurur.
💠 /resume - Şarkıyı devam ettirir.
💠 /skip - Diğer şarkıya geçer.
💠 /stop - Botu kapatır.
💠 /song - Şarkı aratır.

🤖 @Zep_Unb katkılarıyla Kartex'e hazırlanmıştır.
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Bot Sahibi", url="https://t.me/kartex10711453"
                    ),
                    InlineKeyboardButton(
                        "Bot Yaptırmak İçin", url="https://t.me/MoolRehber"
                    )
                ]
            ]
        )
    ) 
