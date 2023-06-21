'''
当需要创建的子进程数量不多时，可以直接利用multiprocessing中的Process动态成多个进程，
但如果是上百甚至上千个目标，手动的去创建进程的工作量巨大，此时就可以用到multiprocessing模块提供的Pool方法
初始化Pool时，可以指定一个最大进程数，当有新的请求提交到Pool中时，如果池还没有满，
那么就会创建一个新的进程用来执行该请求；但如果池中的进程数已经达到了指定的最大值，那么该请求就会等待，
直到池中有进程结束，才会创建新的进程来执行

阻塞式：全部添加到队列中，立刻返回，并没有等待其他的进程完毕，但是回调函数是等到任务完成之后才调用
非阻塞式：
'''

import os
from random import random
from multiprocessing import Pool
import time


# 非阻塞式进程
def task(task_name):
    print('开始做任务啦！', task_name)
    start = time.time()
    # 使用sleep
    time.sleep(random() * 2)
    end = time.time()
    # print("完成任务{}用时:{},进程：{}".format(task_name,(end - start),os.getpid()))
    return "完成任务{}用时:{},进程：{}".format(task_name,(end - start),os.getpid())

container = []
def callback_func(n):
    container.append(n)

if __name__ == '__main__':
    pool = Pool(5)

    tasks = ['听音乐', '吃饭', '洗衣服', '打游戏', '散步', '看孩子', '做饭']
    for task1 in tasks:
        pool.apply_async(task, args=(task1,),callback=callback_func)

    pool.close() #添加任务结束
    pool.join()

    for c in container:
        print(c)

    print('over!!!')

