import re, time
from os import environ
from Script import script 

id_pattern = re.compile(r'^.\d+$')

def is_enabled(value, default):
    if value.strip().lower() in ["on", "true", "yes", "1", "enable", "y"]: return True
    elif value.strip().lower() in ["off", "false", "no", "0", "disable", "n"]: return False
    else: return default


# PyroClient Setup 
API_ID = int(environ['API_ID','26570258'])
API_HASH = environ['API_HASH','5517854d3c51b74c6329b742ec31c1dc']
BOT_TOKEN = environ['BOT_TOKEN','6760890249:AAGOeQHjOKx9Edgy_N_lS5_5NwiojAhJr5w']

# Bot settings
WEBHOOK = bool(environ.get("WEBHOOK", True)) # for web support on/off
PICS = (environ.get('PICS' ,'https://graph.org/file/992c0f0bbb2421b00b03b.jpg https://graph.org/file/027f1b1a04b5d1d2d8570.jpg https://graph.org/file/58897113b411ebc9ba6ed.jpg https://graph.org/file/e631893dade5692d00f4a.jpg https://graph.org/file/2ea5956313f9d26ba4e24.jpg https://graph.org/file/cde23078b696aaf00487b.jpg  https://graph.org/file/6a76d821af95489a230bb.jpg https://graph.org/file/6f9d3dfa3b6873d047bed.jpg https://graph.org/file/04c5c87962ed4c8d456a2.jpg https://graph.org/file/bd8965942893832a66a65.jpg https://graph.org/file/57128f6d942c1313f51de.jpg')).split()
UPTIME = time.time()

# Admins, Channels & Users
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '1790510761').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1002116832887').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('AUTH_CHANNEL')
auth_grp = environ.get('AUTH_GROUP')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None

# MongoDB information
DATABASE_URL = environ.get('DATABASE_URL', "mongodb+srv://Filmy:oiKn0AkUrgeBGDFq@rohidasgavit.pbz03z1.mongodb.net/?retryWrites=true&w=majority")
DATABASE_NAME = environ.get('DATABASE_NAME', "Telegram")
FILE_DB_URL = environ.get("FILE_DB_URL", DATABASE_URL)
FILE_DB_NAME = environ.get("FILE_DB_NAME", DATABASE_NAME)
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

# Filters Configuration 
MAX_RIST_BTNS = int(environ.get('MAX_RIST_BTNS', "10"))
START_MESSAGE = environ.get('START_MESSAGE', script.START_TXT)
BUTTON_LOCK_TEXT = environ.get("BUTTON_LOCK_TEXT", script.BUTTON_LOCK_TEXT)
FORCE_SUB_TEXT = environ.get('FORCE_SUB_TEXT', script.FORCE_SUB_TEXT)

WELCOM_PIC = environ.get("WELCOM_PIC", "")
WELCOM_TEXT = environ.get("WELCOM_TEXT", script.WELCOM_TEXT)
PMFILTER = is_enabled(environ.get('PMFILTER', "True"), True)
G_FILTER = is_enabled(environ.get("G_FILTER", "True"), True)
BUTTON_LOCK = is_enabled(environ.get("BUTTON_LOCK", "True"), True)
RemoveBG_API = environ.get("RemoveBG_API", "")

# url shortner
SHORT_URL = environ.get("SHORT_URL")
SHORT_API = environ.get("SHORT_API")

# Others
IMDB_DELET_TIME = int(environ.get('IMDB_DELET_TIME', "300"))
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002116832887'))
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'MKV_FILES_ROHESH')
P_TTI_SHOW_OFF = is_enabled(environ.get('P_TTI_SHOW_OFF', "True"), True)
PM_IMDB = is_enabled(environ.get('PM_IMDB', "True"), True)
IMDB = is_enabled(environ.get('IMDB', "True"), True)
SINGLE_BUTTON = is_enabled(environ.get('SINGLE_BUTTON', "True"), True)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", "⚡<b>𝙁𝙄𝙇𝙀 𝙐𝙋𝙇𝙊𝘼𝘿𝙀𝘿 𝘽𝙔 [🌟 @𝙁𝙄𝙇𝙈𝙔_𝙍𝙊𝙃𝙀𝙎𝙃_𝙁𝙄𝙇𝙀𝙎™](https://t.me/Filmy_Rohesh_Files)</b>⚡\n\n🎦 <b>File Name: </b> ➥  <i>{file_caption}</i>\n⚙️ <b>Size: </b><i>{file_size}</i>\n\n                ❤️<b>WE LOVE YOU</b>❤️\n🔥  ↭ <b>𝙀𝙉𝙏𝙀𝙍𝙏𝘼𝙄𝙉𝙈𝙀𝙉𝙏 𝙆𝙀 𝙇𝙄𝙔𝙀 𝙅𝙊𝙄𝙉𝙀 𝙆𝘼𝙍𝙀 👁️‍🗨️ [⚜️𝙁𝙄𝙇𝙈𝙔 𝙍𝙊𝙃𝙀𝙎𝙃™⚜️](https://t.me/Filmy_Rohesh)</b> ↭  🔥")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", "⚡<b>𝙁𝙄𝙇𝙀 𝙐𝙋𝙇𝙊𝘼𝘿𝙀𝘿 𝘽𝙔 [🌟 @𝙁𝙄𝙇𝙈𝙔_𝙍𝙊𝙃𝙀𝙎𝙃_𝙁𝙄𝙇𝙀𝙎™](https://t.me/Filmy_Rohesh_Files)</b>⚡\n\n🎦 <b>File Name: </b> ➥  <i>{file_caption}</i>\n⚙️ <b>Size: </b><i>{file_size}</i>\n\n                ❤️<b>WE LOVE YOU</b>❤️\n🔥  ↭ <b>𝙀𝙉𝙏𝙀𝙍𝙏𝘼𝙄𝙉𝙈𝙀𝙉𝙏 𝙆𝙀 𝙇𝙄𝙔𝙀 𝙅𝙊𝙄𝙉𝙀 𝙆𝘼𝙍𝙀 👁️‍🗨️ [⚜️𝙁𝙄𝙇𝙈𝙔 𝙍𝙊𝙃𝙀𝙎𝙃™⚜️](https://t.me/Filmy_Rohesh)</b> ↭  🔥")
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", script.IMDB_TEMPLATE)
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '-1002116832887')).split()]
MELCOW_NEW_USERS = is_enabled(environ.get('MELCOW_NEW_USERS', "True"), True)
PROTECT_CONTENT = is_enabled(environ.get('PROTECT_CONTENT', "False"), False)
PUBLIC_FILE_STORE = is_enabled(environ.get('PUBLIC_FILE_STORE', "True"), True)
LOG_MSG = "{} Iꜱ Rᴇsᴛᴀʀᴛᴇᴅ....✨\n\n🗓️ Dᴀᴛᴇ : {}\n⏰ Tɪᴍᴇ : {}\n\n🖥️ Rᴇᴏᴩ: {}\n🉐 Vᴇʀsɪᴏɴ: {}\n🧾 Lɪᴄᴇɴꜱᴇ: {}\n©️ Cᴏᴩʏʀɪɢʜᴛ: {}"






