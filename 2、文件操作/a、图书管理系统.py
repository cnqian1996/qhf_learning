# 图书管理系统
# 持久化保存：文件
# list 元组，字典 ----> 内存

# 用户注册
def register():
    username = input("请输入用户名：").strip()
    password = input("请输入密码：").strip()
    repassword = input("输入确认密码：").strip()

    if password == repassword:  # 保存信息
        with open(r"C:\Users\QHF\Desktop\qhf_test\users.txt", 'a') as wstream:
            wstream.write("{} {}\n".format(username, password))

        print("用户注册成功！")
    else:
        print("密码不一致！")

#用户登录
def login(func):
    def wrapper(*args,**kwargs):
        username = input("请输入用户名：").strip()
        password = input("请输入密码：").strip()

        if username and password:
            with open(r"C:\Users\QHF\Desktop\qhf_test\users.txt") as rstream:
                while True:
                    user = rstream.readline()

                    if not user:
                        print("用户名或者密码错误！")
                        break

                    input_user = '{} {}\n'.format(username,password)

                    if user == input_user:
                        print("用户登录成功！")
                        func(*args,**kwargs)
                        break
    return wrapper

@login
def show_books():
    print("图书馆里的图书有：".center(50,"*"))
    with open(r"C:\Users\QHF\Desktop\qhf_test\books.txt","r",encoding="utf-8") as rstream:
        books = rstream.readlines()
        for book in books:
            print(book,end="")





register()
# login()  已使用装饰 不需要调用此函数
show_books()

