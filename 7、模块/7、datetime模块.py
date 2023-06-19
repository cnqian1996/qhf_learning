'''
datetime模块: time模块升级版
    time 时间
    date 日期 （data 数据）
    datetime 时间日期
    timedelta 时间差
'''

import datetime
import time

print(str(datetime.time.hour))  # 对象
print(time.localtime().tm_hour)

d = datetime.date(2023, 6, 18)  # 因为date是类，所以要创建对象
print(d.day)
print(datetime.date.day)
print(time.time())
print(datetime.date.ctime(d))

# datetime timedelta
print(datetime.date.today())

timedel = datetime.timedelta(days=3, hours=2)  # 时间差
print(timedel)

now = datetime.datetime.now()  # 得到当前的日期时间
print(now)
result = now + timedel
print(result)

# 缓存：数据redis 作为缓存 redis.set(key,value,时间差)  会话：session
