# with 를 쓰면 꼭 닫기를 하지 않아도 사용이 끝나면 닫아줌
with open('delay.txt', 'r', encoding='utf8') as f:
    for line in f:
        print(line.strip())