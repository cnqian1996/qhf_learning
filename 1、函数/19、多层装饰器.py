'''
1.如果装饰器是多层的，谁距离函数最近，就优先使用哪个装饰器
'''

def zhuang1(func):
    print("--------->1 start")

    def wrapper(*args,**kwargs):
        func()
        print("刷漆")

    print("--------->1 end")
    return wrapper


def zhuang2(func):
    print("--------->2 start")

    def wrapper(*args, **kwargs):
        func()
        print("铺地板。。")

    print("--------->2 end")
    return wrapper

@zhuang2
@zhuang1
def house():
    print("我是毛坯房！...")

house()