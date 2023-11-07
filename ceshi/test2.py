# s1 = 'hello'
# try:
#     int(s1)
# except ValueError as e: # 未捕获到异常，程序直接报错
#     print (e)
#


# s1 = 'hello'
# try:
#     int(s1)
# except IndexError as e:
#     print(e)
# except KeyError as e:
#     print(e)
# except ValueError as e:
#     print(e)
#
# else:
#     print('try内代码块没有异常则执行我')
# finally:
#     print('无论异常与否,都会执行该模块,通常是进行清理工作')

try:
    raise TypeError('类型错误')
except Exception as e:
    print(11)
