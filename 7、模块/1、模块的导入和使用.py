'''
在python中，模块是代码组织的一种方式，把功能相近的函数或者类放到一个文件中，一个文件（.py）就是一个模块（module）
模块名就是文件名去掉后缀py
这样做的好处是：
-提高代码的可复用性、可维护性。一个模块编写完毕后，可以很方便的在其他项目中导入
-解决了命名冲突，不同模块中的相同命名不会冲突

常用标准库： builtins math random time datetime calendar hashlib copy ......

1.自定义模块
2.使用系统一些模块

导入模块：
1.import 模块名
    模块名.变量/函数/类

2. from 模块名 import 变量/函数/类

'''

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
    def __init__(self,num):
        self.num = num

    def test(self):
        print("正在使用Calculate运算")

    @classmethod
    def aaa(cls):
        print("-----------------> Calculate中的类方法")

# --------------模块的使用--------------

# list1 = [4, 2, 7, 8, 9]
#
#
# import test # 导入模块
# result = test.add(*list1)   #  使用函数中的模块 函数名.变量   模块名.函数  模块名.类
# print(result)
#
# print(test.number)  # 使用模块变量
#
# cal = test.Calculate(88) # 使用模块中的类
# cal.test()
#
# test.Calculate.aaa() # 使用模块中的类方法