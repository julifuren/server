from time import sleep

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

try:
    a = "异常测试："
    print(a)
    try:
        print(b)
        print(2)

    except:
        print('异常')

except Exception as msg:
    print(msg)
