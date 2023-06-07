# 关键词参数：key=value

def add(a,b=10): #关键词参数,b默认值为10
    result = a + b
    print(result)

#调用
add(5)
add(4,7) #a=4,b=7

def add1(a,b=10,c=4):
    print(a,b,c)
    result = a + b + c
    print(result)

add1(1)
add1(1,5)

#给c赋值
add1(2,6)
add1(2,c=6) #如果想赋值给c，需要结合关键字的key使用

#------------------------------------------------------------
##函数：计算每位同学的姓名、年龄
# students = {
#     "001":("郑义",99),
#     "002":("王新成",55),
#     "003":("王嘉祥",28),
#     "004":("诸葛伟",41)
#             }
#
# def print_boy(persons):  #persons = students
#     if isinstance(persons,dict):
#         values = persons.values()
#         print(values)
#         for name,age in persons.values():
#             print("{}的年龄是：{}".format(name,age))
#
# #调用
# print("如花",students)
#------------------------------------------------------------

def func(**kwargs): #key word argumets    "**"
    print(kwargs)
#调用
func(a=1,b=2,c=3)
func()
func(a=1)
func(a=1,b=2)

dict1={'001':'java','002':'c++','003':'go语言'}
# func(dict1) 会报错！
func(**dict1) # **dict  传递实参：**变量名  给参数赋值的时候，会将字典进行拆包