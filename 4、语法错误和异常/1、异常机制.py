# 语法的错误和异常

# 异常：程序运行的时候报出来的，例如 xxxError

# 异常处理：
'''
        格式
try:
    可能出现异常的代码
except：
    如果有异常执行的代码
finally：
    无论是否存在异常，都会被执行的代码。


情况1:
  try：
    有可能会产生多种异常
  except 异常的类型1：
      print（“...”）
  except 异常的类型2：
      print（“...”）
  ...
  except Exception：
      print（“...”）


  如果是多个except，异常类型的顺序需要注意，最大的Exception需要放在最下面！

  情况2: 获取Exception的错误原因
  try：
    有可能会产生多种异常
  except 异常的类型1：
      print（“...”）
  except 异常的类型2：
      print（“...”）
  ...
  except Exception as err：   err 的内容就错误的原因！
      print（“...”, err）
  ...
'''


def func():
    try:
        n1 = int(input("输入第一个数字："))
        n2 = int(input("输入第二个数字："))
        per = input("输入运算符（+ - * /)--->>:")

        result = 0

        if per == '+':
            result = n1 + n2
        elif per == '-':
            result = n1 - n2
        elif per == '*':
            result = n1 * n2
        elif per == '/':
            result = n1 / n2

        else:
            print("符号输入错误")

        print("运算的结果是：", result)

        list1 = []
        list1.pop()

        # 文件操作
        with open(r"C:\Users\QHF\Desktop\qhf_test\result.txt", "w") as wstream:
            wstream.write("本次的运算结果是：{}".format(result))
        with open(r"C:\Users\QHF\Desktop\qhf_test\r1esult.txt", "r") as wstream:
            print(wstream.read())


    except ZeroDivisionError:
        print("除数不能为零！！！".center(50, "-"))
    except ValueError:
        print("必须输入输入数字！！！".center(50, "-"))
    except Exception as err:
        print("出错了 !!!",err)


# 调用
func()
print("--------->")
