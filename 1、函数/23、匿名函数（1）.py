# 匿名函数:简化函数定义
# 格式：lambda 参数1，参数2... : 运算


def add(a, b):
    s = a + b
    return s


f = add

s = lambda a, b: a + b

print(s)

result = s(1, 2)
print(result)

s1 = lambda x, y: x * y

result = s1(2, 5)
print(result)


# 匿名函数作为参数：
def func(x, y, func):
    print(x, y)
    print(func)
    s = func(x, y)
    print(s)


# 调用func
func(1, 2, lambda a, b: a + b)

# 匿名函数与内置函数的结合使用
# max sorted zip...
list1 = [3, 5, 8, 9, 0]
m = max(list1)

print("列表的最大值：", m)

list2 = [{"a": 10, 'b': 20}, {"a": 13, 'b': 20}, {"a": 9, 'b': 20}, {"a": 29, 'b': 20}]
m = max(list2, key=lambda x: x["a"])
print("列表的最大值：", m)