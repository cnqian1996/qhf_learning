'''
用户登录：输入用户名、密码、验证码
'''

import random

# 定义生成验证码函数
def generate_chekcode(n):
    s = '951623847qwaeszrdxtfcygvuhbijnokmplPLMOKNIJBUHVYGCTFXRDZESAWQ'
    code = ''
    for i in range(n):
        ran = random.randint(0,len(s)-1)
        code += s[ran]
    return code

# 定义登陆函数
def login():
    username = input("输入用户名：")
    password = input("输入密码：")
    code = generate_chekcode(5) #生成验证码
    print("验证码为:",code)
    code1 = input("请输入验证码：")
    #先验证验证码
    if code.lower() == code1.lower():
        if username == "郑义" and password == "sb945":
            print("用户登录成功！")
        else:
            print("用户名或者密码有误！")
    else:
        print("验证码输入有误！")

login()
