import math
import time
from config import Config
from pyrogram.errors.exceptions import FloodWait
from pyrogram.errors import MessageNotModified

async def ProgressForPyrogram(
    current,
    total,
    ud_type,
    message,
    start
):
    now = time.time()
    diff = now - start
    if round(diff % 5.00) == 0 or current == total:
    # if round(current / total * 100, 0) % 5 == 0:
        percentage = current * 100 / total
        speed = current / diff
        elapsed_time = round(diff) * 1000
        time_to_completion = round((total - current) / speed) * 1000
        estimated_total_time = elapsed_time + time_to_completion
        elapsed_time = TimeFormatter(milliseconds=elapsed_time)
        estimated_total_time = TimeFormatter(milliseconds=estimated_total_time)

        progress = "💦 `[{0}{1}]`\n\n".format(
            ''.join([Config.FINISHED_PROGRESS_STR for i in range(math.floor(percentage / (100/Config.PROGRESSBAR_LENGTH)))]),
            ''.join([Config.UN_FINISHED_PROGRESS_STR for i in range(Config.PROGRESSBAR_LENGTH - math.floor(percentage / (100/Config.PROGRESSBAR_LENGTH)))])
            )
        tmp = progress + Config.PROGRESS.format(
            round(percentage, 2),
            HumanBytes(total),
            HumanBytes(current),
            HumanBytes(total-current), # finished bytes
            HumanBytes(speed),
            elapsed_time if elapsed_time != '' else "0s",
            estimated_total_time if estimated_total_time != '' else "0s"
        )
        if percentage != 100:
            try:
                await message.edit(
                    text="{}\n\n{}".format(
                        ud_type,
                        tmp
                    ),
                    parse_mode='markdown'
                )
            except MessageNotModified:
                pass
            except FloodWait as f_e:
                time.sleep(f_e.x)
                await message.edit(
                        text="{}\n\n{}".format(
                            ud_type,
                            tmp
                        ),
                        parse_mode='markdown'
                    )


def HumanBytes(size):
    # https://stackoverflow.com/a/49361727/4723940
    # 2**10 = 1024
    if not size:
        return ""
    power = 2 ** 10
    n = 0
    Dic_powerN = {0: " ", 1: "K", 2: "M", 3: "G", 4: "T"}
    while size > power:
        size /= power
        n += 1
    return str(round(size, 2)) + " " + Dic_powerN[n] + "B"


def TimeFormatter(milliseconds: int) -> str:
    seconds, milliseconds = divmod(int(milliseconds), 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    tmp = ((str(days) + "d, ") if days else "") + \
        ((str(hours) + "h, ") if hours else "") + \
        ((str(minutes) + "m, ") if minutes else "") + \
        ((str(seconds) + "s, ") if seconds else "") + \
        ((str(milliseconds) + "ms, ") if milliseconds else "")
    return tmp[:-2]

def ReadableTime(seconds: int) -> str:
    result = ''
    (days, remainder) = divmod(seconds, 86400)
    days = int(days)
    if days != 0:
        result += f'{days}d'
    (hours, remainder) = divmod(remainder, 3600)
    hours = int(hours)
    if hours != 0:
        result += f'{hours}h'
    (minutes, seconds) = divmod(remainder, 60)
    minutes = int(minutes)
    if minutes != 0:
        result += f'{minutes}m'
    seconds = int(seconds)
    result += f'{seconds}s'
    return result