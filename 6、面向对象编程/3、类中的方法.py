# 类中方法：动作
# 种类：普通方法 类方法 静态方法 魔术方法

'''
普通方法格式：
def 方法名(self[,参数,参数])：
    pass
'''

class Phone:
    brand = 'xiaomi'
    price = 49999
    type = 'mate 80'

    #Phone类里的方法：call
    def call(self):
        print('self........',self)
        print("正在访问访问通讯录：")
        for person in self.address_book:
            print(person.items())
        print("正在打电话...")
        print('留言是：',self.note)

phone1 = Phone()
phone1.note = '我是phone1111的note'
phone1.address_book = [{"13257530575":'郑义'},{"18851667788":'王新成'}]
print(phone1,'---1---')
# print(phone1.brand)
phone1.call()

print("\n","*"*30,"\n")
phone2 = Phone()
phone2.note = '我是phone2222的note'
print(phone2,'---2---')
phone2.call()
