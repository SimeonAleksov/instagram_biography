from dotenv import load_dotenv
from pathlib import Path

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

URL = "https://i.instagram.com/api/v1/users/{user_id}/info/"

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    'X-IG-App-ID': '936619743392459',
    'Origin': 'https://www.instagram.com',
    'Connection': 'keep-alive',
    'Referer': 'https://www.instagram.com/',
    'Cookie': '',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'TE': 'Trailers'
}
