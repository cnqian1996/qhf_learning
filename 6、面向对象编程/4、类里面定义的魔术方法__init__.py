# 函数 和 类里面定义的方法

# def func(name):
#     print("----->",name)
#
# username = '郑义'
# func(username)

# def func(names):
#     for name in names:
#         print(name)
#
# name_list = ['aa','bb','cc']
# func(name_list)

class Phone:
    # 魔术方法之一:    __名字__() 称为魔术方法
    def __init__(self):
        self.brand = 'xiaomi'
        self.price = 4999

    def call(self):
        print('------->call')
        print('价格',self.price) # 不能保证每个self中都存在price

p = Phone()
print(p.price)
# print(Phone.price)
# p.price = 1000
# p.call()  # p.call() p对象

p1 = Phone()
p1.price = 5999
print(p1.price)

