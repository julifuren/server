# -*- coding: utf-8 -*-
# @Time    : 2023/11/15 17:55
# @Author  : 居里夫人吃橘子
# @File    : zsq.py
# @Software: PyCharm


# def f():
#     print("运行f函数")


def func(foo):  # 装饰函数（装饰器）
    def inner():
        print("打印日志前")
        foo()
        print("打印日志后")

    return inner


#
# a = func(foo=f)
# a()
#
# # 调用 func 函数。然后输入一个实参。
# # a = func(foo=f)
# # a()
# """代码运行的过程如下：
# 1、调用了func 函数，首先会执行 def inner(): 代码，然后发现这是一个 函数的定义。函数定义了以后没有被调用不会执行。
# 所以不会执行 inner 函数的函数体中的内容。
# 2、接下来就会执行到 return inner 这行代码。
# 3、a() 调用完 func函数以后返回了 inner ， 因为 a == inner . 所以就相当于 给 inner 加了一个括号，
# 发现 inner 是函数名，给它加了括号就相当于调用inner函数。 接下来就会执行  print("打印日志前") 。
# 4、foo() ，在调用 func函数的时候传入了一个实参 是 f ，所以 现在 foo == f 。 foo() 就给 f 加了括号，
# 发现 f 是函数名，给它加了括号就相当于调用f函数。
# 5、后面就执行 打印语句。
# """
@func  # 在被装饰的函数 上面使用一个 @+装饰函数的函数名
def f():
    print("运行f函数")


# 调用 f 函数
f()
