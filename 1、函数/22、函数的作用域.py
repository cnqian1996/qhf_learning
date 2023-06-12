'''
函数：
作用域:LEGB
L:local 本地 局部变量
E：encloseing 嵌套
G:global 全局
B:built-in 内置的
'''

a = 100  # G global 全局变量


def func(b):
    a = 10  # 嵌套，位于外层的变量

    def inner_func():
        # a = 1  # local 本地局部变量
        print(max,a,b)

    # inner_func()
    return  inner_func


# 调用外部函数
f = func(7)
f()