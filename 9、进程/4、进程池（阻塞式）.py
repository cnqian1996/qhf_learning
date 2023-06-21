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