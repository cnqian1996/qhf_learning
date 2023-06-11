# 开发：登录验证
import time

islogin = False  # 默认没有登录


# 定义一个登录函数
def login():
    username = input("输入用户名：")
    password = input("输入密码：")
    if username == '郑义' and password == 'sb945':
        return True
    else:
        return False


def login_required(func):
    def wrapper(*args, **kwargs):
        global islogin
        print('----------付款-----------')
        if islogin:
            func(*args, **kwargs)
        else:
            print("用户没有登录，正在跳转到登录页面...")
            time.sleep(3)
            # 跳转到登录页面！
            islogin = login()
            print("result:", islogin)

    return wrapper


@login_required
def pay(money):
    print("正在付款，付款金额是{}元人民币".format(money))
    print("付款中...")
    time.sleep(2)
    print('付款完成！')


pay(10000)

pay(8000)
