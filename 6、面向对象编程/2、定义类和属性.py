# 定义类和属性
class Student:
    # 类属性
    name = 'zhengyi'
    age = 2


zhengyi = Student()

zhengyi.age = 18
print(zhengyi.age)

wangxincheng = Student()
wangxincheng.name = 'xiaowangwang'
print(wangxincheng.name)
print(wangxincheng.age)

Student.age = '王新成'

wxc = Student()
print(wxc.name)
