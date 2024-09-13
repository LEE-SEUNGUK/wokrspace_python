import requests
# 현재 환율 api
# USD 1달러 기준 각 국가의 환율정보 json으로 리턴
# url = "http://open.er-api.com/v6/latest/USD"
# res = requests.get(url)
# data = res.json()
# print(data)

# 달러 to 한화 함수를 작성해주세요
# input: 달러 금액 (ex: 10)
# output: 원화 금액 (ex: 13421.04544)

def fn_to_krw(d_money):
    url = "http://open.er-api.com/v6/latest/USD"
    res = requests.get(url)
    data = res.json()
    korean = data['rates']['KRW']
    k_money = d_money * korean
    return k_money
print(fn_to_krw(10))
print(fn_to_krw(220.91))

