# 写文件
'''
open(path/filename, 'w')
mode 是 ‘w’ 表示就是写操作，每次都会将原来的内容清空！

方法：
    write(内容）  每次都会将原来的内容清空，然后写当前的内容
    writelines(Iterable) 没有换行效果
    stream.writelines("aa\n","bb\n","cc\n") ---->自己加

如果mode='a' 表示追加
'''

stream = open(r"C:\Users\QHF\PycharmProjects\qhf_learning\aa.txt", 'a')

result = stream.writable()
print(result)

s = '''
大家好：
   我是郑义，我是傻逼！
            哈哈哈哈哈哈哈
'''

result = stream.write(s)

stream.writelines(['傻逼郑义\n', "傻逼王新成\n", "傻逼王嘉祥\n"])

stream.write('傻逼诸葛伟')

print(result)

stream.close()  # 释放资源

# stream.write('王新成')
