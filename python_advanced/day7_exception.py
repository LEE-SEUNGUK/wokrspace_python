'''
    python에서 예외 처리는 프로그램이 실행되는 도중 발생할 수 있는 오류나 예외 상황을 관리하는 방법
    'try' 블록에서 오류가 발생하면 해당 오류를 'except' 블록에서 잡아 처리할 수 있음
'''

# 기본 구조
print("프로그램 시작")
try:
    print("1")
    result = 10 / 0
    print("2")
except ZeroDivisionError as e:
    print(f"예외 발생: {e}")
print("프로그램 종료")

def test(values):
    sum = 0
    try:
        sum = values[0] + values[1]
    except IndexError as e:
        print(f"index error 구간: {e}") # index 오류만
    except Exception as e:
        print(f"모든 error: {e}") # 모든 에러 상황
    else:
        print("에러없음") # 에러 없을때 수행
    finally:
        print(sum) # 정상, 오류 모두 수행되는 부분

test(True)