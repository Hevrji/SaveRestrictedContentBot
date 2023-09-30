#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = config(28414026, default=None, cast=int)
API_HASH = config("595e101e4009da570ae71cae7060d20f", default=None)
BOT_TOKEN = config("6452140286:AAEAOTxVxbiu2i77NnaiMJRfZDExzMrqAME", default=None)
SESSION = config("BQGxkEoASPLfn7uj75CM_PSsSplXM-RCHVobIYZcRNEyCKgH7s4tMlzb1tDY67uDCv-uDTi5EhL3JhCWFlcFufqXwUl5UrrgWRezCJDnEp0RRdnrizgZmmrqKwY3AMYa1iRy86ZDLuYR3Oji54lTy0s0ktAQ8qkCG2xPJqXbPTuc14ROuLnPrx8Yw9UsDeWxtQf_80JRhK8kYNJKf9SkQj6Ap7jhYA68bgLaTb7N9pS1yz4NdW5A4W1A3zR4vh2p30vhqrQbic0SHuGf778fWSluyp78XU-vI8WSZSoh3rowv3HQa5IpY3rHgI8Rkf1rhsCHz6bZYTfvOjEU8eJr9z7_rre1HAAAAABX-gQfAA", default=None)
FORCESUB = config("FORCESUB", default=None)
AUTH = config("AUTH", default=None, cast=int)

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("saverestricted", session_string=SESSION, api_hash=API_HASH, api_id=API_ID) 

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
