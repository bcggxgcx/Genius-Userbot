import os
import aiohttp
from os import getenv
from dotenv import load_dotenv
    
if os.path.exists("Internal"):
    load_dotenv("Internal")

aiohttpsession = aiohttp.ClientSession()
admins = {}
que = {}

API_ID = int(getenv("API_ID", "11822563"))
API_HASH = getenv("API_HASH", "12bfd8057541544a482312319d7fe4ae")
BOT_TOKEN = getenv("BOT_TOKEN", "")
STRING_SESSION = getenv("STRING_SESSION", "BAADmM_PkeE1Ka7u9l14uuxmuUmEoUZ25NEXygRAe2jZ6mL7Z2ahVK4cH4Ogo9SFOm6bLelDcM2fevevTGiJW58kOBylU-XfnzvM5528v2oxH6Mv6QFRkFtdp3S-uhwZVhaWvzaax9-cxJXunngAgvgHKQ_UkPKmHk4tH7t1AAOVJDlBvp_86WehUK_7n_RgtYkTE39fvQhrALXZs8yqaU9Xpm4jIkQWdNxIzqSUAbXJuEjkRu49CPoScRev76FF1lRScB0fe8fDQ8_PJCg_9d0bnweqYtJgeqMve_XV-AWSY-QQOKc8FA7_FdBqwIeDtcqIx-UE9nkZFejaIDoov1ysAAAAAUr8w8oA")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "!").split())
MONGO_DB_URL = getenv("MONGO_DB_URL", "mongodb+srv://yalay58680:yalay58680@cluster0.9y14h7v.mongodb.net/")
OWNER_ID = list(map(int, getenv("OWNER_ID", "5553046474").split()))
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1001995914361"))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5553046474").split()))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/XdityaHalder/Genius-Userbot")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "aditya")
