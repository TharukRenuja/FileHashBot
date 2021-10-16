from pyrogram import Client, filters
from config import Config
import psutil
import shutil
import logging
import time
from helper_func.auth_user_check import AuthUserCheck
from helper_func.force_sub import ForceSub
from helper_func.progress import HumanBytes, ReadableTime

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'), logging.StreamHandler()],
    level=logging.INFO)
LOGGER = logging.getLogger(__name__)

@Client.on_message(filters.command(Config.STATS_COMMAND))
async def shell(client, message):
    if await AuthUserCheck(message.chat.id, message.from_user.id):
        # force subscribe +
        FSub = await ForceSub(client, message)
        if FSub == 400:
            return
        # force subscribe -
        try:
            currentTime = ReadableTime(time.time() - Config.botStartTime)
            total, used, free = shutil.disk_usage('.')
            total = HumanBytes(total)
            used = HumanBytes(used)
            free = HumanBytes(free)
            sent = HumanBytes(psutil.net_io_counters().bytes_sent)
            recv = HumanBytes(psutil.net_io_counters().bytes_recv)
            cpuUsage = psutil.cpu_percent(interval=0.5)
            memory = psutil.virtual_memory().percent
            disk = psutil.disk_usage('/').percent
            stats = f'<b>Bot Uptime:</b> <code>{currentTime}</code>\n' \
                f'<b>Total Disk Space:</b> <code>{total}</code>\n' \
                f'<b>Used:</b> <code>{used}</code> ' \
                f'<b>Free:</b> <code>{free}</code>\n\n' \
                f'<b>Upload:</b> <code>{sent}</code>\n' \
                f'<b>Download:</b> <code>{recv}</code>\n\n' \
                f'<b>CPU:</b> <code>{cpuUsage}%</code> ' \
                f'<b>RAM:</b> <code>{memory}%</code> ' \
                f'<b>DISK:</b> <code>{disk}%</code>'
            if Config.CHANNEL_OR_CONTACT is not None:
                stats += "\n\n💎 " + Config.CHANNEL_OR_CONTACT
            await message.reply_text(stats, reply_to_message_id = message.message_id)
        except:
            await message.reply_text("🇬🇧 Maybe your shell message was empty.\n🇹🇷 Boş bir şeyler döndü valla.",
                    reply_to_message_id = message.message_id)
            return
            
