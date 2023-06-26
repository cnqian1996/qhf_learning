'''
GIL: 全局解释器锁

线程： python的线程是伪线程

需要速度，用进程
对于耗时操作，用线程
'''

import threading

n = 0

def task1():
    global n
    for i in range(1000000):
        n += 1

        print("------> task1中的n的值是:",n)

def task2():
    global n
    for i in range(1000000):
        n += 1

        print("------> task2中的n的值是:",n)

if __name__ == '__main__':
    th1 = threading.Thread(target=task1)
    th2 = threading.Thread(target=task2)

    th1.start()
    th2.start()

    th1.join()
    th2.join()

    print("最后打印的n：",n)