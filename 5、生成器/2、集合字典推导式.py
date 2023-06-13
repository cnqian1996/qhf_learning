# 集合推导式 ｛｝类似于列表推导式 在列表推导式的基础上添加了去除重复项的功能
list1 = [1, 2, 1, 3, 5, 2, 1]
set1 = {x - 1 for x in list1}
print(set1)

# 字典推导式
dict1 = {'a': 'A', 'b': 'B', 'c': 'C', 'd': 'D'}
newdict = {value: key for key, value in dict1.items()}
print(newdict)
