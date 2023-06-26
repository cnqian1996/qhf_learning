'''
特点：
添加一个执行一个任务，如果一个任务不结束另一个任务就进不来。

进程池：
pool = Pool(max) 创建进程池对象
pool.apply() 阻塞的
pool.apply_async() 非阻塞的

pool.close()
pool.join() 让主进程让步
'''


from random import random
from multiprocessing import Pool
import time
import os


# 阻塞式进程
def task(task_name):
    print('开始做任务啦！', task_name)
    start = time.time()
    # 使用sleep
    time.sleep(random() * 2)
    end = time.time()
    print("完成任务{}用时:{},进程：{}".format(task_name,(end - start),os.getpid()))
    # return "完成任务{}用时:{},进程：{}".format(task_name, (end - start), os.getpid())


if __name__ == '__main__':
    pool = Pool(5)
    tasks = ['听音乐', '吃饭', '洗衣服', '打游戏', '散步', '看孩子', '做饭']
    for task1 in tasks:
        pool.apply(task, args=(task1,))

    pool.close() #添加任务结束
    pool.join()

    print('over!!!')