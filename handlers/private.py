from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_text(
        f"""Selam Ben {bn}

Ülkeme özel kodlanmış sohbetlerde müzik dinlemenize olanak sağlarım.

          📜Kullanma Kılavuzu📜

💠 /oynat - Şarkıyı oynatır.
💠 /durdur - Şarkıyı durdurur.
💠 /devam - Şarkıyı devam ettirir.
💠 /gec - Diğer şarkıya geçer.
💠 /kapat - Botu kapatır.
💠 /sarkiara - Şarkı aratır.

**Küçük bir ücret karşılığında grubunuza özel müzik botu yaptırabilirsiniz. Detaylı bilgi için @MoolRehber kanalına göz atabilirsiniz.**

🤖 Developer by @Zep_Unb
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Sahip İletişim", url="https://t.me/Zep_Unb"
                    ),
                    InlineKeyboardButton(
                        "Destek Kanalı", url="https://t.me/MoolRehber"
                    )
                ]
            ]
        )
    )
