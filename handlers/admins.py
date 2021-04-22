from asyncio.queues import QueueEmpty

from pyrogram import Client
from pyrogram.types import Message

import callsmusic

from config import BOT_NAME as BN
from helpers.filters import command, other_filters
from helpers.decorators import errors, authorized_users_only


@Client.on_message(command("pause") & other_filters)
@errors
@authorized_users_only
async def pause(_, message: Message):
    if (
            message.chat.id not in callsmusic.pytgcalls.active_calls
    ) or (
            callsmusic.pytgcalls.active_calls[message.chat.id] == 'paused'
    ):
        await message.reply_text(f"**{BN} :-** Durdurulacak bir şey bulamadım!")
    else:
        callsmusic.pytgcalls.pause_stream(message.chat.id)
        await message.reply_text(f"**{BN} :-** Müzik durduruldu!")


@Client.on_message(command("resume") & other_filters)
@errors
@authorized_users_only
async def resume(_, message: Message):
    if (
            message.chat.id not in callsmusic.pytgcalls.active_calls
    ) or (
            callsmusic.pytgcalls.active_calls[message.chat.id] == 'playing'
    ):
        await message.reply_text(f"**{BN} :-** Devam edilecek bir şey yok!")
    else:
        callsmusic.pytgcalls.resume_stream(message.chat.id)
        await message.reply_text(f"**{BN} :-** Müziğe devam ediliyor!")


@Client.on_message(command("stop") & other_filters)
@errors
@authorized_users_only
async def stop(_, message: Message):
    if message.chat.id not in callsmusic.pytgcalls.active_calls:
        await message.reply_text(f"**{BN} :-** Bot zaten çalışmıyor!")
    else:
        try:
            callsmusic.queues.clear(message.chat.id)
        except QueueEmpty:
            pass

        callsmusic.pytgcalls.leave_group_call(message.chat.id)
        await message.reply_text(f"**{BN} :-** Bot kapatıldı tekrar görüşürüüzzz😉❤️!")


@Client.on_message(command("skip") & other_filters)
@errors
@authorized_users_only
async def skip(_, message: Message):
    if message.chat.id not in callsmusic.pytgcalls.active_calls:
        await message.reply_text(f"**{BN} :-** Geçilecek bir parça bulunamadı!")
    else:
        callsmusic.queues.task_done(message.chat.id)

        if callsmusic.queues.is_empty(message.chat.id):
            callsmusic.pytgcalls.leave_group_call(message.chat.id)
        else:
            callsmusic.pytgcalls.change_stream(
                message.chat.id,
                callsmusic.queues.get(message.chat.id)["file_path"]
            )

        await message.reply_text(f"**{BN} :-** Diğer parçaya geçildi!")
