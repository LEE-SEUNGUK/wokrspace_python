# 반복문 while <조선식>: 이 True 일 경우 반복
i = 1
while i <= 5:
    i += 1
    if i == 2:
        continue # continue를 만나면 하위 내용을 건너 뜀
        # break 를 만나면 반복문 즉시 종료
    print(i)
# python은  증감연산자는 없음(++, --)
flag = True
while flag:
    msg = input("종료(q)")
    if msg == 'q':
        flag = False