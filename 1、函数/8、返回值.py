#返回值：将函数中运算的结果，通过return关键词返回出来
def add(a,b):
    result = a + b
    print("函数内执行结果：",result)
    return "aaa",100 #如果‘扔’多个值出来，会把它们放在一个元组里作为整体返回

#调用函数：
x,y= add(2,6)
print("函数外返回值：",x,y)

'''
return 返回值
1、return后面可以是一个参数，接受的时候x=add(1,2)
2、return后面也可以是多个参数，如果是多个参数则底层会将多个参数先放在一个元组里，将元组作为整体返回
3、接受的时候也可以是多个：return 'hello','world'   x,y=('hello','world') → x='hello',y='world'
'''