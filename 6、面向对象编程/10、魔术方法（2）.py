# __del__: delete的缩写 析构魔术方法
# 触发时机：当对象没有用（没有任何变量引用）的时候被触发
import sys
class Person:
    def __init__(self,name):
        self.name = name

    # def __del__(self):
        # pass

p = Person("郑义")
p1 = p
print(p1.name)

p2 = p
print(p2.name)

p1.name = '王新成'
print(p.name)
print(p2.name)

print(sys.getrefcount(p))