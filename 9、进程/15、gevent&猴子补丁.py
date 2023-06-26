'''
greenlet已经实现了协程，但是这个人工切换，是不是觉得太麻烦了，不要着急
python中还有一个比greenlet更强大的并且能够自动切换任务的模块gevent
其原理是当一个greenlet遇到IO（指的是input output输入输出，比如网络、文件操作等）
比如访问网络，就自动切换到其它的greenlet，等到IO完成，再适当地时候切换回来就继续执行。

由于IO操作非常耗时，经常使程序处于等待状态，有了gevent我们自动切换协程，就保证总有greenlet在运行，而不是等待IO
'''

import time

import gevent
from gevent import monkey

monkey.patch_all()

def a():  # 任务A
    for i in range(5):
        print('A' + str(i))
        time.sleep(0.1)


def b():  # 任务B
    for i in range(5):
        print('B' + str(i))
        time.sleep(0.1)


def c():  # 任务C
    for i in range(5):
        print('C' + str(i))
        time.sleep(0.1)


if __name__ == '__main__':
    g1 = gevent.spawn(a)
    g2 = gevent.spawn(b)
    g3 = gevent.spawn(c)

    g1.join()
    g2.join()
    g3.join()


