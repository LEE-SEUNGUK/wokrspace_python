import random
# random 난수 생성 관련 기능 제공
# 업다운 게임
# 3번의 기회
# 사용자 입력이 맞으면 '정답', 작으면 '업', 크면 '다운' 출력
# 틀릴때 마다 몇번의 기회가 있는지 출력
print(("*" * 10) + " 업다운 게임 " + ("*" * 10))
com_num = random.randint(1, 10) # 1 ~ 10 사이 정수 리턴

count = 3

while(count != 0):
    msg = int(input("1~ 10 사이의 정수를 입력하세요:"))
    if msg == com_num:
        print("정답입니다")
        break
    elif msg > com_num:
        print("다운")
    else:
        print("업")
    count -= 1
    if count != 0:
        print("남은 기회", count)
    else:
        print("다음 기회에...정답은", com_num)

