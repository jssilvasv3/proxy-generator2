import requests
import os
import re
from time import sleep

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_banner():
    clear_screen()
    print("""
 ____                             ____                           _             
|  _ \ _ __ _____  ___   _       / ___| ___ _ __   ___ _ __ __ _| |_ ___  _ __ 
| |_) | '__/ _ \ \/ / | | |_____| |  _ / _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|
|  __/| | | (_) >  <| |_| |_____| |_| |  __/ | | |  __/ | | (_| | || (_) | |   
|_|   |_|  \___/_/\_\\__,  |      \____|\___|_| |_|\___|_|  \__,_|\__\___/|_|   
                     |___/""")
    print("===============================================================================")
    print("|                              Codec By : HVmbl3                              |")
    print("|                    Thanks buat team - Kanc0t Cyber Team                     |")
    print("|                       https://github.com/jssilvasv3                         |")
    print("===============================================================================")
    print("")
    print("    [01] 8080")
    print("    [02] 53281")
    print("    [03] 3128")
    print("    [04] 80")
    print("    [05] 41258")
    print("    [06] 20183")
    print("    [07] 9000")
    print("    [08] 8081")
    print("    [09] 8060")
    print("    [10] 8118")
    print("    [11] 41766")
    print("    [99] Keluar")
    print("")

def get_proxies(port, country='ID'):
    try:
        url = f'https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country={country}&port={port}'
        response = requests.get(url)
        if response.status_code == 200:
            proxies = response.text.split('\r\n')
            return [p for p in proxies if p.strip()]  # Filter out empty entries
        return []
    except Exception as e:
        print(f"Error fetching proxies: {e}")
        return []

def display_proxies(port):
    proxies = get_proxies(port)
    if not proxies:
        clear_screen()
        print("Proxy Not Found - Gunakan PORT / COUNTRY yang lain")
        return
    
    clear_screen()
    print("==================================")
    for proxy in proxies:
        try:
            ip, port = proxy.split(':') if ':' in proxy else (proxy, port)
            print(f"IP               : {ip}")
            print(f"PORT             : {port}")
            print("COUNTRY          : Indonesia")
            print("CONNECTION SPEED : N/A (ProxyScrape doesn't provide speed info)")
            print("==================================")
            sleep(0.1)
        except Exception as e:
            continue

def indonesia():
    display_banner()
    try:
        select = int(input("select@port~#"))
    except ValueError:
        print("\nPilihan tidak valid")
        return
    
    port_map = {
        1: 8080,
        2: 53281,
        3: 3128,
        4: 80,
        5: 41258,
        6: 20183,
        7: 9000,
        8: 8081,
        9: 8060,
        10: 8118,
        11: 41766,
        99: None
    }
    
    if select in port_map:
        if select == 99:
            return
        display_proxies(port_map[select])
    else:
        print("\nPilihan tidak ada")

if __name__ == "__main__":
    indonesia()