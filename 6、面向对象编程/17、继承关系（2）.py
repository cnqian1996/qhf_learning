class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(self.name + "正在吃饭...")

    def run(self):
        print(self.name + "正在跑步...")


class Student(Person):
    def __init__(self, name, age, clazz):
        super().__init__(name, age)
        self.clazz = clazz

    def study(self):
        print("{}正在学习{}课程".format(self.name, self.clazz))

    def eat(self, food):  # 黄色 警告   因为父类没参  子类有参数
        super().eat()
        print("{}正在吃饭........喜欢{}！！！".format(self.name, food))


class Employee(Person):
    def __init__(self, name, age, salary, manger):
        super().__init__(name, age)
        self.salary = salary
        self.manger = manger


class Doctor(Person):
    def __init__(self, name, age, patient):
        super(Doctor, self).__init__(name, age)
        self.patient = patient


s = Student("郑义", 18, "Python基础")
s.run()
s.study()
s.eat("屎")

e = Employee("王新成", 28, 20000, "qhf")
e.run()

lists = ["小南", "诸葛伟", "刘灿"]
d = Doctor("王嘉祥", 30, lists)
d.run()
