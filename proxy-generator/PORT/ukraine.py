import requests
import os
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

def get_proxies(port, country='UA'):
    try:
        url = f'https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country={country}&port={port}'
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            proxies = response.text.split('\r\n')
            return [p.strip() for p in proxies if p.strip()]
        return []
    except Exception as e:
        print(f"\nError fetching proxies: {e}")
        return []

def display_proxies(port):
    proxies = get_proxies(port)
    if not proxies:
        clear_screen()
        print("Proxy Not Found - Gunakan PORT / COUNTRY yang lain")
        sleep(2)
        return
    
    clear_screen()
    print(f"\n{'='*35}")
    print(f"Ukraine Proxy List (Port: {port})")
    print(f"{'='*35}\n")
    
    for proxy in proxies:
        try:
            if ':' in proxy:
                ip, port = proxy.split(':')
            else:
                ip = proxy
                port = port  # Uses the port parameter if no port in proxy string
            
            print(f"IP               : {ip}")
            print(f"PORT             : {port}")
            print("COUNTRY          : Ukraine")
            print("PROTOCOL         : HTTP")
            print(f"{'='*35}")
            sleep(0.1)
        except Exception:
            continue

def ukraine():
    while True:
        display_banner()
        try:
            select = input("select@port~# ").strip()
            if select == '99':
                print("\nKeluar dari program...")
                break
            
            port_map = {
                '01': 8080,
                '02': 53281,
                '03': 3128,
                '04': 80,
                '05': 41258,
                '06': 20183,
                '07': 9000,
                '08': 8081,
                '09': 8060,
                '10': 8118,
                '11': 41766
            }
            
            if select in port_map:
                display_proxies(port_map[select])
                input("\nPress Enter to continue...")
            else:
                print("\nPilihan tidak ada")
                sleep(2)
        except KeyboardInterrupt:
            print("\nKeluar dari program...")
            break
        except Exception as e:
            print(f"\nError: {e}")
            sleep(2)

if __name__ == "__main__":
    ukraine()