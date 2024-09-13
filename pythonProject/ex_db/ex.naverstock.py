import requests
import cx_Oracle
import requests
conn = cx_Oracle.connect("member", "member", "localhost:1521/xe")
print(conn.version)
sql = """
    INSERT INTO stocks
    (itemcode, stock_name, close_price) VALUES(:item, :name, :price)
"""

cur = conn.cursor()

for i in range(1, 46):
    url = f"https://m.stock.naver.com/api/stocks/marketValue/KOSPI?page={i}&pageSize=50"
    res = requests.get(url)
    if res.status_code == 200:
        data = res.json()
        arr = data['stocks']
        for v in arr:
            # itemCode, stockName, closePrice
            d = {'item' : v['itemCode'], 'name' :  v['stockName'], 'price' : v['closePrice'].replace(',','')}
            cur.execute(sql, d)

conn.commit()
cur.close()
conn.close()