def login(username,password):
    #相当于数据库注册的账号密码!
    uname = "admin"
    pwd = "abc123"

    for i in range(3):
           if username == uname and password == pwd :
            print("登陆成功！")
            break
        else:
            print("账号密码错误，登录失败！！！")
            username = input("请输入用户名>>:").strip()
            password = input("请输入密码>>:").strip()
    else:
        print("失败次数过多，账号被锁定！")


username = input("请输入用户名>>:").strip()
password = input("请输入密码>>:").strip()

login(username,password)