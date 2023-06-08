def func(a,b):
    c = 10

    def inner_func():
        s = a + b + c
        print("相加之后的结果是：",s)

    return inner_func



# 调用：
# func(6,9)()
x = func(6,9) # x 就是 inner_func
y = func(2,8)

y()
x()


