# 有了else 就不能使用return
def func():
    try:
        n1 = int(input('输入数字：'))
        print(n1)
        # return 1
    except ValueError:
        print("必须是数字！！")
        # return 2
    else:
        print("数字输入完毕！") #没有异常才会执行的代码块！


# 调用函数
func()