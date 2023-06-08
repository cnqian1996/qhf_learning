'''
使用函数的时候
def aa(**kwargs):
    pass
'''


def aa(**kwargs):
    print(kwargs)


aa(a=1, b='hello', c='郑义')  # 装包：{'a': 1, 'b': 'hello', 'c': '郑义'}

# 如果在开发的时候，已知有一个字典

dict1 = {'a': 1, 'b': 'hello', 'c': '郑义'}
aa(**dict1)  # 拆包：把字典拆包


def bb(a, b, *c, **d):
    print(a, b, c, d)


bb(1, 2)  # 1 2 () {}
bb(1, 2, 3, 4)  # 1 2 (3,4) {}  因为没有关键字所以，跟’**d‘无关系
bb(1, 2, x=100, y=200)  # 1 2 () {‘x’：100，‘y’：200）
bb(1, 2, 3, x=100)  # 1 2 (3,) {‘x’：100}


# bb(1, 2, x=100, 5, 6)    会报错，因为跳过‘*c’默认往后都是关键字


def func(a, *args):
    print(a, args)


func(2, 3, 4, 5)
func(2, [1, 2, 3, 4])
func(2, 3, [1, 2, 3, 4, 5])


def func1(a, b=10, c=3, **kwargs):
    print(a, b, c, kwargs)


func1(1)  # 1,10,3 {}
func1(2, b=10)  # 1,10,3,{}
# func1(3,5,6,a=1,b=2) 会报错
func1(3, c=5, b=6, x=1, y=2)  # 3 6 5 {'x': 1, 'y': 2}


def func2(a, *args, **kwargs):
    print(a, args, kwargs)


t = (1, 2, 3, 4)
func2(1, t)  # 1 ((1,2,3,4))

l = [2, 5, 8]
func2(1, 1, c=9, b=6)  # 1 (2,5,8) {'c':9,'b'：6}

dict2 = {'1': 'a', '2': 'b', '3': 'c'}
func2(1, *l, **dict2)  # 拆  #1 (2, 5, 8) {'1': 'a', '2': 'b', '3': 'c'}

'''
courses = ['html','mysql','python']
'''


def func3(name, *args):
    if len(args) > 0:
        for i in args:
            print('{}学过了{}'.format(name, i))
    else:
        print('沒有学任何编程知识！')


courses = ['html', 'mysql', 'python']
func3('郑义', *courses)

'''
总结：

无参数函数：
    def func():
        pass
    func() → 调用

有参数函数：
1、普通参数：
    def func(name,age):
        pass
    func('aa',18) → 形参和实参的个数要一直

2、可变参数：
    def func(*args):
        pass
    func() → 函数调用时，实参的个数可以没有，也可以多个 *不能是关键字参数
    func(4)
    func(5,'h')
    
    def func(**kwargs):
        pass
    func(a=1,b=2) → 函数调用时，实参的个数可以没有，也可以多个， **必须是关键字参数
    
    def func(*args,**kwargs):
        pass
    
    list1 = [1,3,6,7,9]
    dict1 = {'1':'a','2':'b'}
    func(*list1,**dict1)
    
    混用：
    def func(name,*args.**kwargs):
        pass
    func('tom') → 必须赋值

3、有默认值的函数：
    def func(name,age=17):
        pass
    func('tom') → tom 18
    func('tom',age=20) →关键字赋值
'''
