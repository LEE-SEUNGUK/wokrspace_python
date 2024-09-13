import lotto
# 기본 사용 
print(lotto.make_lotto())

# 모듈명을 안써도됨
from math import factorial
print(factorial(10))

# 모든 함수 
from math import *  # * 는 모든을 의미함
print(sqrt(5))

from lotto import lotto_maker as lo   #as 는 별칭을 의미함.
print(lo(20))