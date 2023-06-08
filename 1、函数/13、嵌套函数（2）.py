a = 100
print(globals())

def func():
    b = 99

    def inner_func():
        nonlocal b  # 修改局部变量
        global a
        c = 88
        # 尝试修改
        c += 12
        b += 100
        a += 10
        # 尝试打印
        print(a, b, c)

    inner_func()

    print(locals())  # 使用内置函数进行查看，可以看到在当前函数中声明的内容有哪些  locals是一个字典。 key:value
    print(inner_func)


func()
print(func)
