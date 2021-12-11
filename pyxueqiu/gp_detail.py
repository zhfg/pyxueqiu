# https://xueqiu.com/snowman/provider/zz/gp_detail?symbol=SZ000901

import requests
from retry import retry
import json
from bs4 import BeautifulSoup as BS

def gp_detail_page(ts_code, page):
    datas = []
    ts_code = ts_code
    params = {
        "appn": "detail",
        "action": "data",
        "c": ts_code,
        "p": page
    }

    def parse(content):
        datas = []
        if content != b'':    
            data_str = content[27:-2]
            data_lines = data_str.split(b'|')
            for line in data_lines:
                datas.append(line.split(b'/'))
        return datas
    datas = get_data("https://stock.gtimg.cn/data/index.php", params, parse)
        
    return datas

def gp_detail(ts_code):
    datas = []
    for page in range(0, 60):
        data = gp_detail_page(ts_code, page)
        if data is None:
            break
        datas.append(data)
    return datas

def list_stocks():
    datas = []
    params = {
        "appn": "detail",
        "order": "desc",
        "orderby": "percent",
        "order_by": "percent",
        "size": 5000,
        "market": "CN",
        "type": "sh_sz",
        "_": 1630663053268,
        "p": 1
    }

    def parse(content):
        datas = []
        j = json.loads(content)
        error = get_item(j,'error_code')
        if error == 0:
            data = get_item(j, 'data')
            print(data)



    datas = get_data("https://xueqiu.com/service/v5/stock/screener/quote/list", params, parse)

def get_data(url, params, parse_fun):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
    }
    try:
        r = requests.get(url=url, headers=headers, params=params)
    except Exception as e:
        print(e)
    if r.status_code == 200:
        if r.content != b'':    
            return parse_fun(r.content)
    return None

def get_item(data, key):
    keys = data.keys()
    if key in keys:
        return data[key]
    else:
        return None

def daily_detail(ts_code):
    details = {}

    def has_class(tag, class_name):
        return tag.has_attr(class_name)

    url = "https://xueqiu.com/S/%s" % ts_code
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
    }
    try:
        r = requests.get(url=url, headers=headers)
        if r.status_code == 200:
            b = BS(r.content, 'html.parser')
            close = b.find_all(class_="quote-container")[0].find_all(class_="stock-current")[0].find_all("strong")[0].string
            info_tags = b.find(class_="quote-container").find("table").find_all("td")
            for tag in info_tags:
                print(tag)
                content = tag.contents
                name = content[0]
                n_tag = content[1]
                if name == "最高：":
                    print(n_tag)
            
    except Exception as e:
        print(e)

    return details

if __name__ == "__main__":
    daily_detail("SH600635")
    # list_stocks()
    # print(gp_detail("sz300569"))