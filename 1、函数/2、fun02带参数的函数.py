import random


def generate_random(number): #形参:形式上的参数！
    for i in range(number): #i=0
        ran = random.randint(1,20)
        print(ran)

print(generate_random)
# 👇调用
generate_random(5)    #实参：实际的参数，具体的值


def add(a,b):
    res = a + b
    print("和：",res)

add(1,3)
