'''
python允许多继承：
def 子类(父类1,父类2,...)
    pass
    
'''
# class Person:
#     def __init__(self, name):
#         self.name = name
#
#     def eat(self):
#         print("----------eat1")
#
#     def eat(self, food):   # 遇到同名的 会用后面的
#         print("----------eat:", food)
#
#
# p = Person("郑义")
# p.eat("屎")

class Base:
    def test(self):
        print("-------BASE--------")

class A(Base):
    def test(self):
        print("AAAAAAAAAAAA")

class B(Base):
    def test(self):
        print("BBBBBBBBBBBB")

class C(Base):
    def test(self):
        print("CCCCCCCCCCCC")

class D(B,A,C):   # 哪个靠近D 先搜索哪个
    pass


d = D()
d.test()

import inspect
print(inspect.getmro(D))
print(D.__mro__)
# c.test1()
# c.test2()

