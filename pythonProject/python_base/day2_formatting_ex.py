# 함수를 작성하세요
# input: 원가, 할인율
# output: 할인금액, 계산 금액
# fn_sales_price

def fn_sales_price(price, sales):
    sales_price = int(price*(sales/100))
    price -= sales_price
    return sales_price, price

원가 = 100000

할인율 = 16

할인금액, 계산금액 = fn_sales_price(원가, 할인율)
print(f"원가 {원가} 원")
print(f"할인 퍼센트: {할인율}%")
print(f"할인 금액: {할인금액:.2f} 원") # 소수좀 둘째자리까지 출력
print(f"계산할 금액: {계산금액} 원")
