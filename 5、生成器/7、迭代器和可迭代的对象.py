# 可迭代的对象： 1、生成器 2、元组 列表 集合 字典 字符串
# 如何判断一个对象是否可以迭代？
from collections.abc import Iterable

list1 = [1, 4, 7, 8, 8]
f = isinstance(list1, Iterable)
print(f)

f = isinstance("abc", Iterable)
print(f)

f = isinstance(100, Iterable)
print(f)

g = (x+1 for x in range(5))
f = isinstance(g, Iterable)
print(f)

'''
迭代器是访问集合元素的一种方式。迭代器是一个记住遍历的位置的对象。
迭代器对象从集合的第一个元素开始进行访问，直到所有的元素可以被访问完结束，
迭代器只能往前不会后退。

可以被next()函数调用并不断返回下一个值的对象成为迭代器：Iterable

可迭代的不一定是迭代器！
生成器是可迭代的，也是生成器！
列表是可迭代的，也是生成器！
'''
# list ----》 迭代器
list1 = [1,2,3,4,5,6]
list1 = iter(list1)  # 通过iter()函数将课迭代的变成了一个迭代器
print(next(list1))
print(next(list1))

