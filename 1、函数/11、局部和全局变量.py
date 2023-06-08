# 局部和全局
# 全局变量如果是不可变，在函数中修改需要加global关键词
# 如果局部变量是可变的，在函数中修改的时候就不需要加global

name = '郑义'
list1 = [1,2,4,6]

def func():
    name = '王新成'
    print(name)
    print(list1)

def func1():
    global name
    print(name)
    name += '是傻逼！'
    #修改列表
    list1.append(8)
    print(list1)

def func2():
    name1 = '王嘉祥'
    name1 += "sb"

    print(name1)  #自己的

    global name
    print(name)

# func1()
# func()
func2()