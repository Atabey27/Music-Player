from os import getenv

from dotenv import load_dotenv

load_dotenv()
que = {}
SESSION_NAME = getenv("BAARhgsArX4-KO0WK6QxTi1NIFdn2QVelz8MxwEvHurGLjcwyQqiE8ifw6uyluR1F0O2L21-2UXQ_i1fBd0VkiqOMugRoZS-Y3H3rSpi2n6nFa3X-kT4voEQoE-plUflJvaSEuN4GX5i8UIwXh-ewNH1KRfIj7O9MxQMaKH_hYBZahS_2Pz_lZlXbxMkG190PpkHMzGTKmVK0FL-q9_rehGLf7bG_81M2N11dClxWhVFFQqcCPXILP7htND7mFn6QzvN52SDZmZpuCf7RYVAdiLhEPb_XZkQ4Q2zq5Th36ZD-SHkorafoqF1i03RiStqsujhAI03m_wiVSvF0QNkngVGKy79zAAAAAF79Q4uAQ")
BOT_TOKEN = getenv("6374624814:AAEKpIzru9w_ww4Oz5G8fvn7ueA5h1IJWTc")
BOT_USERNAME = getenv("Muzikcalarxbot")
admins = {}
API_ID = int(getenv("1148427"))
API_HASH = getenv("362406c73185652edcf9942fde49719c")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "10"))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())
SUDO_USERS = list(map(int, getenv("1285704630").split()))
