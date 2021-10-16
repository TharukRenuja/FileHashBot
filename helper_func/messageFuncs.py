import asyncio
from pyrogram.errors.exceptions.bad_request_400 import MessageNotModified
from pyrogram.types import Message
from pyrogram.errors import FloodWait

async def sendMessage(toReplyMessage: Message, replyText):
    try:
        return await toReplyMessage.reply_text(replyText,
            disable_web_page_preview=True, quote=True)
    except FloodWait as e:
        await asyncio.sleep(e.x)
        await sendMessage(toReplyMessage)

async def editMessage(toEditMessage: Message, editText):
    try:
        return await toEditMessage.edit(text=editText,
            parse_mode='markdown')
    except FloodWait as e:
        await asyncio.sleep(e.x)
        await editMessage(toEditMessage)
    except MessageNotModified as e:
        pass
