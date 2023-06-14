# 私有化
# 封装：1.私有化属性 2.定义公有的set和get方法
# __属性：就是将属性私有化，访问范围仅仅限于类中
'''
好处：
1.隐藏属性不被外界随意修改
2.也可以修改：通过函数
    def setXXX(self,xxx):
        # 筛选赋值的内容
        if xxx符合条件
            赋值
        else:
            不赋值
3.如果想获取具体的某一个属性
    使用get函数
        def getXXX(self):
            return self.__XXX
'''

class Student:
    # __age = 18 # 类属性

    def __init__(self, name, age):
        self.__name = name # 长度必须六位以内
        self.__age = age
        self.__socre = 59

    # 定义共有的set和get方法
    # set是为了赋值
    def setAge(self, age):
        if age > 0 and age <= 120:
            self.__age = age
        else:
            print("年龄不在规定的范围内")

    # get是为了取值
    def getAge(self):
        return self.__age

    def setName(self,name):
        if len(name) < 6 :
            self.__name = name
        else:
            print("你输入的名字过长！")

    def getName(self):
        return self.__name

    def __str__(self):
        return "姓名：{}，年龄：{}，考试分数：{}".format(self.__name, self.__age, self.__socre)

    # attribute : setName getName __str__  __init__


zy = Student("郑义", 20)
print(zy)
zy.age = 21
zy.__socre = 11  # 无法修改
zy.setName("煞笔煞笔煞笔")
print(zy)

wxc = Student("王新成", 50)
print(wxc)
wxc.setAge(88)
print(wxc)

print(wxc.getAge())

print(dir(Student)) # 查看类里面的所有属性
print(dir(wxc)) # 查看对象里面的所有属性

# print(_Student__name) # 其实它就是__age,只不过系统自动改名字了。
print(__name__)
