# is a  base class 父类 基类
'''
继承：
    Student,Employee,Doctor  ---> 都属于人类
    相同代码 ---> 代码冗余，可读性不高

    将相同代码提取 ---> Person类

    class Student(Person):
        pass
'''
class Person:
    def __init__(self):
        self.name = "匿名"
        self.age = 18

    def eat(self):
        print(self.name + "正在吃饭...")

    def run(self):
        print(self.name + "正在跑步...")


class Student(Person):
    def __init__(self):
        print("------------------> student的init")


class Employee(Person):
    pass


class Doctor(Person):
    pass


s = Student()
s.run()

e = Employee()
