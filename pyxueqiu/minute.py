# https://stock.xueqiu.com/v5/stock/chart/minute.json?symbol=SZ301070&period=1d
from requests.api import get
from common import Stock, get_data, login
import json

class Minute(Stock):
    '''
    {
    "current": 52.22,
    "volume": 529600,
    "avg_price": 55.078,
    "chg": 24.67,
    "percent": 89.55,
    "timestamp": 1632360600000,
    "amount": 29169057,
    "high": 66,
    "low": 52.22,
    "macd": null,
    "kdj": null,
    "ratio": null,
    "capital": null,
    "volume_compare": {
        "volume_sum": 529600,
        "volume_sum_last": null
    }
}
    '''
    def __init__(self,
                 symbol,
                 current=0.00, 
                 valume=0, 
                 avg_price=0, 
                 chg=0.00, 
                 percent=0.00, 
                 timestamp=None, 
                 amount=0.00, 
                 high=0.00, 
                 low=0.00, 
                 macd=None, 
                 kdj=None, 
                 ratio=None, 
                 capital=None, 
                 vol_sum=0, 
                 vol_sum_last=None):
        self.symbol = symbol
        self.current = current
        self.valume = valume
        self.avg_price = avg_price
        self.chg = chg
        self.percent = percent
        self.timestamp = timestamp
        self.amount = amount
        self.high = high
        self.low = low
        self.macd = macd
        self.kdj = kdj
        self.ratio = ratio
        self.capital = capital
        self.vol_sum = vol_sum
        self.vol_sum_last = vol_sum_last


def minute(symbol):
    # https://stock.xueqiu.com/v5/stock/chart/minute.json?symbol=SZ301070&period=1d

    m_list = []
    params = {
        "symbol": symbol,
        "period": "1d"
    }

    def parse_fun(data):
        j = json.loads(data)
        if j['error_code'] ==  0:
            items = j['data']['items']
            for item in items:
                m = Minute(symbol=symbol)
                m.current = item['current']
                m_list.append(m)
        return m_list
    r = login("https://xueqiu.com")
    m_list = get_data("https://stock.xueqiu.com/v5/stock/chart/minute.json", params=params, parse_fun=parse_fun, cookies=r.cookies)
    return m_list