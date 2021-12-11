# https://stock.xueqiu.com/v5/stock/chart/minute.json?symbol=SZ301070&period=1d
from requests.api import get
from .common import Stock, get_data, login
import json
import pandas as pd
import time

class Kline(Stock):
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


def kline(symbol, start_date=None, type="day"):
    # https://stock.xueqiu.com/v5/stock/chart/kline.json?symbol=SZ300569&begin=1633745213729&period=day&type=before&count=-28400&indicator=kline,pe,pb,ps,pcf,market_capital,agt,ggt,balance
    # https://stock.xueqiu.com/v5/stock/chart/kline.json?symbol=SZ301070&begin=1633745213729&period=day&type=before&count=-28400&indicator=kline%2Cpe%2Cpb%2Cps%2Cpcf%2Cmarket_capital%2Cagt%2Cggt%2Cbalance
    if start_date is None:
        t = (int(time.time() * 1000)) + 86400000
    else:
        t = int(time.mktime(start_date) * 1000 + 86400000)

    m_list = []
    params = {
        "symbol": symbol,
        "begin": t,
        "period": type,
        "type": "before",
        "count": -10000, 
        "indicator": "kline,pe,pb,ps,pcf,market_capital,agt,ggt,balance"
    }

    def parse_fun(data):
        column = []
        items = []
        df = pd.DataFrame()
        j = json.loads(data)
        if j['error_code'] ==  0:
            column = j['data']['column']
            items = j['data']['item']
            
        if len(items) >= 1:
            df = pd.DataFrame(items, columns=column)
            df.timestamp = pd.to_datetime(df.timestamp, unit='ms', utc=True)

            df.timestamp = df.timestamp.dt.tz_convert("Asia/Shanghai")
            return df
        else:
            return df
        
    try:
        r = login("https://xueqiu.com")
        m_list = get_data("https://stock.xueqiu.com/v5/stock/chart/kline.json", params=params, parse_fun=parse_fun, cookies=r.cookies)
    except Exception as e:
        print(e)
    return m_list
