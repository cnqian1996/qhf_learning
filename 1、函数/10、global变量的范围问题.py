#global 变量的范围
#局部变量 全局变量
#声明再函数外层的是全局的，所有函数都可以访问！

name = "郑义"

def func():
    s = 'abcd' #函数内部申明的变量，局部变量  仅限于在函数内部使用！
    s += "X"
    print(s,name)

def func1():
    global name #不修改全局变量，只是获取答应。但是如果要发生修改全局变量，则需要在函数内部声明：global 变量名
    # print(s) 报错
    name += "是个超级大傻逼"  #报错：函数内部的变量可以随便修改，但是全局的变量不能随便在函数内部进行修改，除非加“global”
    print(name)

def func2():
    name = "王新成" #局部变量和全局变量同名
    name += '，是个傻逼'
    print(name)


func()
func1()
func2()
print(name)
# print(s) 报错