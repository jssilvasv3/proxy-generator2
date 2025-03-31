import requests
import os
import sys
from time import sleep

def bangladesh():
    os.system('clear')
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
    
    try:
        select = int(input("select@port~#"))
    except ValueError:
        print("\nPilihan harus berupa angka!")
        sys.exit()

    ports = {
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
        11: 41766
    }

    if select == 99:
        print("Keluar ...")
        sys.exit()
    elif select not in ports:
        print("\nPilihan tidak ada")
        sys.exit()

    port = ports[select]
    
    try:
        # Usando ProxyScrape como fonte alternativa para Bangladesh
        url = f"https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=BD&port={port}"
        r = requests.get(url, timeout=10)
        
        if not r.text.strip():
            os.system('clear')
            print("Proxy Not Found - Gunakan PORT / COUNTRY yang lain")
            sys.exit()

        proxies = [p for p in r.text.splitlines() if p]
        
        os.system('clear')
        print("==================================")
        
        for proxy in proxies[:25]:  # Limita a 25 proxies
            if ':' in proxy:
                ip, port = proxy.split(':')
                print(f"IP               : {ip}")
                print(f"PORT             : {port}")
                print(f"COUNTRY          : Bangladesh")
                print(f"CONNECTION SPEED : N/A ms")  # ProxyScrape não fornece tempo de conexão
                print("==================================")
                sleep(0.1)
                
    except requests.exceptions.RequestException as e:
        print(f"Error: Gagal terhubung ke server proxy ({str(e)})")
        sys.exit()
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit()

if __name__ == "__main__":
    bangladesh()