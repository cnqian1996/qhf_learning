'''
from multiprocessing import Process
process = Proces(target = 函数，name = 进程名字，args=(给函数传递的参数))
process 对象

对象调用方法：
process.start() 启动进程并执行任务
process.run() 只是执行了任务 单是没有启动进程
terminate() 终止

'''

'''
多进程对于全局变量访问，在每一个全局变量里面都放一个m变量
保证每个进程访问变量互不打扰
m = 1 # 不可变类型
list1 = [] # 可变类型
'''

# 创建进程
from multiprocessing import Process
from time import sleep
import os

m = 1 # 不可变类型
list1 = [] # 可变类型

def task1(s, name):
    global m
    while True:
        sleep(s)
        m += 1
        list1.append(str(m)+'task1')
        print('这是任务1.。。。。。。。。。。。。。。。。',m,list1)
        # print('这是任务1............', os.getpid(), '-------', os.getppid(), m)


def task2(s, name):
    global m
    while True:
        sleep(s)
        m += 1
        list1.append(str(m) + 'task2')
        print('这是任务2.。。。。。。。。。。。。。。。。', m, list1)
        # print('这是任务2............',  m)


number= 1
if __name__ == "__main__":
    # 子进程
    p1 = Process(target=task1, name="任务1", args=(1, 'aa'))
    p1.start()
    # print(p1.name)
    p2 = Process(target=task2, name="任务2", args=(2, 'bb'))
    p2.start()
    # print(p2.name)

    while True:
        number += 1
        sleep(0.2)
        if number == 100:
            p1.terminate()
            p2.terminate()
            break
        # else:
            # print("-----------> number:",number)


    # task1()
    # task2()
