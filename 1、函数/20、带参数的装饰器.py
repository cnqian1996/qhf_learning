# 装饰器带参数
'''
带参数的装饰器，是三层的！
最外层函数：负责接收装饰器的参数
里面的内容还是原来装饰器的内容
'''


def outer(a):  # 第一层：负责接收装饰器的参数
    def decorate(func):  # 第二层：负责接收函数
        def wrapper(*args, **kwargs):  # 第三层：负责接收函数的参数
            func(*args, **kwargs)
            print("--------->铺了{}地砖".format(a))

        return wrapper  # 返回第三层

    return decorate  # 返回第二层


@outer(10)
def house(time):
    print("{}我拿到了房子钥匙，是毛坯房！".format(time))


@outer(100)
def street():
    print('新修了一条街道')


house("2023.6.11")
street()
