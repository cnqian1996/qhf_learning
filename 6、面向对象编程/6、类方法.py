# 类方法
'''
特点：
    1.定义需要依赖装饰器 @classmethod
    2.类方法中的参数不是一个对象，而是类
      print(cls) # <class '__main__.Dog'> 类
    3.类方法中只能使用类属性，不能使用对象属性
    4.类方法是否可以使用普通方法？ 不能。

类方法作用：
    因为只能方法类属性和类方法，所以在对象创建之前，如果需要去完成一些动作（功能）
'''

class Dog:
    aa = 'aaa'
    def __init__(self, nickname):
        self.nickname = nickname

    def run(self):  # self 对象
        print("{}在院子里跑来跑去！".format(self.nickname))

    def eat(self):
        print('吃饭中......')
        self.run() # 类中方法的调用，需要通过 self.方法名()

    @classmethod
    def test(cls):  # cls class
        print(cls) # <class '__main__.Dog'> 类
        print(cls.aa)
        # self.run()
        # print(cls.nickname)  报错


d = Dog("郑义")

d.run() #调用run

Dog.test()

