import requests
from typing import Optional, Dict


def get_data(url: str) -> Optional[Dict]:

    try:
        r = requests.get(url)
        return r.json()

    except Exception as e:
        print(f"There is an issue accessing {url}")

