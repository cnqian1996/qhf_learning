# 闭包的应用
# 闭包：
'''
1、保存返回闭包时的状态 （外层函数变量）

闭包缺点：
1、作用域没有那么直观
2、因为变量不会被垃圾回收所以有一定的内存占用问题

闭包的作用：
1、可以使用同级的作用域
2、读取其它元素的内部变量
3、延长作用域

闭包总结:
1、闭包似优化了变量，原来需要类对象完成的工作，闭包也能完成
2、由于闭包引用了外部函数的局部变量，则外部函数的局部变量没有及时释放，消耗内存
3、闭包的好处，使代码变得简洁，便于阅读代码。
4、闭包是理解装饰器的基础

'''


def generate_count():
    container = [0]

    def add_one():
        container[0] += 1
        print('当前是第{}次访问'.format(container[0]))

    return add_one

#内部函数就是一个计数器
counter = generate_count()

counter() #第一次访问
counter() #第二次访问
counter() #第三次访问


'''-------------------------------------------------'''

def func():
    a = 100

    def inner_func1():
        b = 90
        s = a + b
        print(s)

    def inner_func2():
        inner_func1()
        print("-------->inner_func2",a)
        return 'hello'

    return inner_func2

# 调用func
f = func()
print(f)

ff = f()
print(ff)