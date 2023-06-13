#协程
'''
生成器 generator：
定义方式：
1.通过列表推导式的方式
  g = (x+1 for x in range(5))

2.函数+yield
  def func():
      ...
      yield

  g=func()

产生元素：
1.next(generator)  -----> 每次调用都会产生一个新的元素，如果元素产生完毕，再次调用的话就会产生异常
2.生成器自己的方法：
     g.__next__()
     g.send(value)

'''
def task1(n):
    for i in range(n):
        print("王新成正在搬第{}块砖".format(i))
        yield None

def task2(n):
    for i in range(n):
        print("王新成正在听第{}首歌".format(i))
        yield None


g1 = task1(10)
g2 = task2(10)

while True:
    try:
        g1.__next__()
        g2.__next__()
    except:
        break