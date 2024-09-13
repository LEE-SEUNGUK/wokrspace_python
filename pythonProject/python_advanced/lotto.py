# 로또 모듈
import random
# input : x, output : set(로또번호)
def make_lotto():
    user_lotto = set()
    while len(user_lotto) < 6:
        number = random.randint(1, 45)
        user_lotto.add(number)
    return user_lotto
# input : n (생성 수), output : list( 로또 리스트)
def lotto_maker(n):
    lotto_list = []
    for i in range(n):
        lotto_list.append(make_lotto())
    return lotto_list
if __name__ == "__main__":
    # 자체 실행때만 실행됨.
    print(lotto_maker(10))
else:
    print("import해서 사용하는군!")