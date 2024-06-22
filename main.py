import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

PROXIES = []

ACTIVE_PROXIES = []

def load_proxy():
    with open('proxies.txt', 'r') as proxy:
        all = proxy.readlines()
        for p in all:
            PROXIES.append(p.strip('\n'))
load_proxy()  

def save_active_proxy():
    with open('active.txt', 'a') as p:
        for proxy in ACTIVE_PROXIES:
            p.write(f'{proxy} \n')

def spin(proxy: str):
    try:
        res= requests.get('https://ipinfo.io/json', proxies={'https': proxy, 'http': proxy})
        result = res.json()
        # print(result.get('ip'))
        ACTIVE_PROXIES.append(proxy)
        return result.get('ip') + f" [{len(ACTIVE_PROXIES)}]"
    except Exception as e:
        # print(proxy + f" [{len(ACTIVE_PROXIES)}] --Failed")
        return proxy + f" [{len(ACTIVE_PROXIES)}] --Failed"

def filter_active_proxies():
    with ThreadPoolExecutor(max_workers=20) as executor:
        futures = {executor.submit(spin, proxy): proxy for proxy in PROXIES}
        for future in as_completed(futures):
            result = future.result()
            print(result)
    save_active_proxy()
    
# spin("94.79.152.14:80")
filter_active_proxies()
# print(len(PROXIES))