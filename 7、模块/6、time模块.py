# time模块
# 1.时间戳 time.y
'''
重点：
time.time()
time.sleep()
time.strftime('格式') %Y %m %d
'''
import time

t = time.time()
print(t)

time.sleep(3)

t1 = time.time()
print(t1)

t = time.ctime(t)  # 将时间戳转换成字符串
print(t)

t = time.localtime(t1)  # 将时间戳转成元组的方式
print(t)
print(t.tm_mday)

tt = time.mktime(t)  # 将元组转成时间戳
print(tt)


s = time.strftime("%Y-%m-%d %H:%M:%S") # 将元组的时转成字符串
print(s)

r = time.strptime('2023/06/18','%Y/%m/%S') # 将字符串转成元组的方式
print(r)