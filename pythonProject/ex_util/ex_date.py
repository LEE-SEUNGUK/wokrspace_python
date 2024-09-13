import datetime
import calendar
from calendar import firstweekday

# 현재 날짜와 시간
now = datetime.datetime.now()
print(now)
# 특정 날짜와 시간
dday = datetime.datetime(2025, 1, 17 , 17, 50)
print(dday)
# 오늘 날짜
today = datetime.date.today()
print(today)
# 날짜와 시간을 문자열로 반환
formatted = now.strftime('%Y-%m-%d %H:%M:%S')
print(formatted)

# 문자를 날짜로
str_to_dt = datetime.datetime.strptime("2024-08-02",
                                       "%Y-%m-%d")
print(str_to_dt)
st_date = datetime.date(2024, 1, 1)
end_date = datetime.date(2024, 2, 10)
delta = end_date - st_date
print(delta)
print('요일: ', end_date.weekday()) # 월: 0, 화: 1

year = 2024
month = 9
first_weekday , num_days = calendar.monthrange(year, month)
print(f"{first_weekday}, {num_days}") # 시작 요일, 끝나는 날짜
print("  월 화 수 목 금 토 일")
cnt = 0
for i in range(1, num_days+1):
    print(f"{i:2}", end=" ")  # <-- 옆으로 end 구분하여 출력
    # {i:2} <-- 2자리 차지하도록
    cnt += 1
    if (cnt % 7 == 0):
        print("")
