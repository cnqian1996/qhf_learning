# 在开发中常用一些私有化处理：装饰器
class Student:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self,age):
        if age > 0 and age <100:
                self.__age = age
        else:
            print("不在规定的范围内！")


    # def setAge(self,age):
    #     if age > 0 and age <100:
    #         self.__age = age
    #     else:
    #         print("不在规定的范围内！")
    #
    #
    # def getAge(self):
    #     return self.__age

    def __str__(self):
        return "姓名：{}，年龄：{}".format(self.name, self.__age )

s = Student("郑义",20)

s.name = "王新成"
print(s.name)

s.age = 222
print(s.age)
print(s.__dir__())

# 私有化赋值
# s.setAge(30)
# print(s.getAge())

