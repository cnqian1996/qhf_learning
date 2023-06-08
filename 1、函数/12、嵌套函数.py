# 内部函数
'''
特点：
1、可以访问外部函数的变量
2、内部函数可以修改外部函数的可变类型的变量 比如：list1
3、内部函数修改全局的不可变变量时，需要在你的内部函数声明：global 变量名
   内部函数修改外部函数的不可变变量时，需要在内部函数中声明：nonlocal 变量名
4、locals（） 查看本地变量有哪些，以字典的形式输出
   globals（）查看全局变量有哪些，以字典的形式输出（注意里面有一些系统的键值对）
'''

def func():
    # 声明变量：
    n = 100  # 局部变量
    list1 = [3, 6, 9, 4]  # 局部变量

    # 声明内部函数：
    def inner_func():
        nonlocal n
        #对list1里面的元素进行加5操作：
        for index,i in enumerate(list1):
            list1[index] = i + n
        list1.sort()
        #修改n变量
        n += 100

    # 调用下内部的函数：
    inner_func()
    print("打印老大的n：",n)
    print("打印老二list",list1)

func()