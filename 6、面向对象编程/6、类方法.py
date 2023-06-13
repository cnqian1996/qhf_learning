# 类方法
'''
特点：
    1.定义需要依赖装饰器 @classmethod
    2.类方法中的参数不是一个对象，而是类
      print(cls) # <class '__main__.Dog'> 类
    3.类方法中只能使用类属性，不能使用对象属性

'''

class Dog:
    aa = 'aaa'
    def __init__(self, nickname):
        self.nickname = nickname

    def run(self):  # self 对象
        print("{}在院子里跑来跑去！".format(self.nickname))

    @classmethod
    def test(cls):  # cls class
        print(cls) # <class '__main__.Dog'> 类
        print(cls.aa)
        # print(cls.nickname)  报错


d = Dog("郑义")

d.run() #调用run

Dog.test()

