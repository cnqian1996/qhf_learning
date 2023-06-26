import threading
from time import sleep

money = 1000

def run1():
    global money
    for i in range(100):
        sleep(0.1)
        money -= 1

def run2():
    global money
    for i in range(100):
        money -= 1

if __name__ == "__main__":
    # 创建线程
    th1 = threading.Thread(target=run1,name="th1")
    th2 = threading.Thread(target=run1,name="th2")
    th3 = threading.Thread(target=run1,name="th2")
    th4 = threading.Thread(target=run1,name="th2")

    # 启动
    th1.start()
    th2.start()
    th3.start()
    th4.start()

    th1.join()
    th2.join()
    th3.join()
    th4.join()

    print('money:',money)