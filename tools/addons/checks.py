"""This module provides functions to check inputs."""

import os
import sys
from typing import Union

import requests
from colorama import Fore as F
from requests.exceptions import ConnectionError, InvalidURL, ReadTimeout

from tools.addons.ip_tools import __get_local_host_ips, set_target_http


def check_method_input() -> str:
    """Check if the method name is valid.

    Returns:
        - method - A valid method name
    """
    valid_methods = [
        "http",
        "http-proxy",
        "slowloris",
        "slowloris-proxy",
        "syn-flood",
        "arp-spoof",
        "disconnect",
        # Add more methods here as needed
    ]
    while True:
        method = input(f"{F.RED}   ● METHOD: {F.RESET}").lower()
        if method in valid_methods:
            if method in ["syn-flood", "arp-spoof", "disconnect"] and os.name == "nt":
                print(
                    f"{F.RED}   ●{F.MAGENTA} [!] {F.BLUE}Phương pháp này không được hỗ trợ trên Windows!{F.RESET}"
                )
            elif method in ["syn-flood", "arp-spoof", "disconnect"] and os.getuid() != 0:
                print(
                    f"{F.RED}   ●{F.MAGENTA} [!] {F.BLUE}Cuộc tấn công này cần đặc quyền Siêu người dùng!"
                )
                print(
                    f"{F.RED}   ●{F.MAGENTA} [!] {F.BLUE}Run: {F.GREEN}sudo {os.popen('which python').read()[:-1]} Tojimari Eru.py\n{F.RESET}"
                )
                sys.exit(1)
            else:
                return method
        else:
            print(
                f"{F.RED}   ●{F.MAGENTA} [!] {F.BLUE}Có Mỗi Cái Method Cũng NHập Sai{F.RESET}"
            )


def check_number_input(x: str) -> int:
    """Check if an input is an integer number greater than zero.

    Args:
        - x - The name of the input field

    Returns:
        - y - A valid value
    """
    while True:
        y = input(f"{F.RED}   ● {x.upper()}: {F.RESET}")
        try:
            y = int(y)
            if y <= 0:
                raise ValueError
        except ValueError:
            print(
                f"{F.RED}   ●{F.MAGENTA} [!] {F.BLUE}Ngáo Lồn À THREADS đéo j mà mày để 0!!!{F.RESET}"
            )
        else:
            return y


def check_http_target_input() -> str:
    """Check if the target is listening on HTTP port (80).

    Returns:
        - formatted_target - A valid target URL
    """
    while True:
        target = input(f"{F.RED}   ● URL: {F.RESET}")
        formatted_target = set_target_http(target)
        try:
            requests.get("https://google.com", timeout=4)
            try:
                requests.get(formatted_target, timeout=4)
            except Exception as exc:
                raise InvalidURL from exc
        except (ConnectionError, ReadTimeout):
            print(
                f"{F.RED}   ●{F.MAGENTA} [!] {F.BLUE}Thiết bị không được kết nối với internet!{F.RESET}"
            )
        except InvalidURL:
            print(
                f"{F.RED}   ●{F.MAGENTA} [!] {F.BLUE}Sai URL Của WEB Hoặc WEB Đã DIE{F.RESET}"
            )
        else:
            return formatted_target


def check_local_target_input() -> str:
    """Check if the target is in the local network.

    Returns:
        - target - A valid target IP address
    """
    hosts = __get_local_host_ips()
    while True:
        target = input(f"{F.RED}   ● IP: {F.RESET}")
        if target in hosts:
            return target
        else:
            print(
                f"{F.RED}   ●{F.MAGENTA} [!] {F.BLUE}Cannot connect to {F.CYAN}{target}{F.BLUE} on the local network! Please enter a valid IP address.{F.RESET}"
            )


def check_dns_input() -> str:
    """Check if the DNS server is accessible.

    Returns:
        - dns_server - A valid DNS server IP address
    """
    while True:
        dns_server = input(f"{F.RED}   ● DNS SERVER: {F.RESET}")
        try:
            socket.gethostbyname(dns_server)
        except socket.gaierror:
            print(
                f"{F.RED}   ●{F.MAGENTA} [!] {F.BLUE}Cannot resolve DNS server {F.CYAN}{dns_server}{F.BLUE}. Please enter a valid IP address.{F.RESET}"
            )
        else:
            return dns_server


def check_file_path_input() -> str:
    """Check if the file path exists.

    Returns:
        - file_path - A valid file path
    """
    while True:
        file_path = input(f"{F.RED}   ● FILE PATH: {F.RESET}")
        if os.path.exists(file_path):
            return file_path
        else:
            print(
                f"{F.RED}   ●{F.MAGENTA} [!] {F.BLUE}File path {F.CYAN}{file_path}{F.BLUE} does not exist! Please enter a valid file path.{F.RESET}"
            )


def check_proxy_input() -> Union[str, None]:
    """Check if the proxy server is accessible.

    Returns:
        - proxy_server - A valid proxy server IP address
    """
    while True:
        proxy_server = input(f"{F.RED}   ● PROXY SERVER: {F.RESET}")
        if proxy_server.strip() == "":
            return None
        try:
            requests.get("https://google.com", proxies={"http": proxy_server, "https": proxy_server}, timeout=4)
        except (ConnectionError, ReadTimeout):
            print(
                f"{F.RED}   ●{F.MAGENTA} [!] {F.BLUE}Cannot connect to proxy server {F.CYAN}{proxy_server}{F.BLUE}. Please enter a valid IP address.{F.RESET}"
            )
        else:
            return proxy_server
