'''
面向对象：
程序---------->现实中
对象---------->具体的事务

现实中事务 ---> 转成电脑程序
世间万物皆对象

面向对象：
    类
    对象
    属性
    方法

多个对象 -----> 提取对象的共同的特征和动作----->封装到一个类中

'''
# 所有的类名要求首字母大写，多个单词使用驼峰式命名
# ValueError TypeError StopIterable
'''
class 类名[(父类)]:
    属性：特征
    方法：动作
'''


class Phone:
    # 属性
    brand = 'Huawei'
    # 方法

print(Phone)

#使用类创建对象
zhengyi = Phone()
print(zhengyi)
print(zhengyi.brand)
zhengyi.brand = 'Iphone'
print(zhengyi.brand)

wangxincheng = Phone()
print(wangxincheng)
print(wangxincheng.brand)
wangxincheng.brand = 'OPPO'
print(wangxincheng.brand)

wangjiaxiang = Phone()
print(wangjiaxiang.brand)