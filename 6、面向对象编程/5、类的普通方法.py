class Person:
    name = "诸葛伟"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self, food):
        print("{}正在吃{}！。。。。".format(self.name, food))
        print("今年{}岁了。".format(self.age))

    def run(self):
        print("{}，今年{}岁，正在跑步".format(self.name, self.age))


p = Person('zhengyi', 99)
p.name = "郑义"
p.eat("屎")
p.run()

p1 = Person('王嘉祥', 28)
p1.name = "wangjiaxiang"
p1.eat("榴莲")
p1.run()

print(Person.name)
