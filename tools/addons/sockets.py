"""This module provides functions to create socket instances."""

import json
import random
import socket
import sys
import warnings
from typing import Dict, List, Tuple

import requests
import socks
from colorama import Fore as F
from requests.exceptions import ConnectionError, Timeout

from tools.addons.ip_tools import get_target_domain

warnings.filterwarnings("ignore", message="Unverified HTTPS request")

with open("tools/L7/user_agents.json", "r", encoding="utf-8") as agents_file:
    user_agents = json.load(agents_file)["agents"]

def get_socks_proxies() -> List[Dict[str, str]]:
    try:
        response = requests.get(
            "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks5&timeout=10000&country=all&ssl=all&anonymity=all",
            verify=False,
            timeout=10,
        )
        proxies = [{"addr": addr, "port": port} for addr, port in 
                   (proxy.split(":") for proxy in response.text.split("\r\n") if proxy)]
    except (Timeout, ConnectionError):
        print(
            f"\n{F.RED}[!] {F.CYAN}Failed to fetch proxy list. Please check your internet connection and try again.{F.RESET}"
        )
        sys.exit(1)
    return proxies

def get_http_proxies() -> List[Dict[str, str]]:
    try:
        response = requests.get(
            "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all",
            verify=False,
            timeout=10,
        )
        proxies = [{"addr": addr, "port": port} for addr, port in 
                   (proxy.split(":") for proxy in response.text.split("\r\n") if proxy)]
    except (Timeout, ConnectionError):
        print(
            f"\n{F.RED}[!] {F.CYAN}Failed to fetch proxy list. Please check your internet connection and try again.{F.RESET}"
        )
        sys.exit(1)
    return proxies

def get_random_proxy(proxies: List[Dict[str, str]]) -> Dict[str, str]:
    return random.choice(proxies)

def create_socket_proxy(target: str, protocol: str = "socks5") -> Tuple[socket.socket, Dict[str, str]]:
    if protocol.lower() == "socks5":
        proxies = get_socks_proxies()
    elif protocol.lower() == "http":
        proxies = get_http_proxies()
    else:
        raise ValueError("Unsupported protocol. Supported protocols are 'socks5' and 'http'.")

    while True:
        try:
            proxy = get_random_proxy(proxies)
            sock = socks.socksocket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(4)
            sock.set_proxy(socks.SOCKS5, proxy["addr"], int(proxy["port"]))
            connect_socket(target, sock)
            break
        except (socket.timeout, socket.error):
            proxies.remove(proxy)
            if not proxies:
                if protocol.lower() == "socks5":
                    proxies = get_socks_proxies()
                elif protocol.lower() == "http":
                    proxies = get_http_proxies()
                else:
                    raise ValueError("Unsupported protocol. Supported protocols are 'socks5' and 'http'.")
            continue
    return sock, proxy

def create_socket(target: str) -> socket.socket:
    while True:
        try:
            sock = socks.socksocket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(4)
            connect_socket(target, sock)
            break
        except (socket.timeout, socket.error):
            continue
    return sock

def connect_socket(target: str, sock: socket.socket) -> None:
    domain, port = get_target_domain(target)
    try:
        ip = socket.gethostbyname(domain)
        sock.connect((ip, port))
        sock.send(f"GET /?{random.randint(0, 2000)} HTTP/1.1\r\n".encode("utf-8"))
        sock.send(f"User-Agent: {random.choice(user_agents)}\r\n".encode("utf-8"))
        sock.send("Accept-language: en-US,en;q=0.5\r\n".encode("utf-8"))
        sock.send("Accept-Encoding: gzip, deflate\r\n".encode("utf-8"))
    except socket.gaierror:
        print(f"{F.RED}[!] {F.CYAN}Failed to resolve domain: {domain}{F.RESET}")
        sys.exit(1)
    except socket.error as e:
        print(f"{F.RED}[!] {F.CYAN}Socket error: {e}{F.RESET}")
        sys.exit(1)

# Example usage:
if __name__ == "__main__":
    target_domain = "example.com"
    protocol = "socks5"  # or "http"
    socket_proxy, proxy_info = create_socket_proxy(target_domain, protocol)
    print(f"Connected via proxy: {proxy_info['addr']}:{proxy_info['port']}")
