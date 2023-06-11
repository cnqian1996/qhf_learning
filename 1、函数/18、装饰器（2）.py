# 登录校验
import time


def decorate(func):
    def wrapper(*args,**kwargs):
        print('正在进行校验...！！!')
        time.sleep(2)
        print('★！！校验完成！！★')
        func(*args,**kwargs) # 调用原函数
    return wrapper

@decorate
def f1(n):
    print('--------f1--------',n)

f1(5)

@decorate
def f2(name,job):
    print('--------f2--------',name,job)

f2("郑义","sb")

@decorate
def f3(students, clazz='1905'):
    print("{}班级学生如下：".format(clazz))
    for stu in students:
        print(stu)

students = ['郑义','王新成','王嘉祥']
f3(students, clazz='1904')

@decorate
def f4():
    print("----------->: f4")

f4()