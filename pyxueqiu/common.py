import requests

class Stock(object):
    def __init__(self, symbol, name=None):
        self.symbol=symbol
        self.name = name

def login(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
    }
    try:
        r = requests.get(url=url, headers=headers)
        if r.status_code == 200:
            return r
    except Exception as e:
        print(e) 
    return None


def get_data(url, params, cookies, parse_fun):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
    }
    try:
        r = requests.get(url=url, headers=headers, params=params, cookies=cookies)
        # print(r.url)
        if r.status_code == 200:
            if r.content != b'':    
                return parse_fun(r.content)
    except Exception as e:
        print(e)
    
    return None