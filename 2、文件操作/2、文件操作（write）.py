# 写文件
stream = open(r"C:\Users\QHF\PycharmProjects\qhf_learning\aa.txt",'w')

result = stream.writable()
print(result)

s = '''
大家好：
   我是郑义，我是傻逼！
            哈哈哈哈哈哈哈
'''
result = stream.write(s)
print(result)

stream.write('王新成')