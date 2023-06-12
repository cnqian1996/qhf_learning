# 模块：os.py
'''
os.path:
os.path.dirname(__name__) 获取当前文件所在的文件夹目录（绝对路径）
os.path.join(path,"...") 返回的是一个拼接后的新的路径
'''
import os

print(os.path)
path = os.path.dirname(__file__)  # 获取当前文件所在的文件目录（绝对路径）
print(path)
print(type(path))

# 绝对路径
r = os.path.isabs(r'c:\p1\girl.jpg')
print(r)

# 相对路径
r = os.path.isabs('p1\girl.jpg')
print(r)

# ..\..\3、OS模块\test.png  # 返回当前文件的上一级

path = os.getcwd()  # 类似于 os.path.dirname(__file__)
print("-----", path)

# 复制文件
with open(r"C:\Users\QHF\PycharmProjects\qhf_learning\test.png", 'rb') as stream:
    container = stream.read()  # 读取文件内容
    print(stream.name)
    file = stream.name
    filename = file[file.rfind("\\") + 1:]
    print(filename)
    path = os.path.dirname(__file__)
    path1 = os.path.join(path, filename)
    print(path1)
    with open(path1, 'wb') as wstream:
        wstream.write(container)

print("文件复制完成！")

path = r'/3、OS模块/1、os模块（os.path）.py'
result = os.path.split(path)
print(result[1])  # filename = file[file.rfind("\\")+1:]

result = os.path.splitext(path)  # 分割文件和扩展名
print(result)  # ('C:/Users/QHF/PycharmProjects/qhf_learning/3、OS模块/1、os模块简介', '.py')

size = os.path.getsize(path) # 获取文件的大小，单位是字节
print(size)

result = os.path.join(os.getcwd(),'file','aaa','test11.jpg')
print(result)