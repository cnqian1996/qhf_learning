# []表示的是一个范围


import re

s = "哈哈1a"
result = re.search("[0-9][a-z]",s)
print(result.group())



msg = 'abcd7vjkfd8hdf00'

result = re.search('[a-z][0-9][a-z]',msg) # search 只要有匹配的 后面就不会继续进行检索 找到一个匹配的就会停止
print(result.group())

result = re.findall('[a-z][0-9][a-z]',msg) # findall 匹配整个字符串，找到一个继续向下找一直找到字符串结尾
print(result)

#正则符号

# a7a  a88a  a78878a
msg = 'a8qweq990qwe7879qw12322k'
result = re.findall("[a-z][0-9]+[a-z]",msg)
print(result)