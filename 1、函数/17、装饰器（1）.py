# 装饰器
'''
特点：
1、函数A是作为参数出现的（函数B就接收函数A作为参数）
2、要有闭包的特点

'''


# 定义一个装饰器！
def decorate(func):
    a = 100
    print("wrapper外层打印测试！")

    def wrapper():
        func()
        print('-------->刷漆')
        print('-------->铺地板', a)
        print('-------->装门')

    print("wrapper加载完成")
    return wrapper

@decorate #使用装饰器
def house():
    print("我是毛坯房！")

'''
1.house被装饰函数
2.将被装饰函数作为参数传给装饰器decorate
3.执行decorate函数
4.将返回值又赋值给house
'''
print(house)
#  调用函数
house()



# def house1():
#     house()
#     print('刷漆')
#     print('铺地板')


# '''
# 加入购物车，付款，修改收货地址......
# 判断用户的登陆状态
# '''
#
#
#
# def func(number):
#     a = 100
#
#     def inner_func():
#         nonlocal a
#         nonlocal number
#         number += 1
#
#         for i in range(number):
#             a += 1
#         print('修改后的a的值：',a)
#
#     return inner_func
#
# # 调用func
# f = func(5)
# f()
#
# # 函数作为参数
# a = 50
# f1 = func(a)  #a是一个实参
# print(f1)
#
# # 地址引用
# def test():
#     print('------test------')
#
#
# def func1(f):
#     print(f)  # <function test at 0x000001D0B9CCAB90>
#     f()  # ------test------
#     print('---------------> func1')  # ---------------> func1
#
#
# func1(test)
