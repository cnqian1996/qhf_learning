# 文件操作：
'''
系统函数：
open(file,mode,buffering,encoding)
   mode:
         r:read 读
         w:write 写
         b:binary 二进制 字节
         rb: read binary
         wb: write binary

读：
open(path/filename,'rt') ----> 返回值：stream（管道）
container = stream.read()  ----> 读取管道中内容
注意：如果传递的path/filename有误，则会报错：FileNotFoundError
     如果是图片则不能使用默认的读取方式，mode='rb'
'''

stream = open(r"C:\Users\QHF\PycharmProjects\qhf_learning\aa.txt",encoding="utf-8")

# container = stream.read()
# print(container)

result = stream.readable() # 判断是否可以读取 True False
print(result)

# while True:
#     line = stream.readline()
#     print(line)
#     if not line:
#         break

lines = stream.readlines() # 保存再列表里
print(lines)
for i in lines:
    print(i)


stream1 = open(r"C:\Users\QHF\PycharmProjects\qhf_learning\test.png",'rb')
container1 = stream1.read()
print(container1)


