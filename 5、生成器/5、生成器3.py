'''
生成器方法：
    __next__(): 获取下一个元素
    send(value): 向每次生成器传值 注意：第一次调用send(None)

'''

def gen():
    i = 0
    while i < 5:
        temp = yield i
        print("temp:", temp)
        for i in range(temp):
            print("---------->",i)
        print("*****************")
        i += 1
    return "没有更多的数据了。"


g = gen()
# print(next(g))
# print(next(g))
# print(next(g))

# g.__next__()
print(g.send(None))
n1 = g.send(3)
print('n1:', n1)
n2 = g.send(5)
print('n2:', n2)
