'''
    article
        ｜——models.py
        ｜——__init__.py
        ｜——...
    user
        ｜——models.py
        ｜——__init__.py
        ｜——test_out.py

'''

# 用户发表文章
# 创建用户对象

# 发表文章，文章对象

from user.models import User
from article.models import Article

user = User('admin', "123456")  # ----> 通过导入的User类创建的

# 发表文章 文章对象
article = Article("个人总结", "郑义")

user.publish_article(article)


# 外层的导入
from test_out import Qhf