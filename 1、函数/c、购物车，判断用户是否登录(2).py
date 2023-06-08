'''
加入购物车，判断用户是否登录，如果登录成功加入购物车，否则提示请登录后添加。
'''

islogin = False  # 用于判断用户是否登录的变量


def add_shoppingcart(goodsName):
    global islogin

    if islogin:
        if goodsName:
            print("成功将{}加入到购物车！".format(goodsName))
        else:
            print("没有选中任何商品！")
    else:
        answer = input("用户没有登录，是否登录用户？（yes/no）")
        if answer == 'yes':
            username = input("输入用户名：")
            password = input("输入密码：")
            islogin = login(username, password)  # 对函数外参数进行赋值,需要加global
            add_shoppingcart(goodsName)
        else:
            print("很遗憾，您输入的账号密码有误！无法登陆！")


def login(username, password):
    if username == '郑义' and password == 'sb945':
        # print("登录成功！")
        return True
    else:
        # print("用户名或者密码有误！")
        return False


# 调用函数：

username = input("输入用户名：")
password = input("输入密码：")

add_shoppingcart("PlayStaion5")
