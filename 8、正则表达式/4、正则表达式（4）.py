import re
# 起名的方式: (?P<名字>正则)(?P=名字)
msg = '<html><h1>abc</h1></html>'

result = re.match(r"<(?P<name1>\w+)><(?P<name2>\w+)>(.+)</(?P=name2)></(?P=name1)>",msg)
print(result)