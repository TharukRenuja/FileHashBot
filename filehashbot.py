import logging
import os
from config import Config
from pyrogram import idle
import pyrogram
LOGGER = logging.getLogger(__name__)

if __name__ == '__main__':
    #
    if not os.path.isdir(Config.DOWNLOAD_DIR):
        os.mkdir(Config.DOWNLOAD_DIR)
    #
    plugins = dict(root = 'plugins')
    #
    app = pyrogram.Client("FileHashBot", bot_token = Config.BOT_TOKEN,
        api_id = Config.APP_ID, api_hash = Config.API_HASH, plugins = plugins)
    #
    app.start()
    #
    LOGGER.info(msg="App Started.")
    #
    idle()
    #
    LOGGER.info(msg="App Stopped.")
