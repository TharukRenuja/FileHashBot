from config import Config
from pyrogram import Client, filters
from helper_func.auth_user_check import AuthUserCheck
from helper_func.force_sub import ForceSub

@Client.on_message(filters.command(Config.HELP_COMMANDS))
async def start(bot, update):
    if await AuthUserCheck(update.chat.id, update.from_user.id):
        # force subscribe +
        if await ForceSub(bot, update) == 400: return
        # force subscribe -
        await update.reply_text(Config.START_TEXT_STR, reply_to_message_id = update.message_id)
    else:
        await update.reply_text(Config.UNAUTHORIZED_TEXT_STR, reply_to_message_id = update.message_id)
