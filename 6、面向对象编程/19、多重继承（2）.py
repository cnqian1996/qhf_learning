# 多继承的搜索顺序:
# 新式类 （广度优先、深度优先）
'''
1.  D.__mor__ ----> 查看搜索顺序

2.  import inspect:
    print(inspect.getmro(D))
'''
class P1:
    def foo(self):
        print("p1----->foo")

    def bar(self):
        print("p1----->bar")


class P2:
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
# 从左至右，深度优先


