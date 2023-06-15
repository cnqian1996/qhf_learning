# is a  base class 父类 基类
'''
继承：
    Student,Employee,Doctor  ---> 都属于人类
    相同代码 ---> 代码冗余，可读性不高

    将相同代码提取 ---> Person类

    class Student(Person):
        pass

特点：
    1、如果类中不定义__init__，调用父类super class中的__init__
    2、如果类继承了父类，也需要去定义自己的__init__，就需要在当前类的__init__调用一下父类的__init__
    3、如何调用父类的__init__:
        super().__init__(参数)
        super(类名,对象).__init__(参数)
    4、如果父类有eat()，子类页定义一个eat方法，默认搜索的原则：先找当前类，再去找父类
        s.eat()
        override: 重写（覆盖）
        父类提供的方法不能满足子类的需求，就需要在子类中定义一个同名的方法，这种行为：重写
    5、子类的方法中也可以调用父类的方法：
        super().方法名(参数)
'''


class Person:
    def __init__(self, name):
        self.name = name
        self.age = 18

    def eat(self):
        print(self.name + "正在吃饭...")

    def run(self):
        print(self.name + "正在跑步...")


class Student(Person,):
    def __init__(self, name):
        print("------------------> student的init")
        # 如何调用父类的__init__
        super().__init__(name)  # super() 表示父类对象


class Employee(Person):
    pass


class Doctor(Person):
    pass


s = Student("郑义")
s.run()

s = Student("王嘉祥")
s.run()

s = Student("王新成")
s.run()
# e = Employee()
