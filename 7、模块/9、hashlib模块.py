# 加密算法：md5 sha1 sha256 都是单向的
# base64可以解码
import hashlib

msg = '郑义'
md5 = hashlib.md5(msg.encode("utf-8"))
print(md5.hexdigest())  # 573064ee1e160cf8c2597ecf0d150e8b

sha1 = hashlib.sha1(msg.encode("utf-8"))
print(sha1.hexdigest()) # 411c7d6b8a6c206b42b2023772e610fb59c61294



print('---------------------------------------------------')
password = '123456'

list1 = []

sha256 = hashlib.sha256(password.encode('utf-8'))
list1.append(sha256.hexdigest())

pwd = input('请输入密码：')
sha256 = hashlib.sha256(pwd.encode("utf-8"))
pwd = sha256.hexdigest()
print(pwd)
print(list1)
for i in list1:
    if pwd == i:
        print("登陆成功！")