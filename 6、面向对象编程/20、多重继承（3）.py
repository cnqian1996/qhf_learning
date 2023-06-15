# 多继承的搜索顺序： 经典类 （从左到右、深度优先）

class P1(object):
    def foo(self):
        print("p1----->foo")

    def bar(self):
        print("p1----->bar")


class P2(object):
    def foo(self):
        print("p2----->foo")


class C1(P1, P2):
    pass


class C2(P1, P2):
    def bar(self):
        print("C2------>bar")


class D(C1, C2):
    pass

d = D()
print(D.__mro__)

d.foo()
d.bar()