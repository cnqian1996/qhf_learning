# 分组
# 匹配数字0-100数字
import re

n = '100'
result = re.match(r'[1-9]?\d?$|100$', n)
print(result)

# (word|word|word...)  区别 [abc]表示的是一个字母而不是一个单词
# 验证输入的邮箱 163 126 qq
email = '77186121@qq.com'
result = re.match(r'\w{5,20}@(163|126|qq)\.(com|cn)$',email)
print(result)