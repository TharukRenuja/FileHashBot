import os
import logging
import time
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'), logging.StreamHandler()],
    level=logging.INFO)
LOGGER = logging.getLogger(__name__)

class Config:
    
    # eğer heroku gibi bir bulut platformunda çalışıyorsa enviroment variables kullanabilirsiniz.
    # enviroment variables kullanırsanız bu dosyada bir değişiklik yapmamalısınız.
    # gömülü konfig için ne yapman gerektiğini anlatmayacağım. python öğren gel

    # requireds +
    BOT_TOKEN = os.environ.get('BOT_TOKEN', '')
    APP_ID = int(os.environ.get('APP_ID', 1111111))
    API_HASH = os.environ.get('API_HASH', '')
    BOT_USERNAME = os.environ.get('BOT_USERNAME','')
    if not BOT_USERNAME.startswith('@'): BOT_USERNAME = '@' + BOT_USERNAME # bu satıra dokunmayın.
    DOWNLOAD_LIMIT = os.environ.get('DOWNLOAD_LIMIT', None)
    if DOWNLOAD_LIMIT == "" or DOWNLOAD_LIMIT == " " or DOWNLOAD_LIMIT == None or DOWNLOAD_LIMIT == "0" or DOWNLOAD_LIMIT == 0: DOWNLOAD_LIMIT = 0 # bu satıra dokunmayın.
    FORCE_SUBSCRIBE_CHANNEL = os.environ.get('FORCE_SUBSCRIBE_CHANNEL','') # force subscribe channel link.
    if FORCE_SUBSCRIBE_CHANNEL == "" or FORCE_SUBSCRIBE_CHANNEL == " " or FORCE_SUBSCRIBE_CHANNEL == None: FORCE_SUBSCRIBE_CHANNEL = None # bu satıra dokunmayın.
    LOGGER.info(f"FORCE_SUBSCRIBE_CHANNEL: {FORCE_SUBSCRIBE_CHANNEL}") # debug
    # requireds -

    # commands +
    HASH_COMMAND = os.environ.get('HASH_COMMAND','hash')
    HASH_COMMAND = [HASH_COMMAND, HASH_COMMAND+BOT_USERNAME] # bu satıra dokunmayın.
    STATS_COMMAND = os.environ.get('STATS_COMMAND','stats')
    STATS_COMMAND = [STATS_COMMAND, STATS_COMMAND+BOT_USERNAME] # bu satıra dokunmayın.
    SHELL_COMMAND = os.environ.get('SHELL_COMMAND','shell')
    SHELL_COMMAND = [SHELL_COMMAND, SHELL_COMMAND+BOT_USERNAME] # bu satıra dokunmayın.
    CLEARME_COMMAND = os.environ.get('CLEARME_COMMAND', "clearme")
    CLEARME_COMMAND = [CLEARME_COMMAND, CLEARME_COMMAND+BOT_USERNAME] # bu satıra dokunmayın.
    # commands -
    
    # non-required +
    OWNER_ID = int(os.environ.get('OWNER_ID', 0)) # give your owner id # if given 0 shell will not works
    AUTH_IDS = [int(x) for x in os.environ.get("AUTH_IDS", "0").split()] # if open to everyone give 0
    DOWNLOAD_DIR = os.environ.get('DOWNLOAD_DIR', 'downloads')
    BUFFER_SIZE = int(os.environ.get('BUFFER_SIZE', 8192)) # buffer for hash
    FINISHED_PROGRESS_STR = os.environ.get('FINISHED_PROGRESS_STR','●')
    UN_FINISHED_PROGRESS_STR = os.environ.get('UN_FINISHED_PROGRESS_STR','○')
    PROGRESSBAR_LENGTH = int(os.environ.get('PROGRESSBAR_LENGTH', 25))
    PROGRESS = "`🔥 Biten Yüzde / Percent: % {0}\n📀 Toplam Boyut / Total Size: {1}\n📤 Biten Boyut / Finished: {2}\n" + \
        "📥 Kalan Boyut / Remaining: {3}\n⚡️ Anlık Hız / Speed: {4}/s\n⌛️ Geçen Süre / Passed: {5}\n⏳ Kalan Süre / Remaining: {6}`"
    ONE_PROCESS_PER_USER = int(os.environ.get('ONE_PROCESS_PER_USER', 1)) # for stability
    UNAUTHORIZED_TEXT_STR = os.environ.get('UNAUTHORIZED_TEXT_STR', "🇹🇷 Bu bot senin için değil ezik.\n🇬🇧 This bot not for you.")
    ONE_PROCESS_PER_USER_STR = os.environ.get('ONE_PROCESS_PER_USER_STR',
        f"\nYou can clear your all files and quee with `/{CLEARME_COMMAND[0]}`," + \
        " Your process quee will be cleared. If any process runnig at now, it can be cancelled. Be careful.\n\n" + \
        "🇹🇷 Medyanızı gönderin ve `/" + HASH_COMMAND[0] + "` ile yanıtlayın." + \
        f"\nTüm dosyalarınızı ve sıranızı `/{CLEARME_COMMAND[0]}` ile temizleyebilirsiniz." + \
        " İşlem sıranız temizlenir. Şu an bir işlem varsa bozulabilir. Dikkatli olun.")
    CHANNEL_OR_CONTACT = os.environ.get('CHANNEL_OR_CONTACT', "HuzunluArtemis") # give your public channel or contact username
    SHOW_PROGRESS_MIN_SIZE_DOWNLOAD = int(os.environ.get('SHOW_PROGRESS_MIN_SIZE_DOWNLOAD', 12*1024*1024)) # for speedy
    DOWNLOADING_STR = os.environ.get('DOWNLOADING_STR',
        "**🇹🇷 İndiriliyor / 🇬🇧 Downloading:**\n\n🎯 Name / Ad: `{}`\n❄️ Size / Boyut: `{}`")
    
    DOWNLOAD_SUCCESS = os.environ.get('DOWNLOAD_SUCCESS',
        "🇹🇷 Dosya indirildi! / 🇬🇧 File downloaded.\n🇹🇷 Geçen Süre / 🇬🇧 Time: `{}`" + \
        "\n\n🇹🇷 Hesaplanıyor, lütfen bekleyin.\n🇬🇧 Calculating, please wait.")
    
    START_TEXT_STR = os.environ.get('START_TEXT_STR',"🇬🇧 Send media and reply with `/" + HASH_COMMAND[0] + "`" + \
        f"\nYou can clear your all files and quee with `/{CLEARME_COMMAND[0]}`," + \
        " Your process quee will be cleared. If any process runnig at now, it can be cancelled. Be careful.\n\n" + \
        "🇹🇷 Medyanızı gönderin ve `/" + HASH_COMMAND[0] + "` ile yanıtlayın." + \
        f"\nTüm dosyalarınızı ve sıranızı `/{CLEARME_COMMAND[0]}` ile temizleyebilirsiniz." + \
        " İşlem sıranız temizlenir. Şu an bir işlem varsa bozulabilir. Dikkatli olun.")
    HASH_SUCCESS = os.environ.get('HASH_SUCCESS',
        "🇹🇷 Dosya toplamları hesaplandı / 🇬🇧 Calculated file hashes\n{}\n\n{}")
    CLEAR_STR = os.environ.get('CLEAR_STR',
        "🇬🇧 You\'re clean like a baby now. I deleted your files.\n🇹🇷 Şimdi bebek gibi tertemizsin. Dosyalarını sildim.")
    JOIN_CHANNEL_STR = os.environ.get('JOIN_CHANNEL_STR',
        "Merhaba / Hi {}\n\n" + \
        "🇬🇧 First subscribe my channel from button, then send /start again.\n" + \
        "🇹🇷 Önce butondan kanala abone ol, sonra bana /start yaz.")
    YOU_ARE_BANNED_STR = os.environ.get('YOU_ARE_BANNED_STR',
        "🇬🇧 You are Banned to use me.\n🇹🇷 Banlanmışsın ezik.\n\nDestek / Support: {}")
    JOIN_BUTTON_STR = os.environ.get('JOIN_BUTTON_STR', "🇬🇧 Join / 🇹🇷 Katıl")
    # non-required -
    botStartTime = time.time() # dont touch
    
    # elleme:
    if CHANNEL_OR_CONTACT is not None:
        if not CHANNEL_OR_CONTACT.startswith('@'):
            CHANNEL_OR_CONTACT = '@' + CHANNEL_OR_CONTACT
        PROGRESS += "\n\n💎 " + CHANNEL_OR_CONTACT
        DOWNLOAD_SUCCESS += "\n\n💎 " + CHANNEL_OR_CONTACT
        START_TEXT_STR += "\n\n💎 " + CHANNEL_OR_CONTACT
        HASH_SUCCESS += "\n💎 " + CHANNEL_OR_CONTACT
    
    # geliştiriciyseniz elleyebilirsiniz:
    HELP_COMMANDS = ['start', 'help','yardim', "yardım", "y","h"]

    # hiç ellemeyin:
    HELP_COMMANDSR = []
    HELP_COMMANDSR = HELP_COMMANDS.copy()
    for x in HELP_COMMANDS:
        HELP_COMMANDSR.append(x + BOT_USERNAME)
    HELP_COMMANDS = HELP_COMMANDSR
    del HELP_COMMANDSR
    # dont touch
    if ONE_PROCESS_PER_USER == 1:
        LOGGER.info("ONE_PROCESS_PER_USER was true")
        del ONE_PROCESS_PER_USER
        ONE_PROCESS_PER_USER = True
    else:
        LOGGER.info("ONE_PROCESS_PER_USER was false")
        del ONE_PROCESS_PER_USER
        ONE_PROCESS_PER_USER = False
    #
    