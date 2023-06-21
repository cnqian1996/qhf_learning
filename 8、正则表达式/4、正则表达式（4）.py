import re

# 起名的方式: (?P<名字>正则)(?P=名字)
msg = '<html><h1>abc</h1></html>'

result = re.match(r"<(?P<name1>\w+)><(?P<name2>\w+)>(.+)</(?P=name2)></(?P=name1)>", msg)
print(result)
print(result.group(1))
print(result.group(2))
print(result.group(3))

'''
分组：（）  ---> result.group(1) 获取组中匹配内容
    在分组的时候，还可以结合 | 使用
不需要引用分组的内容：
    result = re.match(r"<[0-9a-zA-Z]+>(.+)</[0-9a-zA-Z]+>", msg)
    print(result)
    print(result.group(1))
引用分组匹配内容：
    1.number  \number 应用第number组的数据
        msg = '<html><h1>abc</h1></html>'
        result = re.match(r"<([0-9a-zA-Z]+)><([0-9a-zA-Z]+)>(.+)</\2></\1>$", msg)
        print(result)
        
    2.?P<名字>
        msg = '<html><h1>abc</h1></html>'
        result = re.match(r"<(?P<name1>\w+)><(?P<name2>\w+)>(.+)</(?P=name2)></(?P=name1)>", msg)
        print(result)
        print(result.group(1))
        
re模块：
match 从开头匹配一次
search 只匹配一次
findall 查找所有
sub(正则表达式,'新内容','string') 替换
split 切割
'''


def func(temp):
    num = temp.group()
    num1 = int(num) + 1
    return str(num1)


result = re.sub(r"\d+", func, "java:99,python:100")
print(result)

result1 = re.sub(r"\d+", "1000", "java:99,python:100")
print(result1)

result2 = re.split(r"[:,]","java:99,python:100")
print(result2)