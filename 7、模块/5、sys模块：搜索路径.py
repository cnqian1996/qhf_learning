'''
当你导入一个模块，python解释器对模块位置的搜索顺序是：
1、当前目录
2、如果不在当前目录，python则搜索在shell变量PYTHONPATH下的每个目录
3、如果都找不到，python会查看默认路径。unix下，默认路径一般为/user/local/lib/python/
模块搜索路径存储在system模块的sys.path变量中。变量里包含当前目录，PYTHONPATH
'''

'''
自定义模块
系统模块:
    sys模块
'''

import sys

print(sys.path)

print(sys.version)
print(sys.argv) # 运行程序时的参数，argv是个列表