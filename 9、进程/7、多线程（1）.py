# 线程
'''
    t = threading.Thread(target=download,name='aa',args=(1,))
    t.start()
线程：
    新建、就绪、运行、阻塞、结束

线程：Thread
1、创建线程
    A. t = Thread(target=func,name='',args=(),kwargs={}) ---->新建状态
        t.start()   ----> 就绪状态

        run()
        join()

    B.自定义线程
    class MyThread(Thread):
        def __init__(self,name):
            super().__init__()
            self.name = name

        def run(self):
            任务

    t = MyThread()
    t.start()

2、数据共享
    进程共享数据和线程共享数据的区别：
        进程是每个进程中都有一份
        线程是共同一个数据  ---> 数据安全性问题
'''
import threading

# 进程：Process
# 线程：Thread
from time import sleep

import setuptools


def download(n):
    images = ['gitrl.jpg','boy.jpg','man.jpg']
    for image in images:
        print('正在下载：',image)
        sleep(n)
        print("下载{}成功！".format(image))

def listenMusic():
    musics = ['大碗宽面','土耳其冰激凌','烤面筋','烤馒头片']
    for music in musics:
        sleep(0.5)
        print("正在听：",music)



if __name__ == '__main__':
    # 线程对象
    t = threading.Thread(target=download,name='aa',args=(1,))
    t.start()

    t1 = threading.Thread(target=listenMusic,name='aa')
    t1.start()

    n =1
    while True:
        print(n)
        sleep(1.5)
        n += 1
