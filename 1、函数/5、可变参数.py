# def add(*args):
#     # print(args)
#     sum = 0
#     if len(args) > 0:
#         for i in args:
#             sum += i
#         print("累加的和：",sum)
#     else:
#         print("没有元素可计算，sum",sum)
# add() #（）空元组
# add(1)
# add(1,2)
# add(1,2,3)
# add(1,2,3,4)

#xxx计算出的累加值是多少？
def add(name,age,*args):
    sum = 0
    if len(args) > 0:
        for i in args:
            sum += i
        # print(name,"累加的和：",sum)
        print("%s累加的和是：sum：%s" % (name, sum))
    else:
        print("没有元素可计算，sum", sum)

add("郑义",22,4,5,6) #22为age！固定参数
add("王新成",10) #无参数