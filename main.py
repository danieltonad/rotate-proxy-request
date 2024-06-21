import requests


def spin():
    res= requests.get('https://ipinfo.io/json')
    result = res.json()
    print(result.get('ip'))
    
spin()