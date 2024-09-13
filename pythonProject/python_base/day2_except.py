'''
    try 블록에서 오류가 발생하면
    except 블록에서 잡아서 처리 할 수 있음
    finally: 오류, 정상 모두 마지막에 실행
    else: 정상만 실행
'''
print("프로그램 시작")
try:
    print("1")
    # result = 10 / 0
    a = "팽수"
    print(a[2])
    print("2")
except ZeroDivisionError as e:
    print(f"0을 왜 나눠 {e} 가 발생 했잖아")
except Exception as e: # Exception(어떠한 오류든)
    print(f"{e}가 발생")
else:
    print("난 정상 일때만 등장해")
finally:
    print("오류가 나도, 정상 처리가 되도 난 무조건 나와")
print("프로그램 종료")