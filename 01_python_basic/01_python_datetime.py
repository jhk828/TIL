# * 추가적으로 날짜 관련 사항도 알아보아요
# date, datetime

from datetime import date, datetime

today = date.today()
print(today)        # 2020-07-15

# 오늘 날짜는 : 2020년 07월 15일 입니다.
my_str = "오늘 날짜는 : {}년 {}월 {}일 입니다."
my_str = my_str.format(today.year, today.month, today.day)
print(my_str)

my_datetime = datetime.today()
print(my_datetime)      # 2020-07-15 10:41:12.427045
# 현재 시간은 : 10시 42분 입니다.
print("현재 시간은 : {}시 {}분 입니다.".format(my_datetime.hour, my_datetime.minute))

# 오늘이 07월 15일이에요.
# 내일의 날짜는 07월 16일이에요.   => 이건 쉬워요.

# 오늘이 01월 31일이에요.
# 내일의 날짜는 02월 1일이에요.   => 그래도 할만해요

# 오늘이 03월 01일이에요.
# 어제의 날짜는 02월 29일이에요.   => 어려워욥

## 결론은 날짜 연산은 처리하기가 너무 힘들어서 계산을 통해 처리하는게 아니라
## delta를 이용해서 처리해요!

from datetime import date, datetime, timedelta

today = date.today()     # 오늘 날짜를 구해요!
days = timedelta(days=-20)
print(today + days)     # 2020-06-25 , 차이값에 델타값 (하루 전)을 더해준다

today = datetime.today()
hours = timedelta(hours=-5)
print(today + hours)    # 2020-07-15 05:54:59.888379

# 1달 전 날짜를 알아보아요!
# 예) 오늘 날짜가 3월 31일  => 한달 전 날짜는? 2월 28일

today = date.today()     # 오늘 날짜를 구해요!
days = timedelta(months=-1) # invalid keyword error
days = timedelta(years=-1)  # invalid keyword error
# => 연도와 월에 대한 timedelta는 존재하지 않아요!
#     그래서 새로운 외부 module을 또 사용해야 해요! => python-dateutil 설치

from dateutil.relativedelta import relativedelta

today = date.today()
days1 = relativedelta(months=-5)
print(today + days1)             # 2020-02-15
days2 = relativedelta(years=-1)
print(today + days1 + days2)     # 2019-02-15

# 현재 날짜와 시간만 하고 있어요!
# 문자열로 되어 있는 날짜를 진짜 날짜로 변환해서 연산을 하고 싶어요!

from datetime import datetime
from dateutil.parser import parse

my_date = parse("2019-01-30")
print(my_date)      # 2019-01-30 00:00:00

my_date = datetime(2019, 1, 30)
print(my_date)      # 2019-01-30 00:00:00