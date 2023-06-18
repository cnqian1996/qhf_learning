# 变量
number = 100
name = 'calculation'


# 函数
def add(*args):
    if len(args) > 1:
        sum = 0
        for i in args:
            sum += i
        return sum
    else:
        print("至少传入两个参数！")
        return 0


def minus(*args):
    if len(args) > 1:
        m = 0
        for i in args:
            m -= i
        return m
    else:
        print("至少传入两个参数！")
        return 0


def multiply(*args):
    pass


def divide(*args):
    pass


# 类
class Calculate:
    def __init__(self, num):
        self.num = num

    def test(self):
        print("正在使用Calculate运算")

    @classmethod
    def aaa(cls):
        print("-----------------> Calculate中的类方法")

