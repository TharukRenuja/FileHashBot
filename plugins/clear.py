from config import Config
from pyrogram import Client, filters
from helper_func.auth_user_check import AuthUserCheck
from helper_func.force_sub import ForceSub
import os, shutil

@Client.on_message(filters.command(Config.CLEARME_COMMAND))
async def clear(bot, message):
    if await AuthUserCheck(message.chat.id, message.from_user.id):
        # force subscribe +
        if await ForceSub(bot, message) == 400: return
        # force subscribe -
        downloadFolder = os.path.join(Config.DOWNLOAD_DIR, str(message.from_user.id))
        if os.path.isdir(downloadFolder):
            try:
                shutil.rmtree(downloadFolder) # delete folder for user
            except:
                pass
            try:
                os.rmdir(downloadFolder)
            except:
                pass
        await message.reply_text(Config.CLEAR_STR,
                    reply_to_message_id = message.message_id)
    else:
        await message.reply_text(Config.UNAUTHORIZED_TEXT_STR,
                    reply_to_message_id = message.message_id)
