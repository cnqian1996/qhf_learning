'''
python里数量词默认是贪婪的（再少数语言里也可能是默认非贪婪），总是尝试匹配尽可能多的字符；
非贪婪则相反，总是尝试匹配尽可能少的字符。
在'*','?',','{m,n}'后面加上？，是贪婪变成非贪婪
'''

import re
# 默认是贪婪的
msg = 'abc123abc'

result = re.match(r"abc(\d+?)",msg)

print(result)


path = '<img class="BDE_Image" src="https://imgsa.baidu.com/forum/w%3D580/sign=0756832344a98226b8c12b2fba83b97a/302dc9177f3e670925af44a93cc79f3df9dc5560.jpg">'

result = re.match(r'<img class="BDE_Image" src="(.*?)"',path)

print(result)
print(result.group(1))

import requests
image_path = result.group(1)
response = requests.get(image_path)
with open('aa.jpg',"wb") as wstream:
    wstream.write(response.content)