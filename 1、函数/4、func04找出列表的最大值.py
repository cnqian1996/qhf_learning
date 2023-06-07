#找列表的最大值


def max(iterable): #用在for...in...都是可迭代的！！！
    if isinstance(iterable,(list,tuple)): #判断实参是什么类型的！
        max = iterable[0]
        for i in iterable:
            if i > max :
                max = i
        print("最大值是：",max)
    else:
        print("你输入的并不是list或者tuple！")


# list1=[1,4,5,21,4325,436,54,7,8]
list1="dasdas"
max(list1)

tuple1=(1,34,54547,2423,126)
max(tuple1)
