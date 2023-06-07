import random

def generate_random(): #定义函数
    for i in range(10):
        ran = random.randint(1,20)
        print(ran)

print(generate_random) #打印函数名
# <function generate_random at 0x0000020F6BA43F40>

generate_random() #调用函数：找到函数并执行函数体的内容

