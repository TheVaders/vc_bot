from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_text(
        f"""Selam Ben **{bn}**

__Sesli sohbetlerde müzik dinlemenize olanak sağlarım.__

          **📜Kullanma Kılavuzu📜**

💠 /play - __Şarkıyı oynatır.__
💠 /pause - __Şarkıyı durdurur.__
💠 /resume - __Şarkıyı devam ettirir.__
💠 /skip - __Diğer şarkıya geçer.__
💠 /stop - __Botu kapatır.__
💠 /song - __Şarkı aratır.__

**Grubunuza özel müzik botu yaptırabilirsiniz. Detaylı bilgi için @MoolRehber kanalına göz atabilirsiniz.**

🤖 **@Zep_Unb tarafından @ZeroKeyStore grubuna özel kodlanmıştır.**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Sohbet Grubumuz💬", url="https://t.me/ZeroKeyStore"
                    ),
                    InlineKeyboardButton(
                        "Özel Bot Yaptırmak İçin", url="https://t.me/Zep_Unb"
                    )
                ]
            ]
        )
    )
