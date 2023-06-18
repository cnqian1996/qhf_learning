
list1 = [4, 2, 7, 8, 9]

# 导入模块
import test
result = test.add(*list1)   #  使用函数中的模块 函数名.变量   模块名.函数  模块名.类
print(result)

print(test.number)  # 使用模块变量

cal = test.Calculate(88) # 使用模块中的类
cal.test()

test.Calculate.aaa() # 使用模块中的类方法

