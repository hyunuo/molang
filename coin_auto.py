# -*- coding: utf-8 -*-
"""
Created on Sun Nov 21 23:50:32 2021

@author: 김현우
"""
import time
import pyupbit
import datetime

access = "NyuaKe2GhC6RZbymM0NBJ5lr8aNq4MzmnC8A44qm"          # 본인 값으로 변경
secret = "sPU1bfBUUxAvHux3M9nQyzJMsL2vcSB2nScx4x9g"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)


def get_current_price(ticker):
    """현재가 조회"""
    return pyupbit.get_current_price(ticker)

def get_balance(ticker):
    """잔고 조회"""
    balances = upbit.get_balances()
    for b in balances:
        if b['currency'] == ticker:
            if b['balance'] is not None:
                return float(b['balance'])
            else:
                return 0
    return 0

def open_price(ticker,x):
    df = pyupbit.get_ohlcv((ticker), interval="minute1")
    if df.open[x] is not None:
        return float(df.open[x])
    else:
        return 0
def close_price(ticker,x):
    df = pyupbit.get_ohlcv((ticker), interval="minute1")
    if df.open[x] is not None:
        return float(df.close[x])
    else:
        return 0

while True:
    try:
        a=pyupbit.get_tickers(fiat="KRW")
        time.sleep(0.1)
        b=pyupbit.get_tickers(fiat="KRW")
        if a!=b:
                
            SetList1 = set(a)
            SetList2 = set(b)
            dif_set = (SetList2 - SetList1)
            dif = list(dif_set)
            krw = get_balance("KRW")
            print(dif.plus)
            if krw > 5000*len(dif):
                for i in range(len(dif)):
                    upbit.buy_market_order(dif[i], krw*0.9995/len(dif))
        
                
                while True:
                    try:
                        for k in range(len(dif)):
                            done_order = upbit.get_order(dif[k], state="done")
                            coin = get_balance(dif[k])
                            minus_persent = (open_price(dif[k],0)-close_price(dif,[0]))/open_price(dif[k])
                            if float(get_current_price(dif[k]))> float(done_order["price"]):
                                if  minus_persent > 10 and coin > 0 :
                
                                    upbit.sell_market_order(dif[k], coin*0.9995/len(dif))
                    except Exception as e:
                        print(e)        
        
    except Exception as e:
        print(e)
    

        




