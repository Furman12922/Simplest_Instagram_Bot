import os
import shutil
from instabot import Bot

# Delete old config to prevent login issues
if os.path.exists("config"):
    shutil.rmtree("config")

bot = Bot()
bot.login(username="baltistanies", password="332454")
# bot.follow('aliza_143427')

bot.upload_photo("C:/Simplest_Instagram_Bot/gilgit baltistan",caption="Beautiful Village in gilgit Baltistan")
