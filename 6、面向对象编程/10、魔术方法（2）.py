# __del__: delete的缩写 析构魔术方法
# 触发时机：当对象没有用（没有任何变量引用）的时候被触发

'''
__del__:
    1.对象赋值
        p = Person()
        p1 = p
    说明p和p1共同指向同一个地址

    2.删除地址的引用
        del p1 删除p1对地址的引用

    3.查看对地址的引用次数
        impory sys
        sys.getrefcount(p)

    4.当一块空间没有任何引用，默认执行__del__

'''

import sys


class Person:
    def __init__(self, name):
        self.name = name

    def __del__(self):
        print("---------del-------")


p = Person("郑义")
p1 = p
print(p1.name)

p2 = p
print(p2.name)

p1.name = '王新成'
print(p.name)
print(p2.name)

print(sys.getrefcount(p))

del p2
print('删除p2后打印', p.name)

print(sys.getrefcount(p))

del p1
print('删除p1后打印', p.name)

print(sys.getrefcount(p))

# del p
# print('删除p后打印', p.name)

print('---5---')


