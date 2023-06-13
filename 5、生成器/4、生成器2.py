# g = (x * 3 for x in range(10))
#
# while True:
#     try:
#         e = next(g)
#         print(e)
#     except:
#         print("没有更多的元素了！")
#         break

# 定义生成器的方式二：借助函数完成
# 只要函数中出现yield关键字，说明函数就不是函数啦，变成生成器了。

'''
步骤：
1.定义一个函数，函数中使用yield关键字
2.调用函数，接收调用的结果
3.得到的结果就是生成器
4.借助与next(),__next__()得到
'''


# def func():
#     n = 0
#     while True:
#         n += 1
#         print(n)
#         yield n
#
#
# func()
# g = func()
# next(g)
# next(g)


# 斐波那契数列 0 1 1 2 3 5 8
def fib(length):
    a, b = 0, 1
    n = 0
    while n < length:
        yield b
        a, b = b, a + b
        n += 1
    return "没有更多元素了！"  # return就是在得到StopIteration后提示信息


g = fib(8)
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
