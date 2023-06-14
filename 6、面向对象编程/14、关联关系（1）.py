# 继承： is a
import random

# 声明（定义） Road
class Road:
    def __init__(self,name,len):
        self.name = name
        self.len =len


class Car:
    def __init__(self,brand,speed):
        self.brand = brand
        self.speed = speed

    def get_time(self,road):
        rand_time = random.randint(1,10)
        msg = "{}品牌的车，在{}上，以{}速度行驶了{}小时".format(self.brand ,road.name,self.speed,rand_time)
        print(msg)

    def __str__(self):
        return "{}品牌的，速度是{}km/h".format(self.brand,self.speed)

# 创建实例化对象
r = Road("京藏高速",12000)

print(r.name)
r.name = "京哈高速"

audi = Car("奥迪",120)

print(audi)

audi.get_time(r)


