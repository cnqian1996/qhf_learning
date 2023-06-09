'''
编写一个简单的工资管理程序,系统可以管理以下四类人: 工人 (worker)、销售员(salesman)、经理(manager)、销售经理(salemanger)
所有的员工都具有员工号，姓名，工资等属性，有设置姓名，获取姓名，获取员工号，计算工资等方法。
1)工人:工人具有工作小时数和时薪的属性，工资计算法方法为工作小时数*时薪
2) 销售员:具有销售额和提成比例的属性，工资计算方法为销售额*提成比例。
3)经理:具有固定月薪的属性，工资计算方法为固定月薪。
4)销售经理:工资计算方法为销售额*提成比例+固定月薪请根据以上要求设计合理的类，完成以下功能:
    1) 添加所有类型的人员
    2) 计算月薪
    3)示所有人工资情况
'''


class Person:
    def __init__(self, no, name, salary):
        self.no = no
        self.name = name
        self.salary = salary

    def __str__(self):
        msg = "工号：{}，姓名：{}，本月工资：{}".format(self.no, self.name, self.salary)
        return msg

    def getSalary(self):
        return self.salary


class Worker(Person):
    def __init__(self, no, name, salary, hours, per_hour_money):
        super().__init__(no, name, salary)
        self.hours = hours
        self.per_hour_money = per_hour_money

    def getSalary(self):
        money = self.hours * self.per_hour_money
        self.salary += money
        return self.salary

class Salesmen(Person):
    def __init__(self,no,name,salary,salesmoney,percent):
        super().__init__(no,name,salary)
        self.salesmoney = salesmoney
        self.percent = percent

    def getSalary(self):
        money = self.salesmoney * self.percent
        self.salary += money
        return self.salary

w = Worker('001',"郑义",3500,160,100)
s = w.getSalary()
print("工人的月薪是：",s)
print(w)

print("================================")

saler = Salesmen("002","王嘉祥",5000,5000000,0.003)
s = saler.getSalary()
print("销售员的月薪是：",s)
print(saler)
