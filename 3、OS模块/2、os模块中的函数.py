# os中函数：
'''
os模块下的方法：
os.getcwd() 获取当前目录
os.listdir() 浏览文件夹
os.mkdir() 创建文件夹
os.rmdir() 删除空的文件夹
os.remove() 删除文件
os.chdir() 切换目录
'''

import os

dir = os.getcwd()
print(dir)

all = os.listdir(r"c:\Program Files")  # 返回指定目录下的所有的文件和文件夹，保存到列表中
print(all)

# 创建文件夹
if not os.path.exists(r"C:\Users\QHF\Desktop\qhf_TEST"):
    f = os.mkdir(r"C:\Users\QHF\Desktop\qhf_TEST")
    print(f)

# f = os.rmdir(r"C:\Users\QHF\Desktop\qhf_TEST")  # 只能删除空的文件夹
# f = os.removedirs(r"C:\Users\QHF\Desktop\qhf_TEST")

# os.remove(r"C:\Users\QHF\Desktop\qhf_TEST\aa.txt")

# 删除文件夹
# path = r"C:\Users\QHF\Desktop\qhf_TEST"
#
# filelist = os.listdir(path)
#
# for file in filelist:
#     path1 = os.path.join(path, file)
#     os.remove(path1)
# else:
#     os.rmdir(path)
#
# print('删除成功！')

# 切换目录
f = os.chdir(r'C:\Users\QHF\Desktop\qhf_TEST')
print(f)
path = os.getcwd()
print(path)
