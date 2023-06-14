# __str__
# 触发时机：打印对象名 自动触发去调用__str__里面的内容
# 注意：一定要在__str__中添加return，return后面的内容就是打印对象看到的内容

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return "姓名是：{},年龄是:{}".format(self.name,self.age)


p = Person('郑义', 17)
print(p)

# 单纯打印对象名称，出来的是一个地址。地址对于开发者来说没有太大意义
# 如果想在打印对象名的时候能够给开发者更多一些信息量

'''
总结 魔术方法
重点：__init__ （构造方法，创建完空间之后调用的第一个方法）    __str__

了解：
__new__  作用:开辟空间
__del__  作用：没有指针引用的时候会调用。99%都不需要重写
__call__ 作用：想不想把对象当成函数用

大总结：
方法：
    普通方法  ------> 重点
        def 方法名(self,[参数]):
            方法体
        
        对象.方法()
        
        方法之间的调用：
        class A：
            def a(self):
                pass
            def b(self):
                # 调用a方法
                self.a()
    
    静态方法
    @classmethod
    def 方法名(sls,[参数]):
        psss
        
    类名.方法名()
    对象.方法名()
    
    魔术方法 自动执行的一些方法
    print(p)  -----> __str__
'''
