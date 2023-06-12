# 文件的复制
'''
源文件： c:\p1\girl.jpg
目标文件 c:\p2\girl.jpg

with 结合 open使用，可以帮助我们自动释放资源

'''
# stream = open(r"C:\Users\QHF\PycharmProjects\qhf_learning\test.png",'rb')
with open(r"C:\Users\QHF\PycharmProjects\qhf_learning\test.png",'rb') as stream:
    container = stream.read() # 读取文件内容

    with open(r"C:\Users\QHF\PycharmProjects\qhf_learning\test2.png",'wb') as wstream:
        wstream.write(container)

print("文件复制完成！")

