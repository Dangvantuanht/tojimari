"""This module provides a function that prints the logo's application."""

import os
from colorama import Fore as F

def show_logo() -> None:
    """Print the application logo.

    Args:
        None

    Returns:
        None
    """
    logo = '''
 _____     _ _                      _    _____            
|_   _|__ (_|_)_ __ ___   __ _ _ __(_)  | ____|_ __ _   _ 
  | |/ _ \| | | '_ ` _ \ / _` | '__| |  |  _| | '__| | | |
  | | (_) | | | | | | | | (_| | |  | |  | |___| |  | |_| |     
  |_|\___// |_|_| |_| |_|\__,_|_|  |_|  |_____|_|   \__,_|
        |__/                                                  
            DDoS V1.1                              
    '''
    print(f"{F.RED}{logo}")
    print(f"{F.RED}➤  Youtube: DawnPC")
    print(f"{F.GREEN}➤  Facebook: https://www.facebook.com/profile.php?id=61561394712119")
    print(f"{F.RED}➤  DDOS Tool C2 亗")
    print(f"{F.GREEN}➤ Tojimari Eru 🖥️")
    print(f"{F.RED}➤ Methods|L7: HTTP ● HTTP-PROXY ● SLOWLORIS ● SLOWLORIS-PROXY")
    if os.name != "nt":
        print("╰───╮ LAYER 4: SYN-FLOOD")
        print("╰───╮ LAYER 2: ARP-SPOOF ● DISCONNECT")
    print("╰───╮")
    # Example method
