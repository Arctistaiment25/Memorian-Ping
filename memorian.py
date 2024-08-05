import os
import socket
import time
import subprocess
from ipwhois import IPWhois
from ipwhois.exceptions import IPDefinedError, ASNRegistryError

os.system("title Memorian Ping")

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
        socket.create_connection((host, port), timeout=2).close()
        return True
    except Exception:
        return False

def get_asn_info(ip):
    try:
        obj = IPWhois(ip)
        res = obj.lookup_whois()
        asn = res['asn']
        asn_desc = res['asn_description']
        return asn, asn_desc
    except IPDefinedError:
        return None, "IP is a reserved or private address."
    except ASNRegistryError:
        return None, "ASN information not available."
    except Exception as e:
        return None, f"Error: {str(e)}"

def start():
    os.system("cls" if os.name == "nt" else "clear")
    print(f"""{MAGENTA}
         @@@     @@@    
         @@@,   @@@@    
         @@@@  ,@@@@    
         @@(@@ @@@@@    
         @@( @@@ @@@    
         @@(  @  @@@    
         @@(     @@@  
    {RESET}""")
    print(f"""{BLUE}    Welcome to Memorian Ping.
    Documentation on {RESET} https://github.com/Arctistaiment25""")
    print("")
    choose = input(f"{YELLOW}> ")

    if choose == "-h":
        os.system("cls" if os.name == "nt" else "clear")
        print(f"""{MAGENTA}
         @@@     @@@    
         @@@,   @@@@    
         @@@@  ,@@@@    
         @@(@@ @@@@@    
         @@( @@@ @@@    
         @@(  @  @@@    
         @@(     @@@  
    {RESET}""")
        print("")
        print(f"   {MAGENTA}[Memorian ping -p -t] {RESET} Ping with Delay {MAGENTA}TCP")
        print(f"   {MAGENTA}[Memorian ping -p] {RESET} Ping without Delay {MAGENTA}TCP")
        print(f"   {MAGENTA}[Memorian ping -h] {RESET} Help")
        print("")
        input("  Press Enter to go Back")
        start()

    elif choose == "-p -t":
        os.system("cls" if os.name == "nt" else "clear")
        print(f"""{MAGENTA}
         @@@     @@@    
         @@@,   @@@@    
         @@@@  ,@@@@    
         @@(@@ @@@@@    
         @@( @@@ @@@    
         @@(  @  @@@    
         @@(     @@@  
    {RESET}""")
        print("")
        timeout = input(f"{BLUE}Timeout> JUST SKIP (IN WORK){RESET}")
        ip = input(f"{BLUE}IP>{RESET} ")
        port = input(f"{BLUE}PORT>{RESET} ")
        print("")

        asn, asn_desc = get_asn_info(ip)
        while True:
            if tcp_ping(ip, port):
                print(f"{MAGENTA} [Memorian Ping] {RESET}[End-Point {GREEN}Online{RESET}] \n      [{CYAN}ASN: {asn} - {asn_desc}{RESET}]\n        [{CYAN}IP: {ip}{RESET}]\n         [{CYAN}Port: {port}{RESET}]\n ")
            else:
                print(f"{MAGENTA} [Memorian Ping] {RESET}[End-Point {RED}Offline{RESET}] \n      [{CYAN}ASN: {asn} - {asn_desc}{RESET}]\n        [{CYAN}IP: {ip}{RESET}]\n         [{CYAN}Port: {port}{RESET}]\n ")
            time.sleep(1)

    elif choose == "-p":
        os.system("cls" if os.name == "nt" else "clear")
        print(f"""{MAGENTA}
         @@@     @@@    
         @@@,   @@@@    
         @@@@  ,@@@@    
         @@(@@ @@@@@    
         @@( @@@ @@@    
         @@(  @  @@@    
         @@(     @@@  
    {RESET}""")

        print("")
        print(f"{RED}THERES NO DELAY BE AWARE")

        print("")
        ip = input(f"{BLUE}IP>{RESET} ")
        port = int(input(f"{BLUE}PORT>{RESET} "))
        print("")

        asn, asn_desc = get_asn_info(ip)
        while True:
            if tcp_ping(ip, port):
                print(f"{MAGENTA} [Memorian Ping] {RESET}[End-Point {GREEN}Online{RESET}] \n      [{CYAN}ASN: {asn} - {asn_desc}{RESET}]\n        [{CYAN}IP: {ip}{RESET}]\n         [{CYAN}Port: {port}{RESET}]\n ")
            else:
                print(f"{MAGENTA} [Memorian Ping] {RESET}[End-Point {RED}Offline{RESET}] \n      [{CYAN}ASN: {asn} - {asn_desc}{RESET}]\n        [{CYAN}IP: {ip}{RESET}]\n         [{CYAN}Port: {port}{RESET}]\n ")

start()