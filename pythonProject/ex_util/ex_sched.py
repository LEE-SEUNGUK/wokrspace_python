# pip install apscheduler
from apscheduler.schedulers.blocking import  BlockingScheduler
from datetime import datetime
import  pytz
seoul = pytz.timezone("Asia/Seoul")

# interval 반복적으로 실행
# cron: 원하는 시간, 다양한 시간에 실행
def fn_interval():
    print("interval")

def fn_cron():
    print("cron")
    print(datetime.now())

sched = BlockingScheduler()
sched.add_job(fn_interval, 'interval', seconds = 2, timezone=seoul) # 2초에 한번씩 호출

                                     # 매주 월 ~ 금 16:12 분 호출
sched.add_job(fn_cron, 'cron', day_of_week = 'mon-fri', hour = '16', minute='12', timezone=seoul)
sched.start() # 스케줄러가 시작하는 순간 더 이상 아래 코드는 실행하지 않고 위를 반복하기 때문에 아래 구문은 실행되지 않는다
# sched.shutdown() 스케줄러 종료 