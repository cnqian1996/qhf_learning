def login(username,password):
    #相当于数据库注册的账号密码!
    uname = "admin"
    pwd = "abc123"
    if username == uname and password == pwd :
        print("登陆成功！")
    else:
        print("账号密码错误，登录失败！！！")

username = input("请输入用户名>>:").strip()
password = input("请输入密码>>:").strip()

login(username,password)