# -*- coding: utf-8 -*-

from pprint import pprint
import pybitflyer
pub_api = pybitflyer.API()

#Ticker情報の取得
def get_ticker():
    ticker = pub_api.ticker(product_code='FX_BTC_JPY')
    pprint(ticker)

if __name__ == '__main__':
    get_ticker()
    
