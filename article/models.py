class Article:
    def __init__(self,name,author):
        self.name = name
        self.author = author

    def show(self):
        print("发表文章：{}，名字的作者是：{}".format(self.name,self.author))


class Tag:
    def __init__(self,name):
        self.name = name