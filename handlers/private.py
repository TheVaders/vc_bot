from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_text(
        f"""Selam Ben **{bn}**

Sesli sohbetlerde müzik dinlemenize olanak sağlarım.

          📜Kullanma Kılavuzu📜

💠 /play - __Parçayı oynatır.__
💠 /pause - __Botu durdurur.__
💠 /resume - __Botu devam ettirmeye yarar.__
💠 /skip - __Diğer şarkıya geçmeye yarar.__
💠 /stop - __Botu kapatmaya yarar.__
💠 /song - __Şarkı aratmaya yarar.__

Küçük bir ücret karşılığında grubunuza özel müzik botu yaptırmak için @Zep_Unb ulaşabilirsiniz.

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
