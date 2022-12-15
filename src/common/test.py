# -*- coding: utf-8 -*-
# @Time : 2022/10/12 16:39
# @Author : 居里夫人吃橘子
# @Site : 
# @File : test.py
# @Software: PyCharm
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

# driver = webdriver.Chrome()
# driver.get('https://www.baidu.com/')
# sleep(1)
# eles = driver.find_element(By.CSS_SELECTOR,'[id="kw"]')
# # eles.send_keys("123")
# aa = driver.find_element(By.CSS_SELECTOR,'[id="su"]')
# sleep(2)
# print(type(aa))
# print(aa.text)
# # for kk in aa:
# #     print(kk.text)
# b = aa.text
# print(b)
#
#
# try :
#     # 提示用户输入一个数字
#     num=int(input('请输入数字:'))
# except:
#     print("请输入正确的数字")

def func1(x,y):
    print("this is fun1")
    test1= x+y
    return test1
def func2():

    test2= func1(1,2)
    print(test2)

if __name__ == '__main__':
    func2()