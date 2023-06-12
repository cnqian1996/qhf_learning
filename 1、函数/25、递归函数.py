# 递归函数：函数自己调用自己
'''
函数的分类
 普通函数：def func():pass
 匿名函数：lambda 参数：返回结果
 递归函数：普通函数的一种表现形式

特点：
1.递归函数必须要设定终点
2.通常都会有一个入口
'''


def sum(n):
    if n == 0:
        return 0
    else:
        return n + sum(n - 1)


result = sum(10)
print(result)

s = 0
for i in range(11):
    s += i
print(s)


def f1(n):
    if n > 0 :
        print('----->',n)
        f1(n - 1)
    else:
        print('------>',n)
f1(5)


def sum1(n):
    '''
    求和的函数
    :param n: 从1~n的累加和
    :return: 求和的结果
    '''
    if n == 100:
        pass
    else:
        pass