# https://xueqiu.com/service/v5/stock/screener/quote/list?page=1&size=90&order=desc&orderby=percent&order_by=percent&market=CN&type=sh_sz&_=1633675990239
from requests.api import get
from .common import Stock, get_data, login
import json
import pandas as pd
import time


url = "https://xueqiu.com/service/v5/stock/screener/quote/list"
def quote_list():
    m_list = []
    params = {
        "page": 1,
        "size": 10000,
        "order": "asc",
        "orderby": "code",
        "order_by": "symbol",
        "market": "CN",
        "type": "sh_sz",
        "_": 1633675990239
    }

    def parse_fun(data):
        column = []
        items = []
        df = pd.DataFrame()
        j = json.loads(data)
        if j['error_code'] ==  0:
            items = j['data']['list']
            if len(items) >= 1:
                df = df.from_records(items)
        else:
            print(data)
        return df
        
    r = login("https://xueqiu.com")
    m_list = get_data(url, params=params, parse_fun=parse_fun, cookies=r.cookies)
    return m_list
