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
        res= requests.get('https://ipinfo.io/json', proxies={'https': proxy, 'http': proxy}, timeout=20)
        result = res.json()
        ACTIVE_PROXIES.append(proxy)
        return result.get('ip') + f" [{len(ACTIVE_PROXIES)}]"
    except Exception as e:
        return proxy + f" [{len(ACTIVE_PROXIES)}] --Failed"

def test_proxy(proxy: str):
    try:
        res= requests.get('https://ipinfo.io/json', proxies={'https': proxy, 'http': proxy}, timeout=20)
        result = res.json()
        print(result.get('ip'))
    except Exception as e:
        print(proxy + f" -- Failed")

def filter_active_proxies():
    with ThreadPoolExecutor(max_workers=20) as executor:
        futures = {executor.submit(spin, proxy): proxy for proxy in PROXIES}
        for future in as_completed(futures):
            result = future.result()
            print(result)
    save_active_proxy()
    
test_proxy("196.20.125.133:8083")
# filter_active_proxies()
# print(len(PROXIES))