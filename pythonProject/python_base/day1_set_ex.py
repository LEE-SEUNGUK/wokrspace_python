# 로또 번호 생성
# 사용자 입력 수량 만큼
# 1 ~ 45의 6자리 로또 번호를 생성하여 출력 하시오.
# 6rodml 1 ~ 45 는 중복이 있으면 안됨 ex) {1, 2, 2, 3, 4, 5} x
import random

# # 비어 있는 set()
ex = set()
#
# # 요소 추가
# ex.add(5)
# print(ex)
#
# # set 길이
# print(len(ex))

msg = int(input("몇 게임을 하실건가요?"))

for i in range(msg):
    ex = set()
    while(len(ex) != 6):
        rand_int = random.randint(1, 45)
        ex.add(rand_int)
    print("행운의 로또 번호", ex)