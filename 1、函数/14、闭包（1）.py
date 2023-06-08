# 闭包
# 在函数中提出的概念
'''
条件：
1、外部函数中定义内部函数
2、外部函数是有返回值
3、返回的值是内部函数
4、内部函数引用了外部函数的变量值

格式：
def 外部函数（）：
    ...
    def 内部函数（）:
    ...
    return 内部函数
'''

def func():
    a = 100

    def inner_func():
        b = 99
        print(a, b)

    print(locals())
    return inner_func #不能加括号！加括号表示调用


x = func()

print(x)

# x就是内部函数，x()表示调用函数
x()
