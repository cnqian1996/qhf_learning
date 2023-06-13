# 列表推导式 字典推导式 集合推导式
# 旧的列表 ---> 新的列表

# 1.列表推导式 格式： [表达式 for 变量 in 旧列表] 或者  [表达式 for 变量 in 旧列表 if 条件]

# 过滤掉长度小于或者等于3的人名
names = ['zhengyi', 'wangxincheng', 'wangjiaxiang', 'zhugewei', 'jiweiyi', 'munin', 'tom', 'ha', 'bob']
result = [name for name in names if len(name) > 3]
print(result)

result = [name.capitalize() for name in names if len(name) > 3]
print(result)

'''
def func(names):
    newlist = []
    for name in names:
        if len(name）> 3:
            name = name.title()
            newlist.append(name)
    return newlist
'''

# 将1-100中间能同时被3和5整除，组成新的列表
newlist = [i for i in range(1, 101) if i % 3 == 0 and i % 5 == 0]
print(newlist)

# 求0-5之间的偶数与0-10之间的奇数构成元组列表
newlist = [(x, y) for x in range(5) if x % 2 == 0 for y in range(10) if y % 2 != 0]
print(newlist)

newlist1 = []


def func():
    for i in range(5):
        if i % 2 == 0:
            for j in range(10):
                if j % 2 != 0:
                    newlist1.append((i, j))
    return newlist1


x = func()
print(x)

# list2 = [[1,2,3],[4,5,6],[7,8,9],[1,3,5]]   ----->  [3,6,9,5]
list2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 3, 5]]
newlist3 = [i[2] for i in list2]
print(newlist3)

# if 薪资大于5000加工资200， 低于等于5000加工资500
dict1 = {'name': 'zhengyi', 'salary': 5000}
dict2 = {'name': 'wangxincheng', 'salary': 8000}
dict3 = {'name': 'wangjiaxiang ', 'salary': 4500}
dict4 = {'name': 'zhugewei ', 'salary': 3000}
list3 = [dict1, dict2, dict3, dict4]
newlist4 = [employee['salary'] + 200 if employee['salary'] > 5000 else employee['salary'] + 500 for employee in list3]
print(newlist4)
