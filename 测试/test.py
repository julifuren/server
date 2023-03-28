from time import sleep

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

try:
    a = "异常测试："
    print(a)

except NameError as msg:
    print(msg)
else:
    print("没有异常时执行!")
