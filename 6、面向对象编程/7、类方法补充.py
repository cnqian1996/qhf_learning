# 补充 类方法
class Person:
    __age = 18

    def show(self):
        print('------->', Person.age)

    @classmethod
    def update_age(cls):
        cls.__age = 20
        print('------->类方法')

    @classmethod
    def show_age(cls):
        print('修改后的年龄是：', cls.__age)

# p = Person()
# p.age = p.age + 1
# p.show()

# Person.age = Person.age + 1
# print(Person.age)

Person.update_age()
Person.show_age()
