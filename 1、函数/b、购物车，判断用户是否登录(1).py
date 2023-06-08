'''
加入购物车，判断用户是否登录，如果登录成功加入购物车，否则提示请登录后添加。
'''

islogin = False #用于判断用户是否登录的变量

def add_shoppingcart(goodsName):
    if islogin and goodsName:
        print("成功将{}加入到购物车！".format(goodsName))
    else:
        #没有登录，或者添加任何商品
        print("用户没有登录，或者没有添加任何商品！")

def login(username, password):
    if username == '郑义' and password == 'sb945':
        print("登录成功！")
        return True
    else:
        print("用户名或者密码有误！")
        return False

# 调用函数：添加商品到购物车中：
username = input("输入用户名：")
password = input("输入密码：")

islogin = login(username,password)

add_shoppingcart("PlayStaion5")


