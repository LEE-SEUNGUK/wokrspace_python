import math
# math 모듈 안에 있는 factorial 함수 호출
print(math.factorial(5))
from math import factorial as f
# math 모듈 안에 있는 factorial 함수를 f로 별칭을 붙여서 호출
print(f(10))
import luck
print(luck.make_lotto())