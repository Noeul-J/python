import datetime
from dateutil.relativedelta import relativedelta

today = datetime.date.today()
next_month = today + relativedelta(months=1)
next_month_fday = next_month.strftime('%y%m01')
print(next_month_fday)
next_month_fday = datetime.datetime.strptime(next_month_fday,'%y%m01')
lastday = next_month_fday - datetime.timedelta(days=1)
lastday_date = lastday.strftime('%a')
# lastday_date = lastday.strftime('%m%d')
print(lastday_date)

delta_key = {"Mon": -1, "The": -2, "Wed": -3, "Thu": -4, "Fri": -5, "Sat": -6, "Sun": 0}

last_sun = lastday + datetime.timedelta(days=delta_key[lastday_date])
pre_sun = last_sun - datetime.timedelta(days=7)
pre_sun_date = pre_sun.strftime('%y%m%d')
print(pre_sun_date)


# 오늘이 월요일이고 && 어제가 마지막 일요일이면
# E:F 열을 G:H로 복사하고
# E2~E9 까지 마지막주 데이터를 복사
# E10부터 E37까지 날짜 데이터 입력
