import os
import socket
import time
# from win10toast import ToastNotifier

# Windows Meldung in der Taskleiste beim Öffnen des Programms
# toaster = ToastNotifier()
# toaster.show_toast("WauPing", "Wauping Connected", duration=5)

os.system("title WauPing")

RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
RESET = '\033[0m'
UNDERLINE = '\033[4m'
CYAN = '\033[36m'
MAGENTA = '\033[35m'
BLACK = '\033[30m'

def tcp_ping(host, port):
    try:
        socket.create_connection((host, port)).close()
        return True
    except Exception:
        return False

def start():
    os.system("cls")
    print(f"""{GREEN}
          __      _
        o''))____//
         `_/      )
         (_(_/-(_/  
    {RESET}""")
    print(f"""{BLUE}    Welcome to WauPing The big brother from MiauPing.
    Documentation on {RESET} https://github.com/Arctistaiment25""")
    print("")
    choose = input(f"{YELLOW}> ")

    if choose == "-h":
        os.system("cls")
        print(f"""{GREEN}
          __      _
        o''))____//
         `_/      )
         (_(_/-(_/  
    {RESET}""")
        print("")
        print(f"   {BLUE}[wauping -p -t] {RESET} Ping with Delay {MAGENTA}TCP")
        print(f"   {BLUE}[wauping -p] {RESET} Ping without Delay {MAGENTA}TCP")
        print(f"   {BLUE}[wauping -h] {RESET} Help")
        print("")
        input("  Press Enter to go Back")
        start()

    elif choose == "-p -t":
        os.system("cls")
        print(f"""{GREEN}
          __      _
        o''))____//
         `_/      )
         (_(_/-(_/  
    {RESET}""")
        print("")
        ip = input(f"{BLUE}IP>{RESET} ")
        port = int(input(f"{BLUE}PORT>{RESET} "))
        print("")
        
        while True:
            if tcp_ping(ip, port):
                print(f"{RESET} [#]STATUS: {GREEN}Endpoint Online{RESET}")
                time.sleep(1)
            else:
                print(f"{RESET} [#]STATUS: {RED}Endpoint Dead{RESET}")
                time.sleep(1)

    elif choose == "-p":
        os.system("cls")
        print(f"""{GREEN}
          __      _
        o''))____//
         `_/      )
         (_(_/-(_/  
    {RESET}""")

        print("")
        print(f"{RED}THERES NO DELAY BE AWARE")

        print("")
        ip = input(f"{BLUE}IP>{RESET} ")
        port = int(input(f"{BLUE}PORT>{RESET} "))
        print("")
        
        while True:
            if tcp_ping(ip, port):
                print(f"{RESET} [#]STATUS: {GREEN}Endpoint Online{RESET}")
            else:
                print(f"{RESET} [#]STATUS: {RED}Endpoint Dead{RESET}")

start()
