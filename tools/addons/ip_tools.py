"""This module provides functions to analyze network matters."""

import ipaddress
import os
import re
import socket
import sys
from functools import cache
from time import sleep
from typing import List
from urllib.parse import urlparse

import requests
from colorama import Fore as F
from requests.exceptions import Timeout
from scapy.all import srp
from scapy.layers.l2 import ARP, Ether

def __is_cloud_flare(target: str) -> None:
    domain, _ = get_target_domain(target)
    try:
        origin = socket.gethostbyname(domain)
        iprange = requests.get("https://www.cloudflare.com/ips-v4", timeout=10).text
        ipv4 = [row.rstrip() for row in iprange.splitlines()]
        for ip in ipv4:
            if ipaddress.ip_address(origin) in ipaddress.ip_network(ip):
                print(
                    f"\n{F.RED}[!] {F.CYAN}Trang web này được bảo vệ bởi CloudFlare, cuộc tấn công này có thể không mang lại kết quả như mong muốn.{F.RESET}"
                )
                sleep(1)
    except (Timeout, socket.gaierror):
        print(
            f"{F.RED}\n[!] {F.CYAN}Không thể kiểm tra tính năng bảo vệ của CloudFlare!.{F.RESET}"
        )
        sleep(1)

def get_target_address(target: str) -> str:
    url = set_target_http(target)
    __is_cloud_flare(url)
    return url

def set_target_http(target: str) -> str:
    if not target.startswith("http"):
        target = f"http://{target}"
    return target

def get_target_domain(target: str) -> str:
    parsed_uri = urlparse(target)
    try:
        domain, port = parsed_uri.netloc.split(":")
    except ValueError:
        domain, port = parsed_uri.netloc, 80
    return domain, int(port)

def get_host_ip() -> str:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(0)
    try:
        s.connect(("8.8.8.8", 80))
        IP = s.getsockname()[0]
    except OSError:
        print(
            f"{F.RED}│   └───{F.MAGENTA}[!] {F.BLUE}Không thể tìm thấy IP cục bộ!{F.RESET}"
        )
        sys.exit(1)
    finally:
        s.close()
    return IP

def show_local_host_ips() -> None:
    print(f"{F.RED}│   │")
    print(
        f"{F.YELLOW}│   ├───{F.MAGENTA} [!] {F.LIGHTCYAN_EX}Đang quét mạng cục bộ...{F.RESET}"
    )
    print(f"{F.RED}│   │")
    print(f"{F.RED}│   ├───{F.BLUE} Máy chủ có sẵn:{F.RESET}")
    print(f"{F.RED}│   │")

    try:
        for host in __get_local_host_ips()[1:-1]:
            print(f"{F.RED}│   │    {F.GREEN} {host}{F.RESET}")
        print(f"{F.RED}│   │")
    except IndexError:
        print(f"{F.RED}│   ├───{F.MAGENTA} [!] {F.RED}Không có máy chủ nào khả dụng!{F.RESET}")

@cache
def __get_local_host_ips() -> List[str]:
    report = (
        os.popen(f"nmap -sP {'.'.join(get_host_ip().split('.')[:3]) + '.1-255'}")
        .read()
        .split("\n")
    )
    pattern = re.compile(r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})")
    hosts: List[str] = []
    for line in report:
        match = pattern.search(line)
        if match:
            hosts.append(match.group(0))
    return hosts

@cache
def __get_mac(target: str) -> str:
    while True:
        try:
            arp_request = ARP(pdst=target)
            broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
            packet = broadcast / arp_request
            ans = srp(packet, timeout=5, verbose=False)[0]
            mac_addr = ans[0][1].hwsrc
            return mac_addr
        except IndexError:
            continue
        except KeyboardInterrupt:
            print(f"{F.RED}Người dùng đã hủy thao tác.{F.RESET}")
            sys.exit(1)
