'''
正则表达式是一个特殊的字符序列，它能帮助你方便的检查一个字符串是否与某种模式匹配。
Python 自1.5版本起增加了re 模块，它提供 Perl 风格的正则表达式模式。
re 模块使 Python 语言拥有全部的正则表达式功能。
compile 函数根据一个模式字符串和可选的标志参数生成一个正则表达式对象。该对象拥有一系列方法用于正则表达式匹配和替换。
re 模块也提供了与这些方法功能完全一致的函数，这些函数使用一个模式字符串做为它们的第一个参数。
本章节主要介绍Python中常用的正则表达式处理函数。
'''
'''
总结:
  . 任意字符除（\n）
  ^ 开头
  $ 结尾
  [] 范围 [abc] [a-z] [a-z*$]
  
  正则预定义：
  \s 空白（空格）
  \b 边界
  \d 数字
  \w word [0-9a-zA-Z]
  
  大写反面： \S 非空白     \D 非数字
  '\w[0-9]' -----> \w [0-9] 只能匹配一个字母
  
  量词
  *  >= 0
  + >= 1
  ? 0,1
  
  手机号码正则  re.match('1[35789]/d{9}$',phone)
  
  {m} 固定m位
  {m,} >= m
  {m,n}   m <= phone <=n
  
'''

# qq = input("请输入qq号码：")
# if len(qq) >= 5 and qq[0] != '0':
#     print('合法的！')
# else:
#     print('不合法的！')

import re

msg = '郑义王新成王嘉祥诸葛伟'
pattern = re.compile("王新成")  # 没有匹配
print(pattern.match(msg))

# 使用正则re模块方法：match

s = '郑义王新成王嘉祥诸葛伟'
result = re.match("王新成", s)  # 只要从开头进行匹配，如果匹配不成功则返回None
print(result)

result = re.search('王新成', s)  # search 进行正则 字符串匹配方式，匹配的是整个字符串
print(result)

print(result.span())  # 返回位置
print(result.group())  # 使用group提取到匹配的内容
print(result.groups())

# a2b h6k
msg = "adcd7bjkd8hdf00"
result = re.findall('[a-z][0-9][a-z]', msg)
print(result)

# qq号码验证 5~11 开头不能是0
qq = '14944689962'
result = re.match('^[1-9][0-9]{4,10}$',qq)
print(result.group())

# 用户名可以是字母或者数字，不能是数字开头，用户名长度必须6位以上[0-9a-zA-Z]
username = 'admin001'
result = re.search('^[a-zA-z]\w{5,}$',username)
print(result)

msg = 'aa*py ab.ext bb.py kk.png uu.py'
result = re.findall(r'\w*\.py\b',msg)
print(result)