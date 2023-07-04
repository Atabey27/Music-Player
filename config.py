from os import getenv

from dotenv import load_dotenv

load_dotenv()
que = {}
SESSION_NAME = getenv("Userbot")
BOT_TOKEN = getenv("6374624814:AAEKpIzru9w_ww4Oz5G8fvn7ueA5h1IJWTc")
BOT_USERNAME = getenv("Muzikcalarxbot")
admins = {}
API_ID = int(getenv("1148427"))
API_HASH = getenv("362406c73185652edcf9942fde49719c")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "10"))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())
SUDO_USERS = list(map(int, getenv("1285704630").split()))
